# Lastenheft & Umsetzungsplan – Webpräsenz Feuerwehr Piflas

23.11.2026 · Korbinian · Version 1.6 (WordPress) · Referenz: Demo v5 und Handbuch 1.4

## 0. Auf einen Blick

- **Was:** Neue Website für www.feuerwehr-piflas.de. Ausgewählte Mitglieder pflegen sie mit eigenen Konten.
- **Automatisch:** Einsätze und nicht-private Termine kommen aus DIVERA 24/7. Freigegebene Beiträge gehen auf Wunsch auf Instagram.
- **Technik:** WordPress auf dem bestehenden Hosting, ein eigenes Theme und ein eigenes Plugin. Beides baut Claude Code nach diesem Lastenheft.
- **Leitprinzip:** Ehrenamtliche ohne IT-Kenntnisse können die Seite auch in Jahren noch betreuen (2.11).
- **Vorhanden:**
  - Übergangsseite
  - Klickbare Demo v5 mit Testsuite (430 Prüfungen)
  - Handbuch für den Mitgliederbereich
  - Backup-Paket
- **Wichtigste offene Entscheidung:** Wer betreut die Seite, und in welcher Betriebsvariante (4.3)?

## 1. Ausgangslage & Ziele

**Ist-Zustand (November 2026)**

- feuerwehr-piflas.de zeigt nur noch „Homepage wird neu gestaltet“. Alte Joomla-Seiten sind teils noch erreichbar.
- Betreiber ist der Feuerwehr Piflas e.V. (VR 1115, AG Landshut).
- Die Freiwillige Feuerwehr Piflas ist eine Ortsfeuerwehr des Marktes Ergolding. Partnerfeuerwehren sind Ergolding (www.ff-ergolding.de) und Oberglaim (oberglaim.feuerwehren.bayern).
- Etwa 70 Mitglieder, davon gut 50 aktiv.
- Fuhrpark: Wechsellader mit Kran (36/1), zwei Löschfahrzeuge, 56/1, Mannschaftstransporter 11/1 und Anhänger.
- Aktiver Kanal ist heute Instagram @feuerwehrpiflas.
- 2027 feiert die Feuerwehr 125 Jahre (Gründung 1902, noch zu bestätigen).

**Ziele**

1. Bürgerinnen und Bürger informieren und Nachwuchs gewinnen, Frauen wie Männer. „Mitmachen“ ist so einfach wie möglich.
2. Mitglieder pflegen Inhalte selbst. Die Admins laden sie ein und vergeben Rechte.
3. Einsätze und Termine kommen automatisch. Einsätze werden per Klick am Handy freigegeben.
4. Rechtssicher nach Feuerwehrgesetz, Datenschutz und Persönlichkeitsrechten.
5. Keine höheren laufenden Kosten als heute.
6. Dauerhaft wartbar durch Ehrenamtliche.

**Grundsätze:** Durchgehend Du-Form, Frauen und Männer gleichermaßen angesprochen (N-13), einfache Sprache, alles am Handy bedienbar, nichts, was Einsatzbetroffene erkennbar macht.

## 2. Funktionale Anforderungen

Priorität: **Muss** = zum Go-live, **Soll** = kurz danach, **Kann** = später. Claude Code nennt die IDs in Branches, Tests und Pull Requests.

### 2.1 Seiten & Navigation

| ID | Bereich | Inhalt | Prio |
| --- | --- | --- | --- |
| F-01 | Startseite | Von oben nach unten: (1) Bühne mit Foto und den Buttons „Mitmachen“ und „Fördermitglied werden“. (2) Notruf 112, darunter 14 Tage vor Warntag oder Probealarm ein Hinweis (C-07). (3) Jubiläumsbereich, nur im Festjahr (J-02). (4) Nächste 3 Termine und letzte 3 Einsätze. (5) „Aus dem Vereinsleben“: 3 Foto-Kacheln mit Link zum Beitrag. (6) Mitmach-Bereich (F-06). (7) Bürgertipp oder Sonderhinweis (C-04). (8) Instagram-Vorschau (I-01). Keine Fahrzeugdaten. | Muss |
| F-02 | Aktuelles | Beiträge als Liste mit Foto. Beitragsseite mit Titelbild, Text und Galerie. | Muss |
| F-03 | Einsätze | Liste, filterbar nach Jahr und Art. Detail mit Einsatzart, Ortsteil, gerundeter Uhrzeit und Fahrzeugen. Jahresstatistik (D-07). | Muss |
| F-04 | Termine | Nicht-private DIVERA-Termine (D-05) mit Kategorien. Jubiläumstermine gekennzeichnet. „Vormerken“ als Kalenderdatei (.ics). | Muss |
| F-05 | Fahrzeuge & Technik | Neuestes Fahrzeug hervorgehoben. Je Fahrzeug eine Karte mit Foto, Funkrufname, Typ und Kurzbeschreibung. Dazu Geräte mit Fotos. | Muss |
| F-06 | Mitmachen | Formular ganz oben (Name, Telefon oder E-Mail, Interesse, Datenschutz-Häkchen) mit Hinweis für unter 16-Jährige. Kurzform des Formulars auf der Startseite. Dazu der nächste Übungsabend und Wege zu Jugendfeuerwehr und Fördermitgliedschaft. Anfragen gehen per E-Mail an eine im System-Bereich hinterlegte Adresse. Die Website speichert sie nicht dauerhaft. Spamschutz ohne Drittanbieter (kein reCAPTCHA). | Muss |
| F-07 | Jugendfeuerwehr | Vorstellung, Gruppenstunde, Ansprechperson, Button „Schnuppern kommen“. Fotos nur mit Einwilligung der Eltern. | Muss |
| F-08 | Verein & Chronik | Vorstandschaft, Mitgliedschaft und Chronik ab Gründung. Das Festjahr 2027 bleibt nach dem Jubiläum in der Chronik (J-06). Verweis auf die Partnerfeuerwehren. | Muss |
| F-09 | Partnerfeuerwehren | Eigene Seite. Je Wehr (Ergolding, Oberglaim) eine Karte mit Kurzbeschreibung und Button „Zur Website“. Reine Links mit neuem Tab und rel=noopener, nichts eingebettet. Die Adressen pflegen die Admins im System-Bereich. | Muss |
| F-10 | Bürgerinfos, Fördermitglied, Impressum/Datenschutz | Siehe 2.7, 2.8 und 3.1. | Muss |
| F-11 | Navigation | Kopf mit Logo, Notruf-Button und Menü. Menü: Start · 125 Jahre (nur im Festjahr) · **Aktuell:** Aktuelles, Einsätze, Termine · **Mitmachen:** Aktiv mitmachen, Jugendfeuerwehr, Fördermitglied werden · **Ratgeber:** Bürgerinfos · **Über uns:** Verein & Chronik, Fahrzeuge & Technik, Partnerfeuerwehren. Neue Seiten kommen in eine bestehende Gruppe. Keine eigene Seite für den Gemeinderat. | Muss |
| F-12 | Fußzeile | Adresse, E-Mail, Telefon (nicht ständig besetzt), Impressum, Datenschutz, Instagram, Facebook, Partnerfeuerwehren, Login für Mitglieder, Bildnachweis. | Muss |
| F-13 | Archiv | Ausgewählte alte Einsatzberichte aus Joomla übernehmen, alte Adressen mit 301 weiterleiten. | Soll |
| F-14 | Suche | Volltextsuche. | Kann |

