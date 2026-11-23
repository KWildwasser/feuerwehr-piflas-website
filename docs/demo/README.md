# Referenz-Demo und Testsuite

Die Demo zeigt, wie die Website aussehen und funktionieren soll. Sie ist eine einzige statische HTML-Datei, ohne Server und ohne Datenbank. Ein Neuladen setzt alles zurück. Die Testsuite ist zugleich die Abnahmeliste für die echte WordPress-Website (Lastenheft N-11).

## Dateien

| Datei | Zweck |
|---|---|
| `app-src.html` | Quelltext (Aufbau siehe Kommentar am Anfang des Skripts) – **hier wird geändert** |
| `build.py` | Baut `index.html`: bettet Logo, Schrift und Fotos aus `../assets` ein |
| `index.html` | Fertige Demo, läuft offline im Browser |
| `handbuch.pdf` | Handbuch, nach dem Login in der Demo verlinkt |
| `test_app.py` | Testsuite (Playwright), Ergebnis in `test_results.json`, Bilder in `shots/` |
| `testimg/` | Testbilder (u. a. Foto mit GPS-Daten, Nicht-Bild-Datei) |

## Ausführen

```bash
pip install playwright pillow && python -m playwright install chromium
python build.py && python test_app.py        # Exit-Code 1 bei Fehlern
CHROME=/pfad/zu/chrome python test_app.py    # optional eigener Browser
```

## Was geprüft wird (Lastenheft-IDs)

| Bereich | Prüfungen | IDs |
|---|---|---|
| Seitenrundgang in 360/390/430/1280 px | kein seitliches Scrollen, Überschrift, Namen und Labels, Tippziele ≥ 44 px, Bilder, keine JS-Fehler | N-02, N-03 |
| Startseite | Reihenfolge, Fotos, Instagram-Raster, keine Fahrzeugdaten | F-01, I-01 |
| Recht | keine externen Anfragen, keine IBAN, Hinweis für unter 16-Jährige, Impressum, Datenschutz | N-01, L-03 bis L-11 |
| Ansprache | Du-Form überall, keine rein männlichen Formen (Ausnahmen Kommandant, Admin, FwDV) | N-09, N-13 |
| Navigation | Menügruppen, Partnerseite, Zurück-Taste, unbekannte Adressen, Tastatur | F-09, F-11, N-02 |
| Formulare | Pflichtfelder, Datenschutz-Häkchen, Fehlermeldungen | F-06, W-04 |
| Login und Rollen | 2FA-Schritt, Schnell-Login je Rolle, Bereiche je Rolle, Schutz vor Direktaufruf | B-01 bis B-06 |
| Beiträge und Fotos | Fotos verkleinern, GPS entfernen, nur Bilder, Vorschau, Sprung zum Beitrag | B-09 bis B-11 |
| Fotoverwaltung | Ersetzen, Entfernen mit Nachfrage | B-12 |
| Bearbeiten, Ausblenden, Löschen | Rechte je Rolle, Änderung über Freigabe, Nachfrage, Papierkorb | B-14 bis B-16 |
| Freigabe und DIVERA | Alarm simulieren, Pflicht-Häkchen, Verwerfen, Statistik, Termin-Abgleich | D-, W- |
| Bürgerinfos | Tipp nach Jahreszeit, Sonderhinweis, Warntag und Probealarm | C-04, C-07 |
| Jubiläum | Ankündigung, Festjahr, Aufräumen 2028 | J-01 bis J-06 |
| System | Ampel, Einstellungen, Handbuch-Link, Checkliste Admin-Wechsel | A-01, A-03, B-13 |
| Robustheit | HTML in Eingaben wird nicht ausgeführt, lange Wörter brechen um | N-05, N-03 |

Neue Funktion → zuerst Lastenheft-ID, dann Demo, dann eine Prüfung hier und ein Abschnitt im Handbuch (A-06).
