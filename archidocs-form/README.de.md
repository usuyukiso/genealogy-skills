# archidocs-form

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Erstellt die Tabelle zum Hochladen von Personen nach Archidocs aus den Zeilen von `people_all.xlsx`, die **Sie bereits geprüft haben**. Im Formular stehen moderne Namen (Татиана → Татьяна, Иоанн → Иван, «Петров» → Петрович); Nachnamen bleiben wie im Dokument.

## Wie starten

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code, zum Beispiel:

- „Erstelle das Archidocs-Formular für Teil 4“
- „Ich habe die Zeilen geprüft, baue das Upload-Formular“
- „Baue die Archidocs-Formulare nach meinen Korrekturen in people_all neu“

Oder direkt starten: `/archidocs-form <Teil oder Scans>`.

**Erster Schritt** (davor): Übertragen der Scans in `people_all` — der Skill [scans-to-people-all](../scans-to-people-all/README.de.md).

## Was Sie bekommen

- Einen Ordner `archidocs_ready_to_send_part.N` mit 4 Scans und dem Formular `form_output_…_part.N.xlsx`, eine Zeile pro Person: Nachname, Vorname, Vatersname, Geburtsjahr, Art und Jahr des Dokuments, Ort, Dokumenttitel, Archivsignatur, Dateiname, Kommentar.
- Die Liste der bei der Modernisierung geänderten Namen, damit Sie sie prüfen können.
- Neu gebaute frühere Teile, falls Sie deren Zeilen später in `people_all` korrigiert haben.

Das Hochladen nach Archidocs erledigen Sie selbst.

## Was er braucht

- Python 3 und `openpyxl` (`pip3 install openpyxl`).

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
