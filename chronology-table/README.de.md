# chronology-table

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Liest eine chronologische Tabelle über eine Person — eine Zeile pro Lebensereignis (Geburten, Ehen, Todesfälle, Volkszählungen, Beichtlisten, Patenschaften, Umzüge, Standeswechsel) — und macht daraus eine bereinigte Faktenliste, jede Tatsache mit ihren Quellen: Archivsignaturen, Zellkommentare, Links zu Scans.

## Wie starten

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code, zum Beispiel:

- „Prüfe die Tabelle zu Lapina“
- „Was sagt die Tabelle über Grigoris Kinder?“
- „Schreibe die Biografie nach der Tabelle `sources/people_all.xlsx`“ — dann liest genealogy-biography die Tabelle mit diesem Skill.

Oder direkt starten: `/chronology-table <Datei>`.

## Was Sie bekommen

- Die Tabelle Blatt für Blatt ausgelesen, mit Zeilennummern, Zellkommentaren und Links.
- Eine Faktenliste pro Ereignis: Datum, Ort, Stand, Name wie im Dokument, genannte Personen, Alter, die Quelle jeder Tatsache.
- Fehler in der Tabelle selbst (fehlende Quelle, widersprüchliche Daten, Schreibfehler) — werden Ihnen gemeldet, nicht verborgen.

## Was er braucht

- Python 3 (nur Standardbibliothek). Liest `.ods`, `.xlsx`, `.csv`/`.tsv`.

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
