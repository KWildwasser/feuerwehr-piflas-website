"""Sicherheits- und Ausfall-Tests der Referenz-Demo (Lastenheft N-05, B-03, B-05, B-08, B-20, A-10, A-11, D-08).

Ergänzt test_app.py. Gleiche Regeln: Jede Prüfung ist zugleich Abnahmekriterium für die echte Website.
In WordPress gelten dieselben Fälle für den Server (Capabilities, Nonces, Escaping) – die Demo zeigt das Verhalten.

Aufruf:  python build.py && python test_security.py      (Ergebnis: security_results.json)
Aufbau:  1. Rechte je Rolle: Seitenzugriff (Matrix) und jede schreibende Aktion ohne sichtbaren Knopf (B-03)
         2. Eingaben: HTML/Skript in allen Formularen und in der Adresse wird nie ausgeführt (N-05),
            Höchstlängen an allen Textfeldern (B-20), nur sichere Links
         3. Anmeldung: Sperre nach Fehlversuchen (B-05), „Passwort vergessen“ ohne Konto-Verrat,
            Austritt deaktiviert statt löscht (B-08), Abmelden schützt den Mitgliederbereich
         4. Ausfallsicherheit: Schnittstellen gestört (D-08, A-10, A-11), Doppelklicks, wilde Adressen
         5. Inhalte, die bisher nur indirekt geprüft waren (F-04, F-07, F-12, C-01–C-03, S-01, W-05, W-06, N-08, N-10)
Exit-Code 1, sobald eine Prüfung fehlschlägt.
"""
import asyncio, json, os, sys
from pathlib import Path
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
URL = (HERE / 'index.html').as_uri()
results = []

def rec(ok, name, detail=''):
    results.append((bool(ok), name, detail))
    print(('PASS ' if ok else 'FAIL ') + name + (' – ' + str(detail) if detail else ''))

PUBLIC = ['start','jubilaeum','aktuelles','einsaetze','termine','buerger','foerdern','mitmachen','fahrzeuge','jugend','verein','partner','impressum','datenschutz','login']
BACKR = ['redaktion','beitraege','seiten','fotos','planung','mitglieder','system','lernen','lthema','lernstand','lplan']
# Erwarteter Zugriff je Rolle (Rollentabelle 2.5, E-01, E-05, E-08, B-12)
ALLOWED = {
    'Mitglied': {'lernen'},
    'Autor': {'beitraege','seiten','planung','lernen'},
    'Freigeber': {'redaktion','beitraege','seiten','planung','lernen','lthema','lernstand','lplan'},
    'Administrator': {'redaktion','beitraege','seiten','fotos','planung','mitglieder','system','lernen'},
}
# Schreibende Aktionen mit der mindestens nötigen Rolle (wie NEED/NEEDF in app-src.html)
ACTS = {
    'publish':'frei', 'drop':'frei', 'q-restore':'frei', 'm-del-ok':'adm', 'revoke':'adm', 'resend':'adm', 'm-off-ok':'adm', 'm-on':'adm',
    'if-man':'adm', 'ig-reconnect':'adm', 'c-del-ok':'adm', 'lt-new':'kdt', 'lt-copy':'kdt', 'lt-hide':'kdt', 'lt-show':'kdt',
    'edit':'schreib', 'new':'schreib', 'hide':'schreib', 'h-restore':'schreib', 's-new':'schreib', 's-del-ok':'frei',
}
FORMS = {'f-einsatz':'frei', 'f-invite':'adm', 'f-role':'adm', 'f-settings':'adm', 'f-key':'adm', 'f-lthema':'kdt', 'f-post':'schreib', 'f-item':'schreib', 'f-verein':'schreib', 'f-chronik':'schreib', 'f-plan':'schreib'}
def may(role, need):
    return {'adm': role == 'Administrator', 'kdt': role == 'Freigeber', 'frei': role in ('Administrator','Freigeber'), 'schreib': role != 'Mitglied'}[need]

