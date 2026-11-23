# Umsetzungsplan Website Feuerwehr Piflas – bis Weihnachten 2026

23.11.2026 · Korbinian · Online-Fassung: https://claude.ai/artifact/9NeFg4e1F4VJwP21Mp3VRe · PDF: `Umsetzungsplan-bis-Weihnachten-2026.pdf`

## Auf einen Blick

Bis zum 23.12.2026 ist die ganze Website nach Lastenheft 1.19 gebaut und auf der Testseite geprüft. Die öffentliche Seite mit Beiträgen geht am **Samstag, 19.12.** live. Das sind gut vier Wochen ab dem Pitch – mit Claude Code machbar, wenn Phase 0 in der ersten Woche gelingt.

Der Code ist nicht der Engpass. Engpässe sind Zugänge (Hosting, DIVERA, Meta), Klärungen (Markt, Datenschutz) und die Zeit der Ehrenamtlichen für Prüfen und Inhalte. Deshalb wird alles fertig gebaut, aber drei Teile bekommen einen **Schalter im System-Bereich**. Sie gehen erst an, wenn ihre Klärung da ist:

| Teil | Gebaut bis | Geht live, sobald … |
| --- | --- | --- |
| Öffentliche Seiten, Beiträge, Freigabe, Konten, Mitmachen, Jubiläum | 13.12. | Abnahme und Rechtstexte fertig – Ziel 19.12. |
| Einsätze aus DIVERA (D-, W-) | 13.12. | der Markt zugestimmt hat (L-01) und der API-Zugang läuft |
| Instagram-Post (I-02 bis I-04) | 20.12. | Meta die App freigegeben hat |
| Lernen (E-) | 20.12. | Verantwortlicher und Rechtsgrundlage geklärt sind (L-15) |

Annahme: Eine Person aus dem Verein (Technik) steuert Claude Code mit etwa 10–15 Stunden pro Woche. Ohne diese Person ist der Zeitplan nicht zu halten.

## Am Donnerstag, 26.11. entscheiden

Ohne diese sieben Punkte startet die Umsetzung nicht. Am besten am Ende des Treffens gemeinsam abhaken.

- [ ] **Go oder kein Go** für die Umsetzung bis Weihnachten, auf Basis von Lastenheft 1.19 (danach eingefroren, Änderungen erst nach dem Go-live)
- [ ] **Betreuung (4.3):** Variante A mit zwei namentlich benannten Admins oder Variante B mit Dienstleister
- [ ] **Technik-Person**, die Claude Code steuert und 10–15 Std./Woche hat, plus eine Vertretung
- [ ] **Erstbesetzung der Rollen:** 3 Kommandanten, 2 Admins, Redaktion (Namen)
- [ ] **Wer spricht mit dem Markt Ergolding** (L-01) und bis wann – Ziel: Termin vor dem 11.12.
- [ ] **Wer liefert Inhalte** bis 11.12.: Impressum (Kommandant), Vorstandschaft, Jugendwart, Gründungsjahr, Förderbeitrag und PDFs, Fahrzeugdaten, Ortsteile (Lastenheft 5)
- [ ] **Fachperson Datenschutz** ansprechen (z. B. über den LFV Bayern) – für Rechtstexte und L-15

Direkt nach dem Treffen (bis So 29.11.):

- [ ] Zugang zum Hosting-Kundenbereich für die Technik-Person, Hosting gegen 4.1 prüfen (PHP 8.2, Cronjob, SMTP, Subdomain)
- [ ] GitHub-Organisation auf den Verein anlegen (A-07), Passwort-Tresor des Vereins einrichten
- [ ] Bei DIVERA anfragen: Ist der API-Zugang in unserer Stufe enthalten?
- [ ] Instagram auf professionelles Konto umstellen, Meta-Entwicklerkonto auf den Verein anlegen
- [ ] Joomla komplett sichern, Übergangsseite hochladen

Zugangsdaten gehen nie in den Chat, ins Projekt oder ins Repository – nur in den Tresor und auf den Server.

## Wochenplan

Jede Woche endet mit einer Abnahme am Handy auf der Testseite, meist Samstagvormittag. Erst danach beginnt der nächste Block. Phasen wie im Lastenheft (Abschnitt 6).

