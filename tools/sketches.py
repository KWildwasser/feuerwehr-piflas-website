"""Eigene Skizzen für die Beispiel-Lernthemen (keine fremden Grafiken). Erzeugt docs/demo/sketches.js"""
import json, pathlib
F = 'font-family="Roboto, Arial, sans-serif"'
def svg(body, h=360):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 {h}" {F}><rect width="640" height="{h}" rx="18" fill="#F4F3F0"/>{body}</svg>'
def tri(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0-34 30 18H-30z" fill="#fff" stroke="#CD1719" stroke-width="7" stroke-linejoin="round"/>'
            f'<path d="M0-12v14" stroke="#1F2328" stroke-width="5" stroke-linecap="round"/><circle cx="0" cy="10" r="3" fill="#1F2328"/>'
            f'<path d="M0 18v26" stroke="#555B62" stroke-width="4"/></g>')
def cone(x, y):
    return f'<path d="M{x-9} {y} {x-3} {y-28}h6l6 28z" fill="#E8590C"/><path d="M{x-6} {y-12}h12" stroke="#fff" stroke-width="4"/><rect x="{x-13}" y="{y}" width="26" height="5" rx="2" fill="#555B62"/>'
def truck(x, y):
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="92" height="40" rx="6" fill="#CD1719"/><rect x="66" y="6" width="20" height="14" rx="3" fill="#CFE3F7"/>'
            f'<rect x="8" y="10" width="50" height="5" fill="#fff"/><rect x="56" y="-7" width="16" height="7" rx="2" fill="#1C6DD0"/>'
            f'<circle cx="20" cy="42" r="8" fill="#1F2328"/><circle cx="72" cy="42" r="8" fill="#1F2328"/></g>')
def car(x, y):
    return (f'<g transform="translate({x} {y})"><path d="M0 26v-10l12-14h34l14 14v10z" fill="#8A8F96"/><rect x="14" y="5" width="30" height="11" rx="2" fill="#CFE3F7"/>'
            f'<circle cx="13" cy="28" r="7" fill="#1F2328"/><circle cx="47" cy="28" r="7" fill="#1F2328"/></g>')