### 2.2 DIVERA 24/7

| ID | Anforderung | Prio |
| --- | --- | --- |
| D-01 | Neue Alarme werden alle 15 Minuten abgerufen und als Entwurf „Ausstehender Review“ angelegt. | Muss |
| D-02 | Übernommen werden nur Datum, Uhrzeit (auf die Viertelstunde gerundet), Einsatzart, Ortsteil und eigene Fahrzeuge. Nie Straßen, Hausnummern, Namen, Meldertexte, Kennzeichen oder Patientendaten. Statt medizinischer Details steht „Unterstützung Rettungsdienst“. | Muss |
| D-03 | Zuordnung DIVERA-Stichwort → öffentliche Einsatzart mit Symbol, im Backend pflegbar. | Muss |
| D-04 | Veröffentlichung frühestens 2 Stunden nach dem Alarm (einstellbar), auch nach der Freigabe. | Muss |
| D-05 | Alle nicht-privaten Termine werden alle 15 Minuten übernommen, ebenso Änderungen und Absagen. Nur Titel, Datum, Uhrzeit, Ort und Kategorie, keine Angaben zu Teilnehmenden, keine Notizen. | Muss |
| D-06 | Der Zugangsschlüssel liegt nur auf dem Server. | Muss |
| D-07 | Die Jahresstatistik wird automatisch aus den veröffentlichten Einsätzen berechnet. | Soll |
| D-08 | Fällt DIVERA aus, läuft die Website normal weiter. Der Fehler erscheint in der Ampel (A-03) und kommt per Mail. | Muss |

### 2.3 Freigabe

| ID | Anforderung | Prio |
| --- | --- | --- |
| W-01 | Für jeden Einsatz-Entwurf und jeden eingereichten Beitrag oder jede eingereichte Änderung bekommt die Freigabegruppe eine Nachricht mit Link. Zur Gruppe gehören alle mit der Rolle Kommandant · Freigabe (Kommandant, stellvertretender Kommandant, ggf. Vorstand) und auf Wunsch die Admins. | Muss |
| W-02 | Freigabe am Handy im Bereich „Freigabe“, mit Zähler der offenen Einträge. | Muss |
| W-03 | Vor der Freigabe lassen sich Kurztext und Fotos ergänzen (Regeln wie B-11). | Muss |
| W-04 | Ohne Pflicht-Häkchen keine Veröffentlichung, serverseitig geprüft. Bei Einsätzen lautet es „keine erkennbaren Personen, Kennzeichen, Adressen oder vertraulichen Details“. Bei Beiträgen lautet es „Bildrechte geklärt, Abgebildete informiert bzw. einverstanden (bei Kindern die Eltern)“. | Muss |
| W-05 | Warnhinweis bei technischer Hilfe: Gibt es Verletzte oder Tote, wird erst veröffentlicht, wenn Polizei und Angehörige informiert sind. | Muss |
| W-06 | Häkchen „Auch auf Instagram“, getrennt von der Veröffentlichung auf der Website. | Muss |
| W-07 | Einsätze lassen sich verwerfen, Beiträge „Zurück zur Überarbeitung“ schicken, jeweils mit optionaler Begründung. | Muss |

### 2.4 Instagram

Voraussetzung: @feuerwehrpiflas ist ein professionelles Konto (Business). Eine Facebook-Seite ist nicht nötig.

| ID | Anforderung | Prio |
| --- | --- | --- |
| I-01 | Vorschau mit den neuesten 9 Beiträgen, die der Server abruft und zwischenspeichert. Kein Instagram-Einbetten, keine Cookies, keine Datenübertragung an Meta beim Seitenaufruf. | Muss |
| I-02 | Freigegebene Einsätze und Beiträge mit Häkchen werden als Bild- oder Karussell-Post veröffentlicht. Ohne Foto erzeugt die Website eine Grafik im Feuerwehr-Design. | Muss |
| I-03 | Die Bildunterschrift kommt aus einer Vorlage mit Text, „Link in Bio“ und festen Hashtags. 2027 kommt #125JahreFFPiflas dazu. | Muss |
| I-04 | Der Zugangsschlüssel (Token) erneuert sich automatisch. Bei Problemen meldet sich die Ampel mit dem Knopf „Neu verbinden“, zusätzlich kommt eine Mail. | Muss |
| I-05 | Facebook-Crosspost. | Kann |

### 2.5 Konten, Rollen & Beiträge

