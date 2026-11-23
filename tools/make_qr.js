// Erzeugt einen QR-Code als SVG, ohne Online-Dienst.
// Aufruf: node tools/make_qr.js <URL> <ziel.svg>
// Nutzt die QR-Bibliothek, die mit npm mitgeliefert wird (Paket qrcode-terminal, MIT-Lizenz).
// Falls der Pfad nicht passt: npm install qrcode-terminal und QR_LIB auf node_modules/qrcode-terminal/vendor/QRCode setzen.
const path = require('path'), { execSync } = require('child_process');
const fs = require('fs');
const cands = [process.env.QR_LIB,
  path.join(__dirname, 'node_modules/qrcode-terminal/vendor/QRCode'),
  path.join(path.dirname(process.execPath), '../lib/node_modules/npm/node_modules/qrcode-terminal/vendor/QRCode'),
  (() => { try { return path.join(execSync('npm root -g').toString().trim(), 'npm/node_modules/qrcode-terminal/vendor/QRCode'); } catch (e) { return null; } })()];
const LIB = cands.find(c => c && fs.existsSync(path.join(c, 'index.js')));
if (!LIB) { console.error('QR-Bibliothek nicht gefunden: npm install qrcode-terminal im Ordner tools ausführen'); process.exit(1); }
const QRCode = require(LIB);
const L = require(path.join(LIB, 'QRErrorCorrectLevel'));
const url = process.argv[2], out = process.argv[3];
const q = new QRCode(-1, L.M); q.addData(url); q.make();
const n = q.getModuleCount(), m = 4, S = n + 2*m;
let d = '';
for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) if (q.isDark(r, c)) d += `M${c+m} ${r+m}h1v1h-1z`;
const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${S} ${S}" shape-rendering="crispEdges" role="img" aria-label="QR-Code: ${url}"><rect width="${S}" height="${S}" fill="#fff"/><path fill="#1F2328" d="${d}"/></svg>`;
fs.writeFileSync(out, svg); console.log('modules', n);
