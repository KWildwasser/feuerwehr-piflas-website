# Webpräsenz Feuerwehr Piflas – Backup & Anleitung zum Weitermachen

Stand: **23.11.2026** · Lastenheft **v1.12** · Demo **v11** · Handbuch **1.10** · Testsuite **655/655 bestanden**

Dieses Paket enthält alles, was bisher entstanden ist: Dokumente, Code, Skripte, Bilder und Vorlagen. Damit kannst du (oder jemand aus dem Verein, oder eine neue Claude-Sitzung) jederzeit nahtlos weitermachen. Es enthält keine Zugangsdaten.

---

## 1. Was ist wo?

| Ordner / Datei | Inhalt |
|---|---|
| `PROJEKT-ANWEISUNGEN.md` | Benutzerdefinierte Anweisungen für das Claude-Projekt (zum Einfügen) |
| `lastenheft/lastenheft-v1.12.md` | Das Lastenheft als Text – verbindliche Grundlage |
| `lastenheft/Lastenheft-Feuerwehr-Piflas-v1.12.pdf` | Dieselbe Fassung zum Drucken, mit Diagramm |
| `lastenheft/make_pdf.py` | Erzeugt das PDF aus der neuesten `lastenheft-vX.Y.md` |
| `lastenheft/CLAUDE.md`, `start-prompt-phase1.txt` | Vorlagen für das Code-Repository und die erste Claude-Code-Sitzung |
| `handbuch/Handbuch-Website-Feuerwehr-Piflas.pdf` | Handbuch Mitgliederbereich 1.8 (alle Rollen) |
| `handbuch/inhalt.html`, `shots.py`, `make.py`, `img/` | Quellen: Text, Bildschirmfotos aus der Demo, PDF-Erzeugung |
| `demo/README.md` | Aufbau der Demo und Zuordnung der Prüfungen zu den Lastenheft-IDs |
| `demo/app-src.html` | Quelltext der Demo – **hier wird geändert** |
| `demo/build.py` → `demo/index.html` | Baut die fertige Demo (eine Datei, läuft offline) |
| `demo/test_app.py`, `demo/testimg/` | Testsuite (655 Prüfungen) = Abnahmeliste für die echte Website |
| `betrieb/schnittstellen.md` | Anleitung „Schnittstellen reparieren“ (DIVERA, Instagram) für die Technik – A-12 |
| `index.html`, `assets/screens/`, `assets/qr-projektseite.svg` | Projektseite auf GitHub Pages (mit QR-Code für den Pitch) |
| `../tools/make_qr.js` | Erzeugt den QR-Code offline: `node tools/make_qr.js <URL> <ziel.svg>` |
| `demo/handbuch.pdf` | Handbuch, wie es in der Demo nach dem Login verlinkt ist |
| `design/corporate-design.md` | Logo, Farben, Schrift, Gestaltungsprinzipien |
| `design/mockups/` | Frühe Entwürfe (Bürgerinfo, Einsätze, Freigabe) – überholt durch die Demo |
| `assets/logo.svg`, `logo-weiss.svg`, `logo-png/` | Logo aus dem Briefpapier (Vektor und PNG) |
| `assets/briefpapier.docx` | Briefpapier des Vereins (Original) |
| `assets/fotos/` | Bearbeitete Fotos für Demo und Website (zugeschnitten, ohne Metadaten) |
| `assets/fotos-original/` | Ausgangsfotos (ohne Standortdaten) |
| `assets/fonts/` | Roboto, selbst gehostet (OFL-Lizenz) |
| `uebergangsseite/`, `uebergangsseite.zip` | Statische Übergangsseite – fertig zum Hochladen (siehe `LIESMICH.txt`) |

## 2. Links (Stand 23.11.2026)

- **Lastenheft (online, mit Kommentarfunktion):** https://claude.ai/artifact/RHi6KHi8Bik2Xaj6imtwuy
- **GitHub (alles, öffentlich):** https://github.com/KWildwasser/feuerwehr-piflas-website
- **Demo öffentlich (GitHub Pages):** https://kwildwasser.github.io/feuerwehr-piflas-website/demo/
- **Projektseite (für den Pitch, mit QR-Code):** https://kwildwasser.github.io/feuerwehr-piflas-website/
- **Demo v11 (Claude-Artefakt, gleicher Link wie zuvor):** https://claude.ai/artifact/JDBEcotDJPXWSgDe7dBzhn
- Ältere, öffentlich geteilte Stände: v4 https://claude.ai/artifact/3zpe9uaMATpMUXYjNNLvS4 · v3 https://claude.ai/artifact/PPtQ5Y7QVMb5PSzn52DTCA (nicht mehr aktuell)
- Partnerfeuerwehren: https://www.ff-ergolding.de/ · https://oberglaim.feuerwehren.bayern/
- Instagram: https://www.instagram.com/feuerwehrpiflas/