| ID | Anforderung | Prio |
| --- | --- | --- |
| B-01 | Konten nur per Einladung durch einen Admin (Name, E-Mail, Rolle). Der Link gilt einmalig 48 Stunden, das Passwort vergibt das Mitglied selbst. Keine Selbstregistrierung. | Muss |
| B-02 | Admins können Rollen ändern, Einladungen erneut senden oder zurückziehen und sehen den Status jedes Kontos. | Muss |
| B-03 | Die Rechte sind laut Rollentabelle fest im eigenen Plugin hinterlegt. | Muss |
| B-04 | 2-Faktor-Anmeldung ist Pflicht für Admins und den Kommandanten, für alle anderen empfohlen. | Muss |
| B-05 | „Passwort vergessen“ per Mail. Nach mehreren Fehlversuchen wird das Konto vorübergehend gesperrt. | Muss |
| B-06 | Der Mitgliederbereich ist voll am Handy bedienbar. Die untere Leiste zeigt nur die Bereiche der eigenen Rolle. | Muss |
| B-07 | Protokoll: wer wann was angelegt, freigegeben oder an Rechten geändert hat. | Soll |
| B-08 | Bei Austritt wird das Konto deaktiviert, nicht gelöscht. Die Beiträge bleiben erhalten. | Muss |
| B-09 | Ein Beitrag besteht aus Titel, Kategorie (Verein, Übung, Jugendfeuerwehr, Bürgertipp), Text, Fotos, optionaler Bildbeschreibung, dem Instagram-Häkchen und der Pflicht-Bestätigung (W-04). Kommandant und Admins veröffentlichen direkt, die Redaktion reicht zur Freigabe ein. | Muss |
| B-10 | Nach dem Speichern springt die Seite zum Beitrag. In der Rolle Redaktion erscheint er als „Vorschau – noch nicht öffentlich“, bis er freigegeben ist. | Muss |
| B-11 | Fotos (alle Rollen): mehrere aus Kamera oder Galerie, vor dem Absenden einzeln entfernbar. Das erste ist das Titelbild. Beim Hochladen werden sie auf max. 1600 px verkleinert, Standort- und Kameradaten werden auch im Original entfernt. Nur Bilddateien sind erlaubt. | Muss |
| B-12 | Fotoverwaltung (nur Admins): alle Fotos an einem Ort, jeweils mit Angabe, wo sie verwendet werden. „Ersetzen“ tauscht ein Foto überall aus. „Entfernen“ fragt nach und hinterlässt einen Platzhalter. Instagram-Bilder werden nur auf der Website ausgeblendet. | Muss |
| B-13 | Handbuch: Das PDF „Handbuch Mitgliederbereich“ ist nach dem Login im Kopf jeder Seite verlinkt (Buch-Symbol) und zusätzlich im System-Bereich. Es ist öffentlich nicht verlinkt, im Theme hinterlegt und von den Admins austauschbar. Inhalt und Pflege: A-06. | Muss |
| B-14 | Bearbeiten: Veröffentlichte Beiträge lassen sich im selben Formular ändern (Titel, Kategorie, Text, Fotos, Bildbeschreibung), wieder mit Pflicht-Bestätigung (W-04). Die Redaktion bearbeitet nur eigene Beiträge; ihre Änderung geht zur Freigabe, bis dahin bleibt die bisherige Fassung online. Die Bereichsredaktion bearbeitet im eigenen Bereich, Kommandant und Admins alle Beiträge, jeweils sofort online. Kommandant und Admins können auch den Kurzbericht von Einsätzen ändern. Änderungen werden nicht erneut auf Instagram gepostet. | Muss |
| B-15 | Ausblenden: Mit denselben Rechten wie bei B-14, aber ohne Freigabe, lässt sich ein Beitrag oder Einsatz sofort von der Website nehmen. Er bleibt gespeichert und lässt sich wieder einblenden. Ausgeblendetes erscheint nirgends öffentlich, auch nicht in der Einsatzstatistik. Ein Instagram-Post bleibt bestehen; darauf weist die Website hin. | Muss |
| B-16 | Löschen: nur Admins, für Beiträge und Einsätze, immer erst nach einer Nachfrage. Gelöschtes kommt in den Papierkorb, lässt sich 30 Tage lang wiederherstellen und wird danach endgültig gelöscht. Gelöschte oder ausgeblendete Einsätze legt der DIVERA-Abgleich nicht erneut an. | Muss |

**Rollen**

| Rolle | Für wen | Bereiche | Darf |
| --- | --- | --- | --- |
| Admin | Webmaster/in und eine zweite Person (A-08) | Freigabe, Beiträge, Planung, Fotos, Mitglieder, System | Alles, auch Mitglieder einladen, Rollen vergeben, Fotos verwalten, Einstellungen ändern und Inhalte nach Nachfrage löschen |
| Kommandant · Freigabe | Kommandant, stellvertretender Kommandant, Vorstand | Freigabe, Beiträge, Planung | Beiträge und Einsätze veröffentlichen, alle bearbeiten und ausblenden, Instagram-Post auslösen |
| Redaktion | Pressearbeit, Aktive | Beiträge, Planung | Beiträge mit Fotos schreiben und einreichen, eigene bearbeiten (über die Freigabe) und ausblenden, nicht selbst veröffentlichen |
| Bereichsredaktion | z. B. Jugendwart | Beiträge, Planung | Im eigenen Bereich schreiben, veröffentlichen, bearbeiten und ausblenden |

### 2.6 Überwachung

| ID | Anforderung | Prio |
| --- | --- | --- |
| M-01 | Ein externer Dienst prüft die Startseite alle 5 Minuten. Bei Ausfall und bei Entwarnung gehen sofort Mail und Push an die Admins. | Muss |
| M-02 | Warnung auch bei Teilfehlern: DIVERA seit über 2 Stunden gestört, Backup oder Update fehlgeschlagen, Instagram-Zugang oder Zertifikat laufen in unter 14 Tagen ab, Speicher über 80 %. | Muss |
| M-03 | Monatsbericht per Mail am 1. an Admins und Vorstand: Verfügbarkeit, Updates, Backups, Besuche (ohne Cookies), meistgelesene Seiten, Beiträge im Vergleich zum Ziel, offene Freigaben. Er endet mit „Zu tun“. | Muss |
| M-04 | Die Besucherstatistik läuft selbst gehostet, ohne Cookies und ohne Weitergabe an Dritte. | Muss |

### 2.7 Bürgerinfos

