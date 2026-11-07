---
name: place-page
description: Create, restructure or extend a settlement (place) page of the family-history MkDocs site in family_tree_github/docs/places/PLC1000-<slug>.md — first paragraph with the guberniya and dated parish, the church parish by period first, then the pre-1917 administrative division split by period (18th-century губа/засада/вотчина, then uyezd/volost/stan and «Списки населённых мест»), a table of every mention of the place in documents by year (name as written, губа, source), the compiler's conclusions under their own anchored headings (e.g. an old name of the village), people connected with the place, and the places index and menu kept in sync. Use when the user asks to make, fix or tidy a village page (страница деревни, населённого пункта, «на странице Горелика сделай…», «список всех упоминаний по годам», «церковный приход», «как называлась деревня раньше»). Linking a person to a place inside a biography is genealogy-biography, which follows these rules.
---

# Place page

A place page shows, in time order, what the documents say about a settlement: which
church its people went to, which administrative unit it belonged to and under which
names it appears. Model page: `docs/places/PLC1015-gorelik.md` (Горелик).

New place pages are created only when the user asks. IDs: `next_id.py next PLC`
(genealogy-biography scripts); link people and sources by ID.

## Front matter

```yaml
place_id: PLC1015
name: "Горелик"
name_variants: ["Горѣликъ"]           # spellings found in documents
place_type: деревня
guberniya: "Псковская губерния"       # pre-1917; groups the page in the menu
admin_before_1917: "Полянская волость, Опочецкий уезд, Псковская губерния"
admin_as_of: "волость — по заметкам составителя; стан — 1872–77 гг. [B1011]"
parish_before_1917:
  - "1754–1774: Георгиевская церковь пригорода Воронича"
  - "1790: Покровская церковь погоста Поляне"
admin_after_1917: []
people: [P1111, P1066]                # people with pages connected to the place
sources: [A1292, M1000, A1275, …]
```

## Order of sections

1. **First paragraph.** What the place is, the guberniya once in **bold** tied to the year
   of the data («в 1870-х гг. — Опочецкий уезд **Псковской губернии**»), the parish with
   the years it is attested, who of ours lived there. No modern district here (that goes to
   «После революции 1917 года»).
2. **`## Церковный приход`** — right after the first paragraph (user, 2026-11-07: «это
   важный блок»). Table `| Годы | Церковь | Как известно | Источник |`, one row per period,
   **every** known mention: confession lists, weddings, baptisms, deaths. A record that
   lists the village but not the church gets a row saying so. Facts from the compiler's
   notes: «по заметкам составителя», no ID. Mirror in `parish_before_1917:`.
3. **`## Административное деление` → `### До революции 1917 года`**, split by period with
   the years in `####` headings, newest first:
   - `#### Конец XVIII века – 1917 год: Опочецкий уезд` — the line «Дер. X — волость, уезд,
     **губерния** (по <source> <year> [ID])», the «Списки населённых мест» row (quoted
     table with neighbouring entries, scan link), the earliest document of this period.
   - `#### 1709 – 1770-е годы: Ильинская губа Вороницкой дворцовой вотчины` — list by year
     with sources (census, revisions). The compiler's own map (GeneaBits [W1007]) may be a
     source for the губа in 1745 and 1763.
   - The official division is the user's to state: don't overwrite it on your own; if
     unknown, write only what documents say and ask.
4. **`#### Упоминания в документах по годам {#upominaniya}`** — table
   `| Год | Как записано в документе | Губа | Источник |`, one row per document, quoting
   how the place is named, so that name changes and conflicting divisions are visible.
   In «Губа» put what the document itself says (heading or text) or derives from it
   («той же губы», что …); otherwise «—». Close with a short summary («Ильинскую губу
   называют …; Богородицкую — только …»). Names on maps in the nominative, as written.
5. **Conclusions of the compiler** — each under its own `####` heading with an anchor,
   e.g. `#### Горелик и Пентехово (вывод составителя) {#gorelik-pentekhovo}`, stating the
   evidence (documents, map) and labelled as the compiler's view («составитель считает…»,
   «возможно…»). Source pages link to the anchor: «Читать доказательства — на странице
   Горелика».
6. **`### После революции 1917 года`** — later divisions, modern district; a Familio card
   is linked directly («[карточка Familio](https://familio.org/settlements/…)»), with no
   `W` page. Never link nashipredki.com.
7. **`## Люди`** — `### Персоны с отдельной страницей` (one line each: connection, years,
   sources) and `### Другие жители и связанные люди` (table `| Имя | Связь с местом |
   Источник |`, alphabetical by given name when there are no surnames; patronymics added by
   the compiler go in brackets with a note).
8. **`## Источники`** — list of IDs, plus the Familio link.

## Rules

- **Only documents are facts.** Identifications (this village under another name),
  readings of a map, background knowledge — «по мнению составителя», «по-видимому», or a
  source. Disputed points also go to `research_open_questions.md`; they are not put into
  «Генеалогические загадки» unless the user asks.
- **Quote names as written** in the documents (old spelling in quotes); the page's own
  text uses the modern name.
- When a source page is created about this place, add it to the mentions table, to
  `sources:` and to «Источники».

## Keep in sync

- `docs/places/index.md`: the row «| [PLC…] | <уезд, волость/стан (год)> | <сейчас> |
  <персоны> |» under the right guberniya heading.
- `mkdocs.yml` → «Места» → the guberniya group (Псковская first, others alphabetically),
  alphabetical within it — only for a new page.
- People pages: `places:` and the first mention linked; the place page lists them back.
- `cd family_tree_github && .venv/bin/mkdocs build --strict` — fix every warning.
- Restructuring an existing page: keep all its content and sources; only regroup.
