# archidocs-form

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Makes the spreadsheet for uploading people to Archidocs from the rows of `people_all.xlsx` that **you have already checked**. In the form the names are modern (Татиана → Татьяна, Иоанн → Иван, «Петров» → Петрович); surnames stay as in the document.

## How to start

The skill starts by itself when your request fits it — just describe the task in Claude Code, for example:

- «Сделай форму Archidocs для части 4»
- «Я проверил строки, собери форму для загрузки»
- "Rebuild the Archidocs forms after my corrections in people_all."

Or start it directly: `/archidocs-form <part or scans>`.

**First step** (before this one): copying the scans into `people_all` — the [scans-to-people-all](../scans-to-people-all/README.md) skill.

## What you get

- A folder `archidocs_ready_to_send_part.N` with 4 scans and the form `form_output_…_part.N.xlsx`, one row per person: surname, name, patronymic, year of birth, document type and year, place, document title, archive reference, file name, comment.
- The list of names changed by modernization, so you can check them.
- Earlier parts rebuilt if you corrected their rows in `people_all` later.

You upload the form to Archidocs yourself.

## What it needs

- Python 3 and `openpyxl` (`pip3 install openpyxl`).

The instructions the agent follows are in [SKILL.md](SKILL.md).
