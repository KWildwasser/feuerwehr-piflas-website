# Testabdeckung: Lastenheft-IDs → Prüfungen

Stand 23.11.2026 · Lastenheft 1.19 · Demo v17 · `test_app.py` (700 Prüfungen) und `test_security.py` (68 Prüfungen)

So lesen: „Demo“ nennt, wo die Referenz-Demo die Anforderung prüft (Testname oder Bereich der Testsuite). „Echte Website“ sagt, wie sie in WordPress zusätzlich geprüft wird. „–“ heißt: in der Demo nicht prüfbar (Server, Mail, Menschen, Verträge). Diese Liste ist die Abnahmeliste für Claude Code: Jede Zeile braucht vor dem Go-live einen grünen Test oder eine abgehakte Abnahme.

| ID | Prio | Anforderung | Demo | Echte Website |
| --- | --- | --- | --- | --- |
| A-01 | Muss | Alles Veränderliche wird im Backend gepflegt, ohne Programmieren: Seit… | Bereich „System“ | Abnahme von Hand bzw. Checkliste (Phase 7) |
| A-02 | Muss | Geschütztes Design: Die Redaktion arbeitet mit Bausteinen. Layout, Far… | – (Sperre gibt es nur im WordPress-Theme) | Redaktion versucht Farben oder Layout zu ändern – gesperrt |
| A-03 | Muss | Zustands-Ampel im System-Bereich für Erreichbarkeit, Updates, Backup, … | Bereich „System“ | Abnahme von Hand bzw. Checkliste (Phase 7) |
| A-04 | Muss | Automatische Updates und Backups, das Zertifikat erneuert sich selbst.… | – | Auto-Update und Backup im Monatsbericht sichtbar |
| A-05 | Muss | WordPress-Standard und wenige bekannte, kostenlose Plugins statt Eigen… | – | Plugin-Liste in docs/plugins.md prüfen |
| A-06 | Muss | Das Handbuch (PDF, bebildert, Du-Form) ist Teil der Lieferung. Es erkl… | „Handbuch: für eingeloggte Benutzer im Kopf verlinkt“ | Abnahme von Hand bzw. Checkliste (Phase 7) |
| A-07 | Muss | Konten und Verträge laufen auf den Verein (Domain, Hosting, DIVERA, Me… | – | Checkliste: Verträge und Tresor |
| A-08 | Muss | Immer mindestens zwei Admins. Jährlich eine Übergabe-Übung mit Test de… | 3× direkt, z. B. „A-08: letzter zweiter Admin kann nicht herabgestuft wer“ | Übergabe-Übung mit Wiederherstellung |
| A-09 | Muss | Laientest als Abnahme: Ein Mitglied ohne IT-Kenntnisse erledigt zehn t… | – | Laientest mit drei Mitgliedern (Phase 7) |
| A-10 | Muss | Schnittstellen austauschbar gebaut: Je Schnittstelle (DIVERA, Instagra… | 1× direkt, z. B. „A-10: DIV-FMT – bei geänderter Antwort wird nichts über“ | Abnahme von Hand bzw. Checkliste (Phase 7) |
| A-11 | Muss | Diagnose und Notbetrieb im System-Bereich: je Schnittstelle Status, Fe… | 2× direkt, z. B. „D-08/A-11: beide Schnittstellen gestört – alle öffentli“ | Abnahme von Hand bzw. Checkliste (Phase 7) |
| A-12 | Muss | Reparatur-Anleitung „Schnittstellen reparieren“ (docs/betrieb/schnitts… | Bereich „Schnittstellen“ | Reparatur-Probe nach der Anleitung (unter 2 Stunden) |
| B-01 | Muss | Konten nur per Einladung durch einen Admin (Name, E-Mail, Rolle). Der … | 2× direkt, z. B. „Login: keine Rollenauswahl – die Rolle steht im Konto (“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-02 | Muss | Admins sehen den Status jedes Kontos, senden Einladungen erneut oder z… | 5× direkt, z. B. „B-02: eigene Rolle nicht änderbar“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-03 | Muss | Die Rechte sind laut Rollentabelle fest im eigenen Plugin hinterlegt. | 4× direkt, z. B. „B-03: ohne Anmeldung kein Zugriff auf #r (weiter zum Lo“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-04 | Muss | 2-Faktor-Anmeldung ist Pflicht für Admins und den Kommandanten, für al… | 1× direkt, z. B. „B-02/B-04: Hochstufen zum Kommandanten, Hinweis auf 2FA“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-05 | Muss | „Passwort vergessen“ per Mail, Link einmalig 1 Stunde gültig. Die Antw… | 4× direkt, z. B. „B-05: nach 5 Fehlversuchen ist die Anmeldung gesperrt“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-06 | Muss | Der Mitgliederbereich ist voll am Handy bedienbar. Die untere Leiste z… | Bereich „Seitenrundgang in 360/390/430/1280 px“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-07 | Muss | Verlauf: Jeder Beitrag, Einsatzbericht, jedes Fahrzeug und Gerät und d… | Bereich „Verlauf und Spam-Schutz“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-08 | Muss | Bei Austritt deaktiviert ein Admin das Konto nach Nachfrage, statt es … | 6× direkt, z. B. „B-08: Deaktivieren fragt nach und sagt, dass Beiträge b“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-09 | Muss | Ein Beitrag besteht aus Titel, Kategorie (Verein, Übung, Jugendfeuerwe… | Bereich „Beiträge und Fotos“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-10 | Muss | Nach dem Speichern oder Veröffentlichen bleibt man angemeldet in der b… | 4× direkt, z. B. „B-10: nach dem Veröffentlichen bleibt man in „Inhalte“,“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-11 | Muss | Fotos (alle Rollen): mehrere aus Kamera oder Galerie, vor dem Absenden… | Bereich „Beiträge und Fotos“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-12 | Muss | Fotoverwaltung (nur Admins): alle Fotos an einem Ort, jeweils mit Anga… | Bereich „Fotoverwaltung“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-13 | Muss | Handbuch: Das PDF „Handbuch Mitgliederbereich“ ist nach dem Login im K… | Bereich „System“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-14 | Muss | Bearbeiten im Editor (B-19): Beiträge (Titel, Kategorie, Text, Fotos, … | Bereich „Bearbeiten, Ausblenden, Löschen“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-15 | Muss | Ausblenden: Mit denselben Rechten wie bei B-14, aber ohne Freigabe, lä… | Bereich „Bearbeiten, Ausblenden, Löschen“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-16 | Muss | Löschen: nur Admins, für Beiträge und Einsätze, immer erst nach einer … | Bereich „Bearbeiten, Ausblenden, Löschen“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-17 | Muss | Rückgängig: Nach jeder Änderung (speichern, ausblenden, löschen, entfe… | 3× direkt, z. B. „B-17: Rollenänderung rückgängig“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-18 | Muss | Übersicht „Inhalte“ für Beiträge und Einsatzberichte, ausgelegt auf me… | Bereich „Inhalte-Übersicht“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-19 | Muss | Editor: Ein Eintrag öffnet sich auf einer eigenen Seite mit Formular, … | Bereich „Beiträge und Fotos“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-20 | Muss | Grenzen gegen Missbrauch: Höchstlängen für alle Textfelder ohne Ausnah… | 1× direkt, z. B. „B-20: jedes Textfeld hat eine Höchstlänge“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-21 | Muss | Seiten pflegen (Bereich „Seiten“): Verein (Einleitung, Vorstandschaft … | Bereich „Seiten pflegen“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-22 | Muss | Zähler an den Bereichen: Ist etwas zu tun, zeigt das Symbol in der unt… | 4× direkt, z. B. „B-22: Lernen-Tab zeigt Zähler, solange das Monatsthema “ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| B-23 | Muss | Angemeldet bleiben auf der öffentlichen Seite: Wer angemeldet ist, sie… | 2× direkt, z. B. „B-23: auf der öffentlichen Seite angemeldet bleiben – K“ | PHPUnit je Rolle: Capabilities, Nonces, Escaping; Playwright: Ablauf |
| C-01 | Muss | Notruf richtig absetzen (W-Fragen), Verhalten bis zum Eintreffen der F… | Bereich „Inhalte (`test_security.py`)“ | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-02 | Muss | Gewarnt sein: Warn-Apps wie NINA, Bedeutung der Sirenensignale, Link z… | 1× direkt, z. B. „C-02: Warn-App, Sirenensignale, Pegel-Link“ | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-03 | Muss | Rauchmelderpflicht und Brandschutz im Haushalt. | 1× direkt, z. B. „C-03: Rauchmelderpflicht“ | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-04 | Muss | Der Bürgertipp wechselt automatisch mit der Jahreszeit, aus einem pfle… | Bereich „Bürgerinfos“ | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-05 | Soll | Brandschutzerziehung für Kitas und Schulen, Anfrage über das Formular. | – (Soll) | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-06 | Kann | Amtliche Warnungen für Ergolding, vom Server abgerufen, ohne Einbettun… | – (Kann) | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| C-07 | Muss | Probealarm Bayern (2. Donnerstag im März) und Bundesweiter Warntag (2.… | Bereich „Bürgerinfos“ | Playwright: Inhalte; jährliche Prüfung durch den Kommandanten |
| D-01 | Muss | Neue Alarme werden alle 15 Minuten abgerufen und als Entwurf „Ausstehe… | Bereich „Freigabe und DIVERA“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-02 | Muss | Übernommen werden nur Datum, Uhrzeit (auf die Viertelstunde gerundet),… | 1× direkt, z. B. „Einsatz von Hand: Straße oder Hausnummer im Einsatzort “ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-03 | Muss | Zuordnung DIVERA-Stichwort → öffentliche Einsatzart mit Symbol, im Bac… | Bereich „Freigabe und DIVERA“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-04 | Muss | Veröffentlichung frühestens 2 Stunden nach dem Alarm (einstellbar), au… | Bereich „Einsatz von Hand“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-05 | Muss | Alle nicht-privaten Termine werden alle 15 Minuten übernommen, ebenso … | Bereich „Freigabe und DIVERA“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-06 | Muss | Der Zugangsschlüssel liegt nur auf dem Server. | Bereich „Freigabe und DIVERA“ | Code-Suche: Schlüssel nur in wp-config.php; Diagnosebericht ohne Schlüssel |
| D-07 | Soll | Die Jahresstatistik wird automatisch aus den veröffentlichten Einsätze… | Bereich „Freigabe und DIVERA“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-08 | Muss | Fällt DIVERA aus, läuft die Website normal weiter. Der Fehler erschein… | 3× direkt, z. B. „D-08/A-11: beide Schnittstellen gestört – alle öffentli“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| D-09 | Muss | Einsatz von Hand: Kommandant und Admins legen Einsätze ohne DIVERA an … | Bereich „Einsatz von Hand“ | PHPUnit: Vertragstests mit anonymisierten Beispielantworten, Anonymisierer, Cron-Lauf |
| E-01 | Muss | Rolle „Mitglied“: nur lesen und lernen. Die untere Leiste zeigt nur „L… | 4× direkt, z. B. „E-01: Mitglied landet in „Lernen“ und sieht nur diesen “ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-02 | Muss | Ein Thema besteht aus Titel, Monat, Symbol, Einleitung, Abschnitten (Ü… | 1× direkt, z. B. „E-02: „Das Wichtigste“ als eigene Seite“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-03 | Muss | Ein Thema je Monat. Am Monatsersten wird das geplante Thema automatisc… | 6× direkt, z. B. „E-03: Thema des Monats steht oben, Status „offen““ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-04 | Muss | Material der Staatlichen Feuerwehrschulen Bayern (Feuerwehr-Lernbar, M… | 8× direkt, z. B. „E-04: Lernbar nur als Link, kein Einbetten“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-05 | Muss | Themen anlegen, bearbeiten, kopieren und ausblenden: nur Kommandanten,… | 7× direkt, z. B. „E-05: Entwürfe und Verwaltung für Mitglieder unsichtbar“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-06 | Muss | Test: genau 5 Fragen mit je 2 bis 4 Antworten, genau eine richtig, jed… | 6× direkt, z. B. „E-06: ohne Antwort keine Auswertung“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-07 | Muss | Eigener Lernstand: Jede Person sieht nur ihre eigenen Ergebnisse – je … | 5× direkt, z. B. „E-07: Mitglied sieht den eigenen Lernstand“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-08 | Muss | Lernstand (nur Kommandanten): je Thema Teilnahme (x von y, in %), Zahl… | 5× direkt, z. B. „E-08/E-09: Lernstand mit Datenschutz-Hinweis“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-09 | Muss | Sichtbarkeit: Einzelergebnisse sehen nur die Person selbst und die Kom… | 4× direkt, z. B. „E-09: Mitglied sieht keine Ergebnisse oder Namen andere“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-10 | Muss | Wer zählt: alle Konten mit dem Häkchen „Gehört zur Einsatzabteilung“. … | 2× direkt, z. B. „E-10: Konten außerhalb der Einsatzabteilung gekennzeich“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-11 | Muss | Datensparsam: gespeichert werden nur Konto, Thema, Zeitpunkt, gegebene… | 2× direkt, z. B. „E-11/E-12: Hinweis zu Freiwilligkeit, Sichtbarkeit, Lös“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-12 | Muss | Hinweise: Auf „Lernen“ ein aufklappbarer Hinweis „Wer sieht meine Erge… | 3× direkt, z. B. „E-11/E-12: Hinweis zu Freiwilligkeit, Sichtbarkeit, Lös“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-13 | Soll | E-Mail am Monatsersten an alle Konten der Einsatzabteilung: nur Titel … | – (Mail) | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-14 | Muss | Barrierefrei nach N-02: Tastatur und Vorlesesoftware, ab 360 px ohne s… | Bereich „Lernen“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-15 | Muss | Messbare Ziele: vom Login bis zum ersten Lerninhalt höchstens 2 Tipps;… | Bereich „Gern und leicht lernen“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-16 | Muss | Startseite „Lernen“: persönliche Begrüßung („Servus, Anna!“) und ein S… | 3× direkt, z. B. „E-16: persönliche Begrüßung, Dauer des Themas genannt“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-17 | Muss | Lernen in Schritten: je Abschnitt eine Seite, dann „Das Wichtigste“ mi… | 7× direkt, z. B. „E-16/E-17: „Los geht’s“ auf der Karte führt direkt zur “ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-18 | Muss | Test: eine Frage pro Bildschirm mit großen Antwortflächen. Nach „Antwo… | 3× direkt, z. B. „E-18: eine Frage pro Bildschirm“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-19 | Muss | Ergebnis: „Geschafft!“ mit kurzer Erfolgs-Animation (entfällt bei der … | 4× direkt, z. B. „E-06/E-19: 3 von 5 – nicht bestanden, ermutigend formul“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-20 | Muss | Persönlicher Fortschritt: „x von y Themen geschafft“ mit Balken und di… | 3× direkt, z. B. „E-20: Serie „2 Monate in Folge“ nur für die Person selb“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-21 | Soll | Gemeinsames Ziel: „x von y aus der Einsatzabteilung haben das Thema sc… | 1× direkt, z. B. „E-21: gemeinsames Ziel als anonyme Zahl“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-22 | Muss | Nachholen: offene frühere Themen stehen oben als Karten „Zum Nachholen… | Bereich „Gern und leicht lernen“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-23 | Muss | Jedes Thema hat ein Symbol mit Farbe (Auswahl: Verkehr, Erste Hilfe, G… | 2× direkt, z. B. „E-16/E-23: Thema des Monats als große Karte mit Symbol,“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-24 | Soll | Erinnern ohne zu nerven: höchstens eine freundliche Erinnerung zur Mon… | Bereich „Gern und leicht lernen“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-25 | Soll | Leichter Zugang: Der Link in der Mail führt nach dem Login direkt zum … | Bereich „Gern und leicht lernen“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-26 | Muss | Themenplan für Kommandanten: 12 Monate auf einen Blick (2 zurück, 9 vo… | 5× direkt, z. B. „E-26: Themenplan zeigt 12 Monate, der aktuelle hervorge“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-27 | Muss | Hilfen beim Anlegen: Themenideen zum Antippen (setzen Titel und Symbol… | 3× direkt, z. B. „E-27: Themenideen und Hinweis „Was fehlt noch?““ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| E-28 | Muss | Abnahme mit Laien (wie A-09): Drei Mitglieder ohne Einweisung schaffen… | – (Laientest) | Laientest mit drei Mitgliedern und einem Kommandanten |
| E-29 | Muss | Bilder und Skizzen: Je Abschnitt ein Bild, am besten eine einfache Ski… | 4× direkt, z. B. „E-29: Überblick zeigt die erste Skizze mit Bildbeschrei“ | PHPUnit: Rechteprüfung „Lernstand sehen“, Löschfrist per Cron; Playwright: Ablauf |
| F-01 | Muss | Startseite: Von oben nach unten: (1) Bühne mit Foto und den Buttons „M… | Bereich „Startseite“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-02 | Muss | Aktuelles: Beiträge als Liste mit Foto, filterbar nach Kategorie; zuer… | Bereich „Aktuelles und Einsätze“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-03 | Muss | Einsätze: Liste der neuesten drei Jahre als Knöpfe, ältere Jahre über … | Bereich „Aktuelles und Einsätze“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-04 | Muss | Termine: Nicht-private DIVERA-Termine (D-05) mit Kategorien. Jubiläums… | 1× direkt, z. B. „F-04: Termine mit „Vormerken“ und Kalender-Abo“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-05 | Muss | Fahrzeuge & Technik: Neuestes Fahrzeug hervorgehoben. Je Fahrzeug eine… | „Fahrzeugseite zeigt alle Fotos inkl. Wechsellader“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-06 | Muss | Mitmachen: Formular ganz oben (Name, Telefon oder E-Mail, Interesse, D… | Bereich „Formulare“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-07 | Muss | Jugendfeuerwehr: Vorstellung, Gruppenstunde, Ansprechperson, Button „S… | 1× direkt, z. B. „F-07/L-11: Jugendfeuerwehr mit „Schnuppern“, Fotos nur “ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-08 | Muss | Verein & Chronik: Vorstandschaft, Mitgliedschaft und Chronik ab Gründu… | „Chronik: sofort auf der Website“, „Partner: Verweis von der Verein-Seite“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-09 | Muss | Partnerfeuerwehren: Eigene Seite. Je Wehr (Ergolding, Oberglaim) eine … | Bereich „Navigation“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-10 | Muss | Bürgerinfos, Fördermitglied, Impressum/Datenschutz: Siehe 2.7, 2.8 und… | „Recht/Impressum enthält …“, „Recht/Datenschutz enthält …“ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-11 | Muss | Navigation: Kopf mit Logo und Menü, ohne Notruf-Button (Notruf 112 ste… | 3× direkt, z. B. „F-11: kein Notruf-Knopf im Kopf, Notruf 112 bleibt auf “ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-12 | Muss | Fußzeile: Adresse, E-Mail, Telefon (nicht ständig besetzt), Impressum,… | 1× direkt, z. B. „F-12: Telefon mit Hinweis „nicht ständig besetzt““ | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-13 | Soll | Archiv: Ausgewählte alte Einsatzberichte aus Joomla übernehmen, alte A… | – (Soll, Joomla-Umzug) | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| F-14 | Kann | Suche: Volltextsuche. | – (Kann) | Playwright gegen die Testseite (übertragene Demo-Prüfungen) |
| I-01 | Muss | Vorschau mit den neuesten 9 Beiträgen, die der Server abruft und zwisc… | 1× direkt, z. B. „I-01/A-11: Instagram gestört – statt Vorschau nur ein L“ | PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto |
| I-02 | Muss | Freigegebene Einsätze und Beiträge mit Häkchen werden als Bild- oder K… | „Instagram-Kachel erscheint“ | PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto |
| I-03 | Muss | Die Bildunterschrift kommt aus einer Vorlage mit Text, „Link in Bio“ u… | – | PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto |
| I-04 | Muss | Der Zugangsschlüssel (Token) erneuert sich automatisch. Bei Problemen … | „Wartbarkeit: Instagram mit einem Klick neu verbinden“ | PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto |
| I-05 | Kann | Facebook-Crosspost. | – (Kann) | PHPUnit: Vertragstests mit Beispielantworten; Testpost mit Meta-Testkonto |
| J-01 | Muss | Im System-Bereich: Jubiläum an/aus und Enddatum (Standard: Ankündigung… | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-02 | Muss | Auf der Startseite ein Bereich mit Siegel „125 Jahre“ und Countdown zu… | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-03 | Muss | Eigene Seite mit dem Festjahr als Zeitleiste: Rückblick bei vergangene… | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-04 | Muss | Die Termine kommen aus DIVERA (Kategorie „Jubiläum“). | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-05 | Soll | Nach jedem Fest wird ein Rückblick-Entwurf angelegt. | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-06 | Muss | Nach dem Festjahr verschwinden Bereich, Menüpunkt und Hinweis automati… | Bereich „Jubiläum“ | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| J-07 | Soll | Aufruf zum Mithelfen und zur Fördermitgliedschaft, dazu ein Foto-Hinwe… | – (Soll) | PHPUnit: Zeitsteuerung mit gesetztem Datum; Playwright |
| L-01 | Muss | Art. 4, 5 BayFwG: Verein betreibt, Kommandant gibt frei, schriftlich m… | „Recht/Impressum enthält …“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-02 | Muss | Verschwiegenheit (Art. 20 GO, Merkblatt StMI): Keine vertraulichen Ein… | „E-Mail: nur Hinweis, keine Inhalte …“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-03 | Muss | DSGVO / BayDSG: Keine erkennbaren Personen, Kennzeichen oder Objekte; … | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-04 | Muss | Pietät: Bei Verletzten oder Toten erst nach Information von Polizei un… | 1× direkt, z. B. „W-05/L-04: Warnhinweis bei technischer Hilfe“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-05 | Muss | DSGVO Art. 6, 13, 21; KUG: Fotos von Festen und Übungen: vorher inform… | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-06 | Muss | Urheberrecht: Nur Fotos mit geklärten Rechten | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-07 | Muss | § 5 DDG, § 18 MStV: Vollständiges Impressum | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-08 | Muss | DSGVO Art. 13, 26, 28: Datenschutzerklärung (Hosting, Formulare, Konte… | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-09 | Muss | TDDDG § 25: Keine Cookies beim Besuch, keine Drittanbieter | 1× direkt, z. B. „N-01/L-09: während aller Sicherheitstests keine Anfrage“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-10 | Muss | Satzung, AO: Keine Spenden online | Bereich „Recht“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-11 | Muss | Jugendschutz: Hinweis für unter 16-Jährige, Jugendfotos nur mit Einwil… | 1× direkt, z. B. „F-07/L-11: Jugendfeuerwehr mit „Schnuppern“, Fotos nur “ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-12 | Muss | BFSG / BayBITV: Vermutlich nicht verpflichtend; Ziel trotzdem WCAG 2.2… | Seitenrundgang „Barrierefreiheit-Basics“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-13 | Muss | Haftung für Links: Externe Links erkennbar, Hinweis im Impressum | „Recht/Impressum: Hinweis zu externen Links“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-14 | Muss | Urheberrecht (UrhG): Lehrmaterial der Feuerwehrschulen, der DGUV und a… | „E-04: Lernbar nur als Link“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-15 | Muss | DSGVO Art. 5, 6, 13, 26/28; BayDSG: Lernergebnisse sind personenbezoge… | „E-11/E-12: Hinweis …“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-16 | Muss | Ehrenamt, Persönlichkeitsrecht: Keine Leistungs- oder Verhaltenskontro… | „E-09: Mitglied sieht keine Ergebnisse oder Namen anderer“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| L-17 | Muss | DGUV Vorschrift 49 (§ 8 Unterweisung), FwDV 2, BayFwG: Ausbildung und … | „E-12: Sicherheitshinweis“ | Prüfung durch Fachperson bzw. Markt; technische Teile per Test |
| M-01 | Muss | Ein externer Dienst prüft die Startseite alle 5 Minuten. Bei Ausfall u… | – | Abnahme von Hand: Dienst einrichten, Ausfall simulieren, Mail prüfen |
| M-02 | Muss | Warnung auch bei Teilfehlern: DIVERA seit über 2 Stunden gestört, Back… | „Wartbarkeit: Zustands-Ampel mit 6 Punkten“ | Abnahme von Hand: Dienst einrichten, Ausfall simulieren, Mail prüfen |
| M-03 | Muss | Monatsbericht per Mail am 1. an Admins und Vorstand: Verfügbarkeit, Up… | – | Abnahme von Hand: Dienst einrichten, Ausfall simulieren, Mail prüfen |
| M-04 | Muss | Die Besucherstatistik läuft selbst gehostet, ohne Cookies und ohne Wei… | „Recht/DSGVO: keine Anfragen an Dritte“ | Abnahme von Hand: Dienst einrichten, Ausfall simulieren, Mail prüfen |
| N-01 | Muss | Datenschutz | 1× direkt, z. B. „N-01/L-09: während aller Sicherheitstests keine Anfrage“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-02 | Muss | Barrierefreiheit | Bereich „Seitenrundgang in 360/390/430/1280 px“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-03 | Muss | Mobile first | Bereich „Seitenrundgang in 360/390/430/1280 px“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-04 | Muss | Performance | – | Lighthouse mobil ≥ 90 |
| N-05 | Muss | Sicherheit | 9× direkt, z. B. „B-03/N-05: role – verbotene Aktionen ändern nichts, auc“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-06 | Muss | Betrieb | – | Wiederherstellung auf der Testseite proben |
| N-07 | Muss | Kosten | – | Kostenaufstellung beim Go-live |
| N-08 | Muss | Design | 1× direkt, z. B. „N-08: Rot #CD1719 und selbst gehostete Roboto“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-09 | Muss | Ansprache | Bereich „Ansprache“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-10 | Muss | Bildrechte | Bereich „Inhalte (`test_security.py`)“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-11 | Muss | Tests | Diese Liste | Lighthouse, axe, Security-Header-Scan, Playwright |
| N-12 | Muss | SEO | – | Sitemap und strukturierte Daten prüfen |
| N-13 | Muss | Frauen und Männer | 1× direkt, z. B. „Ansprache: N-13 – keine rein männlichen Formen, Ausnahm“ | Lighthouse, axe, Security-Header-Scan, Playwright |
| R-01 | Muss | Plan im Mitgliederbereich mit Thema, Datum, zuständiger Person und Sta… | „Thema einplanen“ | PHPUnit: Zeitsteuerung und Erinnerungen per Cron; Playwright |
| R-02 | Soll | Feste Formate und Jahresanlässe (Hauptversammlung, Dorffest, Steckerlf… | – (Soll) | PHPUnit: Zeitsteuerung und Erinnerungen per Cron; Playwright |
| R-03 | Muss | Beiträge zeitgesteuert veröffentlichen, auch auf Instagram. | „Einsatz von Hand: 2-Stunden-Regel …“ (gleiche Zeitsteuerung) | PHPUnit: Zeitsteuerung und Erinnerungen per Cron; Playwright |
| R-04 | Muss | Erinnerung an die zuständige Person 3 Tage vor dem Termin. Kommt 14 Ta… | – (Mail) | PHPUnit: Zeitsteuerung und Erinnerungen per Cron; Playwright |
| S-01 | Muss | Seite „Fördermitglied werden“: warum, was der Beitrag bewirkt, Höhe de… | 2× direkt, z. B. „S-01: „Fördermitglied werden“ von Startseite, Mitmachen“ | Playwright |
| S-02 | Muss | Downloads: „Beitrittserklärung Fördermitglied“ und „Spendenformular“ a… | „Beitrittserklärung-PDF verlinkt“ | Playwright |
| S-03 | Soll | Dank an alle, die uns unterstützen, Sponsoren mit Logo, nur mit deren … | – (Soll) | Playwright |
| W-01 | Muss | Für jeden Einsatz-Entwurf und jeden eingereichten Beitrag oder jede ei… | Bereich „Freigabe und DIVERA“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-02 | Muss | Freigabe am Handy im Bereich „Freigabe“, mit Zähler der offenen Einträ… | Bereich „Freigabe und DIVERA“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-03 | Muss | Vor der Freigabe lassen sich Kurztext und Fotos ergänzen (Regeln wie B… | Bereich „Freigabe und DIVERA“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-04 | Muss | Ohne Pflicht-Häkchen keine Veröffentlichung, serverseitig geprüft. Bei… | Bereich „Formulare“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-05 | Muss | Warnhinweis bei technischer Hilfe: Gibt es Verletzte oder Tote, wird e… | 1× direkt, z. B. „W-05/L-04: Warnhinweis bei technischer Hilfe“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-06 | Muss | Häkchen „Auch auf Instagram“, getrennt von der Veröffentlichung auf de… | 1× direkt, z. B. „W-06: eigenes Häkchen „Auch auf Instagram“ je Einreichu“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-07 | Muss | Einsätze lassen sich verwerfen, Beiträge und Änderungen „Zurück zur Üb… | Bereich „Freigabe und DIVERA“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-08 | Muss | Änderungen der Redaktion an Beiträgen, Seiten, Fahrzeugen, Ausrüstung … | Bereich „Seiten pflegen“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |
| W-09 | Muss | E-Mail an die Kommandanten: Bei jeder neuen Einreichung (Einsatz-Entwu… | Bereich „Freigabe und DIVERA“ | PHPUnit: Rechte und Pflicht-Häkchen auf dem Server; Playwright: Ablauf |

**Summe:** 156 Anforderungen. 133 prüft die Demo, 23 lassen sich nur in der echten Website oder von Hand prüfen.

## Sicherheit und Ausfallsicherheit (`test_security.py`)

- **Rechte (B-03):** Rolle × Bereich als Matrix; jede schreibende Aktion und jedes Formular auch ohne sichtbaren Knopf – verbotene ändern nichts und melden „Dafür fehlen dir die Rechte“.
- **Eingaben (N-05, B-20):** Schadcode in allen Formularen aller Rollen und in der Adresse wird nie ausgeführt; jedes Textfeld hat eine Höchstlänge; externe Links nur mit https:// (beim Speichern und bei der Ausgabe).
- **Anmeldung (B-01, B-05, B-08):** keine Meldung verrät, ob es ein Konto gibt; Sperre nach 5 Fehlversuchen, auch beim 2-Faktor-Code; „Passwort vergessen“ antwortet immer gleich; Austritt deaktiviert statt löscht, Beiträge bleiben; eigenes Konto und zweiter Admin geschützt.
- **Ausfall (D-08, A-10, A-11, I-01):** beide Schnittstellen gestört – öffentliche Seiten laufen ohne Fehlermeldung; geänderte DIVERA-Antwort übernimmt nichts; Doppelklick und doppeltes Absenden erzeugen nichts doppelt; 60 wilde Adressen; 1.000 Beiträge.

**In WordPress zusätzlich:** Nonce je Formular, `current_user_can()` je Aktion, PHPCS mit WordPress-Sicherheitsregeln (Escaping, Sanitizing), Security-Header-Scan, Login-Drosselung auf dem Server, Backup-Wiederherstellung auf der Testseite.
