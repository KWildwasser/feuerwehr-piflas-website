# Lastenheft & Umsetzungsplan – Webpräsenz Feuerwehr Piflas

23.11.2026 · Korbinian · Version 1.14 (WordPress) · Referenz: Demo v13 und Handbuch 1.12

## 0. Auf einen Blick

- **Was:** Neue Website für www.feuerwehr-piflas.de. Ausgewählte Mitglieder pflegen sie mit eigenen Konten.
- **Automatisch:** Einsätze und nicht-private Termine kommen aus DIVERA 24/7. Freigegebene Beiträge gehen auf Wunsch auf Instagram.
- **Lernen:** Jeden Monat ein Thema mit kurzem Test für alle Aktiven – so einfach und einladend gestaltet, dass man es gern macht (2.13). Die Kommandanten planen die Themen und sehen den Lernstand (2.12).
- **Technik:** WordPress auf dem bestehenden Hosting, ein eigenes Theme und ein eigenes Plugin. Beides baut Claude Code nach diesem Lastenheft.
- **Leitprinzip:** Ehrenamtliche ohne IT-Kenntnisse können die Seite auch in Jahren noch betreuen (2.11).
- **Vorhanden:**
  - Übergangsseite
  - Klickbare Demo v13 mit Testsuite (693 Prüfungen), öffentlich auf GitHub Pages
  - Anleitung „Schnittstellen reparieren“ für die Technik (A-12)
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
7. Alle Aktiven bilden sich selbständig und regelmäßig fort. Die Kommandanten behalten langfristig den Überblick über den Wissensstand (2.12).

**Grundsätze:** Durchgehend Du-Form, Frauen und Männer gleichermaßen angesprochen (N-13), einfache Sprache, alles am Handy bedienbar, nichts, was Einsatzbetroffene erkennbar macht.

## 2. Funktionale Anforderungen

Priorität: **Muss** = zum Go-live, **Soll** = kurz danach, **Kann** = später. Claude Code nennt die IDs in Branches, Tests und Pull Requests.

### 2.1 Seiten & Navigation

| ID | Bereich | Inhalt | Prio |
| --- | --- | --- | --- |
| F-01 | Startseite | Von oben nach unten: (1) Bühne mit Foto und den Buttons „Mitmachen“ und „Fördermitglied werden“. (2) Notruf 112, darunter 14 Tage vor Warntag oder Probealarm ein Hinweis (C-07). (3) Jubiläumsbereich, nur im Festjahr (J-02). (4) Nächste 3 Termine und letzte 3 Einsätze. (5) „Aus dem Vereinsleben“: 3 Foto-Kacheln mit Link zum Beitrag. (6) Mitmach-Bereich (F-06). (7) Bürgertipp oder Sonderhinweis (C-04). (8) Instagram-Vorschau (I-01). Keine Fahrzeugdaten. | Muss |
| F-02 | Aktuelles | Beiträge als Liste mit Foto, filterbar nach Kategorie; zuerst die neuesten 6, weitere mit „Weitere Berichte laden“. Beitragsseite mit Titelbild, Text und Galerie. | Muss |
| F-03 | Einsätze | Liste der neuesten drei Jahre als Knöpfe, ältere Jahre über eine Auswahl; filterbar nach Einsatzart; je 20 Einsätze, weitere mit „Weitere Einsätze anzeigen“. Detail mit Einsatzart, Ort (Ortsteil bzw. bei überörtlichen Einsätzen die Gemeinde), gerundeter Uhrzeit, Fahrzeugen, Kurzbericht und Fotos. Jahresstatistik (D-07). | Muss |
| F-04 | Termine | Nicht-private DIVERA-Termine (D-05) mit Kategorien. Jubiläumstermine gekennzeichnet. „Vormerken“ als Kalenderdatei (.ics). | Muss |
| F-05 | Fahrzeuge & Technik | Neuestes Fahrzeug hervorgehoben. Je Fahrzeug eine Karte mit Foto, Funkrufname, Typ und Kurzbeschreibung. Dazu Geräte mit Fotos. Alle Angaben und Fotos im Backend pflegbar (B-21). | Muss |
| F-06 | Mitmachen | Formular ganz oben (Name, Telefon oder E-Mail, Interesse, Datenschutz-Häkchen) mit Hinweis für unter 16-Jährige. Kurzform des Formulars auf der Startseite. Dazu der nächste Übungsabend und Wege zu Jugendfeuerwehr und Fördermitgliedschaft. Anfragen gehen per E-Mail an eine im System-Bereich hinterlegte Adresse. Die Website speichert sie nicht dauerhaft. Spamschutz ohne Drittanbieter (kein reCAPTCHA). | Muss |
| F-07 | Jugendfeuerwehr | Vorstellung, Gruppenstunde, Ansprechperson, Button „Schnuppern kommen“. Fotos nur mit Einwilligung der Eltern. | Muss |
| F-08 | Verein & Chronik | Vorstandschaft, Mitgliedschaft und Chronik ab Gründung. Das Festjahr 2027 bleibt nach dem Jubiläum in der Chronik (J-06). Verweis auf die Partnerfeuerwehren. Einleitung, Vorstandschaft und Chronik im Backend pflegbar (B-21). | Muss |
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
| D-02 | Übernommen werden nur Datum, Uhrzeit (auf die Viertelstunde gerundet), Einsatzart, Ortsteil (bei überörtlichen Einsätzen die Gemeinde) und eigene Fahrzeuge. Nie Straßen, Hausnummern, Namen, Meldertexte, Kennzeichen oder Patientendaten. Statt medizinischer Details steht „Unterstützung Rettungsdienst“. | Muss |
| D-03 | Zuordnung DIVERA-Stichwort → öffentliche Einsatzart mit Symbol, im Backend pflegbar. | Muss |
| D-04 | Veröffentlichung frühestens 2 Stunden nach dem Alarm (einstellbar), auch nach der Freigabe. | Muss |
| D-05 | Alle nicht-privaten Termine werden alle 15 Minuten übernommen, ebenso Änderungen und Absagen. Nur Titel, Datum, Uhrzeit, Ort und Kategorie, keine Angaben zu Teilnehmenden, keine Notizen. | Muss |
| D-06 | Der Zugangsschlüssel liegt nur auf dem Server. | Muss |
| D-07 | Die Jahresstatistik wird automatisch aus den veröffentlichten Einsätzen berechnet. | Soll |
| D-08 | Fällt DIVERA aus, läuft die Website normal weiter. Der Fehler erscheint mit Fehlercode in der Ampel (A-03, A-11) und kommt per Mail. Im Freigabe-Bereich erscheint ein Hinweis mit dem Knopf „Einsatz von Hand anlegen“ (D-09). | Muss |
| D-09 | Einsatz von Hand: Kommandant und Admins legen Einsätze ohne DIVERA an (z. B. bei einer Störung) – mit denselben datensparsamen Feldern (D-02): Stichwort, Einsatzart, Einsatzort (Ortsteil oder bei überörtlichen Einsätzen die Gemeinde; Vorschlagsliste im Backend pflegbar; Eingaben mit Ziffern oder Straßenbezeichnungen werden abgewiesen), Datum, Alarmzeit (automatisch auf 15 Minuten gerundet), Fahrzeuge aus der Fahrzeugliste (B-21), Kurzbericht, Fotos, Instagram-Häkchen und Pflicht-Bestätigung (W-04). Alarmzeiten in der Zukunft werden abgewiesen. Die 2-Stunden-Regel (D-04) gilt auch hier: Liegt der Alarm kürzer zurück, wird der Bericht automatisch später veröffentlicht (Status „Geplant“). Kommt der Einsatz später doch aus DIVERA, entsteht kein Doppel. | Muss |

### 2.3 Freigabe