| ID | Inhalt | Prio |
| --- | --- | --- |
| C-01 | Notruf richtig absetzen (W-Fragen), Verhalten bis zum Eintreffen der Feuerwehr, Rettungsgasse. | Muss |
| C-02 | Gewarnt sein: Warn-Apps wie NINA, Bedeutung der Sirenensignale, Link zu den Isar-Pegeln. | Muss |
| C-03 | Rauchmelderpflicht und Brandschutz im Haushalt. | Muss |
| C-04 | Der Bürgertipp wechselt automatisch mit der Jahreszeit, aus einem pflegbaren Tipp-Kalender. Beispiele: Advent, Asche, Rauchmelder, Grillen, Unwetter, Trockenheit und Waldbrand, Herbststürme, Heizsaison. Dazu kommt ein Sonderhinweis für aktuelle Lagen: an/aus, Text und optionales Enddatum, rot hervorgehoben. Die Tipp-Texte gibt der Kommandant frei. | Muss |
| C-05 | Brandschutzerziehung für Kitas und Schulen, Anfrage über das Formular. | Soll |
| C-06 | Amtliche Warnungen für Ergolding, vom Server abgerufen, ohne Einbettung. | Kann |
| C-07 | Probealarm Bayern (2. Donnerstag im März) und Bundesweiter Warntag (2. Donnerstag im September), jeweils 11 Uhr, werden automatisch berechnet. Ab 14 Tage vorher steht ein Hinweis auf der Startseite. Die Bürgerinfos zeigen immer die nächsten Termine und die Bedeutung der Signale. Der Hinweis ist abschaltbar. | Muss |

Bürgerinfos werden jährlich geprüft. Die Erinnerung kommt über den Monatsbericht.

### 2.8 Fördermitglieder

Laut Satzung nimmt die Website **keine Spenden** an: kein Konto, keine IBAN, keine Zahlungsfunktion.

| ID | Anforderung | Prio |
| --- | --- | --- |
| S-01 | Seite „Fördermitglied werden“: warum, was der Beitrag bewirkt, Höhe des Jahresbeitrags. Verlinkt von Startseite, Mitmachen und Jubiläum. | Muss |
| S-02 | Downloads: „Beitrittserklärung Fördermitglied“ und „Spendenformular“ als PDF, mit Hinweis, wo sie abgegeben werden. Austauschbar im Backend, mit Datum des Stands. | Muss |
| S-03 | Dank an alle, die uns unterstützen, Sponsoren mit Logo, nur mit deren Zustimmung. | Soll |

### 2.9 Redaktionsplan

Ziel: mindestens ein Beitrag pro Woche.

| ID | Anforderung | Prio |
| --- | --- | --- |
| R-01 | Plan im Mitgliederbereich mit Thema, Datum, zuständiger Person und Status. | Muss |
| R-02 | Feste Formate und Jahresanlässe (Hauptversammlung, Dorffest, Steckerlfisch, Rauchmeldertag, Advent) mit Textvorlagen. | Soll |
| R-03 | Beiträge zeitgesteuert veröffentlichen, auch auf Instagram. | Muss |
| R-04 | Erinnerung an die zuständige Person 3 Tage vor dem Termin. Kommt 14 Tage lang nichts, geht ein Hinweis an den Kommandanten. | Muss |

### 2.10 Jubiläum „125 Jahre“ (2027)

Über das Jahr verteilt gibt es Feste wie Steckerlfisch-Grillen, Kuppelcup, Tag der offenen Tür und Dorffest. Der Auftritt zeigt das Jubiläum zeitgesteuert und räumt danach selbst auf.

| ID | Anforderung | Prio |
| --- | --- | --- |
| J-01 | Im System-Bereich: Jubiläum an/aus und Enddatum (Standard: Ankündigung ab Oktober 2026, Ende 31.12.2027). | Muss |
| J-02 | Auf der Startseite ein Bereich mit Siegel „125 Jahre“ und Countdown zum nächsten Fest, dazu ein Hinweis in der Bühne. | Muss |
| J-03 | Eigene Seite mit dem Festjahr als Zeitleiste: Rückblick bei vergangenen Festen, „Vormerken“ bei kommenden. | Muss |
| J-04 | Die Termine kommen aus DIVERA (Kategorie „Jubiläum“). | Muss |
| J-05 | Nach jedem Fest wird ein Rückblick-Entwurf angelegt. | Soll |
| J-06 | Nach dem Festjahr verschwinden Bereich, Menüpunkt und Hinweis automatisch. Die Jubiläumsseite leitet dann zur Chronik weiter, keine toten Links. | Muss |
| J-07 | Aufruf zum Mithelfen und zur Fördermitgliedschaft, dazu ein Foto-Hinweis für die Feste (L-05). | Soll |

Die Jubiläumsseite muss vor dem ersten Fest online sein. Ist die Website bis dahin nicht fertig, kündigt die Übergangsseite die Termine an.

### 2.11 Wartbarkeit ohne IT-Kenntnisse

Im Zweifel gewinnt die einfachere, verbreitetere Lösung.

| ID | Anforderung | Prio |
| --- | --- | --- |
| A-01 | Alles Veränderliche wird im Backend gepflegt, ohne Programmieren: Seitentexte, Fotos, Menü, Kontaktdaten, Impressum, E-Mail-Adresse für Anfragen, Tipp-Kalender, Sonderhinweis, Warntag-Hinweis, PDFs, Jubiläum, Partner-Links, Instagram-Verbindung, Handbuch-PDF. | Muss |
| A-02 | Geschütztes Design: Die Redaktion arbeitet mit Bausteinen. Layout, Farben und Schriften sind gesperrt. | Muss |
| A-03 | Zustands-Ampel im System-Bereich für Erreichbarkeit, Updates, Backup, DIVERA, Instagram und Zertifikat, mit Klartext und, wo möglich, einem Knopf zur Lösung. | Muss |
| A-04 | Automatische Updates und Backups, das Zertifikat erneuert sich selbst. Richtwert: 30–60 Minuten Admin-Arbeit pro Monat. | Muss |
| A-05 | WordPress-Standard und wenige bekannte, kostenlose Plugins statt Eigenbau. | Muss |
| A-06 | Das Handbuch (PDF, bebildert, Du-Form) ist Teil der Lieferung. Es enthält Rollen, Anmelden, Beiträge und Fotos, Bearbeiten, Ausblenden und Löschen, Redaktionsplan, Freigeben, Mitglieder- und Fotoverwaltung, System und Einstellungen, regelmäßige Aufgaben, die Checkliste „Admin-Wechsel“, Notfallkontakte und häufige Fragen. Die Bildschirmfotos zeigen die echte Website, nach Phase 2 aus der Staging-Seite neu erstellt. Jede neue Funktion bekommt einen Abschnitt im Handbuch. | Muss |
| A-07 | Konten und Verträge laufen auf den Verein (Domain, Hosting, DIVERA, Meta, GitHub). Die Zugangsdaten liegen im Passwort-Tresor des Vereins, mit Notfallzugang für den Vorstand. | Muss |
| A-08 | Immer mindestens zwei Admins. Jährlich eine Übergabe-Übung mit Test der Wiederherstellung. | Muss |
| A-09 | Laientest als Abnahme: Ein Mitglied ohne IT-Kenntnisse erledigt zehn typische Aufgaben nur mit dem Handbuch. | Muss |