| Woche | Was gebaut wird (Lastenheft-IDs) | Verein liefert | Abnahme |
| --- | --- | --- | --- |
| **KW 48** · 26.–29.11. | Pitch, Entscheidungen. Repository mit CLAUDE.md, Testseite (Staging) eingerichtet | Zugänge, Rollenliste, Ansprechpersonen | Testseite erreichbar, passwortgeschützt |
| **KW 49** · 30.11.–6.12. | Phase 1: Rollen, Einladungen, 2-Faktor, Verlauf (B-01 bis B-08, E-01, E-10, N-05). Phase 2a: Theme und alle öffentlichen Seiten (F-01 bis F-12, C-, S-, J-) | Texte und Fotos für Verein, Fahrzeuge, Jugend; Termin beim Markt vereinbart | Sa 5.12.: jede Rolle kann genau das, was in der Tabelle steht; Seiten am Handy geprüft |
| **KW 50** · 7.–13.12. | Phase 2b: Beiträge, Freigabe, Inhalte, Editor, Seiten pflegen, Fotos, System-Bereich, Rückgängig (B-09 bis B-23, W-, A-01 bis A-03). Phase 4: DIVERA mit Einsatz von Hand (D-01 bis D-09), Schalter aus | Redaktion pflegt erste Inhalte auf der Testseite; DIVERA-Schlüssel auf dem Server | Sa 12.12.: Testalarm erzeugt in 15 Min. einen korrekten, datensparsamen Entwurf; Laientest Teil 1 |
| **KW 51** · 14.–20.12. | Phase 5: Instagram (I-), Schalter aus. Phase 6: Lernen (E-), Schalter aus. Rechtstexte, Überwachung (M-), Handbuch mit Fotos der echten Seite (A-06) | Rechtstexte von der Fachperson geprüft; 3 Mitglieder für den Laientest | Do 17.12.: Laientest (A-09), Wiederherstellung getestet (A-08). **Sa 19.12.: Go-live** |
| **KW 52** · 21.–23.12. | Nur Fehler beheben, nichts Neues | Zwei Admins erreichbar | Mi 23.12.: eine Woche ohne kritische Fehler → Pause bis 6.1. |
| **Januar** | Schalter an für DIVERA, Instagram, Lernen – je nach Klärung. Schulungsabend, erstes Lernthema Februar | Markt, Meta, Datenschutz | Je Schalter eine kurze Abnahme |

Go-live am Samstag statt kurz vor Heiligabend: So bleiben vier Werktage Puffer, und die Admins sind nicht über die Feiertage im Stress.

## Wer macht was

In den vier Wochen fallen zusammen etwa 80–100 Stunden an, die meisten bei der Technik-Person. Die Stunden sind geschätzt (Annahme).

| Rolle | Aufgaben | Std./Woche | Name |
| --- | --- | --- | --- |
| Technik-Person | Claude Code steuern, Pull Requests prüfen, Testseite pflegen, Zugänge einrichten, Go-live | 10–15 | [Platzhalter] |
| Vertretung Technik / 2. Admin | Abnahmen mitmachen, Wiederherstellung üben, Go-live begleiten | 2–3 | [Platzhalter] |
| 1. Kommandant | Entscheidungen, Freigaben testen, Tipp-Kalender und Beispiel-Lernthemen fachlich prüfen, Gespräch mit dem Markt | 2–3 | [Platzhalter] |
| Redaktion (2–3 Personen) | Texte und Fotos liefern, erste Beiträge auf der Testseite | 3–5 je Person | [Platzhalter] |
| Vorstand | Vereinstexte, Förderbeitrag und PDFs, Verträge (Hosting, Auftragsverarbeitung) | 1–2 | [Platzhalter] |
| Laientest | 3 Mitglieder ohne IT-Kenntnisse, je 30 Minuten am 17.12. | einmalig | [Platzhalter] |

Kurze Abstimmung jeden Samstag nach der Abnahme, 30 Minuten, auch per Videoanruf.

## So arbeitet ihr mit Claude Code

