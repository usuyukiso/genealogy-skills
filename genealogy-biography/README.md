# Genealogy Biography — a documents-first family history skill

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

**An Agent Skill for Claude Code that writes the biography of an ancestor from archival records and publishes it as a page of a family-history website.** The input is usually a chronology table (one life event per row: births, marriages, deaths, censuses, confession lists, baptisms as godparent, moves, status changes), but it can also be notes, links or scans. The output is a readable life story in which every fact has a source and every quote is verbatim, together with one page per source document.

The skill is built for a Russian-language [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site about families from the Russian Empire and the USSR. Its instructions are in English; the text it writes for the site is in Russian (or in the language you ask for), and record quotes keep their original pre-reform spelling.

---

## What it does

- **Biography page.** A narrative of the person's life by periods, plus a family list, a chronology table, notes on discrepancies between documents and a separate block of research notes for hypotheses.
- **Source pages.** One page per document with a full archive reference (archive, fond, opis, delo, list), the scan location, the form's column headings, the verbatim text of the record and notes on uncertain readings. Pages are shared between biographies: a document cited by several people has one page.
- **Verbatim quotes.** Records are quoted exactly, with original spelling. Each source page says where the text comes from: read from the scan, the compiler's own transcription, a transcription published by other researchers (with a link) or Yandex Archive OCR. Uncertain words are marked `[?]`, illegible places `[…]` or `[неразборчиво]`.
- **Yandex Archive helper.** `scripts/yandex_archive.py` pulls the recognized text and the catalog reference of a scan from Yandex Archive and searches the archive. OCR text is treated as a draft: it is checked against the scan and corrections are shown.
- **Stable IDs.** Every page has a permanent ID (`P1000` person, `A1000` archive record, `B` book, `F` photo, `W` web page, `PLC` place…). `scripts/next_id.py` finds the next free ID and checks whether a document already has a page, so nothing is duplicated.
- **People index.** Everyone named in a record about the person — relatives, godparents, witnesses, neighbours, priests — gets a line in the shared name index, women under every known surname.
- **Places.** People are linked to settlement pages; the pre-1917 administrative division is quoted from documents with the year of the source.
- **Strict build.** The site is built in strict mode at the end, so a broken link or an unknown ID stops the work until it is fixed.

## Research rules it follows

- **Nothing is invented.** No names, dates, relatives, archive references or quotes that are not in the input. Where the records are silent, the text says so.
- **Every fact has a source,** and the link leads to the exact record, not to an overview page.
- **Inferences are labelled.** A hypothesis goes into the research notes and starts with «Предположение (не подтверждено документами)» ("Assumption, not confirmed by documents"), with arguments for and against and what could confirm it.
- **Kinship is proven link by link.** Each parent–child and spouse link has its own sources; a distant ancestor is proven only through a chain of proven links. Copies of one record are one source. A patronymic names the father but does not show which man he was; a shared surname, village or household is not evidence of kinship.
- **Namesakes stay separate.** Two people with the same name and patronymic in one village are kept apart until records distinguish them.
- **Disagreements are shown, not hidden.** Both versions are given side by side, with who supplied the information and when.
- **A missing record is not proof** that the event did not happen; the page says which books and years were searched.
- **Every archive review is logged,** including negative results, in an internal registry (`internal/checks/reviewed_documents.md`), so nothing is searched twice years later.
- **The working table is never mentioned** on the site: readers see only real sources.

## Requirements

- [Claude Code](https://claude.com/claude-code) or another runtime that supports Agent Skills.
- Python 3 (standard library only).
- A site with the expected layout: `family_tree_github/` with `docs/people/`, `docs/sources/{archives,books,photos,websites}/`, `docs/places/`, the indexes and `mkdocs.yml`, plus the ID-link hook (`hooks/id_links.py`). The paths are written into the skill; to use it with another site, edit the table «Where the output goes» in `SKILL.md` and the `DOCS` path in `scripts/next_id.py` (or set the `DOCS` environment variable).
- Optional: the **chronology-table** skill, which reads `.ods`, `.xlsx` and `.csv` chronology tables and is loaded automatically when the input is a table.

## Install

The skill is part of the [genealogy-skills](https://github.com/usuyukiso/genealogy-skills) set. Clone the set and copy this folder together with **chronology-table**, which it uses for tables (the folder name is the skill name):

```bash
git clone https://github.com/usuyukiso/genealogy-skills ~/genealogy-skills
cp -r ~/genealogy-skills/genealogy-biography ~/genealogy-skills/chronology-table <project>/.claude/skills/
```

or into your personal skills (`~/.claude/skills/`) to use them across projects. See the set's README for the other skills and how they work together.

## Use

The skill starts by itself when your request fits it — just describe the task in Claude Code (or start it directly with `/genealogy-biography`), for example:

- *"Write a biography of Evdokiya Lapina from the table `sources/people_all.xlsx`."*
- *"Update the page of Grigory Pisarev: add the 1943 loss report and quote it."*
- *"Write a biography from these three metric-book scans on Yandex Archive."*

The helpers can also be run by hand from the project root:

```bash
python3 .claude/skills/genealogy-biography/scripts/next_id.py next A A P          # next free IDs
python3 .claude/skills/genealogy-biography/scripts/next_id.py find "23И, оп. 2, д. 24"  # already on the site?
python3 .claude/skills/genealogy-biography/scripts/yandex_archive.py page "<scan url>"
python3 .claude/skills/genealogy-biography/scripts/yandex_archive.py search "Лапина Корсаковск"
```

At the end the agent reports which pages it wrote and reused, how many people were added to the index, which records are quoted from scans and which have no available text, and any discrepancies worth checking.

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | The instructions the agent follows |
| `references/terms.md` | Archive abbreviations (ГИАСО, РГИА ДВ…) and record terms, extended as new ones appear |
| `scripts/next_id.py` | Next free ID, duplicate search, list of all IDs |
| `scripts/yandex_archive.py` | Recognized text and catalog reference of a Yandex Archive scan; archive search |

## Limitations

- Machine-recognized text (Yandex Archive OCR) contains errors in names, numbers and dates; the skill marks it and asks for checking against the scan.
- The skill writes what the input supports. It does not search archives on its own beyond Yandex Archive; finding new records is a separate research task.
- Living people: the site is public, so add only what the family agrees to publish.

## License

[MIT](LICENSE): free to use, change and share, including commercially; keep the copyright notice.
