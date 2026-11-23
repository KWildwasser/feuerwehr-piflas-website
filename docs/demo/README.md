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
| Seitenrundgang in 360/390/430/1280 px | kein seitliches Scrollen, Überschrift, Namen und Labels, Tippziele ≥ 44 px, Bilder, keine JS-Fehler; Mitgliederbereich in 360/390, Kopf ohne Überlappung | N-02, N-03, B-06 |
| Aktuelles und Einsätze | Kategorien, ältere Jahre, Einsatzart, „Weitere laden“ | F-02, F-03 |
| Startseite | Reihenfolge, Fotos, Instagram-Raster, keine Fahrzeugdaten | F-01, I-01 |
| Recht | keine externen Anfragen, keine IBAN, Hinweis für unter 16-Jährige, Impressum, Datenschutz | N-01, L-03 bis L-11 |
| Ansprache | Du-Form überall, keine rein männlichen Formen (Ausnahmen Kommandant, Admin, FwDV) | N-09, N-13 |
| Navigation | Menügruppen, Partnerseite, Zurück-Taste, unbekannte Adressen, Tastatur | F-09, F-11, N-02 |
| Formulare | Pflichtfelder, Datenschutz-Häkchen, Fehlermeldungen | F-06, W-04 |
| Login und Rollen | keine Rollenauswahl (Rolle aus dem Konto), unbekannte E-Mail, 2FA, Schnell-Login, Bereiche je Rolle, 3/2/mehrere Konten | B-01 bis B-06 |
| Beiträge und Fotos | Fotos verkleinern, GPS entfernen, nur Bilder, Titelbild wählen, Vorschau, Sprung zum Beitrag | B-09 bis B-11, B-19 |
| Fotoverwaltung | Ersetzen, Entfernen mit Nachfrage | B-12 |
| Bearbeiten, Ausblenden, Löschen | Rechte je Rolle, Editor, Änderung über Freigabe, Nachfrage, Papierkorb | B-14 bis B-16, B-19 |
| Inhalte-Übersicht | über 300 Einträge, Suche beim Tippen, Filter Art/Jahr/Status, 20 je Seite, Zurücksetzen | B-18 |
| Verlauf und Spam-Schutz | wer/wann/was, Freigabe, Notiz, Fassung wiederherstellen, nur anhängen, keine Leer-Einträge, Zusammenfassen, Begrenzung | B-07, N-05 |
| Rückgängig | Freigabe, Veröffentlichen (auch auf der Beitragsseite), Einplanen, Löschen, Verwerfen, Wiederherstellen, Notbetrieb; letzte Aktion oben sichtbar | B-17 |
| Seiten pflegen | Verein, Vorstandschaft, Chronik (Sortierung), Fahrzeuge (Foto, neu, entfernen, wiederherstellen), Ausrüstung, Redaktion legt Fahrzeuge an (über Freigabe) | B-21, W-08 |
| Einsatz von Hand | Rundung, überörtlicher Einsatzort, Straße wird abgewiesen, Fahrzeug-Pflicht, Foto, 2-Stunden-Regel (geplant), Zukunft abgewiesen | D-09, D-04 |
| Freigabe und DIVERA | 4 Beispiele, Alarm, echte Einsatzfotos, Pflicht-Häkchen, Zurückgeben mit Hinweis, Verwerfen und Wiederherstellen, Statistik, Termin-Abgleich | D-, W- |
| E-Mail an Kommandanten | Hinweis-Mail je Einreichung an alle 3 Kommandanten, nur Art und Person, Link zur Freigabe (Anmeldung), keine Inhalte, „Schon erledigt“, tägliche Erinnerung | W-09 |
| Vergleich vorher/nachher | Freigabe und Verlauf: geänderte Felder Wort für Wort (rot/grün), Überblick nach Art | W-08, B-07 |
| Schnittstellen | Fehlercodes, Verbindung testen, Schlüssel verdeckt, Diagnosebericht ohne Zugangsdaten, Notbetrieb, Instagram-Ausfall unsichtbar | D-08, A-10 bis A-12 |
| Demo-Szenarien | Redaktion reicht ein, Einsatz von Hand, Verlauf, Anmelden als | – |
| Bürgerinfos | Tipp nach Jahreszeit, Sonderhinweis, Warntag und Probealarm | C-04, C-07 |
| Jubiläum | Ankündigung, Festjahr, Aufräumen 2028 | J-01 bis J-06 |
| System | Ampel, Einstellungen, Handbuch-Link, Checkliste Admin-Wechsel | A-01, A-03, B-13 |
| Robustheit | HTML in Eingaben wird nicht ausgeführt, lange Wörter brechen um | N-05, N-03 |

Neue Funktion → zuerst Lastenheft-ID, dann Demo, dann eine Prüfung hier und ein Abschnitt im Handbuch (A-06).
