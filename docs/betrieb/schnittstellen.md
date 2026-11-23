# Schnittstellen reparieren – DIVERA 24/7 und Instagram

**Für wen:** Eine Person mit Programmierkenntnissen, die den Code hat, die Website aber nicht kennt.
**Ziel:** Eine gebrochene Schnittstelle in **unter zwei Stunden** wieder zum Laufen bringen.
**Grundlage:** Lastenheft v1.7, Anforderungen A-10 (Aufbau), A-11 (Diagnose und Notbetrieb), A-12 (Reparatur-Anleitung).

> Stand: Planung. Pfade, Befehle und Dateinamen sind **verbindliche Vorgaben** für die Umsetzung im Plugin
> `ff-piflas-connect`. Alles in eckigen Klammern muss bei der Umsetzung geprüft bzw. ergänzt werden.

---

## 1. Erst einmal: Ist es wirklich kaputt?

1. Im Mitgliederbereich als Admin anmelden → **System** → **Schnittstellen**.
2. Den **Fehlercode** ablesen und unten in Abschnitt 4 nachschlagen.
3. **„Diagnosebericht kopieren“** – der Bericht enthält Zeitpunkt, Code, Adapter, Vertragsversion
   und die letzten Protokollzeilen. Er enthält **nie** Schlüssel, Tokens oder Passwörter.

Solange repariert wird, schaltet ein Admin den **Notbetrieb** ein: Der automatische Abruf pausiert,
Einsätze und Termine werden von Hand gepflegt, die Instagram-Vorschau wird durch einen Link zum Profil
ersetzt. Besucherinnen und Besucher sehen **keinen Fehler**.

## 2. Aufbau in einem Satz

Jede Schnittstelle steckt in **einem eigenen Ordner** mit genau vier Teilen – nichts anderes im Code
spricht direkt mit DIVERA oder Instagram:

```
wp-content/plugins/ff-piflas-connect/
├── src/
│   ├── Divera/
│   │   ├── Client.php                 # nur HTTP: Abruf, Zeitlimit, Wiederholung, Fehlercodes
│   │   ├── Anonymizer.php             # nur Zuordnung: DIVERA-Feld → Website-Feld (+ Datensparsamkeit D-02)
│   │   ├── Contract.php               # Vertrag: welche Felder Pflicht sind und welchen Typ sie haben
│   │   └── README.md                  # Kurzfassung dieser Anleitung + Link zur API-Doku
│   ├── Instagram/                     # gleicher Aufbau (Client, Mapping, Contract, README)
│   └── Health.php                     # Ampel, Fehlercodes, Notbetrieb, Diagnosebericht
├── tests/
│   ├── fixtures/divera/*.json         # echte, ANONYMISIERTE Beispielantworten (Vertragstests)
│   ├── fixtures/instagram/*.json
│   └── ContractTest.php               # prüft Anonymizer/Mapping gegen die Fixtures
└── src/Cli.php                        # WP-CLI-Befehle aus Abschnitt 3
```

Regeln, die das Reparieren einfach halten:

- **Mapping statt Logik:** Ändert der Anbieter einen Feldnamen, wird nur `Anonymizer.php` (DIVERA) bzw. `Mapping.php` (Instagram) angepasst.
- **Vertrag prüfen, bevor etwas gespeichert wird:** Passt eine Antwort nicht zum Vertrag, speichert
  die Website **nichts** und meldet `*-FMT`. Lieber kein Einsatz als ein falscher oder einer mit zu vielen Daten.
- **Datensparsamkeit im Mapping:** Übernommen werden nur Einsatzart, Ortsteil, auf 15 Minuten gerundete
  Uhrzeit und Fahrzeuge (D-03). Adressen, Namen und Freitexte aus DIVERA werden verworfen, nicht gespeichert.
- **Versionen festnageln:** Die verwendete API-Version steht als Konstante in `Client.php`
  (`const API_VERSION = '[prüfen]'`). Kein „latest“.
- **Geheimnisse nie im Code:** Schlüssel und Tokens liegen verschlüsselt in der WordPress-Datenbank
  (Eingabe über System → „Schlüssel neu eintragen“) bzw. im Passwort-Tresor des Vereins. Nie in Git, nie im Protokoll.