Claude Code schreibt den Code, der Verein prüft und entscheidet. Grundlage sind CLAUDE.md, der Start-Prompt aus dem Lastenheft (Abschnitt 7) und die 10 Arbeitspakete in docs/start/ARBEITSPAKETE.md.

1. **Ein Arbeitspaket je Sitzung:** z. B. „Phase 2b: B-09 bis B-12“. Claude Code stellt erst seinen Plan und offene Fragen vor, dann wird gebaut.
2. **Eigener Branch und Pull Request** je Paket, mit der Liste der erfüllten IDs.
3. **Automatische Prüfung** bei jedem Pull Request: PHP-Tests je Rolle, Code-Stil und die aus der Demo übertragenen Playwright-Prüfungen (test_app.py und test_security.py; Zuordnung in ABDECKUNG.md). Rot heißt: nicht zusammenführen.
4. **Automatisch auf die Testseite** nach dem Zusammenführen.
5. **Abnahme am Handy** durch zwei Personen, gegen die Demo als Vorlage.
6. **Änderungswünsche** während der vier Wochen nur als Liste sammeln. Umgesetzt werden sie erst nach dem Go-live, außer bei Fehlern und rechtlichen Punkten.

Auf die echte Website kommt nur, was auf der Testseite abgenommen ist. Auf der Testseite liegen nie echte Mitgliederdaten (4.1).

## Risiken und Plan B

Das größte Risiko ist Zeit bei den Ehrenamtlichen, nicht die Technik. Für jedes Risiko steht fest, was dann passiert.

| Risiko | Folge | Plan B |
| --- | --- | --- |
| Keine Technik-Person mit genug Zeit | Plan nicht zu halten | Go-live auf Ende Januar verschieben; Übergangsseite kündigt Jubiläumstermine an (2.10) |
| Hosting erfüllt 4.1 nicht | Phase 1 stockt | Tarif beim Hoster wechseln oder Variante B (4.3) |
| DIVERA-API nicht in unserer Stufe | Keine automatischen Einsätze | Nur „Einsatz von Hand“ (D-09), Upgrade später entscheiden |
| Markt stimmt noch nicht zu (L-01) | Keine Einsatzberichte | Go-live ohne Einsätze, Schalter bleibt aus |
| Meta-Freigabe dauert | Kein Instagram-Post | Website-Vorschau mit Link zum Profil; Posten weiter von Hand |
| L-15 ungeklärt | Keine Lernergebnisse speichern | Lernen bleibt aus, erstes Thema erst nach Klärung |
| Inhalte fehlen am 11.12. | Leere Seiten | Nur Seiten mit Inhalt ins Menü; Rest im Januar nachziehen |
| Kritischer Fehler nach Go-live | Website gestört | Backup vom Vortag zurückspielen (A-08), Übergangsseite wieder aktivieren |

Am 12.12. fällt die Entscheidung, ob der Go-live am 19.12. bleibt oder in den Januar wandert.

## Checkliste Go-live (Sa 19.12.)

Live geht es nur, wenn jeder Punkt abgehakt ist.

- [ ] Alle Prüfungen grün, Laientest bestanden (A-09)
- [ ] Impressum und Datenschutzerklärung vollständig und von der Fachperson geprüft (L-07, L-08)
- [ ] Verträge zur Auftragsverarbeitung mit Hoster (und DIVERA, falls aktiv) unterschrieben
- [ ] Zwei Admins mit 2-Faktor, Zugänge im Vereins-Tresor (A-07, A-08)
- [ ] Backup läuft täglich, Wiederherstellung einmal getestet
- [ ] Überwachung aktiv, Meldungen kommen bei beiden Admins an (M-01, M-02)
- [ ] Keine externen Anfragen, keine Cookies (N-01, L-09)
- [ ] Alte Joomla-Adressen leiten weiter (F-13), Joomla-Sicherung liegt im Tresor
- [ ] Handbuch mit Fotos der echten Seite im Mitgliederbereich verlinkt (B-13)
- [ ] Schalter für DIVERA, Instagram und Lernen stehen bewusst auf an oder aus
- [ ] Domain umgestellt, Zertifikat aktiv, Startseite am Handy geprüft

Offene Punkte, die keinen Go-live blockieren, stehen im Lastenheft, Abschnitt 5.
