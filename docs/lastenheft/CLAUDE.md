# Website Feuerwehr Piflas e.V. (WordPress)

## Projekt
Nur eigener Code:
- wp-content/themes/ff-piflas/           Block-Theme
- wp-content/plugins/ff-piflas-connect/  Rollen, Einladungen, DIVERA, Freigabe,
                                         Fotos, Instagram, Lernen, System-Bereich
Anforderungen: docs/lastenheft.md (IDs F-, D-, W-, I-, B-, M-, C-, S-, R-, J-,
E-, A-, N-, L-). Vorlage: docs/referenz-demo/ (Abnahme: test_app.py).
Handbuch: docs/handbuch/ (A-06).

## Regeln
- Oberfläche, Commits und Handbuch auf Deutsch in Du-Form, Frauen und Männer
  gleichermaßen ansprechen, neutrale Formen zuerst (N-13); Code englisch.
- WordPress Coding Standards, PHP >= 8.2, kein Page-Builder.
- Inhalte in die Datenbank, nie ins Repo. Alles Veränderliche als
  Einstellung im Backend (A-01).
- Rollen nur in src/Roles.php, DIVERA-Daten nur über src/Divera/Anonymizer.php,
  jeweils mit Tests.
- Schnittstellen nur in src/Divera/ und src/Instagram/ (Client, Mapping,
  Contract, README) mit Vertragstests gegen tests/fixtures/ (A-10 bis A-12).
  Bei jeder Änderung docs/betrieb/schnittstellen.md mitpflegen.
- Jede Änderung an Inhalten über den Verlauf-Dienst (B-07), nur anhängen.
- Veröffentlichen nur mit Pflicht-Bestätigung, serverseitig geprüft (W-04).
- Löschen nur durch Admins, nach Nachfrage, über den Papierkorb (B-16).
- Fotos: verkleinern, EXIF/GPS auch im Original entfernen (B-11).
- Lernergebnisse nur in src/Learning/, eigene Tabelle, lesen nur mit der
  Rechteprüfung „Lernstand sehen“ (nur Kommandant), Löschfrist per Cron (E-09, E-11).
- Zugangsdaten nur in wp-config.php.
- Ausgaben immer escapen (esc_html, esc_attr, wp_kses_post), Eingaben prüfen (N-05).
- Keine externen Requests im Frontend; externe Links mit rel="noopener".
- Fremd-Plugins nur nach Rücksprache (docs/plugins.md).
- Jede neue Funktion: Handbuch-Abschnitt in einfacher Sprache.
- Je Phase ein Branch und ein PR mit Checkliste der erfüllten IDs.

## Entwicklung
npx @wordpress/env start | composer test | composer lint | npm run build