## 3. Nicht-funktionale Anforderungen

| ID | Thema | Anforderung |
| --- | --- | --- |
| N-01 | Datenschutz | Keine externen Ressourcen: Schriften selbst gehostet, kein Google Analytics, keine Einbettungen von Social Media oder Karten. Damit ist kein Cookie-Banner nötig. |
| N-02 | Barrierefreiheit | WCAG 2.2 AA als Ziel: Kontraste, Alt-Texte, Tastaturbedienung mit Sprunglink „Zum Inhalt“, Tippziele mindestens 44 px. |
| N-03 | Mobile first | Voll bedienbar ab 360 px Breite, ohne seitliches Scrollen, auch bei langen Wörtern und Adressen. |
| N-04 | Performance | Lighthouse ≥ 90 mobil, Bilder als WebP/AVIF in mehreren Größen, Seiten-Cache. |
| N-05 | Sicherheit | 2FA, Login-Drosselung, Zugangsschlüssel in wp-config.php, HTTPS, Security-Header. Eingaben werden immer als Text ausgegeben, nie als HTML oder Skript. |
| N-06 | Betrieb | Tägliches Backup auf externen Speicher, Wiederherstellung regelmäßig getestet. |
| N-07 | Kosten | Keine laufenden Kosten über das Hosting hinaus, ggf. wenige Euro für Backup-Speicher. Ausnahme: Variante B (4.3). |
| N-08 | Design | Rot #CD1719, Logo aus dem Briefpapier, Roboto bzw. Roboto Condensed. Die Demo ist freigegebene Grundlage (Projektdokument „Corporate Design“). |
| N-09 | Ansprache | Durchgehend Du-Form, auch im Mitgliederbereich, in Mails, Rechtstexten und im Handbuch. |
| N-10 | Bildrechte | Standardnachweis „Fotos: Feuerwehr Piflas“. Fremde Fotos nur mit schriftlicher Erlaubnis. |
| N-11 | Tests | Die Prüfungen der Demo-Testsuite sind die Abnahmeliste: Rollen, Anonymisierung, Freigabe-Sperre, keine externen Anfragen, Darstellung ab 360 px, Robustheit gegen fehlerhafte Eingaben. Die Zuordnung der Prüfungen zu den IDs steht in demo/README.md. |
| N-12 | SEO | Saubere Adressen, Sitemap, strukturierte Daten für Organisation und Termine. |
| N-13 | Frauen und Männer | Frauen werden genauso angesprochen wie Männer – selbstverständlich, nicht aufdringlich. Wo die Wahl besteht: (1) neutrale Formen zuerst (Mitglieder, Team, Redaktion, Ansprechperson, alle, die helfen). (2) Sonst beide Formen ausgeschrieben (Bürgerinnen und Bürger), in knappen Beschriftungen mit Schrägstrich (Webmaster/in). (3) Keine Sternchen oder Doppelpunkte – besser lesbar und für Vorleseprogramme. Ausnahmen: „Kommandant“ statt „Kommando“, weil ein Kommandant die Feuerwehr leitet, und „Admin“ statt „Administration“. Feuerwehrfunktionen heißen wie in den Feuerwehr-Dienstvorschriften (FwDV) und den bayerischen Vorschriften, z. B. Gruppenführer, Maschinist, Atemschutzgeräteträger, Jugendwart. Rollen auf der Website: Admin, Kommandant · Freigabe, Redaktion, Bereichsredaktion. Fotos und Bildbeschreibungen zeigen, wo möglich, Frauen und Männer. Auf „Mitmachen“ steht ausdrücklich, dass Frauen und Männer gleichermaßen willkommen sind. Gilt auch für Mails, Handbuch und Textvorlagen; die Demo-Testsuite prüft auf rein männliche Formen außerhalb dieser Ausnahmen. |

### 3.1 Rechtlicher Rahmen

Die Freiwillige Feuerwehr ist eine Einrichtung des Marktes Ergolding (Art. 4 BayFwG). Der Verein unterstützt sie (Art. 5 BayFwG) und betreibt die Website. Einsatzinformationen brauchen deshalb die Zustimmung von Kommandant und Markt. Dies ist keine Rechtsberatung. Vor dem Go-live prüft eine Fachperson für Datenschutz oder Recht, z. B. über den LFV Bayern.