Hinweis: Öffentlich geteilte Demos lassen sich nicht mehr überschreiben – jede Änderung danach ergibt eine neue Version mit neuem Link.

## 3. Ändern, bauen, prüfen

Voraussetzung: Python 3.10+.

```bash
pip install playwright pillow markdown pypdf
python -m playwright install chromium

cd demo
python build.py          # erzeugt index.html (ca. 2,3 MB)
python test_app.py       # 2–4 Minuten, Ergebnis: "655 von 655 Prüfungen bestanden", Exit-Code 1 bei Fehlern

cd ../handbuch
python shots.py          # neue Bildschirmfotos aus der Demo
python make.py           # Handbuch-PDF; danach nach demo/handbuch.pdf kopieren

cd ../lastenheft
python make_pdf.py       # PDF aus der neuesten lastenheft-vX.Y.md
```

Reihenfolge bei jeder Änderung: **Lastenheft (ID) → Demo → Prüfung in test_app.py → Handbuch-Abschnitt → PDFs → Backup.**

Regeln für die Demo: Du-Form; Frauen und Männer gleichermaßen ansprechen (neutrale Formen zuerst, sonst beide Formen, keine Sternchen; Ausnahmen Kommandant, Admin und FwDV-Funktionen – N-13); jede Eingabe mit `esc()` ausgeben; keine externen Anfragen. Der Aufbau des Quelltexts steht als Kommentar am Anfang des Skripts in `app-src.html`.

## 4. Nächste Schritte (Reihenfolge)

1. **Übergangsseite online stellen** – `uebergangsseite/LIESMICH.txt`. Vorher Joomla komplett sichern, Logfile-Dauer des Hosters in `datenschutz.html` eintragen.
2. **Pitch** beim Kommandanten, im Gemeinderat und beim Bürgermeister mit der Projektseite und Demo v11 (QR-Code oben auf der Projektseite – alle testen am eigenen Handy; unten rechts „Demo“ mit Szenarien: Einsatz aus DIVERA, Freigabe-Beispiele, Redaktion reicht ein, Einsatz von Hand, E-Mail an die Kommandanten, Verlauf und Rückgängig, Lernen, Störung simulieren).
3. **Betriebsvariante entscheiden** (Lastenheft 4.3): Wer betreut die Seite? Ohne zwei Admins → Wartung durch Dienstleister.
4. **Offene Punkte** aus Lastenheft Abschnitt 5 einsammeln (Kommandant, Ortsteile, Pflege der Vereinsseite laut Satzung, Jubiläumstermine, Fahrzeugtypen, Namen der Fotografinnen und Fotografen, PDFs, Förderbeitrag …).
5. **Phase 0** (Zugänge, Hosting-Prüfung, DIVERA-API, Instagram-Business-Konto), dann **Phase 1** mit Claude Code und dem Start-Prompt.

## 5. So geht es in einer neuen Claude-Sitzung weiter

Dieses ZIP hochladen und z. B. schreiben:

> Hier ist das Backup unserer Website-Planung für die Feuerwehr Piflas (Stand 23.11.2026). Lies zuerst WEITERMACHEN.md und lastenheft/lastenheft-v1.12.md. Baue die Demo mit demo/build.py und prüfe sie mit demo/test_app.py. Danach möchte ich: …

Für die eigentliche Umsetzung mit Claude Code: neues Repository anlegen, `lastenheft/CLAUDE.md` ins Wurzelverzeichnis, `lastenheft/lastenheft-v1.12.md` nach `docs/lastenheft.md`, das Handbuch nach `docs/handbuch/`, `betrieb/` nach `docs/betrieb/`, den Ordner `demo/` nach `docs/referenz-demo/`, dann `start-prompt-phase1.txt` verwenden.

## 6. Wichtige Entscheidungen (Kurzfassung)

