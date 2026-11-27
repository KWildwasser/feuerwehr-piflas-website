"""Erzeugt docs/demo/ABDECKUNG.md: welche Lastenheft-ID welche Prüfung hat.
Aufruf aus dem Ordner docs:  python ../tools/abdeckung.py
Nach jeder neuen ID oder Prüfung neu erzeugen; „manual“ ergänzen, wenn eine Prüfung die ID nicht im Namen trägt."""
import re
L=open(sorted(__import__('glob').glob('lastenheft/lastenheft-v*.md'), key=lambda f: [int(x) for x in re.findall(r'\d+', f)])[-1]).read()
rows=re.findall(r'^\| ([A-Z]-\d\d) \|(.*)$',L,re.M)
allids=[i for i,_ in rows]
desc,prio={},{}
for i,r in rows:
    c=[x.strip() for x in r.split('|')]
    d=c[0] if i[0] not in 'FL' else c[0]+': '+c[1]
    d=re.sub(r'\*\*','',d); desc[i]=(d[:70]+'…') if len(d)>70 else d
    cc=[x for x in c if x]; prio[i]=cc[-1] if cc[-1] in ('Muss','Soll','Kann') else ('Muss' if i[0] in 'NL' else '')
def expand(s):
    out=set()
    for a,b in re.findall(r'([A-Z]-\d\d) bis ([A-Z]-\d\d)',s):
        for x in allids:
            if x[0]==a[0] and int(a[2:])<=int(x[2:])<=int(b[2:]): out.add(x)
    out|=set(re.findall(r'[A-Z]-\d\d',s))
    for p in re.findall(r'(?<![A-Z-])([A-Z])-(?!\d)',s): out|={x for x in allids if x[0]==p}
    return out
area={}
for line in open('demo/README.md'):
    m=re.match(r'\| ([^|]+) \| ([^|]+) \| ([^|]+) \|',line)
    if m and m.group(1).strip() not in ('Bereich','---'):
        for i in expand(m.group(3)): area.setdefault(i,m.group(1).strip())
labs=[]
for f in ['demo/test_app.py','demo/test_security.py']:
    t=open(f).read()
    labs+=re.findall(r"rec\([^\n]*?,\s*f?'([^']{6,160})'",t)
manual={'F-05':'„Fahrzeugseite zeigt alle Fotos inkl. Wechsellader“','F-08':'„Chronik: sofort auf der Website“, „Partner: Verweis von der Verein-Seite“',
'A-02':'– (Sperre gibt es nur im WordPress-Theme)','A-04':'–','A-05':'–','A-06':'„Handbuch: für eingeloggte Benutzer im Kopf verlinkt“','A-07':'–','A-09':'–','A-12':'–',
'B-15':'„Redaktion: eigenen Beitrag ausblenden“','C-01':'„C-01: Notruf (W-Fragen) und Rettungsgasse“','C-05':'– (Soll)','C-06':'– (Kann)',
'D-01':'„Alarm simulieren führt zur Freigabe“','D-03':'–','D-05':'„Termin-Sync meldet Übernahme“, „Zweiter Sync legt nichts doppelt an“','D-06':'„Diagnose: neuer Schlüssel … wird nicht angezeigt“','D-07':'„Statistik zählt neuen Einsatz mit“',
'E-13':'– (Mail)','E-24':'– (Mail)','E-25':'Login zeigt „Auf diesem Gerät angemeldet bleiben“','E-28':'– (Laientest)',
'F-10':'„Recht/Impressum enthält …“, „Recht/Datenschutz enthält …“','F-13':'– (Soll, Joomla-Umzug)','F-14':'– (Kann)',
'I-02':'„Instagram-Kachel erscheint“','I-03':'–','I-04':'„Wartbarkeit: Instagram mit einem Klick neu verbinden“','I-05':'– (Kann)',
'J-07':'– (Soll)','M-01':'–','M-02':'„Wartbarkeit: Zustands-Ampel mit 6 Punkten“','M-03':'–','M-04':'„Recht/DSGVO: keine Anfragen an Dritte“',
'N-04':'–','N-06':'–','N-07':'–','N-10':'„F-12/N-10: Fußzeile … Bildnachweis“','N-11':'Diese Liste','N-12':'–',
'R-01':'„Thema einplanen“','R-02':'– (Soll)','R-03':'„Einsatz von Hand: 2-Stunden-Regel …“ (gleiche Zeitsteuerung)','R-04':'– (Mail)',
'S-02':'„Beitrittserklärung-PDF verlinkt“','S-03':'– (Soll)','W-01':'„E-Mail: an alle Kommandanten …“','W-02':'„Badge zeigt offene Freigaben“','W-03':'„Einsatz-Freigabe: echte Fotos hinzufügen …“','W-07':'„Zurückgeben mit Hinweis …“, „Entwurf verwerfen …“',
'L-01':'„Recht/Impressum enthält …“','L-02':'„E-Mail: nur Hinweis, keine Inhalte …“','L-12':'Seitenrundgang „Barrierefreiheit-Basics“','L-13':'„Recht/Impressum: Hinweis zu externen Links“','L-14':'„E-04: Lernbar nur als Link“','L-15':'„E-11/E-12: Hinweis …“','L-16':'„E-09: Mitglied sieht keine Ergebnisse oder Namen anderer“','L-17':'„E-12: Sicherheitshinweis“',
}
server={'F':'Playwright gegen die Testseite (übertragene Demo-Prüfungen)','D':'PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf','W':'PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf','I':'PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto','B':'PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf','M':'Abnahme von Hand: Dienst einrichten, Ausfall simulieren, Mail prüfen','C':'Playwright: Inhalte; jährliche Prüfung durch den Kommandanten','S':'Playwright','R':'PHPUnit: Zeitsteuerung und Erinnerungen per Cron; Playwright','J':'PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright','E':'PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf','A':'Abnahme von Hand bzw. Checkliste (Phase 7)','N':'Lighthouse, axe, Security-Header-Scan, Playwright','L':'Prüfung durch Fachperson bzw. Markt; technische Teile per Test'}
special={'A-09':'Laientest mit drei Mitgliedern (Phase 7)','A-08':'Übergabe-Übung mit Wiederherstellung','A-12':'Reparatur-Probe nach der Anleitung (unter 2 Stunden)','A-07':'Checkliste: Verträge und Tresor','A-05':'Plugin-Liste in docs/plugins.md prüfen','A-02':'Redaktion versucht Farben oder Layout zu ändern – gesperrt','A-04':'Auto-Update und Backup im Monatsbericht sichtbar','N-04':'Lighthouse mobil ≥ 90','N-06':'Wiederherstellung auf der Testseite proben','N-07':'Kostenaufstellung beim Go-live','N-12':'Sitemap und strukturierte Daten prüfen','D-06':'Code-Suche: Schlüssel nur in wp-config.php; Diagnosebericht ohne Schlüssel','E-28':'Laientest mit drei Mitgliedern und einem Kommandanten'}