| ID | Grundlage | Anforderung | Umsetzung |
| --- | --- | --- | --- |
| L-01 | Art. 4, 5 BayFwG | Verein betreibt, Kommandant gibt frei, schriftlich mit dem Markt abgestimmt | Impressum, Freigabe; Vereinbarung offen |
| L-02 | Verschwiegenheit (Art. 20 GO, Merkblatt StMI) | Keine vertraulichen Einsatzdetails | D-02, W-04 |
| L-03 | DSGVO / BayDSG | Keine erkennbaren Personen, Kennzeichen oder Objekte; Ort nur als Ortsteil | Anonymisierung; Test „keine Adressen“ |
| L-04 | Pietät | Bei Verletzten oder Toten erst nach Information von Polizei und Angehörigen | W-05 |
| L-05 | DSGVO Art. 6, 13, 21; KUG | Fotos von Festen und Übungen: vorher informieren, Widerspruch beachten, Kinder nur mit Einwilligung der Eltern | Foto-Hinweis, Pflicht-Häkchen, Fotoverwaltung |
| L-06 | Urheberrecht | Nur Fotos mit geklärten Rechten | Bildnachweis, N-10 |
| L-07 | § 5 DDG, § 18 MStV | Vollständiges Impressum | Name des Kommandanten offen |
| L-08 | DSGVO Art. 13, 26, 28 | Datenschutzerklärung (Hosting, Formulare, Konten, Einsätze, Fotos, Instagram-Insights); Verträge zur Auftragsverarbeitung mit Hoster und DIVERA | Text in der Demo; Verträge offen |
| L-09 | TDDDG § 25 | Keine Cookies beim Besuch, keine Drittanbieter | N-01; Test „keine externen Anfragen“ |
| L-10 | Satzung, AO | Keine Spenden online | 2.8; Test „keine IBAN“ |
| L-11 | Jugendschutz | Hinweis für unter 16-Jährige, Jugendfotos nur mit Einwilligung der Eltern | F-06, F-07 |
| L-12 | BFSG / BayBITV | Vermutlich nicht verpflichtend; Ziel trotzdem WCAG 2.2 AA | N-02 |
| L-13 | Haftung für Links | Externe Links erkennbar, Hinweis im Impressum | F-09 |

