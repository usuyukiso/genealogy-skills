# source-page

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Makes or fixes one source page of the family-history website: an archive record, a book, a photo, a web page, a map. The page names the delo exactly as on its cover or in the archive inventory (shown in bordeaux), says where the scan lies, quotes the text verbatim in the original spelling with a label saying where the text comes from, explains doubtful readings and marks every guess as a guess.

## How to start

The skill starts by itself when your request fits it, for example:

- "Make a source page for the 1709 census, village Borovovo."
- "Add the 1786 map as a source."
- "Check A1048 against the scan."

Or start it directly: `/source-page <what>`.

## What you get

- A page `docs/sources/…/<ID>-<slug>.md` with a year-first title, a full citation with the delo's own title, the scan location (folder, file, page side), the transcript on «paper», reading notes; for 18th-century censuses and revisions — a comparison table with the other records of the same household (ages by year, birth year, who is missing, the compiler's conclusion).
- On a village's family list (confession list, census, revision tale, household book): links to the previous and the next known year of the same village, built automatically.
- The page registered in the sources index, the menu, the internal check list and the review log; the site built in strict mode.

## What it needs

- The MkDocs site `family_tree_github/` and the scripts of [genealogy-biography](../genealogy-biography/README.md) (`next_id.py`).

The instructions the agent follows are in [SKILL.md](SKILL.md).
