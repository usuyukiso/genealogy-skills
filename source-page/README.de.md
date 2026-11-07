# source-page

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Erstellt oder korrigiert eine Quellenseite der Familiengeschichts-Website: Archiveintrag, Buch, Foto, Webseite, Karte. Die Seite nennt die Akte genau wie auf ihrem Umschlag oder im Archivverzeichnis (in Bordeaux hervorgehoben), sagt, wo der Scan liegt, zitiert den Text wörtlich in alter Rechtschreibung mit einem Vermerk, woher er stammt, erklärt unsichere Lesungen und kennzeichnet jede Vermutung als Vermutung.

## Wie starten

Der Skill startet von selbst, wenn die Bitte passt, zum Beispiel:

- „Lege eine Quellenseite zur Volkszählung 1709, Dorf Borowowo, an.“
- „Füge die Karte von 1786 als Quelle hinzu.“
- „Prüfe A1048 am Scan.“

Oder direkt: `/source-page <was>`.

## Was herauskommt

- Eine Seite `docs/sources/…/<ID>-<slug>.md`: Titel mit dem Jahr vorn, vollständige Angabe mit dem Titel der Akte, Lage des Scans (Ordner, Datei, Seite), Text „auf Papier“, Erläuterungen zur Lesung.
- Die Seite ist im Quellenregister, im Menü, in der internen Prüfliste und im Protokoll der gesichteten Akten eingetragen; die Website ist im strengen Modus gebaut.

## Was es braucht

- Die MkDocs-Website `family_tree_github/` und die Skripte von [genealogy-biography](../genealogy-biography/README.de.md) (`next_id.py`).

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
