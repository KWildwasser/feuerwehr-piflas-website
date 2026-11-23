import re, base64, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from pypdf import PdfWriter, PdfReader
"""Erzeugt das Handbuch-PDF aus inhalt.html und den Bildschirmfotos in img/ (vorher shots.py ausführen)."""
H = Path(__file__).resolve().parent
ROOT = H.parent
def find(*c): return next(Path(x) for x in c if Path(x).exists())
body = (H/'inhalt.html').read_text()
toc=[]; n=[0]
def hid(m):
    n[0]+=1; lvl, txt = m.group(1), m.group(2); i=f'h{n[0]}'
    toc.append((lvl, re.sub(r'<span class="r.*?</span>','',re.sub(r'<(?!span)[^>]+>','',txt)).strip(), i)); return f'<h{lvl} id="{i}">{txt}</h{lvl}>'
body = re.sub(r'<h([23])>(.*?)</h\1>', hid, body)
toc = [(l, re.sub('<.*?>','',t).strip(), i) for l,t,i in toc]
tochtml = '<nav class="toc"><h2>Inhalt</h2><ol>' + ''.join(f'<li class="l{l}"><a href="#{i}">{t}</a></li>' for l,t,i in toc) + '</ol></nav>'
logo = base64.b64encode(find(ROOT/'assets'/'logo.svg', '/home/claude/ff-piflas-start/logo.svg').read_bytes()).decode()
font = base64.b64encode(find(ROOT/'assets'/'fonts'/'roboto-sub.woff', '/home/claude/fonts/roboto-sub.woff').read_bytes()).decode()
css = f'''
@font-face{{font-family:FwText;src:url(data:font/woff;base64,{font}) format("woff");font-weight:100 900;font-stretch:100%}}
@font-face{{font-family:FwCond;src:url(data:font/woff;base64,{font}) format("woff");font-weight:100 900;font-stretch:75%}}
@page{{size:A4;margin:20mm 17mm 19mm 17mm}}
*{{box-sizing:border-box}}
body{{font-family:FwText,sans-serif;font-size:10.4pt;line-height:1.5;color:#1F2328;margin:0}}
.cover{{height:296mm;width:210mm;position:relative;padding:30mm 22mm}}
.cover .bar{{position:absolute;left:0;top:0;bottom:0;width:12mm;background:#CD1719}}
.cover img{{width:95mm}}
.cover h1{{font-family:FwCond;font-weight:800;font-size:40pt;line-height:1.05;margin:36mm 0 6mm}}
.cover .sub{{font-size:15pt;color:#4A4F55;margin:0 0 16mm}}
.cover .rollen{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14mm}}
.cover table{{font-size:11pt;border:0}} .cover td{{border:0;padding:3px 18px 3px 0;background:none!important}} .cover td:first-child{{color:#5B6168}}
.cover .foot{{position:absolute;left:22mm;right:22mm;bottom:22mm;font-size:9pt;color:#5B6168;border-top:2px solid #CD1719;padding-top:4mm}}
.toc{{page-break-after:always}} .toc ol{{list-style:none;padding:0;margin:0}}
.toc li{{padding:2.2px 0;border-bottom:1px dotted #d6d3cc;font-size:9.6pt}} .toc li.l2{{font-weight:700;margin-top:6px}} .toc li.l3{{padding-left:9mm;color:#4A4F55}}
.toc a{{color:inherit;text-decoration:none}}
h2{{font-family:FwCond;font-weight:800;font-size:21pt;color:#CD1719;margin:0 0 4mm;padding-bottom:2mm;border-bottom:2px solid #CD1719;page-break-after:avoid;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
main h2{{page-break-before:always}} main h2:first-child{{page-break-before:auto}}
h3{{font-family:FwCond;font-weight:700;font-size:14.5pt;margin:6mm 0 2.5mm;page-break-after:avoid}}
p{{margin:0 0 2.5mm}} ul,ol{{margin:0 0 3mm;padding-left:6mm}} li{{margin:0 0 1.4mm}}
ol.steps{{list-style:none;counter-reset:s;padding-left:0}}
ol.steps>li{{counter-increment:s;position:relative;padding-left:10mm;margin-bottom:2.2mm}}
ol.steps>li::before{{content:counter(s);position:absolute;left:0;top:0;width:6.5mm;height:6.5mm;border-radius:50%;background:#CD1719;color:#fff;font-weight:700;font-size:9pt;display:flex;align-items:center;justify-content:center}}
.two{{display:grid;grid-template-columns:1.25fr 1fr;gap:7mm;align-items:start;margin-bottom:3mm}}
figure.shot{{margin:0 0 3mm;page-break-inside:avoid}}
figure.shot img{{width:100%;border:1px solid #E4E2DD;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.08);display:block}}
.two figure.shot img{{max-height:125mm;object-fit:contain;object-position:top}}
main > figure.shot img{{width:48mm;margin:0 auto}} main > figure.shot{{text-align:center}}
figure.sm img{{width:62%}}
figcaption{{font-size:8.5pt;color:#5B6168;margin-top:1.5mm}}
.note{{font-size:9.3pt;color:#4A4F55;border-left:3px solid #E4E2DD;padding-left:3mm}}
.box{{background:#F4F3F0;border-radius:8px;padding:4mm 5mm;margin:3mm 0 4mm;page-break-inside:avoid}}
.box.warn{{background:#FFF6DB;border:1px solid #F3E3B0}}
.box .two{{grid-template-columns:1fr 1fr;margin:2mm 0}}
.ok{{color:#1E6B35;font-weight:700;margin:0 0 1mm}} .no{{color:#A51214;font-weight:700;margin:0 0 1mm}}
ul.cl{{list-style:none;padding-left:0}} ul.cl li::before{{content:"☐  ";color:#CD1719;font-size:12pt}}
table{{width:100%;border-collapse:collapse;margin:1mm 0 4mm;font-size:9.3pt}}
thead{{display:table-header-group}} tr{{page-break-inside:avoid}}
th{{background:#1F2328;color:#fff;text-align:left;padding:5px 6px}} td{{border-bottom:1px solid #E4E2DD;padding:5px 6px;vertical-align:top}}
tbody tr:nth-child(even) td{{background:#F8F7F4}}
.r{{display:inline-block;font-family:FwText;font-size:8.5pt;font-weight:700;padding:2px 8px;border-radius:99px;color:#fff;vertical-align:middle;letter-spacing:.02em}}
.r.a{{background:#4A4F55}} .r.f{{background:#A51214}} .r.ad{{background:#1F2328}}
.g{{color:#1E6B35;font-weight:700}} .y{{color:#8A5A00;font-weight:700}} .rd{{color:#A51214;font-weight:700}}
dl.faq dt{{font-weight:700;margin-top:3mm}} dl.faq dd{{margin:1mm 0 0 0}}
'''
cover = f'''<section class="cover"><div class="bar"></div><img src="data:image/svg+xml;base64,{logo}" alt="Feuerwehr Piflas">
<h1>Handbuch<br>Mitgliederbereich</h1><p class="sub">So pflegst du die Website der Feuerwehr Piflas –<br>Schritt für Schritt, am Handy, ohne IT-Kenntnisse.</p>
<div class="rollen"><span class="r a">Alle</span><span class="r f">Kommandant</span><span class="r ad">Admin</span></div>
<table><tr><td>Version</td><td><b>1.11</b></td></tr><tr><td>Stand</td><td>23.11.2026 (auf Basis der Demo v12)</td></tr><tr><td>Grundlage</td><td>Lastenheft v1.13, E-15 bis E-28, B-02, B-22, u. a. A-06, A-10 bis A-12, B-01, B-07, B-13 bis B-21, D-09, W-09, E-01 bis E-14</td></tr><tr><td>Pflege</td><td>Admins – bei jeder neuen Funktion ergänzen</td></tr></table>
<div class="foot">Feuerwehr Piflas e.V. · Gartenstraße 2 · 84030 Ergolding / Piflas · Nur für Mitglieder mit Zugang</div></section>'''
head = f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Handbuch Mitgliederbereich – Website Feuerwehr Piflas</title><style>{css}</style></head><body>'
(H/'cover.html').write_text(head.replace('</style>','@page{margin:0}</style>') + cover + '</body></html>')
(H/'body.html').write_text(head + tochtml + '<main>' + body + '</main></body></html>')
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto((H/'cover.html').as_uri()); await pg.wait_for_timeout(300)
        await pg.pdf(path=str(H/'cover.pdf'), format='A4', print_background=True, prefer_css_page_size=True)
        await pg.goto((H/'body.html').as_uri()); await pg.wait_for_timeout(600)
        hdr = '<div style="font-family:sans-serif;font-size:7.5pt;color:#8a8d91;width:100%;padding:0 17mm;display:flex;justify-content:space-between"><span>Handbuch Mitgliederbereich · Website Feuerwehr Piflas</span><span>Version 1.11 · 23.11.2026</span></div>'
        ftr = '<div style="font-family:sans-serif;font-size:7.5pt;color:#8a8d91;width:100%;padding:0 17mm;display:flex;justify-content:space-between"><span>Feuerwehr Piflas e.V. · nur für Mitglieder mit Zugang</span><span>Seite <span class="pageNumber"></span> von <span class="totalPages"></span></span></div>'
        await pg.pdf(path=str(H/'body.pdf'), format='A4', print_background=True, display_header_footer=True, header_template=hdr, footer_template=ftr, prefer_css_page_size=True, tagged=True, outline=True)
        await b.close()
asyncio.run(run())
w = PdfWriter(); w.append(PdfReader(str(H/'cover.pdf'))); w.append(PdfReader(str(H/'body.pdf')))
w.add_metadata({'/Title':'Handbuch Mitgliederbereich – Website Feuerwehr Piflas','/Author':'Feuerwehr Piflas e.V.','/Subject':'Anleitung für Redaktion, Kommandant und Admins'})
w.write(str(H/'Handbuch-Website-Feuerwehr-Piflas.pdf'))
