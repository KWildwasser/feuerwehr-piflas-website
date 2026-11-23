"""Eigene Skizzen für die Beispiel-Lernthemen (keine fremden Grafiken).

Einheitlicher Stil: 640 × 400, ruhiger heller Grund, wenige Farben (Rot #CD1719,
Anthrazit #1F2328, Grau), Linien 3 px, große Schrift (mind. 22 px, am Handy lesbar).
Erzeugt docs/demo/sketches.js (für die Demo) und docs/demo/sketches/*.svg.
Aufruf: python tools/sketches.py
"""
import json, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 640, 400
RED, RED_L, INK, G1, G2, G3, BG = '#CD1719', '#FBE9E9', '#1F2328', '#5B6168', '#A9ADB3', '#E4E2DD', '#F7F6F3'
FONT = 'font-family="Roboto, Helvetica, Arial, sans-serif"'


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" {FONT}>'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>')


def t(x, y, s, size=24, weight=600, fill=INK, anchor='start', ls=0):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')


def kicker(s):
    return t(32, 48, s.upper(), 17, 700, G1, ls=1.6)


def warn(x, y, s=1.0):  # Warndreieck auf Ständer
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 22v34" stroke="{G1}" stroke-width="3"/>'
            f'<path d="M0-26 26 20H-26z" fill="#fff" stroke="{RED}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M0-8v12" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><circle cx="0" cy="11" r="2.6" fill="{INK}"/></g>')


def truck(x, y):
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="100" height="42" rx="8" fill="{RED}"/>'
            f'<path d="M70 0h22a8 8 0 0 1 8 8v12H70z" fill="#fff" opacity=".9"/><rect x="10" y="12" width="48" height="4" rx="2" fill="#fff" opacity=".85"/>'
            f'<rect x="58" y="-8" width="18" height="8" rx="3" fill="#2F6FD0"/>'
            f'<circle cx="22" cy="44" r="9" fill="{INK}"/><circle cx="78" cy="44" r="9" fill="{INK}"/></g>')


def car(x, y):
    return (f'<g transform="translate({x} {y})"><path d="M0 28v-10l14-15h30l16 15v10z" fill="{G2}"/>'
            f'<path d="M16 6h26l10 11H8z" fill="#fff" opacity=".7"/><circle cx="14" cy="30" r="7" fill="{INK}"/><circle cx="48" cy="30" r="7" fill="{INK}"/></g>')


def pill(cx, y, big, small):
    w = 150
    return (f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="62" rx="14" fill="#fff" stroke="{G3}" stroke-width="2"/>'
            + t(cx, y + 30, big, 26, 800, RED, 'middle') + t(cx, y + 52, small, 17, 600, G1, 'middle'))


def check(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="15" fill="{RED_L}"/>'
            f'<path d="M{x - 7} {y}l5 5 9-10" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')


S = {}

# 1 Verkehrsabsicherung – Abstände
b = kicker('Erste Warnung · Faustwerte')
b += pill(196, 74, 'ca. 200 m', 'Landstraße') + pill(396, 74, 'ca. 100 m', 'innerorts')
b += f'<path d="M196 136v52M396 136v52" stroke="{G2}" stroke-width="2" stroke-dasharray="4 5"/>'
b += f'<rect x="0" y="236" width="{W}" height="92" fill="#D9D7D2"/><rect x="0" y="236" width="{W}" height="3" fill="#fff"/><rect x="0" y="325" width="{W}" height="3" fill="#fff"/>'
b += f'<path d="M0 282H{W}" stroke="#fff" stroke-width="3" stroke-dasharray="24 18"/>'
b += warn(196, 206) + warn(396, 206)
b += car(28, 288) + f'<path d="M104 304h26m-8-7 8 7-8 7" fill="none" stroke="{G1}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
for cx in (452, 478, 504):
    b += f'<path d="M{cx - 8} 318l6-24h4l6 24z" fill="#E8590C"/><path d="M{cx - 5} 306h10" stroke="#fff" stroke-width="3"/>'
