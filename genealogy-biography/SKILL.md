---
name: genealogy-biography
description: Write a biography of a person, usually from archival records — births, marriages, deaths, censuses, confession lists, baptisms as godparent, moves, status changes — often given as a chronology table (.ods, .xlsx, .csv; read it with the chronology-table skill), but also from notes, links or documents. Produces a narrative biography grounded strictly in the input, quoting the records verbatim (from transcriptions and Yandex Archive scan text), as a person page of the MkDocs site in family_tree_github/docs (ID P1000…), with one page per source under typed IDs (A — archive record, B — book, F — photo, W — web page, …) and entries in the shared people index. Use whenever the user asks to write, generate, or update a biography, life story, or genealogical profile of a person.
---

# Biography

The input describes one person's life — most often a chronology spreadsheet (one event
per row, compiled from metric books, confession lists, censuses, court/admin files), but
it can also be notes, links or documents. The output is a readable biography plus source
pages. Accuracy matters more than prose: genealogists will check every claim against the
documents.

**Where the output goes.** Everything is written into the site project
`family_tree_github/` (MkDocs Material; see its `README.md`):

| What | Where |
|---|---|
| Person page | `family_tree_github/docs/people/P1000-<slug>.md` |
| Archive record | `docs/sources/archives/A1000-<slug>.md` |
| Book / publication | `docs/sources/books/B1000-<slug>.md` |
| Photo | `docs/sources/photos/F1000-<slug>.md` (image in `docs/assets/images/people/`) |
| Web page | `docs/sources/websites/W1000-<slug>.md` |
| Place (settlement) | `docs/places/PLC1000-<slug>.md` |
| Index of places | `docs/places/index.md` |
| Index of people | `docs/people/index.md` |
| Index of sources | `docs/sources/index.md` |
| Menu | `nav:` in `family_tree_github/mkdocs.yml` |

The old root files (`sources.md` with numbers 3000–3011, `people.md`,
`*_biography.md`) are legacy: don't write to them. Never mention the old numbers anywhere
on the site — no `legacy_id`, no «Прежний №» column or line.

**IDs.** A prefix plus a four-digit number from 1000, taken from the start of the file
name. An ID never changes and is never reused, even after a page is deleted. Get the next
free one and check for duplicates with:

```bash
python3 .claude/skills/genealogy-biography/scripts/next_id.py next A A P   # A1010, A1011, P1005
python3 .claude/skills/genealogy-biography/scripts/next_id.py find "23И, оп. 2, д. 24"   # is it already there?
python3 .claude/skills/genealogy-biography/scripts/next_id.py list
```

**Links.** Write only the ID; the site's hook (`hooks/id_links.py`) turns it into a link:
`[A1006]` → link labelled «A1006» to the source page; `[P1000]` → link labelled with the
person's name; `[жена](P1000)` → link with your own text. Never write file paths or URLs
to internal pages. An unknown ID breaks the build.

## 1. Read the input

If the input is a chronology spreadsheet (.ods, .xlsx, .csv), load the
**chronology-table** skill first and follow it: it dumps the table, maps the columns and
gives a reconciled fact list per row with sources. Not every biography starts from a
table — if the user gives other material (notes, links, documents), work from that and
skip the table step.

Check whether the person already has a page (`next_id.py find "<surname>"`, and the table
at the top of `docs/people/index.md`). A page marked `!!! warning "Страница-заготовка"` is
a placeholder: write the biography into it, keeping its ID and file name.

### 1a. Read the scans on Yandex Archive

For every record with a `yandex.ru/archive/catalog/...` link, get the recognized text of
the scan:

```bash
python3 .claude/skills/genealogy-biography/scripts/yandex_archive.py page "<url>"
```

It prints the document title and the catalog path (archive / фонд / опись / дело) and
then the recognized lines of the page. Use them to:
- find the record about the person and quote it (see "Quote the records" below);
- pick up details the table lacks: record number, baptism date vs. birth date, the child's
  name and parents, godparents, guarantors at a wedding, priest, cause of death, ages;
- fill in a missing archive reference (fond/opis/delo) from the catalog path.

