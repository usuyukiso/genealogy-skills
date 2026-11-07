# place-page

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Erstellt oder ordnet die Seite eines Dorfes (Ortes) der Familiengeschichts-Website so, dass sie zeitlich gelesen werden kann: zuerst die Kirchengemeinde nach Zeiträumen, dann die Verwaltungsgliederung vor 1917 nach Zeiträumen (die „Guba“ des 18. Jahrhunderts, dann Kreis und Wolost), eine Tabelle aller Erwähnungen des Dorfes in Dokumenten nach Jahren — wie es genannt wird und in welcher Guba — und die Schlüsse des Verfassers (zum Beispiel ein älterer Name des Dorfes) unter eigenen Überschriften, auf die Quellenseiten verweisen können.

## Wie starten

Der Skill startet von selbst, wenn die Bitte passt, zum Beispiel:

- „Liste auf der Seite von Gorelik alle Erwähnungen nach Jahren auf.“
- „Lege eine Seite für das Dorf Borowowo an.“
- „Setze die Kirchengemeinde an den Anfang der Seite von Makowizy.“

Oder direkt: `/place-page <Dorf>`.

## Was herauskommt

- Eine Seite `docs/places/PLC…-<slug>.md` in fester Reihenfolge: erster Absatz, Kirchengemeinde, Gliederung vor 1917 nach Zeiträumen, Erwähnungen nach Jahren, Schlüsse, nach 1917, Personen, Quellen.
- Ortsverzeichnis und Menü abgeglichen; Website im strengen Modus gebaut.

## Was es braucht

- Die MkDocs-Website `family_tree_github/` und die Skripte von [genealogy-biography](../genealogy-biography/README.de.md) (`next_id.py`).

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