| ID | Anforderung | Prio |
| --- | --- | --- |
| W-01 | Für jeden Einsatz-Entwurf und jeden eingereichten Beitrag oder jede eingereichte Änderung bekommt die Freigabegruppe eine Nachricht mit Link. Zur Gruppe gehören alle mit der Rolle Kommandant · Freigabe (Kommandant, stellvertretender Kommandant, ggf. Vorstand) und auf Wunsch die Admins. | Muss |
| W-02 | Freigabe am Handy im Bereich „Freigabe“, mit Zähler der offenen Einträge. | Muss |
| W-03 | Vor der Freigabe lassen sich Kurztext und Fotos ergänzen (Regeln wie B-11). | Muss |
| W-04 | Ohne Pflicht-Häkchen keine Veröffentlichung, serverseitig geprüft. Bei Einsätzen lautet es „keine erkennbaren Personen, Kennzeichen, Adressen oder vertraulichen Details“. Bei Beiträgen lautet es „Bildrechte geklärt, Abgebildete informiert bzw. einverstanden (bei Kindern die Eltern)“. | Muss |
| W-05 | Warnhinweis bei technischer Hilfe: Gibt es Verletzte oder Tote, wird erst veröffentlicht, wenn Polizei und Angehörige informiert sind. | Muss |
| W-06 | Häkchen „Auch auf Instagram“, getrennt von der Veröffentlichung auf der Website. | Muss |
| W-07 | Einsätze lassen sich verwerfen, Beiträge und Änderungen „Zurück zur Überarbeitung“ schicken, jeweils mit optionalem Hinweis. Verworfenes und Zurückgegebenes bleibt 30 Tage in der Liste „Verworfen und zurückgegeben“ und lässt sich wiederherstellen. Die einreichende Person sieht Zurückgegebenes mit Hinweis unter „Inhalte“ und kann es überarbeiten und neu einreichen. | Muss |
| W-08 | Änderungen der Redaktion an Beiträgen, Seiten, Fahrzeugen, Ausrüstung und Chronik sowie neue Fahrzeuge und Geräte (B-21) erscheinen in der Freigabe als Vergleich mit der aktuellen Fassung: nur geänderte Felder, Wort für Wort hervorgehoben (Entferntes rot durchgestrichen, Neues grün unterstrichen), unveränderte Absätze zusammengefasst, Fotos vorher → nachher. Jede Karte zeigt oben die Art (Neuer Einsatzbericht, Neuer Beitrag, Änderung · …, Neu · …) und wer eingereicht hat; oben auf der Seite steht ein Überblick, wie viel von welcher Art wartet. Freigabe mit „Übernehmen“ bzw. „Veröffentlichen“. | Muss |
| W-09 | E-Mail an die Kommandanten: Bei jeder neuen Einreichung (Einsatz-Entwurf, Beitrag, Änderung, neues Fahrzeug oder Gerät) bekommen alle mit der Rolle Kommandant · Freigabe eine kurze E-Mail mit Link zur Freigabe. Solange etwas offen ist, kommt täglich zu einer einstellbaren Uhrzeit (Standard 7:00 Uhr, im System-Bereich abschaltbar) eine Erinnerung. Die Mail nennt nur die Art der Einreichung und die einreichende Person – keine Inhalte, keine Fotos und keine Knöpfe zum Freigeben (Verschwiegenheit, L-02). Freigegeben wird nur auf der Website nach Anmeldung mit 2-Faktor-Code. Ist schon alles erledigt, sagt die Seite das. Versand über den SMTP-Zugang des Hostings, ohne Tracking-Pixel. | Muss |

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
| B-01 | Konten nur per Einladung durch einen Admin (Name, E-Mail, Rolle). Der Link gilt einmalig 48 Stunden, das Passwort vergibt das Mitglied selbst. Keine Selbstregistrierung. Jedes Konto hat genau eine Rolle; beim Anmelden wird keine Rolle gewählt (Mehrfachrollen sind später möglich, aber nicht geplant). Fehlermeldungen beim Login verraten nicht, ob es eine E-Mail-Adresse gibt. | Muss |
| B-02 | Admins sehen den Status jedes Kontos, senden Einladungen erneut oder ziehen sie zurück und ändern Rollen: bei jedem Konto „Rolle ändern“, neue Rolle wählen (Mitglied, Redaktion, Bereichsredaktion, Kommandant · Freigabe, Admin) und das Häkchen „Einsatzabteilung“ (E-10) setzen, „Speichern“. Die Änderung gilt sofort, das Konto zeigt „Rolle geändert am … von …“, sie steht im Protokoll (B-07) und lässt sich rückgängig machen (B-17). Die eigene Rolle ändert immer ein anderer Admin. Wer zum letzten zweiten Admin würde, kann nicht herabgestuft werden (A-08). Wird ein Konto zum Admin oder Kommandanten, ist beim nächsten Login die 2-Faktor-Anmeldung Pflicht (B-04). Lernergebnisse und Beiträge bleiben erhalten. | Muss |
| B-03 | Die Rechte sind laut Rollentabelle fest im eigenen Plugin hinterlegt. | Muss |
| B-04 | 2-Faktor-Anmeldung ist Pflicht für Admins und den Kommandanten, für alle anderen empfohlen. | Muss |
| B-05 | „Passwort vergessen“ per Mail. Nach mehreren Fehlversuchen wird das Konto vorübergehend gesperrt. | Muss |
| B-06 | Der Mitgliederbereich ist voll am Handy bedienbar. Die untere Leiste zeigt nur die Bereiche der eigenen Rolle, höchstens sechs; der Redaktionsplan liegt deshalb unter „Inhalte“. Im Kopf stehen Logo, Handbuch und „Abmelden“ in einer Zeile, Name und Rolle darunter in einer eigenen Zeile – ab 360 px ohne Überlappung. | Muss |
| B-07 | Verlauf: Jeder Beitrag, Einsatzbericht, jedes Fahrzeug und Gerät und die Seite „Verein & Chronik“ hat einen Verlauf mit Zeit, Person, Aktion (erstellt, bearbeitet, ausgeblendet, gelöscht, wiederhergestellt, rückgängig gemacht), Freigabe durch, optionaler Notiz und geänderten Feldern. Jede frühere Fassung lässt sich wiederherstellen (Redaktion: als Änderung zur Freigabe). Sicher: Einträge werden nur angehängt, niemand kann sie ändern oder löschen; die Person kommt aus der Anmeldung, nicht aus dem Formular; der Verlauf ist nur im Mitgliederbereich sichtbar. Darstellung: neueste Änderung oben, aktuelle Fassung markiert; je Eintrag Aktion, Zeit, Person, Freigabe und Notiz, darunter „Was wurde geändert?“ mit demselben Vergleich wie in der Freigabe (W-08). Schutz vor Spam: Speichern ohne Änderung erzeugt keinen Eintrag; Änderungen derselben Person am selben Inhalt innerhalb von 10 Minuten werden zusammengefasst; Begrenzung nach N-05; höchstens 50 Fassungen je Inhalt, ältere Zwischenstände werden ausgedünnt (die erste Fassung bleibt). Zusätzlich protokolliert die Website Anmeldungen und Rechteänderungen. | Muss |
| B-08 | Bei Austritt wird das Konto deaktiviert, nicht gelöscht. Die Beiträge bleiben erhalten. | Muss |
| B-09 | Ein Beitrag besteht aus Titel, Kategorie (Verein, Übung, Jugendfeuerwehr, Bürgertipp), Text, Fotos, optionaler Bildbeschreibung, dem Instagram-Häkchen und der Pflicht-Bestätigung (W-04). Kommandant und Admins veröffentlichen direkt, die Redaktion reicht zur Freigabe ein. | Muss |
| B-10 | Nach dem Speichern oder Veröffentlichen bleibt man angemeldet in der bisherigen Ansicht (z. B. „Inhalte“, „Freigabe“). Eine Meldung bestätigt es und bietet „Beitrag ansehen“ bzw. „Bericht ansehen“ – in der Rolle Redaktion „Vorschau ansehen“ mit dem Hinweis „Vorschau – noch nicht öffentlich“, bis freigegeben ist – sowie „Rückgängig“ (B-17). Beide Knöpfe stehen 5 Minuten lang auch oben in „Zuletzt“. | Muss |
| B-11 | Fotos (alle Rollen): mehrere aus Kamera oder Galerie, vor dem Absenden einzeln entfernbar. Das erste ist das Titelbild. Beim Hochladen werden sie auf max. 1600 px verkleinert, Standort- und Kameradaten werden auch im Original entfernt. Nur Bilddateien sind erlaubt. | Muss |
| B-12 | Fotoverwaltung (nur Admins): alle Fotos an einem Ort, jeweils mit Angabe, wo sie verwendet werden. „Ersetzen“ tauscht ein Foto überall aus. „Entfernen“ fragt nach und hinterlässt einen Platzhalter. Instagram-Bilder werden nur auf der Website ausgeblendet. | Muss |
| B-13 | Handbuch: Das PDF „Handbuch Mitgliederbereich“ ist nach dem Login im Kopf jeder Seite verlinkt (Buch-Symbol) und zusätzlich im System-Bereich. Es ist öffentlich nicht verlinkt, im Theme hinterlegt und von den Admins austauschbar. Inhalt und Pflege: A-06. | Muss |
| B-14 | Bearbeiten im Editor (B-19): Beiträge (Titel, Kategorie, Text, Fotos, Titelbild, Bildbeschreibung) und Einsatzberichte (Stichwort, Einsatzart, Einsatzort, Datum, Uhrzeit, Fahrzeuge, Kurzbericht, Fotos), jeweils mit Pflicht-Bestätigung (W-04) und optionaler Notiz für den Verlauf. Die Redaktion bearbeitet nur eigene Beiträge; ihre Änderung geht zur Freigabe, bis dahin bleibt die bisherige Fassung online. Die Bereichsredaktion bearbeitet im eigenen Bereich, Kommandant und Admins alle Beiträge und Einsatzberichte, jeweils sofort online. Änderungen werden nicht erneut auf Instagram gepostet. | Muss |
| B-15 | Ausblenden: Mit denselben Rechten wie bei B-14, aber ohne Freigabe, lässt sich ein Beitrag oder Einsatz sofort von der Website nehmen. Er bleibt gespeichert und lässt sich wieder einblenden. Ausgeblendetes erscheint nirgends öffentlich, auch nicht in der Einsatzstatistik. Ein Instagram-Post bleibt bestehen; darauf weist die Website hin. | Muss |
| B-16 | Löschen: nur Admins, für Beiträge und Einsätze, immer erst nach einer Nachfrage. Gelöschtes kommt in den Papierkorb, lässt sich 30 Tage lang wiederherstellen und wird danach endgültig gelöscht. Gelöschte oder ausgeblendete Einsätze legt der DIVERA-Abgleich nicht erneut an. Ausnahme: Fahrzeuge und Geräte können auch Kommandanten entfernen und wiederherstellen (B-21). | Muss |
| B-17 | Rückgängig: Nach jeder Änderung (speichern, ausblenden, löschen, entfernen, freigeben, verwerfen, zurückgeben, Einstellungen, Fotos, Einladungen, Notbetrieb) zeigt die Meldung einige Sekunden lang den Knopf „Rückgängig“, der den Stand davor wiederherstellt. Zusätzlich bleibt die letzte Aktion 5 Minuten lang oben auf jeder Seite des Mitgliederbereichs und – für Angemeldete – auch auf der öffentlichen Seite sichtbar („Zuletzt: … · Rückgängig“), damit z. B. ein gerade veröffentlichter Beitrag oder Einsatzbericht direkt auf seiner Seite zurückgenommen werden kann. Das gilt für alle Eingaben, auch Veröffentlichen, Einplanen und Einladen. Danach helfen Verlauf (B-07), Papierkorb (B-16) und die Liste „Verworfen und zurückgegeben“ (W-07). Das Rückgängigmachen steht selbst im Verlauf. Ein Instagram-Post bleibt bestehen; darauf weist die Website hin. Ausnahme: Testversuche im Bereich „Lernen“ lassen sich nicht rückgängig machen (E-07). | Muss |
| B-18 | Übersicht „Inhalte“ für Beiträge und Einsatzberichte, ausgelegt auf mehrere hundert Einträge: Suche beim Tippen (Titel, Text, Ort, Fahrzeug, Name), Filter nach Art (Einsätze, Übungen, Berichte), Jahr und Status (online, ausgeblendet, Änderung wartet, geplant), kombinierbar, mit Trefferzahl; die neuesten 20 zuerst, weitere mit „Weitere 20 anzeigen“; „Filter zurücksetzen“. Oben die Knöpfe „Neuer Beitrag“ und (Kommandant, Admin) „Einsatz von Hand“. Die Redaktion sieht nur eigene Beiträge und darüber „Zurück an dich“. Papierkorb für Admins unten. | Muss |
| B-19 | Editor: Ein Eintrag öffnet sich auf einer eigenen Seite mit Formular, „Weitere Aktionen“ (ansehen, ausblenden, löschen) und Verlauf (B-07). Fotos: hinzufügen, einzeln entfernen und per „Titelbild“ nach vorn holen, ohne dass Eingaben verloren gehen; gilt auch für Einsätze in der Freigabe (W-03). Zurück zur Übersicht mit „← Zur Übersicht“ oder der Zurück-Taste. | Muss |
| B-20 | Grenzen gegen Missbrauch: Höchstlängen für alle Felder (z. B. Titel 120, Text 8.000 Zeichen), Fotos laut B-11. | Muss |
| B-21 | Seiten pflegen (Bereich „Seiten“): Verein (Einleitung, Vorstandschaft als Zeilen Amt – Name), Chronik (Jahr, Titel, Text; automatisch nach Jahr sortiert), Fahrzeuge (Name, Kurzname für Einsatzberichte, Beschreibung, Foto, Bildbeschreibung, Hervorhebung „Neu im Fuhrpark“ mit Vorstellungstext) und Ausrüstung (Bezeichnung, Foto, Bildbeschreibung). Alle Rollen bearbeiten und legen neue Fahrzeuge und Geräte an; die Redaktion über die Freigabe (W-08). Entfernen dürfen Kommandant und Admins (Nachfrage, 30 Tage wiederherstellbar). Neue Fahrzeuge stehen sofort im Formular „Einsatz von Hand“ zur Auswahl. Die zentrale Fotoverwaltung (B-12) ist von hier aus verlinkt. | Muss |
| B-22 | Zähler an den Bereichen: Ist etwas zu tun, zeigt das Symbol in der unteren Leiste eine rote Zahl – Freigabe: offene Einreichungen; Inhalte (Redaktion): „Zurück an dich“; Lernen: das Thema des Monats ist noch nicht bestanden, für Kommandanten zusätzlich je fehlendem Thema für diesen oder nächsten Monat; System: Hinweise der Schnittstellen. Ist alles erledigt, verschwindet die Zahl. Vorlesesoftware liest die Zahl mit Klartext vor (z. B. „Freigabe, 4 warten auf Freigabe“). | Muss |
| B-23 | Angemeldet bleiben auf der öffentlichen Seite: Wer angemeldet ist, sieht auch die öffentlichen Seiten mit dem Kopf des Mitgliederbereichs (Logo, Menü der öffentlichen Seiten, Handbuch, „Abmelden“, Name und Rolle) und der unteren Leiste mit den eigenen Bereichen und Zählern (B-22). Im Menü steht statt „Login für Mitglieder“ „Zum Mitgliederbereich“. Niemand fällt beim Ansehen eines Beitrags aus dem Mitgliederbereich heraus. | Muss |

