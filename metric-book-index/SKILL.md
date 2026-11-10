---
name: metric-book-index
description: Read a whole parish register (metric book — births, marriages, deaths — or a similar register) frame by frame from scans and build a complete internal index of every entry, plus working notes with the search targets, findings (★) and open questions; resumable across sessions. Use when the user asks to go through / дочитать / проиндексировать metric books of a parish (e.g. «добей метрики Дрогачево»), to read all years of a delo, or to find every mention of given surnames or patronymics in a register. Not for confession lists or for filling people_all.xlsx (scans-to-people-all skill) or the Archidocs form (archidocs-form skill).
---

# Metric book index

Goal: one row per record for **every** entry of the book, not only the hits — so later
questions («кто крестил?», «когда умер этот младенец?») are answered from the index
without reopening scans. Two internal files per book (repo `family_tree_github`, under
`internal/metrics/`, not on the site):

- `<years>_<Parish>_index.md` — the full frame-by-frame index;
- `<years>_<Parish>_metric_notes.md` — scans, delos, search targets, results by family,
  open TODO list.

Example of both: `internal/metrics/1881-1892_Drogachevo_index.md` and
`…_metric_notes.md`. Follow their form.

## 0. Start or resume

1. Read the notes file and the index header: what has been read («Где остановились»),
   which frames are missing, the search targets (★ surnames/patronymics), the parish
   villages and volost abbreviations already in use.
2. Check `internal/checks/reviewed_documents.md` and `research_open_questions.md` for this
   parish.
3. New book: create both files. Notes header: scans path and frame range; archive, fond,
   opis, delo(s) with frame ranges; FamilySearch DGS if any; what years are missing in the
   delo; the search targets. Index header: scans path, delos, «Как читать таблицу»
   (abbreviations, see below), «Где остановились», the ★ rule.

## 1. Cut and read the scans

Frames are usually spreads (left page = numbers/names/parents, right page = godparents,
priest). Read at full resolution; a downscaled whole spread loses handwriting.

```bash
swiftc -O .claude/skills/metric-book-index/scripts/crop.swift -o /tmp/scan_crop   # once
/tmp/scan_crop <frame.jpg> /tmp/f.jpg 0.07 0.93                 # spread without margins
/tmp/scan_crop <frame.jpg> /tmp/z.jpg 0.15 0.70 0.25 0.45       # zoom on one entry
```

- Read in batches (a year or ~10 frames), then write them into the index before going on;
  update «Где остановились» after every batch, so a stop loses nothing.
- **Re-read with a zoom** every ★ entry and every doubtful name that matters before
  writing it down. Words lost in the gutter stay `[…]`: never guess them into a target
  surname (e.g. «Егор […]симов» stays as is — not «Анисимов»).
- `sips -c` ignores the crop offset on some files — use `crop.swift`.
- An enhanced copy (contrast, enlarged crop) that settled a reading is kept in the folder
  of the original scans as `<original file name>_der.<Village>_enhanced.jpg` (e.g.
  `2026-04-09 16-39-44_der.Boravovo_enhanced.jpg`) — the rule is in the source-page skill, § 1.

## 2. Index format

One section per year: `## 1892 (д. 39)`, then a line «Причт: …» (priest, deacon, psalmist,
changes during the year, the dean's certification dates). Three tables per year:

| Part | Columns |
|---|---|
| births | `Кадр \| Лист \| Запись \| Дата \| Деревня \| Родители / стороны \| Восприемники / поручители / прочее` |
| marriages | `Кадр \| Лист \| Запись \| Дата \| Деревня \| Жених \| Невеста / поручители` |
| deaths | `Кадр \| Лист \| Запись \| Дата \| Деревня \| Умерший \| Причина / прочее` |

- **Запись:** `Р м №5 Василий`, `Р ж №1 Татиана`, `Б №3`, `С ж №2`; twins in one row
  («Р м №6 Хрисанф и Р ж №6 Дария, близнецы»). **Дата:** birth/baptism or death/burial
  `4/6 мар`. **Лист** as written on the page (`96об–97`).
- Names in normal modern spelling, patronymics as written («Иванов» = Иванович); volost
  abbreviations defined in «Как читать таблицу» («вол. С.» = Селецкая). `?` — uncertain;
  `[…]` — not visible (gutter/illegible); fragments in brackets: `Ки[риллова]`.
- Row for every page-level item too: empty spreads, part titles, missing frames,
  marginal later notes («поздняя помета "…копия 10/IX 67"»), the dean's certification.
- **Cross-links:** link records about the same people by frame — «(брак 13.01.1891,
  кадр 224)», «Умер 17.02.1892 (кадр 258)», «(род. 24.01.1892, кадр 237)». Do this as you
  go: when a death of a child is read, find its birth row.
- **★** marks every mention of a search target (as parent, child, godparent, witness,
  deceased). Bold the target name: `**Мария Онисимова** ★`.
- Disagreements between records (different patronymic or surname of the same person in
  two years, different father of the same child) are written in the row **and** added to
  the TODO list — keep both readings, never pick one silently.
- After each part: the monthly totals as the book gives them («Итог марта: м 2, ж 2») and
  a yearly summary paragraph: totals, the ★ findings in one or two sentences. Check the
  totals against the yearly statement («Вѣдомость») at the end of the book; if they
  disagree, say so.
- End of year: «**1892 г. пройден полностью** (кадры 236–265).»

## 3. Notes file and logs

After each year (or session):
- notes: «Статус» line; TODO list — tick done years with the date and the new ★ findings
  in one line; add new TODOs (re-read frame N, download missing frame, conflicting
  readings); keep the per-family tables of ★ findings (frame, leaf, record) up to date;
  the «Прочее» list of parish villages and clergy.
- `research_open_questions.md`: one dated line under the parish with the year's result and
  any new conflict («Статус: открыт»).
- `reviewed_documents.md`: the delo, frames, years read, what was searched, result
  (including «Анисимовых нет»), what remains.
- A missing year or frame is recorded as missing, not as «no such event».

## 4. Report to the user

Short: which frames/years were read; totals; the ★ findings with frame numbers; what was
re-read with a zoom and the result; conflicts found; what this book cannot answer (years
it does not cover) and the next source. Use the user's terms («кадр», «лист»).

Site pages are not changed by this skill. A finding becomes a site source page or a
biography update only when the user asks — then use the genealogy-biography skill.