The text is machine-recognized handwriting. Table columns come out as separate lines, so
match dates and ages to their columns by order, and treat numbers and rare names with
caution. To look for records that have no link in the table (e.g. a death record), try
`yandex_archive.py search "<name forms, place>"`. Its snippets come from structured
markup and sometimes read better than the page lines (e.g. an age). Record every search
you tried, so a negative result can be reported.

**Log every archive review.** Before reviewing a delo or a set of scans, check
`family_tree_github/internal/checks/reviewed_documents.md` (internal, not on the site) —
it may already have been searched. After reviewing one — a metric book read for this
person, a Yandex Archive search, a delo browsed for a missing record — add or extend its
entry there, **including negative results**: what (archive, fond, opis, delo or scan
path), date, how (all leaves / sample / search only), what was searched (names, places),
result (found → [A…] or frames; not found → «искали …, не нашли»), what remains unread.
Large scan collections are searched with the archive-scan-search skill; whole metric
books are indexed with the metric-book-index skill.

## 2. Extract facts and reconcile them

Before writing, have a fact list per event with its supporting source (from the
chronology-table skill when the input is a table), with ages, name variants, status
changes, family and gaps reconciled. Explain status transitions plainly; see
`references/terms.md`.

## 3. Write the biography

**The input table is not a source — never mention it.** The chronology table (and any
other working notes the user gives) is the user's private research file; readers of the
site don't know it exists and know nothing about genealogy or archival search. So in all
output text:
- Never write "в таблице", "по таблице", "из таблицы", "в исходных данных", "столбец", "строка N"
  and the like. Cite only real sources: archive records, scans, publications, websites.
- Where nothing is known, say it in general terms: "в имеющихся источниках об этом не
  сказано", "дословный текст записи недоступен", "архивный шифр неизвестен", "скан найти не
  удалось".
- A transcription from the comment column is called just "расшифровка" (the text of the
  record), not "расшифровка из таблицы".
- Errors and gaps in the table itself (wrong prefecture, birth date given instead of
  baptism date, rows without a place, misspelled names) are not discussed in the
  biography: use the correct value in the text and report the table issue to the user
  in chat (step 6). Mention a variant spelling in the notes only if it appears in a real
  source.
- Explain everything for a lay reader: what a record type is, what an abbreviation or a
  status means.

**Ground every factual claim in the input data.** Never invent dates, places, relatives,
occupations, causes, or motives. Where the data is silent, either stay silent or say
plainly that records don't show it. Phrases like "probably", "likely" are allowed only
for reasonable inferences directly supported by the data (e.g. a move inferred from
records in a new place), and must be marked as inferences. A working hypothesis
(e.g. that two records are the same person) goes under «Исследовательские заметки»,
starting with **Предположение (не подтверждено документами).**

**Prove kinship link by link.** Each parent–child and spouse link is a separate claim with
its own sources; a grandparent or more distant ancestor is proven only through a chain of
proven links. When writing about a link:
- Say what it rests on. A link named in one record is written as such («по записи о
  рождении 1919 г.»), not as a settled fact from many sources. It counts as confirmed by
  several documents only if they are independent: a copy, extract, certificate or retelling
  of the same record is the same source.
- A patronymic only names the father ("Яковлевич" = father named Яков); it does not show
  *which* Яков. Shared surname, village or household is not evidence of kinship either.
- Keep full namesakes (same name and patronymic, same village) as separate people until
  records distinguish them; a namesake outside the tree gets his own comparison page.
- When records disagree (e.g. a mother's patronymic), give both versions side by side with
  who supplied the information and when: a record made at the event or from the person
  themselves usually weighs more than a later one from others. Log it in
  `research_open_questions.md`.
- A family story or the compiler's note is a lead, not a document: attribute it «по
  заметкам составителя» and never present it as a record.

Brief **historical context** is welcome when it helps the reader understand a record
(what the Sakhalin penal colony was, what Chekhov's 1890 census was, what being a godparent
meant, what "ссыльнопоселенец" status allowed). Keep it short, general, and clearly about
the era — never present it as a fact about this person.

**Always describe visited places.** Whenever the person visited a specific site — a temple,
shrine, church, monastery, museum, castle, farm, factory, park, school, memorial, etc. —
add a short description of it (2–5 sentences): what it is, where exactly it is, when and
by whom it was founded, what it is known for, what a visitor sees there. Look the facts up
(official site, Wikipedia, encyclopedias) and keep them accurate; the person's own
connection to the place (with whom, what they did there) comes only from the data. A
city, town or region on its own doesn't need a description (one short line of context is
optional). If a site name in the data looks misspelled or can't be found, use the most
likely real name in the text and note the original spelling under the notes section.