out=['# Testabdeckung: Lastenheft-IDs → Prüfungen','',
'Stand 27.11.2026 · Lastenheft 1.21 · Demo v17 · `test_app.py` (703 Prüfungen) und `test_security.py` (68 Prüfungen)','',
'So lesen: „Demo“ nennt, wo die Referenz-Demo die Anforderung prüft (Testname oder Bereich der Testsuite). „Echte Website“ sagt, wie sie in WordPress zusätzlich geprüft wird. „–“ heißt: in der Demo nicht prüfbar (Server, Mail, Menschen, Verträge). Diese Liste ist die Abnahmeliste für Claude Code: Jede Zeile braucht vor dem Go-live einen grünen Test oder eine abgehakte Abnahme.','',
'| ID | Prio | Anforderung | Demo | Echte Website |','| --- | --- | --- | --- | --- |']
cnt=[0,0]
for i in sorted(desc,key=lambda x:(x[0],int(x[2:]))):
    hits=[l for l in labs if re.search(r'(?<![A-Z])'+re.escape(i)+r'(?!\d)',l)]
    if hits: d=f'{len(hits)}× direkt, z. B. „{re.sub(r"[{}]","",hits[0])[:55]}“'
    elif i in area: d=f'Bereich „{area[i]}“'
    else: d=manual.get(i,'–')
    cnt[0 if not d.startswith('–') else 1]+=1
    out.append(f'| {i} | {prio[i]} | {desc[i].replace("|","/")} | {d} | {special.get(i,server[i[0]])} |')
out+=['',f'**Summe:** {len(desc)} Anforderungen. {cnt[0]} prüft die Demo, {cnt[1]} lassen sich nur in der echten Website oder von Hand prüfen.','',
'## Sicherheit und Ausfallsicherheit (`test_security.py`)','',
'- **Rechte (B-03):** Rolle × Bereich als Matrix; jede schreibende Aktion und jedes Formular auch ohne sichtbaren Knopf – verbotene ändern nichts und melden „Dafür fehlen dir die Rechte“.',
'- **Eingaben (N-05, B-20):** Schadcode in allen Formularen aller Rollen und in der Adresse wird nie ausgeführt; jedes Textfeld hat eine Höchstlänge; externe Links nur mit https:// (beim Speichern und bei der Ausgabe).',
'- **Anmeldung (B-01, B-05, B-08):** keine Meldung verrät, ob es ein Konto gibt; Sperre nach 5 Fehlversuchen, auch beim 2-Faktor-Code; „Passwort vergessen“ antwortet immer gleich; Austritt deaktiviert statt löscht, Beiträge bleiben; eigenes Konto und zweiter Admin geschützt.',
'- **Ausfall (D-08, A-10, A-11, I-01):** beide Schnittstellen gestört – öffentliche Seiten laufen ohne Fehlermeldung; geänderte DIVERA-Antwort übernimmt nichts; Doppelklick und doppeltes Absenden erzeugen nichts doppelt; 60 wilde Adressen; 1.000 Beiträge.',
'','**In WordPress zusätzlich:** Nonce je Formular, `current_user_can()` je Aktion, PHPCS mit WordPress-Sicherheitsregeln (Escaping, Sanitizing), Security-Header-Scan, Login-Drosselung auf dem Server, Backup-Wiederherstellung auf der Testseite.']
open('demo/ABDECKUNG.md','w').write('\n'.join(out)+'\n'); print(cnt)