## 3. Werkzeuge (WP-CLI)

| Befehl | Zweck |
|---|---|
| `wp ff-piflas diagnose` | Status beider Schnittstellen, letzte Fehler, Notbetrieb an/aus |
| `wp ff-piflas divera test` | Ein Testabruf, zeigt Code und Antwortzeit, speichert nichts |
| `wp ff-piflas divera dump --anonymize > neu.json` | Aktuelle Antwort anonymisiert speichern (für Fixtures) |
| `wp ff-piflas instagram test` | Testabruf Instagram |
| `wp ff-piflas notbetrieb divera on\|off` | Notbetrieb ohne Backend schalten |
| `composer test` | Alle Tests inkl. Vertragstests gegen `tests/fixtures/` |

## 4. Fehlercodes und was zu tun ist

| Code | Bedeutung | Wer behebt | Vorgehen |
|---|---|---|---|
| `DIV-401` | Schlüssel abgelehnt (HTTP 401/403) | Admin, ohne Technik | Neuen API-Schlüssel in DIVERA erzeugen [Menüpfad laut DIVERA-Hilfe], unter System → „Schlüssel neu eintragen“, „Verbindung testen“ |
| `DIV-NET` | Nicht erreichbar (Timeout, DNS, 5xx) | niemand / Hoster | Automatische Wiederholung alle 5 Min. Nach 24 Std. Notbetrieb + Hoster fragen |
| `DIV-FMT` | Antwort passt nicht zum Vertrag | Technik | Abschnitt 5 |
| `IG-EXP` | Instagram-Token läuft bald ab | Admin | System → „Neu verbinden“ |
| `IG-190` | Instagram-Token ungültig | Admin | System → „Neu verbinden“, mit dem Vereinskonto anmelden |
| `IG-FMT` | Antwort passt nicht zum Vertrag | Technik | Abschnitt 5 (Ordner `instagram/`) |

## 5. „Antwort hat sich geändert“ (`*-FMT`) reparieren

1. **Notbetrieb** ist an (Admin oder `wp ff-piflas notbetrieb divera on`).
2. Auf einer **Kopie** arbeiten (Staging-Seite oder VM laut Lastenheft 4.1; nie mit echten Daten auf der VM).
3. Aktuelle Antwort holen: `wp ff-piflas divera dump --anonymize > tests/fixtures/divera/AAAA-MM-TT.json`
4. Mit der alten Fixture vergleichen: `diff tests/fixtures/divera/letzte.json tests/fixtures/divera/AAAA-MM-TT.json`
5. In der **API-Dokumentation des Anbieters** nachsehen, was geändert wurde (Links im `README.md` des Ordners `src/Divera/` bzw. `src/Instagram/`).
6. **Nur** `Anonymizer.php`/`Mapping.php` (Feldnamen) und ggf. `Contract.php` (Pflichtfelder) anpassen.
   Die Datensparsamkeit (D-03) darf dabei nicht verloren gehen – der Test `ContractTest::testNurErlaubteFelder` prüft das.
7. `composer test` – alle Tests grün, auch mit der **neuen** Fixture.
8. Ändert sich die API-Version: Konstante `API_VERSION` anpassen.
9. Über GitHub einspielen (Pull Request, Tests laufen automatisch), dann auf dem Hosting aktualisieren.
10. System → „Verbindung testen“ → grün. **Notbetrieb aus.** Eintrag in `CHANGELOG.md`.

## 6. Nach der Reparatur

- Von Hand angelegte Einsätze bleiben bestehen; der Import legt **keine Doppel** an
  (Abgleich über die DIVERA-Einsatznummer, die intern gespeichert, aber nie angezeigt wird [prüfen]).
- Im Verlauf jedes Einsatzes steht, ob er „aus DIVERA“ oder „von Hand“ kam.
- Diese Anleitung aktualisieren, falls ein Schritt nicht gepasst hat.

## 7. Links

- DIVERA 24/7 – API-Dokumentation: [Link vom Anbieter eintragen]
- Instagram API mit Instagram-Login (Meta for Developers): [Link eintragen]
- Lastenheft: `docs/lastenheft/` · Handbuch Kapitel 10.2 · Demo: System → Schnittstellen