**Quote the records.** Wherever the text of a record is available (a transcription in
the table's comment column, or recognized text from the scan), quote it verbatim, in the
form: `Согласно записи в метрической книге: «Корсаковской тюрьмы ссыльно-каторжная
Евдокія Андреева Лапина…» [A1000].` This applies to every event: births, deaths (including
the cause and age as written), marriages, godparenthood, censuses, and confession lists.
- Keep the original spelling, including pre-reform orthography and name variants.
- In the biography, fix obvious OCR errors silently. On the source page, show them in
  square brackets: `Корсаковскаго [в распознании: «Корожковскаго»]`.
- Interpretation and explanation are welcome and stay in the text. Put them *next to* the
  quote, not instead of it, e.g. «…(старости)» — то есть умерла от старости.
- If no text exists (no transcription in the table, and no scan or an unreadable one),
  say so plainly in the text: "Дословный текст записи недоступен, скан найти не удалось."
  Never paraphrase a record as if it had been quoted.
- Where a quote comes from is stated on its **source page**, not in the biography (see
  "Text origin label" in step 4). The general explanation of these labels and of the
  marks [?], […], [неразборчиво], [в распознании: «…»] lives once in the section
  «Откуда взяты цитаты» of docs/sources/index.md; don't repeat it on person pages.

**Cite inline.** After each claim, add the source ID in brackets:
`...родились близнецы Иван и Мария [A1000].` Several in a row: `[B1000][A1005]`. Every ID
used must have a page, and every source page of this person should be cited at least once.

**Link people.** When a person who has their own page is mentioned, link them:
`[Егор Почеревин](P1001)` in running text, `[P1001]` in lists (renders as the full name).
People without a page stay plain text — don't create pages for everyone mentioned.

**Language.** Write in the language the user asked for. If not specified, use the language
of the table's content (for Russian tables — Russian). Keep names and quoted record text in
their original form; when writing in another language, transliterate names and give the
original in parentheses on first mention.

**Structure** (adapt headings to the person's life; skip sections with no data):

```markdown
---
person_id: P1005
name: "Имя Отчество Фамилия"
name_variants:
  - "<как записан в документах>"
birth_date: "1885-07-15"        # ISO; "1851/1857" for a range; "" if unknown
birth_date_status: confirmed    # confirmed | probable | unknown
death_date: ""
death_date_status: unknown
parents: [P1000]                # only IDs of people who have pages
spouses: []
children: []
sources: [A1000, A1005]
---

# <Full name> (<birth year or range> – <death year>)

<One-paragraph summary: who, where, the arc of the life in 3–4 sentences.>

Do NOT add a paragraph explaining source codes ("Коды в квадратных скобках — ...", source types,
OCR caveats). That general explanation lives once in docs/research-method.md and
docs/sources/index.md, not on person pages.

## <Life period 1, e.g. Origins>
## <...>
## <Last years and death>

## Семья
<Spouses and children with dates, as a short list; link those who have pages.>

## Хронология
| Дата | Событие | Место | Источник |
<Compact table, one line per row of the input.>

## Замечания о документах
<Discrepancies in ages, names, dates; gaps; unresolved questions worth further research;
which records have no available text; OCR readings that need checking against the scan.>

## Исследовательские заметки
<Hypotheses and research leads, each marked «Предположение». Skip if none.>

## Источники
- [A1000] — <short description>
- ...

## Связанные персоны
- <role> — [P1000]
```

## 4. Source pages (mandatory when any sources exist)

**One page per distinct document**, shared by all biographies. If several rows cite the
same record, cite the same ID. Before creating a page, search for it
(`next_id.py find` by archive reference, scan URL, original code): if it exists, reuse
the ID, add any new details or quotes about this person to that page, and add the person
to its `related_people` and «Связанные персоны».

**Choosing the prefix** — by the role of the material, not where it is stored:
- `A` — an archive record: metric book entry, confession list, census card, file. The page
  holds the archive reference (архив, фонд, опись, дело, лист) and the scan link. Use `A`
  even when the reference is unknown but it clearly is an archive record.
- `D` — a concrete file or document (local scan/PDF, the compiler's notes, a certificate).
  **For now `D` sources are not published:** create no `D` pages, put no `[D…]` links on
  the site and copy no scans/PDFs into `docs/`. If an archive record has a local scan,
  write on its `A` page: «Скан документа есть у составителя в личной коллекции.» Facts
  from the compiler's notes are attributed in the text («по заметкам составителя»),
  without a link; in a table's source column write «заметки составителя». Unpublished
  `D` pages and files are kept in `unpublished/` at the project root — don't link to them.
- `B` — a book or published edition (also a publication of archive documents).
- `F` — photo; `W` — web page (encyclopedia, article, site); `N` — newspaper;
  `L` — letter; `I` — interview, oral account; `M` — map; `DB` — external database;
  `V` — audio/video; `O` — official report. Don't invent new prefixes.

**Page template** (file `<ID>-<slug>.md`, slug in Latin, lowercase, hyphens; e.g.
`A1006-giaso-23i-2-24-l25-1895-marriage.md`):

```markdown
---
source_id: A1010
source_type: archive          # archive | document | book | photo | website | …
title: "1895 Метрическая книга, ч. 2 (о бракосочетавшихся), № 2: брак Почеревина и Лапиной"
repository: "ГИАСО"           # only fields that are known; never invent a reference
collection: "23И"              # фонд
inventory: "2"                 # опись
record: "24"                   # дело
page: "25"                     # лист
document_date: "1895-01-15"
url: "https://yandex.ru/archive/catalog/…"
evidence_kind: "primary"       # primary | secondary | unknown
related_people:
  - P1000
accessed: "<today, YYYY-MM-DD>"
---

# <title> (A1010)

**Полное описание:** <full readable citation: archive, ф., оп., д., л., document title, part, year, record number>

<One line on what the record is about, e.g. "Крещение Александра, Е. А. Лапина — восприемница".>
В личной библиотеке автора сайта документ хранится как файл `<original code>.<ext>`.   (if known)
Скан: Яндекс Архив, <URL>

Графы бланка (номера граф — те, что в таблице ниже):    (when the record is a table)

1. «<column heading, verbatim, old spelling>»;
2. «…».

Текст записи (распознавание Яндекс Архива / прочтение скана):

> | 1 | 2 | 3 | … |
> |---|---|---|---|
> | <cell> | <cell> | <cell> | … |

Пояснения к прочтению:

- <each abbreviation, number or doubtful reading explained>

<Remarks: doubtful readings, two readings of one number, "Архивный шифр взят из каталога
Яндекс Архива", differences between the original code and the catalog (F.23 vs Фонд 23И).>

## Связанные персоны

- [P1000]
```

- **Text origin label.** The line before the quoted text always says where the text comes
  from, using one of the labels explained in «Откуда взяты цитаты» (docs/sources/index.md):
  `Текст записи (прочтение скана):` — read from the scan while making the page (add
  «орфография оригинала, сокращения не раскрыты; в квадратных скобках — пояснения и
  неуверенные прочтения» when useful); `Текст (расшифровка составителя):` — the user's own
  transcription, verbatim; `Текст записи (расшифровка; опубликована на …, <URL>):` — a
  third-party transcription with a link; `Текст записи (распознавание Яндекс Архива):` —
  Yandex OCR, corrections in square brackets. When the text is later checked against the
  scan, add «сверено со сканом <ГГГГ-ММ-ДД>». Machine OCR of a whole collection (e.g. the
  `_ocr/` folders of the Peasant Land Bank scans) is a search aid only: never quote it —
  read the passage on the scan and label it «прочтение скана». If you add a new kind of
  label, add it to «Откуда взяты цитаты» too.
- If there is no text: a bold **Текст недоступен:** line saying why. If a scan was searched
  for and not found, list the search queries tried.
- Titles and the page heading stay neutral: what the document is, not the person's story.
- **Year first** (all sources except `W` web pages and `DB` databases): the title starts
  with the document's year (from `document_date`) and a space, and the year is not
  repeated later in the title: «1850 ГАПО, ф. 39, оп. 1, д. 2723: исповедные росписи
  Опочецкого уезда, дд. Маковицы и Захарино», «1908 Метрическая книга Шкотовской церкви,
  ч. 1 (о родившихся), 4 декабря: …». A year span stays («1888–1890 Изба …»). The page
  heading is the same title followed by the ID in parentheses: `# <title> (A1010)`.
- **Decode archive codes** into a readable citation using `references/terms.md`, and keep
  the original code as the file name in the author's library, with its extension:
  «В личной библиотеке автора сайта документ хранится как файл `<code>.<ext>`.» Never
  write a bare `[исходный код: …]`.
- **Digitize records as tables, close to the original.** Whenever the record is a form,
  register or list with columns, reproduce it as a Markdown table with the same columns in
  the same order, inside a quote (`> | … |`) so it gets the «old paper» style from
  `extra.css`. Column headings are often long: list them verbatim as a numbered list
  above the table and use just the numbers as the table header. Empty cells stay empty.
  Lists without a known form (исповедные росписи, ревизские сказки, database card
  fields) are tables too, one entry per row — never consecutive `> ` lines, which
  Markdown merges into one paragraph. Group them under `###` headings (e.g. one per
  household: «### Двор 8 (л. 206)»); headings not taken from the form go in `[…]`.
- **Always add «Пояснения к прочтению»** after the text: abbreviations, numbers, empty
  columns, neighbouring entries that matter, and which readings are guesses.
- **Local files:** scans and PDFs are not published for now (see `D` above). Images for
  `F` pages go to `docs/assets/…`; keep them small (≤ 1 MB).
- Build the list from the `Источник`, `Комментарий2`, hyperlink, and comment columns,
  plus sources implied by the event itself (e.g. an event type "Сахалинская перепись
  Чехова" is itself a source even if `Источник` is empty).
- **Rows without any source:** do not fabricate a citation. Use the comment/event to
  describe the record type if clear (an `A` page "Исповедная роспись, 1889 — архивный шифр
  неизвестен"); otherwise mention the gap under «Замечания о документах» by date and name
  (never by table row numbers — give the row numbers to the user in chat).
- If the input has **no sources at all**, create no source pages; say in the biography's
  «Источники» section that sources are not given.

**Register each new source** in two places:
1. a row in the table in `docs/sources/index.md`: `| [A1010] | Архивная запись | <title> |`
   (keep the table sorted by year of `document_date`, then by ID: A, B, DB, F, L, W, then
   number; sources without a date go last);
2. `nav:` in `mkdocs.yml`, under the matching group («Архивные записи», «Книги»;
   add a group for a new type), sorted the same way (year, then ID).

## 5. People index (mandatory)

All biographies share **one index of people**, `docs/people/index.md`. Every time a
biography is written, updated or reworked, update the index in the same step — also when
the user edits a biography by hand and asks to sync. Read it first and edit it in place;
never rewrite it wholesale.

It has three `##` sections, which the site shows as tabs (hook `page_tabs.py`, marker
`<!-- h2-tabs -->` — keep it, and add no other `##` headings on this page):
- **«Список биографий»** — a table of everyone with a `P` page:
  `| 1916 | [Фамилия (девичья/другая) Имя Отчество](P1005) | годы жизни | P1005 |`.
  **Order by year of birth**, not by ID: take the first four-digit year of `birth_date`
  (for a range like «1851/1857» or «ок. 1851–1857» — the first year). People with no
  known birth year go below everyone else, alphabetically by surname, with «—» in the
  year column. Add the new person in the right place; remove «(заготовка)» when a
  placeholder gets its biography.
- **«Указатель имён: по фамилиям»** — everyone with a known surname mentioned in any biography.
- **«Указатель имён: без фамилий»** — everyone whose surname is unknown.

**Who goes in the name index:** everyone named or described in the biography who belongs
to the person's life or to a record about them — relatives, spouses, children, godparents,
witnesses, guarantors, neighbours, priests who performed the rite, record-keepers like the
census taker, travel companions, friends. Historical figures mentioned only to describe a
place or the era (founders of a temple, rulers, writers of a novel) do not go in.

**Entry format** — one line per person:

```markdown
- **Фамилия Имя Отчество** (variants) — who they are: status, place, approx. years, role in relation to the subject. — [Фамилия И. О.](P1005) [A1000][A1003]
```

- If the person has their own page, link the bold name too: `- **[Фамилия Имя Отчество](P1005)** (…)`.
- Name in the form the documents use (old-style patronymic «Авдей Иванов» is kept as is).
  Spelling variants in parentheses; for each variant *surname* add a cross-reference line
  `- **Вариант Имя** — см. Основная Фамилия Имя.`
- Foreign names in Russian letters, original spelling in parentheses. If the Russian
  form is reconstructed from Latin, say so.
- **Women: list under every known surname** — maiden name and each husband's surname,
  each as a full entry (not only «см.»), saying which surname is which. If it is unknown
  whether a surname is maiden or by marriage, say so. A patronymic-looking second name
  («Марфа Фокина») is a patronymic, not a maiden name — don't treat it as a surname.
- After the description: a link to every biography (person page) where the person appears
  and the source IDs where they are named. If the person already has an entry, add the
  new biography and sources to it instead of duplicating; merge entries only when the
  identity is clear, otherwise keep them separate and note the possible match.
- Never invent a surname. A child recorded without one (e.g. an illegitimate child named
  only by first name) goes to the no-surname list.

**Order:** by surname in Russian alphabetical order under `#### <letter>` headings placed
directly under «Указатель имён: по фамилиям» (no extra heading such as «Люди с известной
фамилией» — the user removed it); within a surname, by given name. People whose
surname is unknown (only a first name, or only a role like «первый муж», «мать») go in the
last section «Указатель имён: без фамилий», ordered by first name or description.

## 6. Save, check and report

Save the biography as `docs/people/<ID>-<slug>.md` (slug: Latin transliteration of the
name, e.g. `P1000-evdokiya-lapina.md`). The ID is permanent: never renumber a person when
their name or dates are corrected (keep this technical note out of the site pages). Add it to `nav:` under «Персоны» in
`mkdocs.yml` with an explicit label «<год рождения> <Фамилия> <Имя> <Отчество>», e.g.
`- 1851 Лапина Евдокия Артемьевна: people/P1000-evdokiya-lapina.md` (first year of an
approximate range; no year → label without it). Keep the «Персоны» entries in the same
order as the table in `docs/people/index.md`: by birth year, then the people without a
year alphabetically.

**Places.** Settlements have pages `docs/places/PLC1000-<slug>.md` (list them with
`next_id.py list`). When the person lived in, was born in or was otherwise connected to a
settlement that has a page:
- add its ID to the person's front matter `places: [PLC1000]` and link the first mention
  in «Краткие сведения»: `[д. Шевелёвка](PLC1000)`;
- on the place page, add the person to «Персоны с отдельной страницей» (one line: the
  connection and sources) and to `people:` in its front matter; add the other people from
  the name index who are connected to the place to the table «Другие жители и связанные
  люди» (alphabetical: `| Фамилия Имя Отчество | связь с местом | [A1000] |`);
- documentary mentions of the place's administrative division go under «До революции
  1917 года» / «После революции 1917 года», quoted with sources. The official pre-1917
  division is written by the user — never fill or overwrite it yourself.
A Familio settlement card gets **no** `W` source page: link it directly on the place page
(«[карточка деревни на сайте Familio](https://familio.org/settlements/…)»).
A new place page is created only when the user asks; add it to `nav:` under «Места»
(alphabetically) and to the table in `docs/places/index.md`. A placeholder page is filled in place. If the page already holds a written
biography, overwrite it only after confirming with the user, unless they asked to
regenerate or rework it. When the person is closely related to another page (spouse,
parent, child), add the link to that page's «Связанные персоны» and front matter too.

Then build the site in strict mode — it fails on broken links and unknown IDs:

```bash
cd family_tree_github && .venv/bin/mkdocs build --strict
```

Fix every warning before reporting. Then tell the user in a few lines:
- which page was written and the life span covered;
- which source pages were created (IDs) and which existing ones were reused or extended;
- how many people were added to the index, and which existing entries were extended;
- which records are quoted from scans, and which have no available text;
- any discrepancies, source-less rows, or OCR readings they may want to check;
- errors and gaps in the table itself (these go only here, never into the biography).
