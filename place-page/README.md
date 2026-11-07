# place-page

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Makes or tidies a village (settlement) page of the family-history website so that it reads in time order: the church parish by period first, then the administrative division before 1917 by period (the 18th-century губа, then uyezd and volost), a table of every mention of the village in documents by year — how it was named and in which губа — and the compiler's conclusions (for example, an older name of the village) under their own headings that source pages can link to.

## How to start

The skill starts by itself when your request fits it, for example:

- "On the Gorelik page, list all mentions by year."
- "Make a page for the village of Borovovo."
- "Put the church parish first on the Makovitsy page."

Or start it directly: `/place-page <village>`.

## What you get

- A page `docs/places/PLC…-<slug>.md` in a fixed order: first paragraph, church parish, division before 1917 by period, mentions by year, conclusions, after 1917, people, sources.
- The places index and the menu kept in sync; the site built in strict mode.

## What it needs

- The MkDocs site `family_tree_github/` and the scripts of [genealogy-biography](../genealogy-biography/README.md) (`next_id.py`).

The instructions the agent follows are in [SKILL.md](SKILL.md).