**Quellen:** [Bayerisches Feuerwehrgesetz](https://www.gesetze-bayern.de/Content/Document/BayFwG/true) · [StMI: Merkblatt Verschwiegenheitspflicht](https://www.stmi.bayern.de/media/a-z/feuerwehr/bestimmungen-im-feuerwehrwesen/Merkblatt_%C3%BCber_die_Verschwiegenheitspflicht_.pdf) · [BayLDA: FAQ Bilder und Verein](https://www.lda.bayern.de/media/FAQ_Bilder_und_Verein.pdf) · [LfDI Rheinland-Pfalz: Einsatzberichte im Internet](https://www.datenschutz.rlp.de/themen/fallboerse/buergerdienste-soziales-gesundheit-ordnungsverwaltung) · [DSK: FAQ Fanpages](https://www.Datenschutzkonferenz-online.de/media/oh/20221121_oh_Fanpages_FAQ_Stand2022_11_21.pdf) · [Plugin Einsatzverwaltung](https://wordpress.org/plugins/einsatzverwaltung/)

## 4. Infrastruktur

### 4.1 Überblick

WordPress auf dem Vereins-Hosting ist das Herzstück. Dort pflegen die Mitglieder die Inhalte. Ein eigenes Plugin holt Einsätze und Termine aus DIVERA und postet auf Instagram. GitHub dient nur der Entwicklung: Dort liegt der Code, nicht die Inhalte.

*[Architekturdiagramm: DIVERA, WordPress, Instagram, Mitglieder, GitHub, Website-Besuch – siehe Online-Dokument bzw. PDF]*

**So entsteht ein Einsatzbericht:**

1. DIVERA meldet einen Alarm, und das Plugin legt einen anonymisierten Entwurf an.
2. Der Kommandant bekommt eine Nachricht.
3. Wer freigeben darf, ergänzt bei Bedarf Text und Foto, setzt das Pflicht-Häkchen und veröffentlicht.
4. Frühestens 2 Stunden nach dem Alarm erscheint der Bericht, auf Wunsch auch auf Instagram.

**Bausteine**

| Baustein | Wahl | Zweck |
| --- | --- | --- |
| CMS | WordPress | Konten, Beiträge, Seiten, Mediathek |
| Theme | Eigenes Block-Theme „ff-piflas“ | Design nach der Demo, geschützte Bausteine |
| Einsatzberichte | Plugin Einsatzverwaltung | Einsatzliste und Statistik |
| Eigenes Plugin | „ff-piflas-connect“ | Rollen, Einladungen, DIVERA, Freigabe, Instagram, Foto-Bereinigung und -Übersicht, System-Bereich, Handbuch-Link |
| Weitere Plugins | z. B. Two Factor, UpdraftPlus, Simple History, Enable Media Replace | 2FA, Backup, Protokoll, Foto ersetzen; Auswahl in Phase 0 |

**Hosting muss bieten:** PHP ≥ 8.2, MySQL ≥ 8 oder MariaDB ≥ 10.6, einen echten Cronjob, SFTP, SMTP, mindestens 5 GB Speicher und eine Subdomain für die Testseite (Staging).

**Zugangsdaten** für DIVERA, Instagram und SMTP stehen nur in `wp-config.php`, nie im Repository oder in der Datenbank.

**Entwicklung:** Möglich lokal oder auf einer eigenen VM, die als Werkbank und Testserver dient. Der Code liegt trotzdem auf GitHub. Auf der VM laufen keine echten Mitgliederdaten, die Testseite ist passwortgeschützt und nicht für Suchmaschinen sichtbar. Die echte Website läuft nie auf der VM.

### 4.2 Referenz-Demo, Handbuch und Dokumente

Bei Widersprüchen gilt das Lastenheft. Demo und Handbuch werden dann angepasst.

| Dokument | Wofür | Wo |
| --- | --- | --- |
| Lastenheft (dieses Dokument) | Was gebaut wird | Online-Dokument, Claude-Projekt, PDF |
| Demo v5 | Verbindliche Vorlage für Aufbau, Texte und Abläufe. Statisch, ohne Datenbank; Demo-Steuerung und Schnell-Login gibt es nur dort; die Bereichsredaktion ist in der Demo nur bei der Einladung wählbar. | Artefakt-Link, Backup |
| Testsuite (430 Prüfungen) | Abnahmeliste für die echte Website | Backup (`demo/test_app.py`) |
| Handbuch Mitgliederbereich 1.4 | Anleitung für alle Rollen (A-06), in der Demo nach dem Login verlinkt | PDF, Backup |
| Corporate Design | Logo, Farben, Schrift | Claude-Projekt |
| Backup-Paket mit WEITERMACHEN.md | Alles, um später weiterzuarbeiten | ZIP |

### 4.3 Betrieb & Betreuung

Eine Website mit Mitgliederkonten braucht laufende Betreuung. Die heute verantwortliche Person hat dafür keine Zeit. Deshalb wird vor Phase 1 eine Variante gewählt:

| Variante | Technik betreut | Aufwand Verein | Funktionen | Kosten |
| --- | --- | --- | --- | --- |
| A – selbst betreut | Zwei Admins | 30–60 Min./Monat, gelegentlich mehr | Alles | Nur Hosting |
| B – mit Dienstleister | Hoster oder Dienstleister | Nur Inhalte und Freigaben | Alles | Monatsgebühr (Angebote einholen) |
| C – Website-Kit LFV Bayern | Landesfeuerwehrverband | Nur Inhalte | Voraussichtlich ohne DIVERA, Freigabe, eigenes Design und Instagram-Post (zu prüfen) | Zu prüfen |

Empfehlung: A, oder B, wenn sich keine zwei Admins finden.

## 5. Offene Punkte

**Entscheidungen**

- [ ] Betriebsvariante (4.3) und zwei Admins
- [ ] Freigabegruppe und Erstbesetzung der Rollen
- [ ] Abstimmung mit dem Markt Ergolding (L-01), dabei auch klären, ob die Sirenen bei Probealarm und Warntag mitmachen (C-07)
- [ ] Ist ein Online-Antrag für Fördermitglieder laut Satzung zulässig?
- [ ] An welche E-Mail-Adresse gehen Mitmach-Anfragen (F-06)?

**Zugänge (Phase 0)**

- [ ] Hosting prüfen (4.1)
- [ ] DIVERA: API-Zugang in der gebuchten Stufe? Wie sind private und Jubiläumstermine markiert?
- [ ] Instagram auf professionelles Konto umstellen, Meta-Entwicklerkonto auf den Verein anlegen
- [ ] Joomla sichern, Umfang des Archivs festlegen (F-13)

**Inhalte**

- [ ] Kommandant (Impressum), Vorstandschaft, Jugendwart und Gruppenstunde
- [ ] Gründungsjahr und Meilensteine der Chronik; Jubiläumstermine 2027 und Jubiläumslogo
- [ ] Fahrzeugtypen und Funkrufnamen; Namen der Fotografinnen und Fotografen; Herkunft des Fotos vom 11/1
- [ ] Fotos und Texte vom Vereinsleben (Dorffest, Steckerlfisch, Atemschutz)
- [ ] Förderbeitrag und beide PDFs
- [ ] Kurztexte zu den Partnerfeuerwehren
- [ ] Tipp-Kalender durch den Kommandanten freigeben
- [ ] Notfallkontakte (Handbuch 10.3)

**Recht**

- [ ] Verträge zur Auftragsverarbeitung mit Hoster und DIVERA
- [ ] Verzeichnis der Verarbeitungstätigkeiten
- [ ] Foto-Einwilligung in die Aufnahmeformulare
- [ ] Prüfung durch eine Fachperson für Datenschutz oder Recht vor dem Go-live

## 6. Umsetzungsplan

**Stand 23.11.2026:**

| Ergebnis | Stand |
| --- | --- |
| Übergangsseite | Fertig zum Hochladen |
| Demo v5 + Testsuite | Fertig |
| Handbuch | Version 1.4 fertig |
| Lastenheft | Version 1.6 |
| Backup-Paket | Wird mit jeder Version aktualisiert |

**Sofort:** Übergangsseite hochladen. Vorher Joomla komplett sichern und die Speicherdauer der Logfiles in datenschutz.html eintragen.

Jede Phase endet mit einer Abnahme durch den Verein. Claude Code arbeitet in einem eigenen Branch je Phase und öffnet einen Pull Request mit der Liste der erfüllten IDs.

1. **Phase 0 – Klärung und Zugänge** (Verein): offene Punkte aus Abschnitt 5, Hosting, GitHub-Organisation des Vereins, Staging-Subdomain.
2. **Phase 1 – Grundgerüst:**
   - WordPress mit 2FA, Backup, Protokoll und SMTP
   - Rollen und Einladungen (B-01 bis B-08)
   - Tests und automatisches Hochladen auf die Testseite (Staging)
   - Abnahme: Jede Rolle kann genau das, was in der Tabelle steht; eine Wiederherstellung ist getestet.
3. **Phase 2 – Theme und Mitgliederbereich:**
   - Alle Seiten aus 2.1
   - Beiträge mit Fotos, Bearbeiten, Ausblenden und Löschen (B-09 bis B-11, B-14 bis B-16)
   - Fotoverwaltung (B-12)
   - Handbuch-Link (B-13)
   - System-Bereich (A-01, A-03)
   - Bürgerinfos (C-04, C-07)
   - Abnahme: Design freigegeben, Demo-Tests übertragen und grün.
4. **Phase 3 – Inhalte und Schulung:**
   - Die Redaktion pflegt die Seiten selbst ein.
   - Redaktionsplan für 6 Monate
   - Archiv übernehmen
   - Handbuch mit Bildschirmfotos der echten Seite aktualisieren (A-06)
5. **Phase 4 – DIVERA und Freigabe** (D-, W-): Abnahme, wenn ein Testalarm in 15 Minuten einen korrekten, datensparsamen Entwurf erzeugt.
6. **Phase 5 – Instagram** (I-): Abnahme, wenn der Testpost und die Vorschau funktionieren.
7. **Phase 6 – Go-live:**
   - Rechtstexte final
   - Überwachung und Monatsbericht (M-)
   - Barrierefreiheitsprüfung
   - Schulungsabend
   - Umzug auf www.feuerwehr-piflas.de
   - Abnahme: Laientest (A-09), Übergabe-Übung (A-08), zwei Wochen ohne kritische Fehler
8. **Phase 7 – Ausbau (optional):** Facebook, Suche, amtliche Warnungen.

## 7. Vorlagen für Claude Code

Ins Repository gehören diese Vorlage als `CLAUDE.md`, das Lastenheft als `docs/lastenheft.md`, die Demo mit Testsuite nach `docs/referenz-demo/` und das Handbuch nach `docs/handbuch/`.

```markdown
# Website Feuerwehr Piflas e.V. (WordPress)

## Projekt
Nur eigener Code:
- wp-content/themes/ff-piflas/           Block-Theme
- wp-content/plugins/ff-piflas-connect/  Rollen, Einladungen, DIVERA, Freigabe,
                                         Fotos, Instagram, System-Bereich
Anforderungen: docs/lastenheft.md (IDs F-, D-, W-, I-, B-, M-, C-, S-, R-, J-,
A-, N-, L-). Vorlage: docs/referenz-demo/ (Abnahme: test_app.py).
Handbuch: docs/handbuch/ (A-06).

## Regeln
- Oberfläche, Commits und Handbuch auf Deutsch in Du-Form, Frauen und Männer
  gleichermaßen ansprechen, neutrale Formen zuerst (N-13); Code englisch.
- WordPress Coding Standards, PHP >= 8.2, kein Page-Builder.
- Inhalte in die Datenbank, nie ins Repo. Alles Veränderliche als
  Einstellung im Backend (A-01).
- Rollen nur in src/Roles.php, DIVERA-Daten nur über src/Divera/Anonymizer.php,
  jeweils mit Tests.
- Veröffentlichen nur mit Pflicht-Bestätigung, serverseitig geprüft (W-04).
- Löschen nur durch Admins, nach Nachfrage, über den Papierkorb (B-16).
- Fotos: verkleinern, EXIF/GPS auch im Original entfernen (B-11).
- Zugangsdaten nur in wp-config.php.
- Ausgaben immer escapen (esc_html, esc_attr, wp_kses_post), Eingaben prüfen (N-05).
- Keine externen Requests im Frontend; externe Links mit rel="noopener".
- Fremd-Plugins nur nach Rücksprache (docs/plugins.md).
- Jede neue Funktion: Handbuch-Abschnitt in einfacher Sprache.
- Je Phase ein Branch und ein PR mit Checkliste der erfüllten IDs.

## Entwicklung
npx @wordpress/env start | composer test | composer lint | npm run build
```

**Start-Prompt für Phase 1**

```text
Lies CLAUDE.md, docs/lastenheft.md und docs/referenz-demo/. Setze Phase 1
um: wp-env, Plugin ff-piflas-connect mit den Rollen aus 2.5, Einladungen
per E-Mail (48 Std., erneut senden, zurückziehen), keine
Selbstregistrierung (B-01 bis B-08), PHPUnit-Tests je Rolle, PHPCS und
eine GitHub Action, die auf Staging deployt. Stelle vorher deinen Plan,
offene Fragen und die geplanten Fremd-Plugins vor. Am Ende: PR mit
Checkliste der IDs.
```

## 8. Änderungsverlauf

| Version | Datum | Änderungen |
| --- | --- | --- |
| 0.1–0.2 | 22.11.2026 | Erste Fassungen; Umstieg auf WordPress; Monitoring, Bürgerinfos, Fördermitglieder, Redaktionsplan, Jubiläum, Recht, Wartbarkeit |
| 1.0 | 22.11.2026 | An Demo v5 angeglichen: Partnerseite, Menügruppen, Du-Form, Fotos, Fotoverwaltung, Betriebsvarianten |
| 1.1 | 23.11.2026 | Bürgertipp nach Jahreszeit und Sonderhinweis (C-04), Warntag und Probealarm (C-07), Instagram als professionelles Konto |
| 1.2 | 23.11.2026 | Handbuch aufgenommen (B-13, A-06, 4.2, Phasen 2 und 3). Auf Vollständigkeit geprüft und gestrafft. Neu: Ziel der Mitmach-Anfragen und Spamschutz (F-06), Entwicklung auf VM (4.1), Dokumentenübersicht (4.2), offene Punkte nach Themen. IDs neu geordnet: F-10 bis F-14, M-01 bis M-04, S-01 bis S-03, R-01 bis R-04, A-01 bis A-09, N-01 bis N-12. |
| 1.3 | 23.11.2026 | Neu N-13: Frauen und Männer gleichermaßen ansprechen. Rollen umbenannt (Administration, Kommando · Freigabe, Redaktion, Bereichsredaktion), Menügruppe „Für Bürger“ heißt jetzt „Ratgeber“, „Zurück an Autor“ heißt „Zurück zur Überarbeitung“. Text des Lastenhefts, Demo und Handbuch 1.1 entsprechend angepasst; Testsuite 401 Prüfungen. |
| 1.4 | 23.11.2026 | Neu B-14 bis B-16: Beiträge und Einsätze gemäß Rolle bearbeiten und ausblenden, Löschen nur durch die Administration nach Nachfrage, mit Papierkorb (30 Tage). Rollentabelle, W-01, A-06, Phase 2 und CLAUDE.md-Vorlage ergänzt. Demo, Handbuch 1.2 und Testsuite (424 Prüfungen) angepasst. |
| 1.5 | 23.11.2026 | Ausnahmen von N-13: „Kommandant“ statt „Kommando“, „Admin“ statt „Administration“; Feuerwehrfunktionen nach FwDV (z. B. Gruppenführer, Jugendwart). Rollen umbenannt in Admin und Kommandant · Freigabe, Freigabegruppe: Kommandant und stellvertretender Kommandant. Texte in Lastenheft, Demo und Handbuch 1.3 angepasst; Demo-Personen getauscht (Kommandant: Max Mustermann, Admin: Erika Musterfrau). |
| 1.6 | 23.11.2026 | Gesamtprüfung von Testsuite, Demo, Lastenheft und Handbuch. Präzisiert: W-01 (Freigabegruppe = Rolle Kommandant · Freigabe), Rollentabelle, N-02 (Sprunglink), N-03 (lange Wörter), N-05 (Eingaben nie als HTML), N-11 (Robustheit, ID-Zuordnung in demo/README.md), 4.2, CLAUDE.md-Vorlage. Demo: Sprungleiste unter „Beiträge“, Sprunglink repariert, Umbruch langer Wörter. Testsuite 430 Prüfungen mit Exit-Code, Handbuch 1.4. |
