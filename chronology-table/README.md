# chronology-table

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Reads a chronology spreadsheet about one person — one life event per row (births, marriages, deaths, censuses, confession lists, baptisms as godparent, moves, status changes) — and turns it into a clean list of facts, each with its sources: archive references, cell comments, links to scans.

## How to start

The skill starts by itself when your request fits it — just describe the task in Claude Code, for example:

- "Check the table on Lapina."
- "What does the table say about Grigory's children?"
- "Write a biography from the table `sources/people_all.xlsx`" — then genealogy-biography uses this skill to read the table.

Or start it directly: `/chronology-table <file>`.

## What you get

- The table read out sheet by sheet, with row numbers, cell comments and hyperlinks.
- A list of facts per event: date, place, status, the name as written, people mentioned, ages, the source of each fact.
- Problems in the table itself (missing sources, conflicting dates, misspellings) — reported to you, not hidden.

## What it needs

- Python 3 (standard library only). Reads `.ods`, `.xlsx`, `.csv`/`.tsv`.

The instructions the agent follows are in [SKILL.md](SKILL.md).