**Rollen** (je Konto genau eine, B-01; geplante Besetzung: 3 Kommandanten, 2 Admins, mehrere Personen in der Redaktion, alle übrigen Aktiven als Mitglied)

| Rolle | Für wen | Bereiche | Darf |
| --- | --- | --- | --- |
| Admin | Webmaster/in und eine zweite Person (A-08), geplant 2 | Freigabe, Inhalte (mit Planung), Seiten (mit Fotos), Lernen, Mitglieder, System | Alles, auch Mitglieder einladen, Rollen vergeben, Fotos verwalten, Einstellungen und Schnittstellen, Inhalte nach Nachfrage löschen. Ausnahme: sieht keine Lernergebnisse anderer und legt keine Lernthemen an (E-05, E-09) |
| Kommandant · Freigabe | Kommandant und Stellvertretung, geplant 3 | Freigabe, Inhalte (mit Planung), Seiten, Lernen (mit Lernstand) | Beiträge, Einsätze und Änderungen veröffentlichen, Einsätze von Hand anlegen, alles bearbeiten und ausblenden, Seiten pflegen, Fahrzeuge und Geräte hinzufügen und entfernen, Instagram-Post auslösen, Lernthemen anlegen, den Lernstand aller sehen |
| Redaktion | Pressearbeit, Aktive, geplant mehrere | Inhalte (mit Planung), Seiten, Lernen | Beiträge mit Fotos schreiben und einreichen, eigene bearbeiten (über die Freigabe) und ausblenden, Änderungen an Seiten sowie neue Fahrzeuge und Geräte vorschlagen, nicht selbst veröffentlichen |
| Bereichsredaktion | z. B. Jugendwart | Inhalte (mit Planung), Seiten, Lernen | Im eigenen Bereich schreiben, veröffentlichen, bearbeiten und ausblenden |
| Mitglied | Alle übrigen Aktiven der Einsatzabteilung, geplant gut 40 | Lernen | Nur lesen und lernen: Themen ansehen, Tests machen, eigene Ergebnisse sehen. Keine Schreib- oder Bearbeitungsrechte (E-01) |

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
| R-01 | Plan im Mitgliederbereich mit Thema, Datum, zuständiger Person und Status, erreichbar über „Inhalte“ (B-06). | Muss |
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
| A-06 | Das Handbuch (PDF, bebildert, Du-Form) ist Teil der Lieferung. Es enthält Rollen, Anmelden, Inhalte (schreiben, finden, bearbeiten, ausblenden, löschen, Rückgängig und Verlauf), Redaktionsplan, Freigeben (auch Änderungen mit Vergleich, Einsatz von Hand und E-Mail-Hinweis), Seiten pflegen, Lernen (Thema und Test), Lernthemen verwalten (Themenplan, anlegen, bearbeiten, kopieren, ausblenden, Lernstand), Mitglieder- und Fotoverwaltung, System mit Schnittstellen-Diagnose und Notbetrieb, regelmäßige Aufgaben, die Checkliste „Admin-Wechsel“, Notfallkontakte und häufige Fragen. Die Bildschirmfotos zeigen die echte Website, nach Phase 2 aus der Staging-Seite neu erstellt. Jede neue Funktion bekommt einen Abschnitt im Handbuch. | Muss |
| A-07 | Konten und Verträge laufen auf den Verein (Domain, Hosting, DIVERA, Meta, GitHub). Die Zugangsdaten liegen im Passwort-Tresor des Vereins, mit Notfallzugang für den Vorstand. | Muss |
| A-08 | Immer mindestens zwei Admins. Jährlich eine Übergabe-Übung mit Test der Wiederherstellung. | Muss |
| A-09 | Laientest als Abnahme: Ein Mitglied ohne IT-Kenntnisse erledigt zehn typische Aufgaben nur mit dem Handbuch. | Muss |
| A-10 | Schnittstellen austauschbar gebaut: Je Schnittstelle (DIVERA, Instagram) ein eigener Ordner mit Client (nur HTTP, Zeitlimit, Wiederholung), Zuordnung (Mapping, inkl. Datensparsamkeit D-02), Vertrag (Pflichtfelder und Typen) und README. Die API-Version ist festgelegt. Vertragstests prüfen das Mapping gegen anonymisierte Beispielantworten (Fixtures). Passt eine Antwort nicht zum Vertrag, wird nichts gespeichert (Fehler *-FMT). | Muss |
| A-11 | Diagnose und Notbetrieb im System-Bereich: je Schnittstelle Status, Fehlercode mit Klartext (DIV-401, DIV-NET, DIV-FMT, IG-EXP, IG-190, IG-FMT), Schritte „So behebst du es“, „Verbindung testen“, „Schlüssel neu eintragen“ (verdeckt, verschlüsselt gespeichert, nie wieder angezeigt) bzw. „Neu verbinden“, „Notbetrieb“ (Import pausiert, Einsätze und Termine von Hand; Instagram-Vorschau durch Profil-Link ersetzt) und „Diagnosebericht kopieren“ ohne Zugangsdaten. Besucherinnen und Besucher sehen nie eine Fehlermeldung. | Muss |
| A-12 | Reparatur-Anleitung „Schnittstellen reparieren“ (docs/betrieb/schnittstellen.md) für eine Person, die den Code hat, die Website aber nicht kennt: Aufbau, WP-CLI-Befehle (diagnose, test, dump --anonymize, notbetrieb), Fehlercodes, Schritt-für-Schritt-Reparatur bei geänderter Antwort, Nacharbeiten. Ziel: Reparatur in unter zwei Stunden. Wird bei jeder Änderung an einer Schnittstelle mitgepflegt. | Muss |

