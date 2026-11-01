# archive-scan-search

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Durchsucht einen großen Ordner mit Archivaufnahmen — Tausende Aufnahmen aus vielen Akten, etwa die Fotos des RGIA, Fonds 592 (Bauernagrarbank) von velikie.org — nach einem Dorf, einer Wolost oder einem Nachnamen. Er liest alle Aufnahmen maschinell, ermittelt, zu welcher Akte jede Aufnahme gehört, findet Kandidaten und prüft dann jeden Kandidaten am Scan selbst.

## Wie starten

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code, zum Beispiel:

- „Suche das Dorf Glaski in den Akten der Bauernbank für den Kreis Rschew“
- „Lies den Kreis Gomel, dort liegen unsere Dörfer Glasowka und Rudnja-Bartolomejewskaja“
- „Erstelle eine Liste der Orte, die in diesen Akten vorkommen“

Oder direkt starten: `/archive-scan-search <Ordner> <was gesucht wird>`.

Der erste Lauf auf einem neuen Ordner erkennt alle Aufnahmen; das dauert (etwa eine halbe Stunde für 7.000 Aufnahmen). Das geschieht nur einmal; spätere Suchen im selben Ordner dauern Minuten.

## Was Sie bekommen

- Was gefunden wurde: Akte, Jahr, eine Zeile dazu, die anzusehenden Aufnahmen — alles am Scan geprüft.
- Was nicht gefunden wurde und warum es trotzdem vorhanden sein kann (handschriftliche Listen liest die Maschine schlecht).
- Ein Register der in den Akten genannten Orte, nach Wolost — für spätere Suchen.
- Ein Eintrag im Durchsichtsprotokoll, auch für Suchen ohne Fund, damit derselbe Ordner nicht erneut durchsucht wird. Die Website wird nicht verändert.

## Was er braucht

- macOS (die systemeigene Texterkennung, Swift), Python 3.

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