- **WordPress** statt statischer Seite, weil Mitglieder mit eigenen Konten pflegen sollen.
- **Keine Selbstregistrierung** – nur Einladung durch einen Admin; immer mindestens zwei Admins.
- **Keine Spenden online** (Satzung) – nur Werbung für Fördermitgliedschaft mit PDFs.
- **DIVERA:** Einsätze datensparsam (nur Ortsteil, Uhrzeit gerundet), Freigabe durch den Kommandanten mit Pflicht-Bestätigung, frühestens 2 Std. nach Alarm; alle nicht-privaten Termine automatisch.
- **Jubiläum 2027** zeitgesteuert, verschwindet danach automatisch und bleibt nur in der Chronik.
- **Du-Form** überall, **gegliedertes Menü** (Aktuell, Mitmachen, Ratgeber, Über uns), **keine Gemeinderat-Seite**, **Partnerfeuerwehren** auf eigener Seite.
- **Frauen und Männer** gleichermaßen ansprechen (N-13). Rollen: Admin, Kommandant · Freigabe, Redaktion, Bereichsredaktion; Ausnahmen „Kommandant“ und „Admin“, Feuerwehrfunktionen nach FwDV.
- **Bearbeiten und Ausblenden** gemäß Rolle (Redaktion: eigene, Änderung über Freigabe); **Löschen** nur Admins nach Nachfrage, 30 Tage Papierkorb (B-14 bis B-16).
- **Lernen (2.12, E-01 bis E-14):** Monatsthema vom Kommandanten mit Multiple-Choice-Test; Rolle „Mitglied“ nur lesen und lernen; Lernstand nur für Kommandanten (keine Admins), keine Rangliste, Löschfrist 3 Jahre (Annahme); Lehrmaterial der Feuerwehrschulen nur verlinken. Offen: Verantwortlicher und Rechtsgrundlage (L-15). Test mit genau 5 Fragen, bestanden ab 4 richtigen (E-06).
- **Rote Zähler** an den Bereichen, wenn etwas zu tun ist (B-22); **Rollen ändern** durch Admins am Konto, nicht die eigene, immer zwei Admins (B-02).
- **Eine Rolle je Konto**, kein Rollen-Auswahlfeld beim Login. Geplante Besetzung: 3 Kommandanten, 2 Admins, mehrere Redaktion.
- **Rückgängig überall** (B-17), letzte Aktion 5 Minuten oben sichtbar – auch nach dem Veröffentlichen, und **Verlauf** je Inhalt, nur anhängen, mit Spam-Schutz (B-07, N-05).
- **Inhalte-Übersicht** mit Suche, Filtern und Seitenweise-Laden für hunderte Einträge (B-18); **Einsatz von Hand** für Kommandanten (D-09).
- **Seiten pflegen:** Verein, Chronik, Fahrzeuge, Ausrüstung; alle legen Fahrzeuge und Geräte an (Redaktion über Freigabe), entfernen nur Kommandant und Admins (B-21).
- **E-Mail-Hinweis:** kurze Mail an alle Kommandanten je Einreichung und täglich um 7 Uhr, nur mit Link zur Freigabe – keine Inhalte, Freigeben nur auf der Website (W-09).
- **Freigabe und Verlauf als Vergleich:** geänderte Felder Wort für Wort (rot weg, grün neu) (W-08, B-07).
- **Überörtliche Einsätze:** Einsatzort als Ortsteil oder Gemeinde, nie Straße (D-02, D-09).
- **Schnittstellen** austauschbar mit Fehlercodes, Diagnose, Notbetrieb und Reparatur-Anleitung (A-10 bis A-12).
- **Fotos:** alle Rollen dürfen Fotos zu Beiträgen hinzufügen; nur Admins verwalten alle Fotos; Standard-Bildnachweis „Feuerwehr Piflas“.
- **Wartbarkeit** ist Leitprinzip: alles Veränderliche im Backend, Zustands-Ampel, Handbuch, zwei Admins.

## 7. Datenschutz-Hinweis zu diesem Paket

Die Fotos sind ohne Standortdaten. Das Paket enthält keine Zugangsdaten, Passwörter oder Schlüssel – und soll auch künftig keine enthalten. Die Demo enthält nur erfundene Beispielpersonen (z. B. Max Mustermann, Erika Musterfrau, Jonas Beispiel, Mia Muster) und erfundene Archiv-Beispiele für Einsätze 2016–2024 und Berichte 2019–2025.