### 2.12 Lernen (Fortbildung für Aktive)

Anforderung des 1. Kommandanten (23.11.2026): Die Website dient zusätzlich als einfache Lernplattform für alle aktiven Mitglieder. Jeden Monat gibt es ein neues Thema (z. B. Verkehrsabsicherung, Erste Hilfe), das der Kommandant erstellt. Die Mitglieder lesen die Inhalte und machen danach einen kleinen Multiple-Choice-Test. Ziel: Alle Aktiven bilden sich selbständig und regelmäßig fort, die Kommandanten behalten langfristig den Überblick über den Wissensstand. Das Lernen ergänzt Ausbildung, Übungsabende und Unterweisungen, es ersetzt sie nicht (L-17).

| ID | Anforderung | Prio |
| --- | --- | --- |
| E-01 | Rolle „Mitglied“: nur lesen und lernen. Die untere Leiste zeigt nur „Lernen“. Keine Schreib- oder Bearbeitungsrechte, keine Freigabe, kein Zugriff auf andere Bereiche – serverseitig geprüft. Einladung wie bei B-01 durch einen Admin, mit dem Häkchen „Gehört zur Einsatzabteilung“ (E-10). Alle anderen Rollen sehen „Lernen“ ebenfalls und können mitlernen. | Muss |
| E-02 | Themenseite (in Schritten, E-17): Titel, Monat, Einleitung, Abschnitte (Überschrift und Text), „Das Wichtigste“ als Merksätze, Links zum Weiterlernen, Quelle mit Stand, „Fachlich geprüft: Name“ und ein Sicherheitshinweis (E-12). Darunter der Test (E-06). Fotos nur eigene, ohne erkennbare Einsatzbetroffene und Kennzeichen (Kann). | Muss |
| E-03 | Ein Thema je Monat. Am Monatsersten wird das geplante Thema automatisch „Thema des Monats“, vorher ist es für Mitglieder unsichtbar. Frühere Themen bleiben mit Test abrufbar. Fehlt für den laufenden oder nächsten Monat ein veröffentlichtes Thema, sehen die Kommandanten einen Hinweis. | Muss |
| E-04 | Material der Staatlichen Feuerwehrschulen Bayern (Feuerwehr-Lernbar, Merkblätter der Feuerwehrschulen), der DGUV und anderer Stellen wird in eigenen Worten zusammengefasst und verlinkt, nicht kopiert und nicht eingebettet (N-01, L-14). Links nur mit https://, sie öffnen sich in einem neuen Fenster. Die Quelle mit Stand ist Pflicht. | Muss |
| E-05 | Themen anlegen, bearbeiten, kopieren und ausblenden: nur Kommandanten, im Themenplan (E-26), ohne Programmieren (A-01). Formular mit „+ Abschnitt“ und „+ Link“ und genau fünf Fragen; Eingaben bleiben beim Hinzufügen erhalten. „Als Entwurf speichern“ oder „Veröffentlichen“ (für einen späteren Monat: geplant). Veröffentlichen nur mit vollständigen Pflichtangaben und dem Pflicht-Häkchen „Ich habe den Inhalt fachlich geprüft. Quellen sind angegeben, fremde Texte und Bilder sind nicht ohne Erlaubnis kopiert.“ Je Monat ein veröffentlichtes Thema. Ausblenden statt Löschen, die Ergebnisse bleiben bis zur Löschfrist (E-11); Löschen nur durch Admins (B-16). Verlauf (B-07) und Rückgängig (B-17). Admins und Redaktion legen keine Themen an. | Muss |
| E-06 | Test: genau 5 Fragen mit je 2 bis 4 Antworten, genau eine richtig, jede mit kurzer Erklärung. Eine Frage pro Bildschirm mit sofortiger Rückmeldung (E-18); ausgewertet wird, wenn alle Fragen beantwortet sind. Bestanden ab 4 von 5 richtigen Antworten. Danach je Frage: richtig oder falsch, die richtige Antwort und die Erklärung. Beliebig oft wiederholbar, ohne Zeitlimit. Die Vorschau eines Entwurfs speichert kein Ergebnis. | Muss |
| E-07 | Eigener Lernstand: Jede Person sieht nur ihre eigenen Ergebnisse – je Thema „bestanden“, „noch nicht bestanden“ oder „offen“ und „x von y Themen bestanden“. Ein Testversuch lässt sich nicht rückgängig machen (Ausnahme von B-17). | Muss |
| E-08 | Lernstand (nur Kommandanten): je Thema Teilnahme (x von y, in %), Zahl der Bestandenen, Durchschnitt im ersten Versuch, „Welche Fragen waren schwer?“ (Anteil falscher Antworten im ersten Versuch), Verlauf der Teilnahme über die Monate und eine Übersicht pro Person für die letzten vier Themen (✓ bestanden, ✗ versucht, – offen). Jedes frühere Thema ist auswählbar. Ein Export für die Ausbildungsplanung ist Kann und erst nach Klärung von L-15 erlaubt. | Muss |
| E-09 | Sichtbarkeit: Einzelergebnisse sehen nur die Person selbst und die Kommandanten – keine Admins, keine Redaktion, niemand öffentlich, auch nicht über Monatsbericht, Diagnosebericht oder Exporte. Keine Rangliste, keine Veröffentlichung, keine Weitergabe. Technisch: eigene Tabelle, Zugriff nur über eine Rechteprüfung „Lernstand sehen“, die nur die Rolle Kommandant · Freigabe hat. Hinweis im Lernstand: zur Planung von Übungen, nicht zur Bewertung Einzelner. | Muss |
| E-10 | Wer zählt: alle Konten mit dem Häkchen „Gehört zur Einsatzabteilung“. Der Admin setzt es bei der Einladung und kann es ändern; Konten ohne Häkchen sind in der Kontenliste gekennzeichnet. | Muss |
| E-11 | Datensparsam: gespeichert werden nur Konto, Thema, Zeitpunkt, gegebene Antworten, Punktzahl und „bestanden“. Ergebnisse werden nach 3 Jahren automatisch gelöscht (Annahme, L-15), beim Austritt (B-08) sofort. | Muss |
| E-12 | Hinweise: Auf „Lernen“ ein aufklappbarer Hinweis „Wer sieht meine Ergebnisse?“ (freiwillig, nur Kommandanten, keine Rangliste, Löschfrist, ersetzt keine Ausbildung und keine Unterweisung). Auf jeder Themenseite: „Sicherheit geht vor: Diese Lerneinheit ersetzt keine Ausbildung, keine Übung und keine Unterweisung. Im Einsatz gilt, was deine Führungskraft anordnet.“ Beispielinhalte sind als solche gekennzeichnet. | Muss |
| E-13 | E-Mail am Monatsersten an alle Konten der Einsatzabteilung: nur Titel des Themas und Link, ohne Ergebnisse; je Thema abschaltbar. | Soll |
| E-14 | Am Handy gut bedienbar: große Antwortflächen (mindestens 44 px), Tastatur bedienbar, ab 360 px ohne seitliches Scrollen; die Übersicht pro Person scrollt bei Bedarf in sich. | Muss |

