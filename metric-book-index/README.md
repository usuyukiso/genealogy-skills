# metric-book-index

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Reads a whole parish metric book (births, marriages, deaths) from the scans, frame by frame, and writes down **every** entry — not only the ones you are looking for. The result is an internal index: later questions like "who was the godfather?" or "when did this child die?" are answered from it without opening the scans again. The people you are searching for are marked ★.

## How to start

The skill starts by itself when your request fits it — just describe the task in Claude Code, for example:

- "The Drogachevo metric books need to be read and digitized."
- "Finish reading the Drogachevo metric books, starting from 1892."
- "Find every mention of the Kharlamovs and of anyone with the patronymic Anisimovich in this book."

Or start it directly: `/metric-book-index <book or folder>`.

Long books are read in portions. If you stop, say "continue" next time — the skill continues from the frame where it stopped.

## What you get

- An index file: a section per year, tables of births, marriages and deaths — frame, leaf, record number, date, village, parents or bride and groom, godparents or witnesses, cause of death — with cross-references («умер … (кадр 260)», "died … (frame 260)").
- A notes file: what was searched for, what was found (★) by family, conflicts between records, what to re-read or to get next.
- Monthly and yearly totals checked against the summary at the end of the book.
- Entries in the review log and the list of open questions. The website is not changed.

## What it needs

- The scans in a folder; macOS for cropping and zooming the scans (Swift, included).

The instructions the agent follows are in [SKILL.md](SKILL.md).
