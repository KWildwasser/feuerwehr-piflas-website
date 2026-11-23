import base64, json, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
def find(*cands):
    for c in cands:
        if Path(c).exists(): return Path(c)
    raise SystemExit('Nicht gefunden: ' + ' | '.join(map(str, cands)))
# Backup-Layout: ../assets/...  ·  Arbeitsumgebung: /home/claude/...
LOGO  = find(HERE.parent/'assets'/'logo.svg', '/home/claude/ff-piflas-start/logo.svg')
FOTOS = find(HERE.parent/'assets'/'fotos', '/home/claude/fotos/out')
FONT  = find(HERE.parent/'assets'/'fonts'/'roboto-sub.woff', '/home/claude/fonts/roboto-sub.woff')
s=open(HERE/'app-src.html').read()
b=base64.b64encode(open(LOGO,'rb').read()).decode()
s=s.replace('--sab:env(safe-area-inset-bottom)}','--sab:env(safe-area-inset-bottom);--logo:url("data:image/svg+xml;base64,'+b+'")}',1)
assert '--logo:url' in s
m={'thl':'thl_breit','wlf_hoch':'wlf_hoch','fz_wlf':'fz_wlf','halle':'halle_nacht','blau':'hero_haus_blau','fz_man':'fz_man','fz_magirus':'fz_magirus','fz_561':'fz_561','fz_mtw':'fz_mtw'}
for k in ['g_ultrapower','g_pumpe','g_stromerzeuger','g_hitzeschutz','g_schlauch','g_armaturen','g_saugkorb','g_schnellangriff','g_schlauchlager']+[f'ig{i}' for i in range(6)]: m[k]=k
d={k:'data:image/jpeg;base64,'+base64.b64encode(open(FOTOS/f'{v}.jpg','rb').read()).decode() for k,v in m.items()}
f64=base64.b64encode(open(FONT,'rb').read()).decode()
ff='@font-face{font-family:FwText;src:url(data:font/woff;base64,'+f64+') format("woff");font-weight:100 900;font-stretch:100%;font-display:swap}\n@font-face{font-family:FwCond;src:url(data:font/woff;base64,'+f64+') format("woff");font-weight:100 900;font-stretch:75%;font-display:swap}'
assert '/*FONTFACE*/' in s
s=s.replace('/*FONTFACE*/',ff,1)
assert '/*IMGDATA*/' in s
s=s.replace('/*IMGDATA*/','const IMG = '+json.dumps(d)+';',1)
open(HERE/'index.html','w').write(s)
print(len(s)//1024,'KB')
