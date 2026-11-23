import re, base64, markdown, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
"""Erzeugt das Lastenheft als druckfertiges PDF (Deckblatt, Inhaltsverzeichnis, Diagramm).
Aufruf: python make_pdf.py   – nimmt die neueste lastenheft-vX.Y.md im selben Ordner (oder in ../lastenheft)
und schreibt Lastenheft-Feuerwehr-Piflas-vX.Y.pdf daneben. Braucht: pip install markdown playwright pypdf"""
import tempfile
HERE = Path(__file__).resolve().parent
L = HERE if list(HERE.glob('lastenheft-v*.md')) else HERE.parent / 'lastenheft'
def find(*c): return next(Path(x) for x in c if Path(x).exists())
SRC = max(L.glob('lastenheft-v*.md'), key=lambda f: tuple(int(x) for x in re.findall(r'\d+', f.stem)))
VER = '.'.join(re.findall(r'\d+', SRC.stem))
src = SRC.read_text()
REF = re.search(r'Referenz: (Demo \S+) und (Handbuch [\d.]+)', src); NTEST = re.search(r'Testsuite \((\d+) Prüfungen\)', src).group(1)
STAND = re.search(r'^(\d\d\.\d\d\.\d{4})', src.split('\n')[2]).group(1)
T = Path(tempfile.mkdtemp())
ROOT = L.parent
mark = '*[Architekturdiagramm: DIVERA, WordPress, Instagram, Mitglieder, GitHub, Website-Besuch – siehe Online-Dokument bzw. PDF]*'
assert mark in src
p1, p2 = src.split(mark)
# Titelzeilen raus (stehen auf dem Deckblatt)
p1 = re.sub(r'^# .*?\n\n\d\d\.\d\d\.\d{4} · .*?\n\n', '', p1, flags=re.S)
DIAG = '''<figure class="diag"><svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="FwText, sans-serif">
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8a8d91"/></marker></defs>
<style>.b{fill:#fff;stroke:#c9c6bf;stroke-width:1.5}.t{font-size:14px;font-weight:700;fill:#202124}.s{font-size:11.5px;fill:#5f6368}.l{font-size:11px;fill:#6b6e73}.ln{stroke:#8a8d91;stroke-width:1.4;fill:none;marker-end:url(#a)}</style>
<rect class="b" x="10" y="20" width="210" height="80" rx="10"/><text class="t" x="24" y="46">DIVERA 24/7</text><text class="s" x="24" y="66">Alarme und Termine</text><text class="s" x="24" y="82">per API (Zugangsschlüssel)</text>
<rect x="275" y="14" width="210" height="140" rx="10" fill="#FDECEC" stroke="#CD1719" stroke-width="2.2"/><text class="t" x="289" y="40" fill="#A31012">WordPress (euer Hosting)</text>
<text class="s" x="289" y="62">Theme „ff-piflas“</text><text class="s" x="289" y="79">Plugin Einsatzverwaltung</text><text class="s" x="289" y="96">Plugin ff-piflas-connect</text><text class="s" x="289" y="113">Rollen, 2FA, Backups, Ampel</text><text class="s" x="289" y="132" font-weight="700">Entwurf → Freigabe → online</text>
<rect class="b" x="540" y="20" width="210" height="80" rx="10"/><text class="t" x="554" y="46">Instagram</text><text class="s" x="554" y="66">Business-Konto</text><text class="s" x="554" y="82">Vorschau lesen, Posts veröffentlichen</text>
<rect class="b" x="10" y="230" width="210" height="80" rx="10"/><text class="t" x="24" y="256">Mitglieder mit Konto</text><text class="s" x="24" y="276">Admins, Kommandant, Redaktion</text><text class="s" x="24" y="292">Login mit 2FA, am Handy</text>
<rect class="b" x="275" y="230" width="210" height="80" rx="10"/><text class="t" x="289" y="256">GitHub</text><text class="s" x="289" y="276">Code für Theme und Plugin</text><text class="s" x="289" y="292">Deploy per SFTP</text>
<rect class="b" x="540" y="230" width="210" height="80" rx="10"/><text class="t" x="554" y="256">Website-Besuch</text><text class="s" x="554" y="276">Website ohne Cookies</text><text class="s" x="554" y="292">und ohne Tracking</text>
<path class="ln" d="M220,60 H273"/><text class="l" x="230" y="52">Sync</text>
<path class="ln" d="M485,48 H538"/><text class="l" x="497" y="42">Post</text>
<path class="ln" d="M540,76 H487"/><text class="l" x="497" y="92">Vorschau</text>
<path class="ln" d="M115,230 V130 H273"/><text class="l" x="125" y="124">pflegen, freigeben</text>
<path class="ln" d="M380,230 V156"/><text class="l" x="388" y="200">Updates</text>
<path class="ln" d="M485,130 H645 V228"/><text class="l" x="560" y="124">Website</text>
</svg><figcaption>Architektur: Mitglieder pflegen WordPress, DIVERA und Instagram laufen automatisch mit.</figcaption></figure>'''
md = p1.rstrip() + '\n\n@@DIAG@@\n\n' + p2.lstrip()
html = markdown.markdown(md, extensions=['tables','fenced_code','sane_lists'])
html = html.replace('<p>@@DIAG@@</p>', DIAG)
html = html.replace('<li>[ ] ', '<li class="cb">').replace('<li>\n<p>[ ] ', '<li class="cb">\n<p>')
# ID-Spalten nicht umbrechen
html = re.sub(r'<td>([A-Z]-\d\d)</td>', r'<td class="id">\1</td>', html)
html = re.sub(r'<td>(Muss|Soll|Kann)</td>', lambda m: f'<td class="prio {m.group(1).lower()}">{m.group(1)}</td>', html)
# Inhaltsverzeichnis aus h2/h3
toc=[]; n=[0]
def hid(m):
    n[0]+=1; lvl, txt = m.group(1), m.group(2); i=f'h{n[0]}'; toc.append((lvl, re.sub('<.*?>','',txt), i)); return f'<h{lvl} id="{i}">{txt}</h{lvl}>'
