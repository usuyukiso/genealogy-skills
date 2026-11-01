# scans-to-people-all

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Copies a confession list (or a metric book, or a similar parish register) from the scans into the spreadsheet `sources/people_all.xlsx`, sheet `people_all2` — one row per person, **exactly as written in the document** (Татиана, Иоанн, отчество «Петров»). Then it stops and waits for you to check the rows.

## How to start

The skill starts by itself when your request fits it — just describe the task in Claude Code, for example:

- «Внеси сканы 078–081 в people_all»
- «Оцифруй следующие четыре листа исповедной ведомости»
- "Transcribe these confession-list scans into the spreadsheet."

Or start it directly: `/scans-to-people-all <scans>`.

## What you get

- New rows in `people_all2`: surname, name, patronymic, age, year of birth, household (двор) number, the clerk's running numbers, relation («жена», «дети их»), page and scan file name.
- Words that are hard to read are **filled yellow** with a note «читается неуверенно (А / Б)» — you check them against the scan and remove the fill.
- Surnames or patronymics that are not written in the document are in italics.
- A short report: how many people on each leaf, how many doubtful readings.

**Next step:** after you have checked the rows, ask for the Archidocs form — that is the [archidocs-form](../archidocs-form/README.md) skill.

## What it needs

- Python 3 and `openpyxl` (`pip3 install openpyxl`).
- `people_all.xlsx` closed in LibreOffice/Excel while the skill writes to it.

The instructions the agent follows are in [SKILL.md](SKILL.md).
