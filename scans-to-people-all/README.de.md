# scans-to-people-all

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Überträgt eine Beichtliste (oder ein Kirchenbuch oder ein ähnliches kirchliches Register) von den Scans in die Tabelle `sources/people_all.xlsx`, Blatt `people_all2` — eine Zeile pro Person, **genau wie im Dokument geschrieben** (Татиана, Иоанн, Vatersname «Петров»). Danach hält er an und wartet, bis Sie die Zeilen geprüft haben.

## Wie starten

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code, zum Beispiel:

- „Trage die Scans 078–081 in people_all ein“
- „Digitalisiere die nächsten vier Blätter der Beichtliste“
- „Übertrage diese Scans der Beichtliste in die Tabelle“

Oder direkt starten: `/scans-to-people-all <Scans>`.

## Was Sie bekommen

- Neue Zeilen in `people_all2`: Nachname, Vorname, Vatersname, Alter, Geburtsjahr, Hofnummer, die laufenden Nummern des Schreibers nach Geschlecht, Verwandtschaft («жена», «дети их»), Blatt und Dateiname des Scans.
- Schwer lesbare Wörter sind **gelb hinterlegt** mit dem Vermerk «читается неуверенно (А / Б)» („unsicher gelesen“) — Sie prüfen sie am Scan und entfernen die Markierung.
- Nach- oder Vatersnamen, die im Dokument selbst nicht stehen, sind kursiv.
- Ein kurzer Bericht: wie viele Personen pro Blatt, wie viele unsichere Lesungen.

**Nächster Schritt:** Wenn Sie die Zeilen geprüft haben, bitten Sie um das Archidocs-Formular — das ist der Skill [archidocs-form](../archidocs-form/README.de.md).

## Was er braucht

- Python 3 und `openpyxl` (`pip3 install openpyxl`).
- `people_all.xlsx` muss in LibreOffice/Excel geschlossen sein, solange der Skill hineinschreibt.

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
