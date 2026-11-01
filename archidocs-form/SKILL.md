---
name: archidocs-form
description: Build the Archidocs upload form (.xlsx, one row per person — Фамилия, Имя, Отчество, Год рождения, Тип документа, Год документа, Место события, Название документа, Архивный шифр, Название файла, Комментарий) from rows of sources/people_all.xlsx (sheet «people_all») that the user has already checked, modernizing church names and patronymics (Татиана → Татьяна, Иоанн → Иван, «Петров» → Петрович); put it with its scans into archidocs_ready_to_send_part.N; keep earlier parts in sync with later corrections in people_all. Use when the user asks for the Archidocs form / форму для Archidocs / archidocs_ready_to_send / form_output_*.xlsx. Transcribing scans into people_all is the scans-to-people-all skill and comes first.
---

# people_all → Archidocs form

**Only from checked rows.** The source is `sources/people_all.xlsx`, sheet `people_all` (called
«people_all2» before 2026-11-01; the older master sheet is now `people_all_orig` and is not used
here; columns are found by their headers in row 2), after
the user has verified the rows (yellow fills he removed are settled readings; doubts he left
stay as text in the comment). Never build the form straight from scans or from unchecked
rows — that is the scans-to-people-all skill, and its output must be checked first.
people_all keeps the document spelling; only the form gets modern names.

Scripts in `.claude/skills/archidocs-form/scripts/` (plain `python3`, not `-I` — openpyxl is in
the user site-packages): `$SK` below.

## 1. Parts and folders

- **One Archidocs part = 4 leaves (scans).** Part 1 = 014–017, part 2 = 074–077, … Each part
  is a folder `sources/_vinnik/archidocs_ready_to_send_part.<N>/` with the 4 scans copied in and
  `form_output_<doc>_part.<N>.xlsx` (e.g. `form_output_1900_ispoved_Stanichne_DAHO_40-110-914_part.3.xlsx`).
- If fewer than 4 scans of the next batch are checked, the part isn't finished — build it
  with what is ready and add the rest later (rebuild from people_all with all its scans).
- The template for styles and header is the previous part's form.

## 2. Build the form

```bash
python3 $SK/people_all_to_form.py sources/people_all.xlsx <TEMPLATE_FORM.xlsx> <OUT.xlsx> scan1.jpg scan2.jpg …
```

- Takes the people_all rows whose FileName is one of the given scans, in sheet order (so
  the user's corrections are included).
- Converts names via `modern_names.py`: Татиана → Татьяна, Иоанн → Иван, Стефан → Степан,
  Параскева → Прасковья; «Петров» → Петрович, «Петрова» → Петровна, «Ильина» → Ильинична,
  «Фомина» → Фоминична. **Surnames and comments are not modernized.**
- Rebuilds place, archive cipher (ends with «лист 228» / «лист 228 об.»), and
  Комментарий = people_all «additional info» + «; возраст N лет» (год/года/лет by Russian
  plural rules; under one year — as written, «5 недель»).
- No colour fills in the form; doubtful readings left by the user go as text in the comment.
- Not in the form: двор numbers, per-sex running numbers (Муж/жен) — they live only in people_all.
- If it prints **UNKNOWN** patronymics — add them to `PATR` in `modern_names.py` and rerun.
  A church name without an established modern form stays as is (Синклитикия, Епистимия).
- Back up any existing form before overwriting it (`sources/_vinnik/_backup_forms_<date>/`).

`python3 $SK/modern_names.py form.xlsx …` modernizes an existing form in place (back it up first).

## 3. Keep earlier parts in sync

The user edits people_all after a form is made. Before building a new part, rebuild every
previous part into the scratchpad with `people_all_to_form.py` and diff it with the saved
form; if anything changed, back up the old form and replace it. Say which parts changed.

**Parts already uploaded to Archidocs are frozen** — never overwrite their form. If people_all
changed for such a part, only list the differences (row, person, old → new) so the user can fix
them on Archidocs by hand. Uploaded so far (update this list when the user says so):
- part 1 (scans 014–017) — uploaded by 2026-11-01. Known differences then: Томенко Терентий
  (note «в документе номер стоит в графе женского пола (305)» added) and Рудич Дмитрий («,» →
  «;» before the age).

## 4. Report

Tell the user: which part, which scans, how many people; the list of name changes made by
modernization (document form → form name) for anything not obvious; new patronymics added
to `modern_names.py`; which earlier parts were rebuilt after people_all corrections. The
user uploads the form to Archidocs himself.