XSS = ['<img src=x onerror="window.__x=1">', '"><svg onload="window.__x=1">', "'><script>window.__x=1</script>", '{{constructor.constructor("window.__x=1")()}}']
SNAP = "JSON.stringify(window.__demo.state(), (k, v) => ['nid','toastT'].includes(k) ? undefined : v)"
FUZZ_JS = r'''(p) => { const out = []; document.querySelectorAll('main form').forEach(f => {
  f.querySelectorAll('input, textarea').forEach(el => {
    if (['checkbox','radio','file','hidden','submit','button'].includes(el.type)) { if (el.type === 'checkbox') el.checked = true; return; }
    if (el.type === 'email') el.value = 'a+' + Math.random().toString(36).slice(2, 6) + '@beispiel.de';
    else if (el.type === 'url' || /^(u|url|link)/.test(el.name)) el.value = 'https://beispiel.de/?"><img src=x onerror=window.__x=1>';
    else if (['date','time','datetime-local','number'].includes(el.type) || el.inputMode === 'numeric') return;
    else { const ml = el.maxLength > 0 ? el.maxLength : 500; el.value = p.slice(0, ml); }
    el.dispatchEvent(new Event('input', {bubbles:true}));
  }); out.push(f.id); }); return out; }'''
TXT_NO_MAX = r'''() => [...document.querySelectorAll('main form input, main form textarea')].filter(el =>
  !['checkbox','radio','file','hidden','submit','button','date','time','number','datetime-local','month'].includes(el.type) && !(el.maxLength > 0)).map(el => (el.closest('form').id || '?') + ':' + (el.name || el.type))'''
HIT = "!!window.__x || !!document.querySelector('main img[src=\"x\"], main svg[onload], main script:not([src])')"

