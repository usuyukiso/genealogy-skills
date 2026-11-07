---
name: chronology-table
description: Read a genealogical chronology spreadsheet (.ods, .xlsx, .csv) where each row is a dated life event of one person — births, marriages, deaths, censuses, confession lists, baptisms as godparent, moves, status changes — and turn it into a clean list of facts with their sources (cell comments, hyperlinks, archive codes, Yandex Archive links). Use whenever a task takes such a table as input — writing or updating a biography from it, checking it, extracting relatives or sources, or when the user points at a spreadsheet of events about a person.
---

# Reading a chronology table

The table describes one person's life, one event per row, compiled from archival
documents (metric books, confession lists, censuses, court/admin files).

## 1. Dump the table

```bash
python3 .claude/skills/chronology-table/scripts/read_table.py "<file>" [--sheet NAME]
```

The script (stdlib only, no pandas needed) prints each sheet as a Markdown table with
spreadsheet row numbers, plus cell comments and hyperlinks. Long search-snippet URLs are
shortened to the page address. If the user didn't name a file, use the single
.ods/.xlsx/.csv in the working directory; if there are several, ask which one.
A `.~lock.<name>#` file next to it only means the file is open in LibreOffice — the
script still reads the last saved version, so mention that unsaved edits won't be seen.

## 2. Understand the columns

Column names vary between tables; map them by meaning. Typical layout (Russian headers):

| Column | Meaning | How to use it |
|---|---|---|
| Год / Месяц / Число | Date (year, month, day) | Day may be a range ("сент14-окт10") — keep it as a range |
| Event type | Kind of event | May be empty — infer it from the comment or the source code (e.g. `..._became_peasant_...`) |
| Country / Region / City/Town/Place | Location | Use historical names as written (Ярославская губ., Сахалин) |
| Приход/церковь | Parish / church | Name it when describing church records |
| Звание | Social / legal status at the time | Track how it changes — it is often the spine of the story |
| Кто | Canonical name of the person | Use as the subject's name |
| ФИО как в документах | Name as spelled in that document | Spelling variants — mention notable ones, don't "fix" them silently |
| Photo / Doc | Attached images/documents | Mention if present |
| Комментарий | Transcriptions and notes | Richest source of facts: relatives, ages, household members |
| Источник | Source: archive reference code and/or URL | Goes into the source list |
| Комментарий2 | Extra notes, often a URL to the scanned page | Also a source link for that row |

## 3. Extract facts per row

For each row note: date, place, status, name form, people mentioned (spouse, children,
godchildren, household members), ages stated, the transcription text if any, and every
source attached to it (`Источник`, `Комментарий2`, hyperlinks, cell comments). Sources can
also be implied by the event itself (an event type "Сахалинская перепись Чехова" is a
source even if `Источник` is empty). Keep the spreadsheet row number with each fact so
it can be traced back.

Then reconcile across rows:
- **Ages vs. birth year.** Compute implied birth years from every stated age. If they
  disagree (e.g. census says 35 in 1890 → ~1855, death record says 70 in 1921 → ~1851),
  keep the range and note which documents disagree. Old records rounded ages freely.
- **Name variants.** Patronymic or surname differing between documents (Артемьева /
  Андреева, Лапина / Ланина, Евдокия / Авдотья) — note them as variants; Авдотья is a
  vernacular form of Евдокия.
- **Status progression.** e.g. ссыльнокаторжная → ссыльнопоселенка → крестьянка →
  гражданка (terms and archive codes: `.claude/skills/genealogy-biography/references/terms.md`).
- **Family.** Collect children, spouses, and their fates across rows (a child born in one
  row may die in the next, or appear in a later census or confession list).
- **Gaps.** Note long periods with no records and moves between places, without
  inventing what happened in between.
- **Rows without any source** — list their row numbers so the gap stays visible.