html = re.sub(r'<h([23])>(.*?)</h\1>', hid, html)
html = html.replace('<table>\n<thead>\n<tr>\n<th>Baustein</th>', '<table class="bs">\n<thead>\n<tr>\n<th>Baustein</th>')
tochtml = '<nav class="toc"><h2>Inhalt</h2><ol>' + ''.join(f'<li class="l{l}"><a href="#{i}">{t}</a></li>' for l,t,i in toc) + '</ol></nav>'
logo = base64.b64encode(find(ROOT/'assets'/'logo.svg', '/home/claude/ff-piflas-start/logo.svg').read_bytes()).decode()
font = base64.b64encode(find(ROOT/'assets'/'fonts'/'roboto-sub.woff', '/home/claude/fonts/roboto-sub.woff').read_bytes()).decode()
css = f'''
@font-face{{font-family:FwText;src:url(data:font/woff;base64,{font}) format("woff");font-weight:100 900;font-stretch:100%}}
@font-face{{font-family:FwCond;src:url(data:font/woff;base64,{font}) format("woff");font-weight:100 900;font-stretch:75%}}
@page{{size:A4;margin:22mm 18mm 20mm 18mm}}

*{{box-sizing:border-box}}
body{{font-family:FwText,sans-serif;font-size:9.6pt;line-height:1.45;color:#202124;margin:0}}
.cover{{height:296mm;width:210mm;position:relative;page-break-after:always;padding:30mm 22mm;background:#fff}}
.cover .bar{{position:absolute;left:0;top:0;bottom:0;width:12mm;background:#CD1719}}
.cover img{{width:95mm}}
.cover h1{{font-family:FwCond;font-weight:800;font-size:38pt;line-height:1.05;margin:38mm 0 6mm;color:#202124}}
.cover .sub{{font-size:15pt;color:#5f6368;margin:0 0 18mm}}
.cover table.meta{{width:auto;border:0;font-size:11pt}}
.cover table.meta td{{border:0;padding:3px 18px 3px 0;background:none}}
.cover table.meta td:first-child{{color:#6b6e73}}
.cover .foot{{position:absolute;left:22mm;right:22mm;bottom:22mm;font-size:9pt;color:#6b6e73;border-top:2px solid #CD1719;padding-top:4mm}}
.toc{{page-break-after:always}}
.toc ol{{list-style:none;padding:0;margin:0}}
.toc li{{padding:3px 0;border-bottom:1px dotted #d6d3cc}}
.toc li.l3{{padding-left:9mm;color:#3c4043}}
.toc li.l2{{font-weight:700;margin-top:6px}}
.toc a{{color:inherit;text-decoration:none}}
h2{{font-family:FwCond;font-weight:800;font-size:19pt;color:#CD1719;margin:0 0 4mm;padding-bottom:2mm;border-bottom:2px solid #CD1719;page-break-after:avoid}}
main h2{{page-break-before:always}}
main h2:first-child{{page-break-before:auto}}
h3{{font-family:FwCond;font-weight:700;font-size:13.5pt;margin:7mm 0 2.5mm;page-break-after:avoid;color:#202124}}
p{{margin:0 0 2.5mm}}
strong{{font-weight:700}}
ul,ol{{margin:0 0 3mm;padding-left:6mm}} li{{margin:0 0 1mm}}
li.cb{{list-style:none;margin-left:-5mm}} li.cb::before{{content:"☐ ";font-size:11pt;color:#CD1719}}
table{{width:100%;border-collapse:collapse;margin:1mm 0 4mm;font-size:8.6pt;page-break-inside:auto}}
thead{{display:table-header-group}}
tr{{page-break-inside:avoid}}
th{{background:#202124;color:#fff;text-align:left;font-weight:700;padding:4px 6px}}
td{{border-bottom:1px solid #e3e0da;padding:4px 6px;vertical-align:top}}
tbody tr:nth-child(even) td{{background:#f7f6f3}}
td.id{{white-space:nowrap;font-weight:700;color:#A31012;width:12mm}}
td.prio{{white-space:nowrap;width:12mm;font-weight:700}}
td.muss{{color:#A31012}} td.soll{{color:#8a5a00}} td.kann{{color:#5f6368}}
code{{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:8pt;background:#f1efea;padding:0 3px;border-radius:3px}}
pre{{background:#f7f6f3;border-left:3px solid #CD1719;padding:3mm 4mm;font-size:7.6pt;line-height:1.4;white-space:pre-wrap;page-break-inside:auto}}
pre code{{background:none;padding:0}}
a{{color:#A31012}}
table.bs td:nth-child(1){{width:24%;font-weight:700}} table.bs td:nth-child(2){{width:38%}} table.bs td:nth-child(3){{width:38%}}
figure.diag{{margin:3mm 0 5mm;page-break-inside:avoid}} figure.diag svg{{width:100%;height:auto}}
figcaption{{font-size:8.5pt;color:#6b6e73;margin-top:2mm}}
'''
doc = f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Lastenheft Webpräsenz Feuerwehr Piflas v{VER}</title><style>{css}</style></head><body>
<!--C--><section class="cover"><div class="bar"></div><img src="data:image/svg+xml;base64,{logo}" alt="Feuerwehr Piflas">
<h1>Lastenheft &amp;<br>Umsetzungsplan</h1><p class="sub">Webpräsenz der Freiwilligen Feuerwehr Piflas<br>www.feuerwehr-piflas.de</p>
<table class="meta"><tr><td>Version</td><td><b>{VER}</b> (WordPress)</td></tr><tr><td>Stand</td><td>{STAND}</td></tr><tr><td>Erstellt von</td><td>Korbinian</td></tr><tr><td>Referenz</td><td>{REF.group(1)} ({NTEST} Prüfungen), {REF.group(2).replace('Handbuch', 'Handbuch Mitgliederbereich')}</td></tr><tr><td>Status</td><td>Entwurf zur Abstimmung im Verein</td></tr></table>
<div class="foot">Feuerwehr Piflas e.V. · Gartenstraße 2 · 84030 Ergolding / Piflas · VR 1115 AG Landshut</div></section><!--/C-->
{tochtml}<main>{html}</main></body></html>'''
(T/'lastenheft.html').write_text(doc)
head, rest = doc.split('<!--C-->'); cover, body = rest.split('<!--/C-->')
(T/'cover.html').write_text(head.replace('</style>','@page{margin:0}</style>') + cover + '</body></html>')
(T/'body.html').write_text(head + body)
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto((T/'cover.html').as_uri()); await pg.wait_for_timeout(300)
        await pg.pdf(path=str(T/'cover.pdf'), format='A4', print_background=True, prefer_css_page_size=True)
        await pg.goto((T/'body.html').as_uri()); await pg.wait_for_timeout(500)
        hdr = '<div style="font-family:sans-serif;font-size:7.5pt;color:#8a8d91;width:100%;padding:0 18mm;display:flex;justify-content:space-between"><span>Lastenheft Webpräsenz Feuerwehr Piflas</span><span>Version '+VER+' · '+STAND+'</span></div>'
        ftr = '<div style="font-family:sans-serif;font-size:7.5pt;color:#8a8d91;width:100%;padding:0 18mm;display:flex;justify-content:space-between"><span>Feuerwehr Piflas e.V.</span><span>Seite <span class="pageNumber"></span> von <span class="totalPages"></span></span></div>'
        await pg.pdf(path=str(T/'body.pdf'), format='A4', print_background=True, display_header_footer=True, header_template=hdr, footer_template=ftr, prefer_css_page_size=True, tagged=True, outline=True)
        await b.close()
asyncio.run(run())
from pypdf import PdfWriter, PdfReader
w = PdfWriter(); w.append(PdfReader(str(T/'cover.pdf'))); w.append(PdfReader(str(T/'body.pdf')))
w.add_metadata({'/Title':'Lastenheft & Umsetzungsplan – Webpräsenz Feuerwehr Piflas, Version '+VER,'/Author':'Korbinian, Feuerwehr Piflas e.V.','/Subject':'Lastenheft Website feuerwehr-piflas.de'})
OUT = L / f'Lastenheft-Feuerwehr-Piflas-v{VER}.pdf'
w.write(str(OUT)); print('PDF:', OUT)
