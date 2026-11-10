---
name: scans-to-people-all
description: Transcribe scans of a confession list (исповедная роспись), metric book or similar parish register into sources/people_all.xlsx (sheet «people_all») — one row per person, in the document spelling, with household numbers, per-sex running numbers, ages, relations and yellow-marked doubtful readings — then stop for the user's check. Use whenever the user asks to digitize / оцифровать / внести в табличку / в people_all from scans like sources/_vinnik/1900_ispoved_Stanichne_DAHO_40-110-914_*/…_scanNNN_pageNNN.jpg. The next step, the Archidocs upload form from the checked rows, is the archidocs-form skill. Not for reading a metric book through for research with an internal frame-by-frame index — that is metric-book-index.
---

# Scans → people_all

**Order of work (user's rule, 2026-10-28):**
1. Transcribe scans in the **document spelling** (Татиана, Иоанн, отчество «Петров/Петрова»).
2. Append them to `sources/people_all.xlsx`, sheet `people_all` (§5). people_all stays **as in the original** — never modernize there.
3. The user verifies/corrects the rows in people_all. **This skill ends here.**
4. Only then, as a separate step, the **archidocs-form** skill builds the Archidocs form from
   people_all with modernized names (Татьяна, Иван, отчество «Петрович/Петровна»).

**Sheets of `sources/people_all.xlsx`** (renamed by the user 2026-11-01):
- `people_all` — the working sheet for confession-list data, the one this skill writes to (was
  «people_all2»). Row 1 = the user's group notes («Данные со сканов», «Отчество или фамилия
  курсивом — добавлено мной (не было в оригинальном документе)», «1 — внес в дерево эту
  запись»), row 2 = column headers, data from row 3.
- `people_all_orig` — the user's older master sheet (was «people_all»); read it for context
  (e.g. how a family's род was grouped), never write to it.
- Always find columns **by their header in row 2**, never by letter: the user changes the
  layout (2026-11-01 he removed «Filter for comparison», and every column after it moved).

## 1. Find the previous batch and learn from it
- Read the last rows of sheet `people_all` (and the newest `archidocs_ready_to_send_part.N/` form):
  they show which family continues onto the first new scan, the current village section, the leaf,
  and the user's corrections — their spelling choices are the standard (Розова for the whole family,
  Брижань vs Брижанев as written).
- **Batches of 4 leaves (scans)** — the size of one Archidocs part (part 1 = 014–017, part 2 =
  074–077), so take the next 4 scans after the last batch. The part folders and forms themselves
  are made by the archidocs-form skill.

## 2. Read the scans
- View the whole page first, then crop zoomed strips with `sips` into the scratchpad
  (`sips -c H W --cropOffset Y X src --out strip.jpg; sips -Z 1600 strip.jpg`): ~4–7 strips of the
  names + ages columns, then tighter crops for every doubtful word.
- An enhanced copy (contrast, enlarged crop) that settled a reading is kept in the folder of the
  original scans as `<original file name>_der.<Village>_enhanced.jpg` (e.g.
  `2026-04-09 16-39-44_der.Boravovo_enhanced.jpg`) — the rule is in the source-page skill, § 1.
- **Align ages by the running numbers, not by the line.** The clerk often writes ages one row
  below the name. The columns «мужеска/женска пола» carry sequential numbers per sex; walk the
  names in order, assign each a sex, and match against the sequence of male/female ages. Crossed-out
  numbers mean a correction — follow the surviving one and mention the struck value in the comment.
- Church Slavonic letters: Ѳ → Ф (Феодор, Фекла, Мефодий), і → и, ѣ → е, drop final ъ.
  Keep church name forms as written (Иоанн, Симеон, Евфимий, Параскева); «Иванъ» stays Иван.
- A capital Д in this hand looks like Ѳ/О — check against known words (Даниилова, Дария).

## 3. Fill the rows — conventions (from parts 1–3, 1900 Станичное)
- One row per person, in document order. Surname: as written in the document; if written only at
  the head, copy it to the household, using the feminine form only when the document uses one
  (Шилеина, Брижанева, Крамаренкова); otherwise the same form for all (Винник, Прасол, Розова).
- Patronymic: of household members from the father's name (Евфимий → Евфимиев, Сергий → Сергеев,
  Илия → Ильин, Савва → Саввин, Иван → Иванов); for wives — the document's «X-ова дочь» → X-ова.
- Возраст меньше года — как в оригинале, строкой: `"5 недель"`, `"3 месяца"` (в rows.json тоже
  строкой); год рождения тогда = год документа.
- Год рождения = год документа − возраст (int). Год документа is a **string** ('1900').
- Место события: «Хутор X, Караванская волость, Валковский уезд, Харьковская губерния» — from the
  section heading («Хутора Винникова крестьяне»). Archive cipher ends with «лист 228» / «лист 228 об.».