**Beispielthemen in der Demo** (Beispielinhalt, vom Kommandanten fachlich zu prüfen und mit dem aktuellen Stand der Quellen abzugleichen): Verkehrsabsicherung nach dem Merkblatt 6.003 der Staatlichen Feuerwehrschule Würzburg (Version 5.0, Stand 05/2023), Wiederbelebung nach den Leitlinien des ERC in der deutschen Fassung des German Resuscitation Council, Gefahren an der Einsatzstelle nach dem Schema AAAA-C-EEEE. Für Dezember liegt ein unfertiger Entwurf „Feuerlöscher richtig einsetzen“ bereit.

**Quellen:** [Feuerwehr-Lernbar Bayern](https://www.feuerwehr-lernbar.bayern/) · [Staatliche Feuerwehrschule Würzburg](https://www.sfs-w.de/) · [DGUV Vorschrift 49 Feuerwehren](https://publikationen.dguv.de/) · [DGUV FBFHB-037 (2024)](https://publikationen.dguv.de/regelwerk/publikationen-nach-fachbereich/feuerwehren-hilfeleistungen-brandschutz/feuerwehren-und-hilfeleistungsorganisationen/5074/fbfhb-037-absicherung-von-einsatzstellen-im-oeffentlichen-verkehrsraum-unter-beruecksichtigung-der-zu) · [German Resuscitation Council](https://www.grc-org.de/)

### 2.13 Gern und leicht lernen (Gestaltung und Ablauf)

Es ist davon auszugehen, dass nicht alle Mitglieder gern Weiterbildungen machen und sich nicht von selbst zum Lernen anmelden. Deshalb sind einfache Bedienung und Freude am Lernen zentraler Teil des Bereichs „Lernen“ – gleichrangig mit dem Inhalt. Der Ablauf ist am Handy in einer kurzen Pause zu schaffen, lädt freundlich ein und belohnt, ohne Druck aufzubauen oder Einzelne vorzuführen (L-16).

**Leitlinien**

- **Ein Schritt, ein Knopf:** Jeder Bildschirm hat genau eine Hauptaktion („Los geht’s“, „Weiter“, „Antwort prüfen“).
- **Kurz:** ein Thema in höchstens 10 Minuten, ein Abschnitt passt auf einen Handybildschirm.
- **Freundlich:** Du-Form, ermutigende Sprache („Fast!“, „Knapp vorbei“), nie „falsch“ in Rot ohne Erklärung.
- **Sichtbarer Fortschritt:** Fortschrittsbalken, „Weiterlernen“, Serie und Jahresstand – nur für die Person selbst.
- **Kein Druck:** keine Rangliste, keine Namen anderer, keine Zeitlimits, beliebig oft wiederholbar.

| ID | Anforderung | Prio |
| --- | --- | --- |
| E-15 | Messbare Ziele: vom Login bis zum ersten Lerninhalt höchstens 2 Tipps; ein Thema samt Test in höchstens 10 Minuten; alles mit einer Hand am Handy ab 360 px bedienbar; Tippflächen im Test mindestens 56 px hoch. | Muss |
| E-16 | Startseite „Lernen“: persönliche Begrüßung („Servus, Anna!“) und ein Satz je nach Stand (offen, mittendrin, geschafft); das Thema des Monats als große farbige Karte mit Symbol, Titel, Einleitung, Dauer („ca. 8 Min.“), Fragenzahl, Status und einem Hauptknopf („Los geht’s“, „Weiterlernen“ oder „Nochmal ansehen“); daneben „Kenn ich schon – direkt zum Test“. | Muss |
| E-17 | Lernen in Schritten: Start mit Überblick, dann je Abschnitt eine Seite, dann „Das Wichtigste“ mit Links, Quelle und Sicherheitshinweis, dann der Test. Oben ein Fortschrittsbalken („Schritt 2 von 11“), unten „Zurück“ und „Weiter“ gut erreichbar. Der Fortschritt wird je Person gespeichert; „Weiterlernen“ springt an die richtige Stelle. Nach dem Bestehen beginnt das Thema wieder vorn. | Muss |
| E-18 | Test: eine Frage pro Bildschirm mit großen Antwortflächen. Nach „Antwort prüfen“ sofort die Rückmeldung – „Richtig!“ oder „Fast! Richtig ist: …“ – mit der Erklärung, richtige Antwort grün, gewählte falsche Antwort markiert. Dann „Nächste Frage“. | Muss |
| E-19 | Ergebnis: „Geschafft!“ mit kurzer Erfolgs-Animation (entfällt bei der Systemeinstellung „Bewegung reduzieren“) bzw. „Knapp vorbei“ mit Ermutigung, „Nochmal versuchen“ und „Inhalt nochmal lesen“. Die eigenen Antworten mit Lösung sind aufklappbar. Ist noch ein früheres Thema offen, folgt der Vorschlag „Noch eins nachholen“. | Muss |
| E-20 | Persönlicher Fortschritt: „x von y Themen geschafft“ mit Balken und die Serie „n Monate in Folge dabei“. Nur für die Person selbst sichtbar. | Muss |
| E-21 | Gemeinsames Ziel: „x von y aus der Einsatzabteilung haben das Thema schon geschafft“ – nur als Zahl, ohne Namen. Von den Kommandanten abschaltbar (Annahme; mit L-16 prüfen). | Soll |
| E-22 | Nachholen: offene frühere Themen stehen oben als Karten „Zum Nachholen“ mit Symbol und Status, geschaffte darunter. | Muss |
| E-23 | Jedes Thema hat ein Symbol mit Farbe (Auswahl: Verkehr, Erste Hilfe, Gefahren, Brand, Funk, Technik, Wasser, Atemschutz, Allgemein; eigene Zeichnungen, keine fremden Grafiken). Die Lesezeit wird automatisch berechnet (etwa 150 Wörter pro Minute plus 2 Minuten für die Fragen). | Muss |
| E-24 | Erinnern ohne zu nerven: E-Mail am Monatsersten (E-13) und höchstens eine freundliche Erinnerung zur Monatsmitte, nur an Konten, die das Thema noch nicht geschafft haben – ohne Ergebnisse im Text, abbestellbar. Dazu die rote Zahl am Bereich „Lernen“ (B-22). | Soll |
| E-25 | Leichter Zugang: Der Link in der Mail führt nach dem Login direkt zum Thema. Mit „Auf diesem Gerät angemeldet bleiben“ bleibt ein Konto mit der Rolle Mitglied bis zu 90 Tage angemeldet (Annahme, Sicherheit prüfen; die Rolle hat keine Schreibrechte). 2-Faktor-Anmeldung ist für Mitglieder empfohlen, nicht Pflicht (B-04). | Soll |
| E-26 | Themenplan für Kommandanten: 12 Monate auf einen Blick (2 zurück, 9 voraus, der aktuelle hervorgehoben), je Monat Thema mit Symbol, Status (Entwurf, geplant, veröffentlicht, ausgeblendet) und Teilnahme oder „Noch kein Thema · + Thema für …“. Je Thema: Bearbeiten, Ansehen (Vorschau wie bei Mitgliedern, speichert keine Ergebnisse), Kopieren (z. B. ein Thema aus dem Vorjahr, landet im nächsten freien Monat), Ausblenden bzw. Einblenden. Ältere Themen aufklappbar. Löschen nur durch Admins (B-16). | Muss |
| E-27 | Hilfen beim Anlegen: Themenideen zum Antippen (setzen Titel und Symbol; Liste im Backend pflegbar, A-01), Symbolwahl, Tipps für gute Themen und Fragen, Anzeige der Lesezeit und „Noch offen zum Veröffentlichen: …“, das alle fehlenden Angaben auf einmal nennt. | Muss |
| E-28 | Abnahme mit Laien (wie A-09): Drei Mitglieder ohne Einweisung schaffen ein Thema am eigenen Handy in höchstens 10 Minuten und würden es „gern wieder“ machen; ein Kommandant legt nur mit dem Handbuch ein Thema an und plant es für den nächsten Monat. | Muss |

## 3. Nicht-funktionale Anforderungen

| ID | Thema | Anforderung |
| --- | --- | --- |
| N-01 | Datenschutz | Keine externen Ressourcen: Schriften selbst gehostet, kein Google Analytics, keine Einbettungen von Social Media oder Karten. Damit ist kein Cookie-Banner nötig. |
| N-02 | Barrierefreiheit | WCAG 2.2 AA als Ziel: Kontraste, Alt-Texte, Tastaturbedienung mit Sprunglink „Zum Inhalt“, Tippziele mindestens 44 px. |
| N-03 | Mobile first | Voll bedienbar ab 360 px Breite, ohne seitliches Scrollen, auch bei langen Wörtern und Adressen. |
| N-04 | Performance | Lighthouse ≥ 90 mobil, Bilder als WebP/AVIF in mehreren Größen, Seiten-Cache. |
| N-05 | Sicherheit | 2FA, Login-Drosselung, Zugangsschlüssel in wp-config.php, HTTPS, Security-Header. Eingaben werden immer als Text ausgegeben, nie als HTML oder Skript. Begrenzung von Änderungen: höchstens 30 Speichervorgänge je Person in 10 Minuten, danach Hinweis „Bitte warte ein paar Minuten“; Höchstlängen der Felder (B-20). |
| N-06 | Betrieb | Tägliches Backup auf externen Speicher, Wiederherstellung regelmäßig getestet. |
| N-07 | Kosten | Keine laufenden Kosten über das Hosting hinaus, ggf. wenige Euro für Backup-Speicher. Ausnahme: Variante B (4.3). |
| N-08 | Design | Rot #CD1719, Logo aus dem Briefpapier, Roboto bzw. Roboto Condensed. Die Demo ist freigegebene Grundlage (Projektdokument „Corporate Design“). |
| N-09 | Ansprache | Durchgehend Du-Form, auch im Mitgliederbereich, in Mails, Rechtstexten und im Handbuch. |
| N-10 | Bildrechte | Standardnachweis „Fotos: Feuerwehr Piflas“. Fremde Fotos nur mit schriftlicher Erlaubnis. |
| N-11 | Tests | Die Prüfungen der Demo-Testsuite sind die Abnahmeliste: Rollen, Anonymisierung, Freigabe-Sperre, keine externen Anfragen, Darstellung ab 360 px, Robustheit gegen fehlerhafte Eingaben. Die Zuordnung der Prüfungen zu den IDs steht in demo/README.md. |
| N-12 | SEO | Saubere Adressen, Sitemap, strukturierte Daten für Organisation und Termine. |
| N-13 | Frauen und Männer | Frauen werden genauso angesprochen wie Männer – selbstverständlich, nicht aufdringlich. Wo die Wahl besteht: (1) neutrale Formen zuerst (Mitglieder, Team, Redaktion, Ansprechperson, alle, die helfen). (2) Sonst beide Formen ausgeschrieben (Bürgerinnen und Bürger), in knappen Beschriftungen mit Schrägstrich (Webmaster/in). (3) Keine Sternchen oder Doppelpunkte – besser lesbar und für Vorleseprogramme. Ausnahmen: „Kommandant“ statt „Kommando“, weil ein Kommandant die Feuerwehr leitet, und „Admin“ statt „Administration“. Feuerwehrfunktionen heißen wie in den Feuerwehr-Dienstvorschriften (FwDV) und den bayerischen Vorschriften, z. B. Gruppenführer, Maschinist, Atemschutzgeräteträger, Jugendwart. Rollen auf der Website: Admin, Kommandant · Freigabe, Redaktion, Bereichsredaktion, Mitglied. Fotos und Bildbeschreibungen zeigen, wo möglich, Frauen und Männer. Auf „Mitmachen“ steht ausdrücklich, dass Frauen und Männer gleichermaßen willkommen sind. Gilt auch für Mails, Handbuch und Textvorlagen; die Demo-Testsuite prüft auf rein männliche Formen außerhalb dieser Ausnahmen. |

### 3.1 Rechtlicher Rahmen

Die Freiwillige Feuerwehr ist eine Einrichtung des Marktes Ergolding (Art. 4 BayFwG). Der Verein unterstützt sie (Art. 5 BayFwG) und betreibt die Website. Einsatzinformationen brauchen deshalb die Zustimmung von Kommandant und Markt. Dies ist keine Rechtsberatung. Vor dem Go-live prüft eine Fachperson für Datenschutz oder Recht, z. B. über den LFV Bayern.

| ID | Grundlage | Anforderung | Umsetzung |
| --- | --- | --- | --- |
| L-01 | Art. 4, 5 BayFwG | Verein betreibt, Kommandant gibt frei, schriftlich mit dem Markt abgestimmt | Impressum, Freigabe; Vereinbarung offen |
| L-02 | Verschwiegenheit (Art. 20 GO, Merkblatt StMI) | Keine vertraulichen Einsatzdetails | D-02, W-04; Freigabe-Mails ohne Inhalte (W-09) |
| L-03 | DSGVO / BayDSG | Keine erkennbaren Personen, Kennzeichen oder Objekte; Ort nur als Ortsteil bzw. Gemeinde | Anonymisierung; Test „keine Adressen“ |
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
| L-14 | Urheberrecht (UrhG) | Lehrmaterial der Feuerwehrschulen, der DGUV und anderer nur verlinken; Texte, Grafiken oder Bilder nur mit schriftlicher Erlaubnis übernehmen | E-04, Pflicht-Häkchen E-05 |
| L-15 | DSGVO Art. 5, 6, 13, 26/28; BayDSG | Lernergebnisse sind personenbezogene Daten: Verantwortlichen klären (Verein als Betreiber, Markt als Träger der Feuerwehr, ggf. Vereinbarung), Rechtsgrundlage festlegen (Annahme: freiwillige Teilnahme mit Transparenzhinweis), Zweck nur Ausbildungsplanung, Löschfrist, Information der Mitglieder, Eintrag im Verzeichnis der Verarbeitungstätigkeiten, Verpflichtung der Admins mit Datenbankzugriff | E-09 bis E-12; Datenschutzhinweis ergänzen; offen (5) |
| L-16 | Ehrenamt, Persönlichkeitsrecht | Keine Leistungs- oder Verhaltenskontrolle, keine Rangliste, kein Druck; Nicht-Teilnahme hat keine Folgen | E-07, E-09, E-12 |
| L-17 | DGUV Vorschrift 49 (§ 8 Unterweisung), FwDV 2, BayFwG | Ausbildung und jährliche, dokumentierte Unterweisung bleiben Aufgabe der Feuerwehr vor Ort; das Lernen ersetzt sie nicht und darf Merkblättern und Dienstvorschriften nicht widersprechen | E-05 (fachlich geprüft, Quelle mit Stand), E-12 |

Für den Bereich „Lernen“ (L-14 bis L-17) prüft zusätzlich eine Fachperson für Datenschutz, wer verantwortlich ist und auf welcher Rechtsgrundlage Ergebnisse gespeichert werden; Fragen zu Unterweisung und Ausbildung klärt der Kommandant mit dem Kreisbrandrat bzw. der KUVB.

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
| Demo v13 | Verbindliche Vorlage für Aufbau, Texte und Abläufe. Statisch, ohne Datenbank; Demo-Steuerung und Schnell-Login gibt es nur dort; die Bereichsredaktion ist in der Demo nur bei der Einladung wählbar. | Artefakt-Link, Backup |
| Testsuite (693 Prüfungen) | Abnahmeliste für die echte Website | GitHub, Backup (`demo/test_app.py`) |
| Anleitung „Schnittstellen reparieren“ | Reparatur von DIVERA und Instagram durch die Technik (A-12) | GitHub, Backup (`betrieb/schnittstellen.md`) |
| Handbuch Mitgliederbereich 1.12 | Anleitung für alle Rollen (A-06), in der Demo nach dem Login verlinkt | PDF, Backup |
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
- [ ] Erstbesetzung der Rollen (geplant: 3 Kommandanten, 2 Admins, mehrere Personen in der Redaktion)
- [ ] Wer pflegt Vorstandschaft und Vereinstexte (Vorstand oder Kommandant)? Bisher Annahme: wie alle Inhalte – Redaktion reicht ein, Kommandant oder Admin gibt frei (B-21). Laut Satzung prüfen.
- [ ] Fahrzeuge entfernen auch durch Kommandanten (Ausnahme von B-16) bestätigen
- [ ] Abstimmung mit dem Markt Ergolding (L-01), dabei auch klären, ob die Sirenen bei Probealarm und Warntag mitmachen (C-07)
- [ ] Ist ein Online-Antrag für Fördermitglieder laut Satzung zulässig?
- [ ] An welche E-Mail-Adresse gehen Mitmach-Anfragen (F-06)?
- [ ] Lernen: Verantwortlicher und Rechtsgrundlage für Lernergebnisse (Verein oder Markt, L-15) – Fachperson Datenschutz, ggf. Markt Ergolding
- [ ] Lernen: Löschfrist (Annahme 3 Jahre), Mail am Monatsersten und Erinnerung zur Monatsmitte (E-13, E-24) bestätigen
- [ ] Lernen: „Angemeldet bleiben“ bis 90 Tage für die Rolle Mitglied (E-25) und anonyme Teilnahmezahl (E-21) bestätigen
- [ ] Lernen: Dürfen Kommandanten eigene, nie veröffentlichte Entwürfe löschen? Bisher feste Entscheidung: Löschen nur durch Admins
- [ ] Lernen: Wer zählt zur Einsatzabteilung (E-10)? Sollen auch Jugendliche der Jugendfeuerwehr teilnehmen? Dann Einwilligung der Eltern klären

**Zugänge (Phase 0)**

- [ ] Hosting prüfen (4.1)
- [ ] DIVERA: API-Zugang in der gebuchten Stufe? Wie sind private und Jubiläumstermine markiert?
- [ ] Instagram auf professionelles Konto umstellen, Meta-Entwicklerkonto auf den Verein anlegen
- [ ] Joomla sichern, Umfang des Archivs festlegen (F-13)
- [ ] SMTP-Versand über den Hoster prüfen (Zustellbarkeit, SPF/DKIM) für Freigabe-Mails (W-09)

**Inhalte**

- [ ] Kommandant (Impressum), Vorstandschaft, Jugendwart und Gruppenstunde
- [ ] Gründungsjahr und Meilensteine der Chronik; Jubiläumstermine 2027 und Jubiläumslogo
- [ ] Liste der Ortsteile und häufigen Nachbargemeinden für Einsatzberichte (D-09)
- [ ] Name für „Verantwortlich nach § 18 Abs. 2 MStV“ im Impressum
- [ ] Fahrzeugtypen und Funkrufnamen; Namen der Fotografinnen und Fotografen; Herkunft des Fotos vom 11/1
- [ ] Fotos und Texte vom Vereinsleben (Dorffest, Steckerlfisch, Atemschutz)
- [ ] Förderbeitrag und beide PDFs
- [ ] Kurztexte zu den Partnerfeuerwehren
- [ ] Tipp-Kalender durch den Kommandanten freigeben
- [ ] Lernen: Themenplan für 12 Monate und fachliche Prüfung der drei Beispielthemen durch den Kommandanten
- [ ] Notfallkontakte (Handbuch 11.3) und technische Ansprechperson für Schnittstellen (A-12)

**Recht**

- [ ] Verträge zur Auftragsverarbeitung mit Hoster und DIVERA
- [ ] Verzeichnis der Verarbeitungstätigkeiten
- [ ] Foto-Einwilligung in die Aufnahmeformulare
- [ ] Datenschutzhinweis um „Lernen“ ergänzen (L-15)
- [ ] Optional: Erlaubnis der Feuerwehrschulen, Grafiken aus Merkblättern zu übernehmen (L-14)
- [ ] Prüfung durch eine Fachperson für Datenschutz oder Recht vor dem Go-live

## 6. Umsetzungsplan

**Stand 23.11.2026:**

| Ergebnis | Stand |
| --- | --- |
| Übergangsseite | Fertig zum Hochladen |
| Demo v13 + Testsuite (693 Prüfungen) | Fertig, auf GitHub Pages |
| Handbuch | Version 1.12 fertig |
| Lastenheft | Version 1.14 |
| Backup-Paket | Wird mit jeder Version aktualisiert |

**Sofort:** Übergangsseite hochladen. Vorher Joomla komplett sichern und die Speicherdauer der Logfiles in datenschutz.html eintragen.

Jede Phase endet mit einer Abnahme durch den Verein. Claude Code arbeitet in einem eigenen Branch je Phase und öffnet einen Pull Request mit der Liste der erfüllten IDs.

1. **Phase 0 – Klärung und Zugänge** (Verein): offene Punkte aus Abschnitt 5, Hosting, GitHub-Organisation des Vereins, Staging-Subdomain.
2. **Phase 1 – Grundgerüst:**
   - WordPress mit 2FA, Backup, Protokoll und SMTP
   - Rollen samt „Mitglied“ und Einladungen (B-01 bis B-08, E-01, E-10), Verlauf und Spam-Schutz (B-07, B-20, N-05)
   - Tests und automatisches Hochladen auf die Testseite (Staging)
   - Abnahme: Jede Rolle kann genau das, was in der Tabelle steht; eine Wiederherstellung ist getestet.
3. **Phase 2 – Theme und Mitgliederbereich:**
   - Alle Seiten aus 2.1
   - Beiträge mit Fotos, Bearbeiten, Ausblenden und Löschen (B-09 bis B-11, B-14 bis B-16)
   - Inhalte-Übersicht, Editor, Rückgängig, Seiten pflegen (B-17 bis B-21), Einsatz von Hand (D-09)
   - Schnittstellen nach A-10 mit Diagnose und Notbetrieb (A-11), Anleitung (A-12)
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
7. **Phase 6 – Lernen** (E-): Themen in Schritten, Test, eigener Lernstand, Themenplan und Lernstand für Kommandanten. Abnahme: Laientest nach E-28, ein Admin sieht keine Ergebnisse, L-15 ist geklärt.
8. **Phase 7 – Go-live:**
   - Rechtstexte final
   - Überwachung und Monatsbericht (M-)
   - Barrierefreiheitsprüfung
   - Schulungsabend
   - Umzug auf www.feuerwehr-piflas.de
   - Abnahme: Laientest (A-09), Übergabe-Übung (A-08), zwei Wochen ohne kritische Fehler
9. **Phase 8 – Ausbau (optional):** Facebook, Suche, amtliche Warnungen.

## 7. Vorlagen für Claude Code

Ins Repository gehören diese Vorlage als `CLAUDE.md`, das Lastenheft als `docs/lastenheft.md`, die Demo mit Testsuite nach `docs/referenz-demo/` und das Handbuch nach `docs/handbuch/`.

```markdown
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
| 1.7 | 23.11.2026 | Neu: D-09 (Einsatz von Hand), W-08 (Änderungen an Seiten freigeben), B-17 (Rückgängig), B-18 (Übersicht mit Suche, Filtern und Seitenweise-Laden für mehrere hundert Einträge), B-19 (Editor, Titelbild wählen), B-20 (Höchstlängen), B-21 (Verein, Chronik, Fahrzeuge und Ausrüstung pflegen; Kommandanten fügen Fahrzeuge und Geräte hinzu und entfernen sie), A-10 bis A-12 (Schnittstellen austauschbar, Diagnose und Notbetrieb, Reparatur-Anleitung). Geändert: B-01 (eine Rolle je Konto, keine Rollenauswahl beim Login), B-07 (Verlauf jetzt Muss, sicher und mit Spam-Schutz), B-14 (Editor, Einsätze vollständig bearbeitbar), B-16 (Ausnahme Fahrzeuge), W-07 (verworfen/zurückgegeben 30 Tage wiederherstellbar, mit Hinweis), D-08, F-02, F-03, F-05, F-08, N-05 (Begrenzung), A-06, Rollentabelle mit geplanter Besetzung (3 Kommandanten, 2 Admins, mehrere Redaktion), 4.2, 5, 6, CLAUDE.md-Vorlage. Demo v6 (Fehler behoben: Fotos beim Einsatzbericht), Testsuite (539 Prüfungen), Handbuch 1.5. Annahmen: Redaktion pflegt Seiten über die Freigabe; Ortsteil-Liste Piflas, Ergolding, Oberglaim vorläufig. |
| 1.8 | 23.11.2026 | Neu W-09: E-Mail an alle Kommandanten bei jeder Einreichung und tägliche Erinnerung (Uhrzeit einstellbar), mit Inhalt und Knöpfen „Freigeben“/„Verwerfen“; sichere Einmal-Links mit Bestätigungsseite und Pflicht-Häkchen. Geändert: B-21 und W-08 (alle Rollen legen Fahrzeuge und Geräte an, Redaktion über die Freigabe; entfernen weiter nur Kommandant und Admins), B-06 (Kopf im Mitgliederbereich am Handy), Rollentabelle, A-06, L-02, 4.2, 5, 6. Demo v7, Testsuite (565 Prüfungen), Handbuch 1.6. |
| 1.9 | 23.11.2026 | Geändert: W-09 (Mail nur noch als Hinweis mit Link zur Freigabe, ohne Inhalte und ohne Freigeben aus der Mail – Verschwiegenheit), W-08 (Freigabe als Vergleich: geänderte Felder Wort für Wort hervorgehoben, Überblick nach Art), B-07 (Verlauf mit „Was wurde geändert?“), D-02, D-09, F-03, B-14, L-02, L-03 (Einsätze auch überörtlich: Einsatzort als Ortsteil oder Gemeinde, Straßen und Hausnummern werden abgewiesen), A-06, 4.2, 5, 6. Demo v8 (u. a. mehr Monate in der Datumssimulation), Testsuite (568 Prüfungen), Handbuch 1.7. |
| 1.10 | 23.11.2026 | B-17 ergänzt: Rückgängig auch beim Veröffentlichen gut erreichbar – die letzte Aktion bleibt 5 Minuten oben sichtbar („Zuletzt: … · Rückgängig“), auch auf der Seite des gerade veröffentlichten Beitrags; gilt für alle Eingaben (auch Einplanen). Demo v9, Testsuite (573 Prüfungen), Handbuch 1.8. |
| 1.11 | 23.11.2026 | Neu 2.12 „Lernen“ (E-01 bis E-14, Anforderung des 1. Kommandanten): Rolle „Mitglied“ ohne Schreib- und Bearbeitungsrechte, Monatsthema mit Inhalt, Merksätzen, Links zu den Feuerwehrschulen und Multiple-Choice-Test, eigener Lernstand, Lernstand nur für Kommandanten, Datensparsamkeit und Löschfrist. Neu L-14 bis L-17 (Urheberrecht, Datenschutz der Lernergebnisse, keine Leistungskontrolle, DGUV-Unterweisung bleibt). Geändert: B-06 und R-01 (Redaktionsplan unter „Inhalte“, höchstens sechs Bereiche in der Leiste), B-17 (Ausnahme Testversuche), Rollentabelle, Ziele, A-06, N-13, 0, 4.2, 5, 6 (neue Phase 6), CLAUDE.md-Vorlage (Präfix E-). Annahmen: bestanden ab 80 %, Löschfrist 3 Jahre, freiwillige Teilnahme. Demo v10, Testsuite (643 Prüfungen), Handbuch 1.9. |
| 1.12 | 23.11.2026 | Neu B-22: rote Zähler an den Bereichen, wenn etwas zu tun ist (Freigabe, Inhalte, Lernen, System). Geändert: E-06 (genau 5 Fragen, bestanden ab 4 richtigen Antworten), E-05, B-02 (Admins ändern Rollen am Konto: nicht die eigene, immer mindestens zwei Admins, Hinweis auf 2FA, rückgängig machbar), 0, 4.2, 5, 6. Demo v11, Testsuite (655 Prüfungen), Handbuch 1.10. |
| 1.13 | 23.11.2026 | Neu 2.13 „Gern und leicht lernen“ (E-15 bis E-28): Leitlinien und messbare Ziele, Startseite mit Begrüßung und großer Themenkarte, Lernen in Schritten mit Fortschritt und „Weiterlernen“, eine Frage pro Bildschirm mit sofortiger Rückmeldung, Ergebnis mit Erfolgsmoment, persönlicher Fortschritt und Serie, anonymes gemeinsames Ziel, Nachholen, Symbole und Lesezeit, Erinnerungen, leichter Zugang, Themenplan für Kommandanten (12 Monate, anlegen, bearbeiten, kopieren, ausblenden), Hilfen beim Anlegen, Laientest als Abnahme. Geändert: E-02, E-05, E-06, A-06, 0, 4.2, 5, 6. Demo v12, Testsuite (686 Prüfungen), Handbuch 1.11. |
| 1.14 | 23.11.2026 | Geändert B-10: Nach dem Speichern bleibt man im Mitgliederbereich in der bisherigen Ansicht; die Meldung bietet „Beitrag ansehen“ bzw. „Vorschau ansehen“ und „Rückgängig“. Neu B-23: Angemeldete sehen auch die öffentlichen Seiten mit Kopf und unterer Leiste des Mitgliederbereichs. Demo v13, Testsuite (693 Prüfungen), Handbuch 1.12. |