b += truck(532, 276)
b += t(32, 372, 'Vor Kurven und Kuppen weiter vorziehen · Autobahn: 400 / 600 / 800 m', 18, 600, G1)
S['sk-vk-strecke'] = (svg(b), 'Skizze: Straße mit Fahrzeug der Feuerwehr an der Einsatzstelle rechts. Warndreiecke stehen innerorts etwa 100 Meter, auf der Landstraße etwa 200 Meter davor. Vor Kurven und Kuppen weiter vorziehen; auf der Autobahn bei etwa 400, 600 und 800 Metern warnen.')

# 2 Warnkleidung
b = kicker('Sehen und gesehen werden')
b += f'<circle cx="170" cy="200" r="132" fill="#fff"/>'
b += f'<circle cx="170" cy="118" r="26" fill="#E7CDB3"/><path d="M140 112a30 22 0 0 1 60 0z" fill="{RED}"/><rect x="136" y="108" width="68" height="8" rx="4" fill="{INK}"/>'
b += f'<path d="M120 156q50-14 100 0l14 112h-128z" fill="#F2D33C"/>'
b += f'<path d="M110 214h120M108 238h124" stroke="#C7CBD1" stroke-width="10"/><path d="M146 150v64M194 150v64" stroke="#C7CBD1" stroke-width="10"/>'
b += f'<path d="M134 268h72v46h-72z" fill="#2D3B52"/>'
rows = [('EN ISO 20471', 'Warnkleidung nach Norm'), ('Mindestens Klasse 2', 'Weste oder Jacke'), ('Auch bei Tag', 'immer im Verkehrsraum')]
for i, (a, c) in enumerate(rows):
    y = 126 + i * 84
    b += check(352, y - 8) + t(380, y, a, 26, 800) + t(380, y + 28, c, 19, 500, G1)
S['sk-vk-weste'] = (svg(b), 'Skizze: Einsatzkraft mit gelber Warnweste und grauen Reflexstreifen. Daneben: Warnkleidung nach EN ISO 20471, mindestens Klasse 2, auch bei Tag.')

# 3 Erste Hilfe – Ablauf
b = kicker('In drei Schritten')
eye = f'<path d="M-26 0q26-24 52 0q-26 24-52 0z" fill="none" stroke="{INK}" stroke-width="3.5"/><circle r="8" fill="{INK}"/>'
phone = f'<rect x="-15" y="-26" width="30" height="52" rx="7" fill="none" stroke="{INK}" stroke-width="3.5"/>' + t(0, 7, '112', 15, 800, RED, 'middle')
hands = (f'<ellipse cx="0" cy="4" rx="24" ry="12" fill="#F3DCC6" stroke="{INK}" stroke-width="3"/>'
         f'<ellipse cx="0" cy="-6" rx="20" ry="10" fill="#F3DCC6" stroke="{INK}" stroke-width="3"/>'
         f'<path d="M0 22v12m-7-6 7 7 7-7" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')
steps = [('Prüfen', 'ansprechen,', 'Atmung max. 10 s', eye), ('Rufen', 'Notruf 112,', 'AED holen lassen', phone), ('Drücken', '30 × drücken,', '2 × beatmen', hands)]
b += f'<path d="M140 168H500" stroke="{G3}" stroke-width="3"/>'
for i, (ti, l1, l2, ic) in enumerate(steps):
    cx = 120 + i * 200
    b += (f'<circle cx="{cx}" cy="168" r="62" fill="#fff" stroke="{G3}" stroke-width="2"/><g transform="translate({cx} 168)">{ic}</g>'
          f'<circle cx="{cx + 44}" cy="122" r="16" fill="{RED}"/>' + t(cx + 44, 129, str(i + 1), 18, 800, '#fff', 'middle')
          + t(cx, 274, ti, 28, 800, INK, 'middle') + t(cx, 306, l1, 20, 500, G1, 'middle') + t(cx, 332, l2, 20, 500, G1, 'middle'))
S['sk-eh-ablauf'] = (svg(b), 'Skizze in drei Schritten: 1. Prüfen – ansprechen, Atmung höchstens 10 Sekunden prüfen. 2. Rufen – Notruf 112, AED holen lassen. 3. Drücken – 30-mal drücken, 2-mal beatmen.')

