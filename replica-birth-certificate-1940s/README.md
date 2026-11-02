# replica-birth-certificate-1940s

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Part of the [genealogy-skills](../README.md) set.

Makes a **typed copy of a Soviet birth certificate of the war years** (about 1941–1946: NKVD USSR ZAGS form, a landscape sheet folded in two, series and number like «РТ № 952045»). It is not a scan but an HTML/CSS copy laid out like the original: the unfolded cover (front, and the back with the Goznak imprint and a passport stamp if there is one) and the inside with the same fields, the printed text and the handwriting in a script font. The copy goes on a document page of the website together with a verbatim transcript (handwriting in blue italics) and reading notes; at the bottom the page says which skill made it.

Example: [D1001 — birth certificate of Valeriy Pisarev, 1942](https://usuyukiso.github.io/family-history/sources/documents/D1001-svidetelstvo-o-rozhdenii-pisarev-valeriy-1942/).

## How to start

The skill starts by itself when your request fits it, for example:

- «Отрисуй свидетельство о рождении 1944 года по образцу бланка»
- "Make a replica of this 1940s birth certificate."

Or start it directly: `/replica-birth-certificate-1940s <scan file>`.

## What you get

- A document page `D####` with the copy of the form, the transcript, notes on dating and readings, linked to the people on it.
- The page added to the menu, the list of sources, the internal check list and the person pages.
- A list of uncertain readings (signatures, stamps, folds) for you to check on the scan.

## What it needs

- The scan (PDF, TIFF or JPEG). macOS renders PDFs with the built-in PDFKit.
- Once per site: the styles from [assets/replica.css](assets/replica.css), the fonts and two small MkDocs hooks (see SKILL.md).

The instructions the agent follows are in [SKILL.md](SKILL.md).