def txt(x, y, t, size=18, w=600, fill="#1F2328", anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{t}</text>'
def dim(x1, x2, y, label):
    return (f'<path d="M{x1} {y}H{x2}" stroke="#1F2328" stroke-width="2.5" stroke-dasharray="6 5"/><path d="M{x1} {y-9}v18M{x2} {y-9}v18" stroke="#1F2328" stroke-width="2.5"/>'
            + txt((x1 + x2) / 2, y - 12, label, 17, 700, anchor="middle"))

S = {}
# 1 Verkehrsabsicherung: Abstände
b = txt(24, 44, 'Erste Warnung vor der Einsatzstelle', 28, 800)
b += txt(24, 76, 'Vor Kurven und Kuppen weiter vorziehen', 21, 600, '#555B62')
b += '<rect x="0" y="170" width="640" height="104" fill="#5B5F64"/><path d="M0 222H640" stroke="#fff" stroke-width="4" stroke-dasharray="26 18"/>'
b += car(18, 232) + '<path d="M92 250h34" stroke="#fff" stroke-width="5" stroke-linecap="round"/><path d="M118 242l10 8-10 8" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
b += tri(214, 140) + tri(408, 140) + cone(470, 268) + cone(500, 268) + cone(530, 268) + truck(540, 226)
b += txt(214, 306, 'Landstraße', 21, 700, anchor="middle") + txt(214, 334, 'ca. 200 m', 25, 800, '#CD1719', anchor="middle")
b += txt(408, 306, 'Innerorts', 21, 700, anchor="middle") + txt(408, 334, 'ca. 100 m', 25, 800, '#CD1719', anchor="middle")
b += txt(562, 306, 'Einsatzstelle', 21, 700, anchor="middle")
b += txt(24, 368, 'Autobahn: gestaffelt bei ca. 400, 600, 800 m', 20, 600, '#555B62')
S['sk-vk-strecke'] = (svg(b, 392), 'Skizze: Straße mit Fahrzeug der Feuerwehr an der Einsatzstelle rechts. Warndreiecke stehen innerorts etwa 100 Meter, auf der Landstraße etwa 200 Meter davor. Auf der Autobahn wird bei etwa 400, 600 und 800 Metern gewarnt.')

# 2 Warnkleidung
b = txt(24, 44, 'Sehen und gesehen werden', 28, 800)
b += '<circle cx="170" cy="96" r="30" fill="#E9C9A8"/><path d="M128 84a42 30 0 0 1 84 0z" fill="#CD1719"/><rect x="126" y="78" width="88" height="10" rx="5" fill="#1F2328"/>'
b += '<path d="M112 136h116l18 120h-32l-6 70h-76l-6-70H94z" fill="#F2D21B"/>'
b += '<rect x="104" y="186" width="132" height="12" fill="#C9CDD2"/><rect x="104" y="214" width="132" height="12" fill="#C9CDD2"/>'
b += '<rect x="132" y="136" width="12" height="50" fill="#C9CDD2"/><rect x="196" y="136" width="12" height="50" fill="#C9CDD2"/>'
b += '<rect x="132" y="256" width="76" height="70" fill="#2B3A55"/>'
for i, t in enumerate(['Warnkleidung', 'EN ISO 20471,', 'mindestens Klasse 2', 'auch bei Tag', 'verkehrsabgewandt', 'arbeiten']):
    b += txt(280, 112 + i * 40 + (16 if i > 3 else 0), t, 27 if i < 4 else 22, 800 if i < 4 else 600, '#CD1719' if i == 2 else '#1F2328' if i < 4 else '#555B62')
S['sk-vk-weste'] = (svg(b), 'Skizze: Einsatzkraft mit gelber Warnweste und grauen Reflexstreifen. Daneben: Warnkleidung nach EN ISO 20471, mindestens Klasse 2, auch bei Tag; möglichst auf der verkehrsabgewandten Seite arbeiten.')

# 3 Erste Hilfe: Prüfen – Rufen – Drücken
b = txt(24, 44, 'Prüfen – Rufen – Drücken', 28, 800)
def step(cx, n, title, l1, l2, icon):
    return (f'<circle cx="{cx}" cy="150" r="62" fill="#fff" stroke="#CD1719" stroke-width="6"/>{icon}'
            f'<circle cx="{cx - 46}" cy="104" r="17" fill="#CD1719"/>' + txt(cx - 46, 111, str(n), 19, 800, '#fff', 'middle')
            + txt(cx, 254, title, 27, 800, anchor='middle') + txt(cx, 286, l1, 19, 600, '#555B62', 'middle') + txt(cx, 312, l2, 19, 600, '#555B62', 'middle'))
eye = '<path d="M80 150q30-30 60 0q-30 30-60 0z" fill="none" stroke="#1F2328" stroke-width="5"/><circle cx="110" cy="150" r="9" fill="#1F2328"/>'
phone = '<rect x="303" y="118" width="34" height="62" rx="7" fill="none" stroke="#1F2328" stroke-width="5"/>' + txt(320, 158, '112', 17, 800, '#CD1719', 'middle')
hands = '<ellipse cx="530" cy="150" rx="30" ry="16" fill="#E9C9A8" stroke="#1F2328" stroke-width="4"/><ellipse cx="530" cy="140" rx="26" ry="13" fill="#E9C9A8" stroke="#1F2328" stroke-width="4"/><path d="M530 176v20M520 186l10 10 10-10" fill="none" stroke="#CD1719" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
b += step(110, 1, 'Prüfen', 'ansprechen,', 'Atmung max. 10 s', eye)
b += step(320, 2, 'Rufen', 'Notruf 112,', 'AED holen lassen', phone)
b += step(530, 3, 'Drücken', '30 × drücken,', '2 × beatmen', hands)
b += '<path d="M188 150h40M220 140l10 10-10 10M398 150h40M430 140l10 10-10 10" fill="none" stroke="#555B62" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
S['sk-eh-ablauf'] = (svg(b, 340), 'Skizze in drei Schritten: 1. Prüfen – ansprechen, anfassen, Atmung höchstens 10 Sekunden prüfen. 2. Rufen – Notruf 112, AED holen lassen. 3. Drücken – 30-mal drücken, 2-mal beatmen.')

# 4 Herzdruckmassage
b = txt(24, 44, 'Herzdruckmassage (Erwachsene)', 28, 800)
b += '<path d="M70 330V170q0-50 50-62l40-10h80l40 10q50 12 50 62v160z" fill="#E9C9A8" stroke="#1F2328" stroke-width="4"/>'
b += '<path d="M200 120v150" stroke="#B98A63" stroke-width="4" stroke-dasharray="8 6"/>'
b += '<ellipse cx="200" cy="200" rx="40" ry="20" fill="#F7E3CF" stroke="#1F2328" stroke-width="4"/><ellipse cx="200" cy="190" rx="34" ry="16" fill="#F7E3CF" stroke="#1F2328" stroke-width="4"/>'
b += '<circle cx="200" cy="196" r="7" fill="#CD1719"/>'
b += '<path d="M248 196h80" stroke="#CD1719" stroke-width="3"/>'
rows = [('Mitte Brustkorb', 'Handballen übereinander'), ('5 bis 6 cm tief', 'danach ganz entlasten'), ('100–120 pro Minute', 'möglichst ohne Pausen'), ('30 : 2', '30 × drücken, 2 × beatmen')]
for i, (a, c) in enumerate(rows):
    b += txt(336, 102 + i * 66, a, 25, 800, '#CD1719' if i == 0 else '#1F2328') + txt(336, 128 + i * 66, c, 19, 600, '#555B62')
S['sk-eh-druck'] = (svg(b), 'Skizze: Oberkörper von vorn, zwei übereinandergelegte Handballen in der Mitte des Brustkorbs. Daneben: 5 bis 6 Zentimeter tief, 100- bis 120-mal pro Minute, 30-mal drücken und 2-mal beatmen.')

# 5 Gefahrenschema AAAA-C-EEEE
b = txt(24, 44, 'Gefahren: AAAA-C-EEEE', 28, 800)
def tile(x, y, letter, word, col, bg):
    return (f'<rect x="{x}" y="{y}" width="140" height="84" rx="12" fill="{bg}"/>' + txt(x + 12, y + 38, letter, 32, 800, col)
            + ''.join(f'<text x="{x + 14}" y="{y + 62 + j * 18 - (4 if ',' in word else 0)}" font-size="18" font-weight="700" fill="#1F2328">{w}</text>' for j, w in enumerate(word.split(', '))))
A = ['Atemgifte', 'Angst-, reaktion', 'Ausbreitung', 'Atomare, Gefahren']
E = ['Erkrankung, Verletzung', 'Explosion', 'Elektrizität', 'Einsturz']
for i, w in enumerate(A): b += tile(20 + i * 152, 62, 'A', w, '#A11214', '#FBEBEB')
b += tile(20, 160, 'C', 'Chemische, Stoffe', '#8A5A00', '#F9EEDA')
b += txt(176, 196, 'Bei jeder Erkundung', 24, 800) + txt(176, 226, 'durchgehen und melden.', 22, 600, '#555B62')
for i, w in enumerate(E): b += tile(20 + i * 152, 258, 'E', w, '#1D4F8C', '#E7F1FB')
S['sk-gf-matrix'] = (svg(b, 362), 'Übersicht als Kacheln: vier A für Atemgifte, Angstreaktion, Ausbreitung und atomare Gefahren; C für chemische Stoffe; vier E für Erkrankung oder Verletzung, Explosion, Elektrizität und Einsturz.')

out = {k: 'data:image/svg+xml,' + __import__('urllib.parse').parse.quote(v[0]) for k, v in S.items()}
alts = {k: v[1] for k, v in S.items()}
p = pathlib.Path(__file__).resolve().parent.parent / 'docs/demo/sketches.js'
p.write_text('/* Eigene Skizzen für die Beispielthemen – erzeugt mit tools/sketches.py */\nconst SKETCH = ' + json.dumps(out) + ';\nconst SKETCH_ALT = ' + json.dumps(alts, ensure_ascii=False) + ';\n')
for k, v in S.items(): (pathlib.Path(__file__).resolve().parent.parent / 'docs/demo/sketches' / f'{k}.svg').write_text(v[0])
print('ok', {k: len(v) for k, v in out.items()})
