# Arbeitspakete für Claude Code

Stand 23.11.2026 · Lastenheft 1.19 · passt zum Umsetzungsplan bis Weihnachten 2026 (`../plan/`)

Je Paket eine Sitzung mit Claude Code, ein Branch und ein Pull Request mit der Liste der erfüllten IDs. Ein Paket gilt als fertig, wenn alle Tests grün sind und zwei Personen es auf der Testseite am Handy abgenommen haben (Spalte „Abnahme“). Vorlage für Aussehen und Abläufe ist immer die Demo (`docs/referenz-demo/`). Welche ID wie geprüft wird, steht in `ABDECKUNG.md`.

## Vorher (Verein, Phase 0)

- [ ] Hosting erfüllt Lastenheft 4.1 (PHP 8.2, MySQL 8 oder MariaDB 10.6, Cronjob, SFTP, SMTP, 5 GB, Subdomain für die Testseite)
- [ ] GitHub-Organisation des Vereins mit diesem Repository, zwei Personen mit Zugriff
- [ ] Testseite (Staging) angelegt, mit Passwortschutz und `noindex`
- [ ] Zugangsdaten für Deploy und Schnittstellen im Vereins-Tresor; als GitHub-Secrets bzw. in `wp-config.php` – nie im Chat oder im Code
- [ ] DIVERA-API-Zugang geklärt, Instagram professionell, Meta-Entwicklerkonto auf den Verein

## Pakete

| Nr. | Woche | Paket | IDs | Abnahme |
| --- | --- | --- | --- | --- |
| 1 | KW 49 | Grundgerüst: wp-env, Plugin mit 5 Rollen und Capabilities, Einladungen, 2-Faktor, Login-Drosselung, Austritt, CI und Deploy auf die Testseite | B-01 bis B-08, E-01, E-10, N-05, A-08 | Jede Rolle kann genau das, was in der Rollentabelle steht; Sicherheitstests „Rechte“ und „Anmeldung“ grün |
| 2 | KW 49 | Theme nach der Demo: Kopf, Menü, Fußzeile, Startseite, alle öffentlichen Seiten, Schrift und Logo selbst gehostet | F-01 bis F-12, C-01 bis C-04, C-07, S-01, S-02, J-01 bis J-06, N-01 bis N-03, N-08 bis N-10, N-13 | Seitenrundgang 360–1280 px grün; keine Anfrage an fremde Server |
| 3 | KW 50 | Beiträge: Editor, Fotos (verkleinern, GPS entfernen), Pflicht-Häkchen, Inhalte-Übersicht, Bearbeiten, Ausblenden, Löschen mit Papierkorb | B-09 bis B-12, B-14 bis B-16, B-18 bis B-20, W-04 | Redaktion reicht ein, Kommandant gibt frei; Admin löscht und stellt wieder her |
| 4 | KW 50 | Freigabe mit Vergleich, Verlauf (nur anhängen), Rückgängig, E-Mail-Hinweis an die Kommandanten, Angemeldet bleiben, Zähler | W-01 bis W-03, W-05 bis W-09, B-07, B-10, B-13, B-17, B-22, B-23 | Änderung der Redaktion erscheint als Vergleich; Mail ohne Inhalte |
| 5 | KW 50 | Seiten pflegen (Verein, Chronik, Fahrzeuge, Ausrüstung), Fotoverwaltung, System-Bereich mit Ampel und Schaltern, Redaktionsplan | B-21, B-12, A-01, A-03, R-01 bis R-04 | Kommandant legt ein Fahrzeug an, es steht sofort im Einsatzformular |
| 6 | KW 50 | DIVERA: Abruf, Anonymisierer, Vertragstests, Einsatz von Hand, Termine, Diagnose und Notbetrieb, Reparatur-Anleitung – Schalter aus | D-01 bis D-09, A-10 bis A-12, L-02, L-03 | Testalarm erzeugt in 15 Minuten einen datensparsamen Entwurf; DIV-FMT übernimmt nichts |
| 7 | KW 51 | Instagram: Vorschau vom Server, Post nach Freigabe, Token erneuern, Diagnose – Schalter aus | I-01 bis I-04 | Testpost mit Meta-Testkonto; Störung zeigt nur den Profil-Link |
| 8 | KW 51 | Lernen: Rolle Mitglied, Themen in Schritten, Test, Lernstand, Themenplan, Löschfrist – Schalter aus | E-01 bis E-29, L-14 bis L-17 | Laientest E-28 mit drei Mitgliedern; Admin sieht keine Ergebnisse |
| 9 | KW 51 | Betrieb: Überwachung, Monatsbericht, Besucherstatistik ohne Cookies, Backup und Wiederherstellung, Security-Header, Rechtstexte | M-01 bis M-04, N-04, N-06, N-12, L-07 bis L-09, A-04 | Wiederherstellung geprobt; Lighthouse mobil ≥ 90 |
| 10 | KW 51 | Handbuch mit Bildschirmfotos der echten Seite, Laientest, Go-live-Checkliste | A-06, A-09, F-13 | Laientest bestanden; Checkliste im Umsetzungsplan abgehakt |

## So startest du eine Sitzung

Für Paket 1 den Start-Prompt aus `lastenheft/start-prompt-phase1.txt` verwenden. Für alle weiteren Pakete:

```text
Lies CLAUDE.md, docs/lastenheft.md, docs/start/ARBEITSPAKETE.md und
docs/referenz-demo/ABDECKUNG.md. Setze Arbeitspaket <Nr.> um (IDs laut
Tabelle). Übertrage dazu die passenden Prüfungen aus test_app.py und
test_security.py als Playwright-Tests und ergänze PHPUnit-Tests für die
Rechte. Stelle zuerst Plan und offene Fragen vor. Am Ende: PR mit
Checkliste der IDs und Hinweis, was im Handbuch zu ergänzen ist.
```

## Regeln für alle Pakete

- Zugangsdaten nie in den Chat, ins Repository oder in Claude-Projekte – nur in `wp-config.php` auf dem Server und im Vereins-Tresor.
- Änderungswünsche während der Umsetzung sammeln; nur Fehler und rechtliche Punkte sofort.
- Abnahme immer am Handy auf der Testseite, gegen die Demo als Vorlage. Echte Mitgliederdaten nur auf der echten Website.
