# archive-scan-search

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Searches a large folder of archive photos — thousands of frames from many delos, for example the RGIA fond 592 (Peasant Land Bank) photos from velikie.org — for a village, a volost or a surname. It machine-reads every frame, works out which delo each frame belongs to, finds the candidates, and then checks every candidate by looking at the scan itself.

## How to start

The skill starts by itself when your request fits it — just describe the task in Claude Code, for example:

- "Look for the village of Glazki in the Peasant Land Bank delos for Rzhev uyezd"
- "Read Gomel uyezd, our villages Glazovka and Rudnya-Bartolomeevskaya are there"
- "Make a list of the settlements mentioned in these delos"

Or start it directly: `/archive-scan-search <folder> <what to look for>`.

The first run on a new folder recognizes all frames, which takes time (about half an hour for 7,000 frames). This is done once; later searches in the same folder take minutes.

## What you get

- What was found: delo, year, one line about it, the frames to look at — each checked on the scan.
- What was not found, and why it may still be there (handwritten lists are read poorly by the machine).
- An index of the places mentioned in the delos, by volost — for future searches.
- An entry in the review log, including searches that found nothing, so the same folder is not searched again for the same thing. The website is not changed.

## What it needs

- macOS (the text recognition built into the system, Swift), Python 3.

The instructions the agent follows are in [SKILL.md](SKILL.md).