async def main():
    async with async_playwright() as p:
        exe = os.environ.get('CHROME') or ('/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None)
        br = await p.chromium.launch(executable_path=exe, args=['--no-sandbox']) if exe else await p.chromium.launch()
        ctx = await br.new_context(viewport={'width':390,'height':844}, is_mobile=True, has_touch=True, locale='de-DE')
        pg = await ctx.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
        pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' and 'ERR_' not in m.text else None)
        ext = []
        pg.on('request', lambda r: ext.append(r.url) if not r.url.startswith(('file:', 'data:', 'blob:', 'about:')) else None)

        async def fresh():
            await pg.goto(URL + '#start'); await pg.reload(); await pg.wait_for_timeout(300)
        async def go(r):
            await pg.evaluate(f"location.hash='{r}'"); await pg.wait_for_timeout(110)
        async def h(): return (await pg.evaluate('location.hash')).lstrip('#')
        async def login(role):
            if await pg.evaluate('!!window.__demo.state().user'): await logout()
            await go('login'); await pg.click(f'#quick [data-role="{role}"]'); await pg.wait_for_timeout(150)
        async def logout():
            await pg.evaluate("(() => { const d = window.__demo, S = d.state(); S.user = null; S.pending2fa = null; location.hash = 'start'; d.render(); })()"); await pg.wait_for_timeout(120)
        async def act(attrs):
            await pg.evaluate("""(a) => { const b = document.createElement('button'); Object.entries(a).forEach(([k, v]) => b.dataset[k] = v);
                b.style.cssText = 'position:fixed;left:0;top:0;width:10px;height:10px'; document.body.appendChild(b); b.click(); b.remove(); }""", attrs)
            await pg.wait_for_timeout(90)
        async def sub(fid):
            await pg.evaluate("""(id) => { const f = document.createElement('form'); f.id = id; f.innerHTML = '<input name="t" value="x"><button type="submit">s</button>';
                document.body.appendChild(f); f.requestSubmit(); f.remove(); }""", fid)
            await pg.wait_for_timeout(90)
        async def toast(): return await pg.inner_text('#toast')

        # ================= 1. Rechte je Rolle (B-03, E-01, E-05, E-09, B-12) =================
        await fresh()
        for r in BACKR:
            await go(r); rec(await h() == 'login', f'B-03: ohne Anmeldung kein Zugriff auf #{r} (weiter zum Login)', await h())
        for role, allowed in ALLOWED.items():
            await fresh(); await login(role)
            bad = []
            for r in BACKR:
                await go(r); got = await h()
                if (got == r) != (r in allowed): bad.append(f'{r}→{got}')
            rec(not bad, f'B-03: {role} kommt genau in die erlaubten Bereiche ({len(allowed)})', ', '.join(bad))
            # jede schreibende Aktion, auch ohne sichtbaren Knopf
            await go(sorted(allowed)[0])
            wrong = []
            for a, need in ACTS.items():
                if may(role, need): continue
                s0 = await pg.evaluate(SNAP)
                await act({'act': a, 'id': 'lv', 'i': '0', 'k': 'n', 'key': 'fz:1', 'm': '2027-01', 's': 'div'})
                if await pg.evaluate(SNAP) != s0: wrong.append(a)
            for fid, need in FORMS.items():
                if may(role, need): continue
                s0 = await pg.evaluate(SNAP); await sub(fid)
                if await pg.evaluate(SNAP) != s0: wrong.append(fid)
            rec(not wrong, f'B-03/N-05: {role} – verbotene Aktionen ändern nichts, auch ohne Knopf', ', '.join(wrong))
            if role == 'Mitglied':
                await act({'act': 'publish', 'id': 'x'}); rec('Rechte' in await toast(), 'B-03: verbotene Aktion meldet „Dafür fehlen dir die Rechte“')
        # Admin sieht keine Lernergebnisse anderer (E-09) – auch nicht im Mitglieder- oder System-Bereich
        await fresh(); await login('Administrator')
        leak = []
        for r in ['mitglieder', 'system', 'redaktion', 'beitraege']:
            await go(r); t = await pg.inner_text('main')
            if any(x in t for x in ['von 5 richtig', 'Teilnahme', 'nicht geschafft', 'Versuche']): leak.append(r)
        rec(not leak, 'E-09: Admin sieht nirgends Lernergebnisse', ', '.join(leak))
        # Abmelden schützt den Mitgliederbereich, auch über „Zurück“
        await go('mitglieder'); await go('beitraege')
        await pg.click('[data-act=logout]'); await pg.wait_for_timeout(150)
        await pg.go_back(); await pg.wait_for_timeout(200)
        rec(await h() in ('login', 'start', '') and await pg.locator('.btabs').count() == 0, 'Abmelden: „Zurück“ führt nicht wieder in den Mitgliederbereich', await h())

        # ================= 2. Eingaben (N-05, B-20, E-04) =================
        pages = [('Administrator', ['mitglieder', 'system']),
                 ('Freigeber', ['beitraege:new-n', 'beitraege:new-e', 'seiten:verein', 'seiten:chronik', 'seiten:fz', 'planung', 'lthema']),
                 (None, ['mitmachen', 'start', 'login'])]
        nomax, fuzzed = [], []
        for pay in XSS:
            await fresh()
            for role, rs in pages:
                if role: await login(role)
                else: await logout()
                for r in rs:
                    base, _, sub_ = r.partition(':')
                    await go(base)
                    if sub_.startswith('new-'):
                        await pg.click(f'[data-act=new][data-k={sub_[4:]}]'); await pg.wait_for_timeout(150)
                    elif base == 'seiten' and sub_:
                        await pg.click(f'[data-act=sp][data-v={sub_}]'); await pg.wait_for_timeout(120)
                        if sub_ in ('chronik', 'fz') and await pg.locator('[data-act=s-new]').count(): await pg.click('[data-act=s-new] >> nth=0'); await pg.wait_for_timeout(120)
                    elif base == 'lthema':
                        await go('lplan'); await pg.click('[data-act=lt-new] >> nth=0'); await pg.wait_for_timeout(150)
                    if pay == XSS[0]: nomax += await pg.evaluate(TXT_NO_MAX)
                    ids = await pg.evaluate(FUZZ_JS, pay)
                    for fid in ids:
                        if await pg.locator(f'#{fid}').count() == 0: continue
                        btn = pg.locator(f'#{fid} button[type=submit]')
                        if await btn.count(): await btn.last.click(); await pg.wait_for_timeout(150)
                        if await pg.locator('#c-ok, [data-act=c-del-ok]').count() == 0: pass
                    fuzzed += [f'{role or "öffentlich"}:{r}']
            # alles einmal ansehen
            if not (await pg.evaluate('!!window.__demo.state().user')): await login('Freigeber')
            for r in PUBLIC + ['redaktion', 'beitraege', 'seiten', 'planung', 'lernen', 'lplan']:
                await go(r)
                if await pg.evaluate(HIT): break
            hit = await pg.evaluate(HIT)
            rec(not hit, f'N-05: Eingabe „{pay[:28]}…“ in allen Formularen wird nirgends ausgeführt', '' if not hit else await h())
        rec(len(set(fuzzed)) >= 12, 'N-05: Formulare aller Rollen wurden mit Schadcode befüllt', str(len(set(fuzzed))))
        rec(not nomax, 'B-20: jedes Textfeld hat eine Höchstlänge', ', '.join(sorted(set(nomax)))[:300])
        # Schadcode in der Adresse
        await fresh()
        for hsh in ['<img src=x onerror="window.__x=1">', '"><svg onload=window.__x=1>', 'thema?x=<script>window.__x=1</script>', '%3Cimg%20src%3Dx%20onerror%3Dwindow.__x%3D1%3E']:
            await pg.evaluate("(h) => location.hash = h", hsh); await pg.wait_for_timeout(150)
        h1 = await pg.evaluate("(document.querySelector('h1')||{}).textContent||''")
        rec(not await pg.evaluate(HIT) and 'Piflas' in h1, 'N-05: Schadcode in der Adresse wird ignoriert, Startseite erscheint', h1[:40])
        # Lernthema: nur https-Links, kein javascript:
        await fresh(); await login('Freigeber'); await go('lplan'); await pg.click('[data-act=lt-new] >> nth=0'); await pg.wait_for_timeout(150)
        lin = pg.locator('#f-lthema input[name^="lu"], #f-lthema input[name*="url"], #f-lthema input[type=url]')
        if await lin.count():
            await pg.fill('#f-lthema [name=t]', 'Linktest'); await lin.first.fill('javascript:window.__x=1'); await pg.click('#f-lthema button[value=pub]') if await pg.locator('#f-lthema button[value=pub]').count() else None
            await pg.wait_for_timeout(150)
            bad_l = await pg.evaluate("window.__demo.state().topics.some(x => x.links.some(l => /^javascript:/i.test(l.u)))")
            rec(not bad_l and 'https://' in await pg.inner_text('#e-lthema'), 'E-04/N-05: „javascript:“-Link im Lernthema wird abgewiesen')
        else:
            rec(False, 'E-04/N-05: Link-Feld im Lernthema gefunden')
        # Partner-Link im System-Bereich: nur https
        await fresh(); await login('Administrator'); await go('system')
        pl = pg.locator('#f-settings input[name^="p"]')
        if await pl.count():
            await pl.first.fill('javascript:window.__x=1'); await pg.click('#f-settings button[type=submit]'); await pg.wait_for_timeout(150)
            rec('https://' in await pg.inner_text('#e-settings'), 'N-05: System-Bereich weist „javascript:“-Link ab')
            await go('partner'); hrefs = await pg.eval_on_selector_all('main a[target=_blank]', 'els => els.map(e => e.getAttribute("href"))')
            rec(all(x.startswith('https://') for x in hrefs) and hrefs, 'N-05: Partner-Links bleiben https, „javascript:“ wird nicht übernommen', str(hrefs)[:120])
        else:
            rec(False, 'N-05: Partner-Link-Feld im System-Bereich gefunden')

        # ================= 3. Anmeldung (B-05, B-08, B-01) =================
        await fresh(); await go('login')
        async def try_login(mail, code=None):
            if await pg.locator('#f-login').count():
                await pg.fill('#f-login [name=mail]', mail); await pg.fill('#f-login [name=pw]', 'falsch-falsch'); await pg.click('#f-login button[type=submit]'); await pg.wait_for_timeout(120)
            if code is not None and await pg.locator('#f-2fa').count():
                await pg.evaluate("(c) => document.querySelector('#f-2fa [name=code]').value = c", code); await pg.click('#f-2fa button[type=submit]'); await pg.wait_for_timeout(120)
        await try_login('niemand@beispiel.de'); m1 = await pg.inner_text('#e-login')
        rec('stimmt nicht' in m1 and 'gibt es nicht' not in m1 and 'unbekannt' not in m1, 'B-01: Fehlermeldung verrät nicht, ob es das Konto gibt', m1[:80])
        for _ in range(4): await try_login('niemand@beispiel.de')
        rec('gesperrt' in await pg.inner_text('#e-login'), 'B-05: nach 5 Fehlversuchen ist die Anmeldung gesperrt', (await pg.inner_text('#e-login'))[:80])
        await try_login('max@beispiel.de')
        rec(await pg.locator('#f-2fa').count() == 0 and 'gesperrt' in await pg.inner_text('#e-login') and not await pg.evaluate('!!window.__demo.state().user'), 'B-05: auch ein echtes Konto kommt während der Sperre nicht hinein')
        await fresh(); await go('login')
        for _ in range(5): await try_login('max@beispiel.de', '12ab')
        rec('gesperrt' in await pg.inner_text('#e-login') and not await pg.evaluate('!!window.__demo.state().user'), 'B-05: falsche 2-Faktor-Codes zählen als Fehlversuche')
        # Passwort vergessen – gleiche Antwort für bekannte und unbekannte Adressen
        await fresh(); await go('login'); await pg.click('[data-act=pw-forgot]'); await pg.wait_for_timeout(120)
        out = []
        for mail in ['max@beispiel.de', 'niemand@beispiel.de']:
            if not await pg.locator('#f-pw').count(): await pg.click('[data-act=pw-forgot]'); await pg.wait_for_timeout(100)
            await pg.fill('#f-pw [name=m]', mail); await pg.click('#f-pw button[type=submit]'); await pg.wait_for_timeout(120); out.append(await toast())
        rec(out[0] == out[1] and 'Wenn es ein Konto' in out[0], 'B-05: „Passwort vergessen“ antwortet immer gleich (kein Konto-Verrat)', out[0][:70])
        # Austritt (B-08)
        await fresh(); await login('Administrator'); await go('mitglieder')
        jonas = pg.locator('#mlist .card', has_text='Jonas Beispiel')
        await jonas.locator('[data-act=m-off]').click(); await pg.wait_for_timeout(120)
        rec(await pg.locator('#moff-ask').count() == 1 and 'bleiben erhalten' in await pg.inner_text('#moff-ask'), 'B-08: Deaktivieren fragt nach und sagt, dass Beiträge bleiben')
        await pg.click('#moff-ask [data-act=m-off-ok]'); await pg.wait_for_timeout(150)
        rec('Deaktiviert' in await jonas.inner_text() and await jonas.locator('[data-act=m-on]').count() == 1, 'B-08: Konto deaktiviert, nicht gelöscht, wieder aktivierbar')
        n_by = await pg.evaluate("window.__demo.state().news.filter(n => n.by === 'Jonas Beispiel').length")
        rec(await pg.evaluate("!window.__demo.state().results.some(r => r.u === 'Jonas Beispiel')"), 'B-08/E-11: beim Austritt werden die Lernergebnisse sofort gelöscht')
        rec(n_by > 0, 'B-08: Beiträge der ausgetretenen Person bleiben erhalten', str(n_by))
        await logout(); await go('login'); await try_login('jonas@beispiel.de')
        rec(await pg.locator('#f-2fa').count() == 0 and 'stimmt nicht' in await pg.inner_text('#e-login'), 'B-08: deaktiviertes Konto kann sich nicht anmelden (gleiche Meldung wie unbekannt)')
        await fresh(); await login('Administrator'); await go('mitglieder')
        rec(await pg.locator('#mlist .card', has_text='Erika Musterfrau').locator('[data-act=m-off]').count() == 0, 'B-08: eigenes Konto nicht deaktivierbar')
        other = pg.locator('#mlist .card').filter(has=pg.locator('.tag', has_text='Admin')).filter(has_not_text='Erika Musterfrau')
        if await other.count():
            await other.first.locator('[data-act=m-off]').click(); await pg.wait_for_timeout(100); await pg.click('#moff-ask [data-act=m-off-ok]'); await pg.wait_for_timeout(150)
            rec(await pg.evaluate("window.__demo.state().members.filter(m => m.r === 'Administrator' && !m.inv && !m.off).length") >= 2, 'A-08: der zweite Admin kann nicht deaktiviert werden')
        else:
            rec(False, 'A-08: zweiter Admin in der Kontenliste gefunden')
        # Rolle eines deaktivierten oder des eigenen Kontos lässt sich auch ohne Knopf nicht ändern
        s0 = await pg.evaluate(SNAP)
        await pg.evaluate("(() => { const d = window.__demo, S = d.state(); S.rch = S.members.findIndex(m => m.n === S.user.name); d.render(); })()")
        await pg.evaluate("""() => { const f = document.createElement('form'); f.id = 'f-role'; f.innerHTML = '<select name="r"><option value="Mitglied" selected>M</option></select><input type="checkbox" name="akt" checked><button type="submit">s</button>'; document.body.appendChild(f); f.requestSubmit(); f.remove(); }""")
        await pg.wait_for_timeout(120)
        rec(await pg.evaluate("window.__demo.state().members.find(m => m.n === window.__demo.state().user.name).r") == 'Administrator', 'B-02: die eigene Rolle lässt sich auch ohne Knopf nicht ändern')

        # ================= 4. Ausfallsicherheit (D-08, A-10, A-11, I-01) =================
        await fresh()
        await pg.evaluate("(() => { const d = window.__demo, S = d.state(); S.iface = {div:{st:'bad', code:'DIV-FMT', man:false}, ig:{st:'bad', code:'IG-190', man:false}}; d.render(); })()")
        bad = []
        for r in PUBLIC:
            await go(r); t = await pg.inner_text('body')
            if not (await pg.evaluate("(document.querySelector('h1')||{}).textContent||''")).strip() or any(x in t for x in ['DIV-', 'IG-190', 'Fehler', 'Störung', 'undefined', 'NaN']): bad.append(r)
        rec(not bad, 'D-08/A-11: beide Schnittstellen gestört – alle öffentlichen Seiten laufen, Besucher sehen keine Fehlermeldung', ', '.join(bad))
        await go('start'); rec(await pg.locator('#ig-fallback').count() == 1 and await pg.locator('.ig img').count() == 0, 'I-01/A-11: Instagram gestört – statt Vorschau nur ein Link zum Profil')
        q0 = await pg.evaluate('window.__demo.state().queue.length')
        await login('Freigeber'); await act({'act': 'alarm'}); await pg.wait_for_timeout(200)
        rec(await pg.evaluate('window.__demo.state().queue.length') == q0, 'A-10: DIV-FMT – bei geänderter Antwort wird nichts übernommen')
        await go('redaktion'); rec('von Hand' in await pg.inner_text('main'), 'D-08: Freigabe zeigt bei Störung „Einsatz von Hand anlegen“')
        await go('termine'); rec(await pg.locator('.list .li, .list > *').count() > 0, 'D-08: bei DIVERA-Störung bleiben die bisherigen Termine sichtbar')
        # Doppelklick beim Veröffentlichen erzeugt nichts doppelt
        await fresh(); await login('Freigeber'); await go('redaktion')
        n0 = await pg.evaluate('window.__demo.state().news.length + window.__demo.state().einsaetze?.length || 0')
        q0 = await pg.evaluate('window.__demo.state().queue.length')
        card = pg.locator('[data-act=publish]').first
        qid = await card.get_attribute('data-id')
        await pg.locator(f'.q[data-id="{qid}"] input[type=checkbox], #q-{qid} input[type=checkbox]').first.check() if await pg.locator(f'#q-{qid} input[type=checkbox]').count() else None
        await pg.evaluate("(id) => { const b = document.querySelector(`[data-act=publish][data-id='${id}']`); if (b) { b.click(); b.click(); } }", qid); await pg.wait_for_timeout(200)
        q1 = await pg.evaluate('window.__demo.state().queue.length')
        rec(q0 - q1 <= 1, 'Robustheit: Doppelklick auf „Veröffentlichen“ veröffentlicht höchstens einmal', f'{q0}→{q1}')
        # Doppelt abgeschickter Beitrag
        await go('beitraege'); await pg.click('[data-act=new][data-k=n]'); await pg.wait_for_timeout(150)
        await pg.fill('#f-post [name=t]', 'Doppelklick-Test'); await pg.fill('#f-post [name=txt]', 'Text für den Doppelklick-Test.')
        for c in await pg.locator('#f-post input[type=checkbox][required], #f-post input[name=ok]').all(): await c.check()
        await pg.evaluate("() => { const f = document.querySelector('#f-post'); const b = f.querySelector('button[type=submit]'); b.click(); b.click(); }"); await pg.wait_for_timeout(250)
        dup = await pg.evaluate("window.__demo.state().news.filter(n => n.t === 'Doppelklick-Test').length")
        rec(dup <= 1, 'Robustheit: doppelt abgeschickter Beitrag entsteht nur einmal', str(dup))
        # Wilde Adressen und schnelles Hin und Her
        await fresh()
        import random
        random.seed(7)
        for _ in range(60):
            r = random.choice(PUBLIC + BACKR + ['', '#', 'xyz', '../../etc', 'thema/999', 'n/9999', 'e/xyz'])
            await pg.evaluate("(h) => location.hash = h", r); await pg.wait_for_timeout(15)
        await pg.wait_for_timeout(200)
        rec(bool((await pg.evaluate("(document.querySelector('h1')||{}).textContent||''")).strip()), 'Robustheit: 60 schnelle, teils unsinnige Adressen – Seite bleibt bedienbar')
        # Sehr viel Inhalt: 1000 Beiträge
        await pg.evaluate("""(() => { const d = window.__demo, S = d.state(), b = S.news[0]; for (let i = 0; i < 1000; i++) S.news.push({...b, id: 'bulk' + i, t: 'Massentest ' + i}); d.render(); })()""")
        await go('aktuelles'); n_vis = await pg.locator('main .nk article, main article').count()
        rec(0 < n_vis <= 30, 'Robustheit: 1000 Beiträge – Aktuelles zeigt seitenweise, nicht alles auf einmal', str(n_vis))

        # ================= 5. Inhalte, die bisher nur indirekt geprüft waren =================
        await fresh()
        await go('termine'); rec(await pg.locator('[data-act=ical]').count() == 1 and await pg.locator('[data-act=vormerken]').count() > 0, 'F-04: Termine mit „Vormerken“ und Kalender-Abo')
        await go('jugend'); t = await pg.inner_text('main')
        rec('Schnuppern' in t and 'Einwilligung der Eltern' in t, 'F-07/L-11: Jugendfeuerwehr mit „Schnuppern“, Fotos nur mit Einwilligung der Eltern')
        ft = await pg.inner_text('footer')
        rec(all(x in ft for x in ['Impressum', 'Datenschutz', 'Instagram', 'Partner', 'Anmelden', 'Fotos: Feuerwehr Piflas']), 'F-12/N-10: Fußzeile mit Rechtstexten, Instagram, Partnern, Anmelden und Bildnachweis', ft[:120])
        rec('nicht ständig besetzt' in ft, 'F-12: Telefon mit Hinweis „nicht ständig besetzt“')
        await go('buerger'); t = await pg.inner_text('main')
        rec(all(x in t for x in ['112', 'Wo', 'Rettungsgasse']), 'C-01: Notruf (W-Fragen) und Rettungsgasse')
        rec('NINA' in t and 'Sirene' in t and 'Pegel' in t, 'C-02: Warn-App, Sirenensignale, Pegel-Link')
        rec('Rauchmelder' in t, 'C-03: Rauchmelderpflicht')
        links = []
        for r in ['start', 'mitmachen', 'jubilaeum']:
            await go(r); links.append(await pg.locator('main a[href="#foerdern"]').count())
        rec(all(links), 'S-01: „Fördermitglied werden“ von Startseite, Mitmachen und Jubiläum verlinkt', str(links))
        await go('foerdern'); t = await pg.inner_text('main')
        rec('[' in t or '€' in t, 'S-01: Höhe des Jahresbeitrags genannt oder als Platzhalter markiert')
        await login('Freigeber'); await act({'act': 'alarm'}); await pg.wait_for_timeout(250); await go('redaktion')
        th = await pg.locator('main').inner_text()
        rec('Polizei und Angehörige' in th, 'W-05/L-04: Warnhinweis bei technischer Hilfe')
        ig = pg.locator('main input[id^=ig-]')
        rec(await ig.count() > 0, 'W-06: eigenes Häkchen „Auch auf Instagram“ je Einreichung')
        root = await pg.evaluate("[getComputedStyle(document.documentElement).getPropertyValue('--rot').trim(), getComputedStyle(document.body).fontFamily]")
        rec(root[0].upper() == '#CD1719' and 'FwText' in root[1], 'N-08: Rot #CD1719 und selbst gehostete Roboto', str(root))
        rec(not ext, 'N-01/L-09: während aller Sicherheitstests keine Anfrage an fremde Server', ', '.join(ext[:3]))
        rec(not errs, 'Keine JS-Fehler während der Sicherheits- und Ausfalltests', '; '.join(errs)[:400])
        await br.close()
    fails = [r for r in results if not r[0]]
    print(f'\n{len(results)-len(fails)} von {len(results)} Sicherheits- und Ausfallprüfungen bestanden')
    json.dump(results, open(HERE / 'security_results.json', 'w'), ensure_ascii=False, indent=1)
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