- Комментарий = `<relation/status>; возраст N лет` (год/года/лет by Russian plural rules). Relations
  copied from the document wording: «жена», «жена (Трофима)» when the husband isn't the line above,
  «дети их», «сын его от 1-й жены», «вдова по 1 браку», «второго брака оба», «Андрея жена».
  The first child of a group carries «дети их», the rest only the age.
- Section start: «в документе — раздел «Хутора Винникова крестьяне»». Family split across leaves:
  last row «семья продолжается на следующем листе»; first row on the next leaf names the parents
  «(родители — на л. 228: Севастиан Антонов Розова и жена Мария Захариева)».
- Doubts go in the comment, never silently, always with the variants you see and only with the word
  «неуверенно» (never «неразборчиво»): «фамилия читается неуверенно (А / Б)», «имя читается
  неуверенно (А / Б)», «возраст читается неуверенно (73 / 74)» — every doubt, even a small one.
  In people_all also fill the doubtful cell(s) **yellow** (FFFFFF00, as the user does): surname →
  «род» + «фамилия», name → «Имя», patronymic → «Отчество», age → «age». The user checks against the scan and,
  if he reads it, removes the fill and the «неуверенно» note; what stays later goes to Archidocs
  as text. Implausible ages (parent < 16 at birth etc.) — keep the
  documented age and note it. Never invent kinship the document doesn't state.
- Don't record the «за малолетством / не были» column.
- **Двор number** (first column «Домовъ или дворовъ»): 9th element of the row, only on the row where
  the document writes it (as the user does: the number stands where the clerk put it, even a row above
  the household head — always so, don't mention it in the report) → people_all
  «Family # / Двор №». Not in Archidocs.
- **Italic = not written in the document** (people_all row 1: «Отчество или фамилия курсивом —
  добавлено мной (не было в оригинальном документе)»):
  10th element `"S"` if this person's surname is not written next to them (household members under
  the head), `"P"` if the patronymic is ours (children «Дети их: Анна» → Петрова), `"SP"` both.
  Wives' «Ирина Даниилова дочь» is written → no P. people_all gets italic фамилия / Отчество.
- **Numbering (always; parts 1–3 already done in people_all):** record each person's number from «мужеска/женска пола» as the
  8th element of the row, `"M1751"` / `"F1729"`; it goes to people_all columns Муж / жен (not to
  Archidocs — that's why people_all is the source of truth). The clerk often writes the number a
  row off — assign by the running sequence per sex, and check the first/last number of each page
  against the scan. Clerk anomalies stay as written, with a note in the comment (1900, л. 198 об.:
  Терентий Николаев Томенко got female no. 305, so a naive count of male numbers after him is off
  by one — Филипп Романов Винник is 349, not 350). A crossed-out number → the surviving one.

## 4. Build a raw form (document spelling) in the scratchpad
Write a `rows.json` in the scratchpad (format in the script docstring) and run
`python3 .claude/skills/scans-to-people-all/scripts/build_form.py rows.json SCRATCH/raw_part.N.xlsx`
(plain `python3`, not `-I` — openpyxl is in user site-packages). This is only an intermediate file.

## 5. Append to sources/people_all.xlsx → sheet people_all (document spelling)
Sheet `people_all`, one row per person (columns by their headers in row 2): Год 1900, DocType Confession_book,
detailed/фонд as in the existing 1900 Винники rows, нас.пункт Винники / Брижанев / Лычев / Пивнев,
Page `228` or `'227об'`, Сословие военный (part.1) / крестьянин (part.2+; check the section heading),
род = masculine surname (Винникова → Винник as the user grouped it, -кая → -кий, -ова/-ева/-ина → без «а»),
additional info = comment without the age, фамилия/Имя/Отчество, age (int, or "5 недель"),
BirthYearCalculated `=A<row>-<age column><row>` (the script picks the letter of «age»), FileName =
scan file name. Муж/жен numbers are not in the Archidocs forms. New rows get the style of the
sheet's last row (blue «Год», italics only where flagged; a yellow doubt fill is not copied).
The file must be closed in LibreOffice (no `.~lock.people_all.xlsx#`); back it up first
(`sources/backup/_backup_people_all_<date>.xlsx`).
`python3 .claude/skills/scans-to-people-all/scripts/to_people_all.py SRC OUT --estate=крестьянин raw_part.N.xlsx` appends rows that aren't in the
sheet yet (never rebuilds an existing sheet — the user edits it). Set --estate from the section heading
(«…крестьяне» / «…военные»); split the raw form if a batch spans both.
Then report (§6) and **stop** — wait for the user to verify people_all. Don't build the Archidocs
form in the same step; after the check the user asks for it (archidocs-form skill).

## 6. Report
Tell the user: number of people per leaf and where the rows went. Uncertain readings are not listed
in chat — they are in sheet people_all itself (yellow fill + «… читается неуверенно (А / Б)» in
additional info); just give their count. Do mention clerk anomalies kept as written (e.g. «третьего
брака» husband with «жена 2 брака») — in the chat only, no note in the sheet.
