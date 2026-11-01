# Genealogy skills

Languages: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

**A set of Agent Skills for Claude Code for documents-first family history research on the Russian Empire and the USSR:** reading archive scans and parish registers, digitizing them into a spreadsheet and an Archidocs upload form, and writing source-cited ancestor biographies for a family-history website.

Each skill is a folder with a `SKILL.md` (instructions for the agent), helper scripts and its own README. You don't run them by hand: you describe your task in plain words, and Claude starts the skill that fits it. The skills hand work to each other, so it helps to know the chain below.

---

## The skills

| Skill | What it does | Ask, for example |
|---|---|---|
| [archive-scan-search](archive-scan-search/README.md) | Searches a large folder of archive scans (thousands of frames, many delos): OCR of every frame, frame → delo by the microfilm cards, search by word fragments, checking every hit on the scan, an index of places | «Поищи деревню Глазки в делах Крестьянского банка по Ржевскому уезду» |
| [metric-book-index](metric-book-index/README.md) | Reads a whole metric book frame by frame and builds an internal index of every birth, marriage and death, with ★ for the people searched for; can be resumed | «Дочитай метрики Дрогачева за 1892 год» |
| [scans-to-people-all](scans-to-people-all/README.md) | Transcribes a confession list or register into `people_all.xlsx` (sheet `people_all2`), one row per person, in the document's spelling; doubtful readings marked yellow; then stops for your check | «Внеси сканы 078–081 в people_all» |
| [archidocs-form](archidocs-form/README.md) | Builds the Archidocs upload form from the rows you have checked, with modern names and patronymics; keeps earlier parts in sync with your later corrections | «Сделай форму Archidocs для части 4» |
| [chronology-table](chronology-table/README.md) | Reads a chronology spreadsheet (one life event per row, `.ods/.xlsx/.csv`) into a clean list of facts with sources, comments and links | used by genealogy-biography; or «Проверь таблицу по Лапиной» |
| [genealogy-biography](genealogy-biography/README.md) | Writes a person page of the website: the life story with verbatim quotes, one page per source document, the name index, links to places; builds the site to check links | «Напиши биографию Якова Писарева» |

## How they fit together

```
 find records                    digitize                         publish
 ─────────────                   ────────                         ───────
 archive-scan-search ─┐
   (big scan folders) │          scans-to-people-all
 metric-book-index  ──┼── finds ──►  (people_all2)                chronology-table
   (a parish book)    │               │                                │
                      │          you check the rows                    ▼
                      │               ▼                          genealogy-biography
                      │          archidocs-form                  (person + source pages)
                      │          (upload form)                         ▲
                      └──────── a find about a family member ─────────┘
                                 (only when you ask)
```

- **Search skills don't change the website.** archive-scan-search and metric-book-index write internal files (indexes, notes, the review log). A find becomes a site page only when you ask, and then genealogy-biography writes it.
- **The spreadsheet is checked by you between the two digitizing steps.** scans-to-people-all stops after writing the rows; archidocs-form works only from rows you have checked.
- **Everything reviewed is logged,** including searches that found nothing, in `family_tree_github/internal/checks/reviewed_documents.md`. Every skill checks this log before searching and adds to it after, so the same delo is not searched twice.
- **Open questions and conflicts** between documents go to `research_open_questions.md`.

## Rules shared by all skills

- Nothing is invented: names, dates, kinship, archive references and quotes come only from documents. Where the records are silent, the text says so.
- Quotes are verbatim in the original spelling; uncertain words are marked `[?]`, illegible places `[…]`; machine-recognized text (OCR) is used to find a place in the scans, never quoted without reading the scan.
- Kinship is proven link by link; a patronymic, a shared surname or a village is not proof; namesakes stay separate people until documents tell them apart.
- A missing record is not proof that the event did not happen.
- Inferences are labelled as hypotheses, with what could confirm or refute them.

## Requirements

- [Claude Code](https://claude.com/claude-code) (or another runtime with Agent Skills).
- Python 3. The spreadsheet skills (scans-to-people-all, archidocs-form) need `openpyxl`; the others use only the standard library.
- macOS for archive-scan-search and the scan-cropping helpers (Swift + the system Vision OCR).
- The project layout these skills were written for (paths are inside the `SKILL.md` files; change them for another project):

```
<project>/
  .claude/skills/          ← these skills
  family_tree_github/      ← MkDocs Material website: docs/people, docs/sources, docs/places,
                             internal/checks (review log, place indexes), internal/metrics (book indexes)
  sources/                 ← scans and spreadsheets (people_all.xlsx, chronology tables)
  research_open_questions.md
```

## Install

You need [Git](https://git-scm.com/downloads), Python 3 and [Claude Code](https://claude.com/claude-code) (or Codex). For the two spreadsheet skills also install `openpyxl` once:

```bash
pip3 install openpyxl
```

1. **Download the repository:**

   ```bash
   git clone https://github.com/usuyukiso/genealogy-skills
   ```

2. **Copy the skills you need into the `skills` folder.** Each skill is a folder (`genealogy-biography`, `metric-book-index`, …); copy the whole folder.
   - Claude Code: `.claude/skills/` inside your project folder (create it if it doesn't exist).
   - Codex: `~/.codex/skills/`.

   Copy the skill folders themselves, not the whole `genealogy-skills` folder. genealogy-biography needs chronology-table — copy both.

3. **Restart Claude Code.** Type `/` — the skills appear in the list. How to start each skill and what to ask is in its own README (links in the table above).

To update later, run `git pull` in the downloaded folder and copy the skills again.

## Usage

1. Open a terminal **in your project folder** (where `family_tree_github/` and `sources/` are) and start Claude Code: `claude`.
2. Describe the task in your own words, in any language. A skill starts by itself when your request fits it. Examples:
   - «Нужно прочитать и оцифровать метрики» → metric-book-index
   - «Поищи деревню Глазки в делах Крестьянского банка по Ржевскому уезду» → archive-scan-search
   - «Внеси сканы 078–081 в people_all» → scans-to-people-all; you check the rows; then «Сделай форму Archidocs для части 4» → archidocs-form
   - «Напиши биографию Якова Писарева по таблице» → genealogy-biography (with chronology-table)
3. To start a particular skill yourself, begin the message with `/` and its name: `/metric-book-index дочитай Дрогачево`.
4. Long jobs (OCR of thousands of frames, a whole metric book) run in steps; the skills save progress in their files, so you can stop and later say «продолжи» — work resumes where it stopped.
5. Read the agent's report at the end: what was found, what was not found, what needs your check. Nothing is published on the website unless you ask for it.

## License

[MIT](LICENSE): free to use, change and share, including commercially; keep the copyright notice.