# 4 Herzdruckmassage
b = kicker('Herzdruckmassage · Erwachsene')
b += f'<path d="M60 400V226q0-46 46-58l34-8h88l34 8q46 12 46 58v174z" fill="#F3DCC6"/><path d="M164 140h40v24h-40z" fill="#E9CBAF"/><circle cx="184" cy="108" r="36" fill="#F3DCC6"/>'
b += f'<path d="M184 170v170" stroke="#D9B596" stroke-width="3" stroke-dasharray="6 7"/>'
b += f'<circle cx="184" cy="236" r="46" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="5 6"/>'
b += f'<ellipse cx="184" cy="242" rx="34" ry="16" fill="#fff" stroke="{INK}" stroke-width="3"/><ellipse cx="184" cy="232" rx="28" ry="13" fill="#fff" stroke="{INK}" stroke-width="3"/>'
stats = [('Mitte', 'des Brustkorbs'), ('5–6 cm', 'tief drücken, ganz entlasten'), ('100–120', 'mal pro Minute'), ('30 : 2', 'drücken : beatmen')]
for i, (a, c) in enumerate(stats):
    y = 112 + i * 72
    b += t(366, y, a, 30, 800, RED if i == 0 else INK) + t(366, y + 26, c, 19, 500, G1)
    if i < 3: b += f'<path d="M366 {y + 44}H604" stroke="{G3}" stroke-width="2"/>'
S['sk-eh-druck'] = (svg(b), 'Skizze: Oberkörper von vorn, zwei übereinandergelegte Hände in der Mitte des Brustkorbs. Daneben: 5 bis 6 Zentimeter tief drücken, 100- bis 120-mal pro Minute, 30-mal drücken und 2-mal beatmen.')

# 5 Gefahrenschema
b = kicker('Gefahren erkennen · AAAA-C-EEEE')
def tile(x, y, letter, words, col, bg):
    s = f'<rect x="{x}" y="{y}" width="136" height="92" rx="14" fill="{bg}"/>' + t(x + 16, y + 34, letter, 26, 800, col)
    for j, w in enumerate(words):
        s += t(x + 16, y + (58 if len(words) > 1 else 68) + j * 20, w, 17, 700, INK)
    return s
A = [['Atemgifte'], ['Angst-', 'reaktion'], ['Ausbreitung'], ['Atomare', 'Gefahren']]
E = [['Erkrankung,', 'Verletzung'], ['Explosion'], ['Elektrizität'], ['Einsturz']]
for i, w in enumerate(A): b += tile(32 + i * 148, 72, 'A', w, RED, '#FBEBEB')
b += tile(32, 176, 'C', ['Chemische', 'Stoffe'], '#8A5A00', '#F7EBD3')
b += t(196, 216, 'Bei jeder Erkundung', 25, 800) + t(196, 246, 'durchgehen und sofort melden', 20, 500, G1)
for i, w in enumerate(E): b += tile(32 + i * 148, 280, 'E', w, '#1D4F8C', '#E6EEF8')
S['sk-gf-matrix'] = (svg(b), 'Übersicht als Kacheln: vier A für Atemgifte, Angstreaktion, Ausbreitung und atomare Gefahren; C für chemische Stoffe; vier E für Erkrankung oder Verletzung, Explosion, Elektrizität und Einsturz.')

out = {k: 'data:image/svg+xml,' + urllib.parse.quote(v[0]) for k, v in S.items()}
alts = {k: v[1] for k, v in S.items()}
(ROOT / 'docs/demo/sketches.js').write_text('/* Eigene Skizzen für die Beispielthemen – erzeugt mit tools/sketches.py */\nconst SKETCH = '
                                            + json.dumps(out) + ';\nconst SKETCH_ALT = ' + json.dumps(alts, ensure_ascii=False) + ';\n')
(ROOT / 'docs/demo/sketches').mkdir(exist_ok=True)
for k, v in S.items():
    (ROOT / 'docs/demo/sketches' / f'{k}.svg').write_text(v[0])
print('ok', len(S))
