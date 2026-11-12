---
name: source-page
description: Create or fix one source page of the family-history MkDocs site in family_tree_github/docs/sources/ — an archive record (A), book (B), photo (F), web page (W), map (M), letter (L) and the like — with a year-first title, a full citation that names the delo verbatim in «…» (from its cover or the archive inventory; shown in bordeaux), where the scan lies (folder, file, page side), a labelled verbatim transcript on «paper», reading notes, guesses marked as guesses, and registration in the sources index, menu and internal check lists. Use when the user asks to make, add, fix or check a source page (страница источника, оформи источник, заведи A-страницу, добавь карту как источник, сверь источник со сканом) without writing a person's biography. A biography is genealogy-biography, which uses this skill for its source pages.
---

# Source page

One page per distinct document. Accuracy over prose: genealogists will check each line
against the scan. Everything below applies to new pages; old pages are brought up to it
when the user checks them (see «Old pages»), not in bulk.

Site: `family_tree_github/` (MkDocs Material). Paths, IDs and links work as described in
the genealogy-biography skill: get the next free ID with
`python3 .claude/skills/genealogy-biography/scripts/next_id.py next A` (B, F, W, M…), look
for an existing page first with `next_id.py find "<archive ref or URL>"`, link pages by ID
only (`[A1048]`, `[Горелик](PLC1015)`) — never by file path, except anchors on a page
without an ID (`../../genealogy-puzzles.md`) or a section anchor
(`../../places/PLC1015-gorelik.md#gorelik-pentekhovo`). `D` pages are not published.

## 1. Before writing

- Check `family_tree_github/internal/checks/reviewed_documents.md` — the delo may already
  have been looked at; afterwards log this review there too (including negative results).
- Read the scan yourself (or the user's own transcription) — never quote machine OCR of a
  whole collection; read the passage on the scan.
- **Enhanced copies of a scan** (contrast, background levelling, enlarged crop — anything
  made to read it better) that helped a reading are kept, not left in the scratchpad:
  save them **in the same folder as the original scans**, named as the original file
  (without extension) + `_der.<Village>` + `_enhanced`, e.g.
  `2026-04-09 16-39-44_der.Boravovo_enhanced.jpg`. `<Village>` is the village in Latin
  letters (as in the page slug / the user's file names). Several copies of one frame get a
  tail after `enhanced`: `…_enhanced_lines3-4_left.jpg`, `…_enhanced_2.jpg`. No separate
  `_enhanced_*` folders and no names by frame number (`638_R_…`). Never overwrite or
  rename the original. On the page and in the notes cite such a file as «рабочая копия,
  не источник», next to the original file name: name only the main copy
  (`2026-03-16 15-55-17_cc2_der.Boravovo_enhanced.jpg`) — no list of the crops, no `*`
  mask, no file count; the crops lie next to it under the same name with a tail. Throw-away trial crops stay in
  the scratchpad.
- Find the **delo's own title**: on its cover (photograph of the cover/first frames) or,
  if the cover has none, in the archive inventory (e.g. `sources/opisi/1209-opis_1-2.pdf`;
  `pypdf` in a scratch venv extracts the text). A delo may hold several books with
  different titles by leaf ranges — take the book the cited leaves belong to.

## 1a. One delo, several villages: a general delo page

When the site has records of **more than one village from the same delo** (a census, a
revision, a confession-list delo), make one page per village **plus one general page of the
delo** (user, 2026-11-08). Model: [A1296] (1709, РГАДА ф. 1209, оп. 1, д. 8505) with the
village pages A1291, A1292, A1293, A1295.

- **General page** (`A…-<archive>-<fond>-<opis>-<delo>-<year>-delo.md`, title «<year>
  <archive ref>: <what the books are> (описание дела)»). Everything that does not belong to
  one village goes here:
  - the delo's own title(s) verbatim in «…» (bordeaux span): every book of the delo with its
    leaf range, from the cover or the archive inventory;
  - who made it, when; what the cover says;
  - how the book is arranged (chain of headings uyezd → губа → owner → village, quoted with
    leaf and scan file; how entries follow each other; totals);
  - formulas met in many entries («лѣтны», «дворъ впусте», «тому N лет», «708 году»);
  - where the scans lie (folders, leaf ranges, files of the headings);
  - **a table of the site's villages in this delo** — `| Деревня на сайте: как записана в книге |
    Губа, владелец | Лист | Файл | Страница записи |` (one cell: «[Порухово](PLC1011): «Деревня
    Порухово, на речки Порховки»», for compactness), each village linked to its PLC page,
    the village page by ID or «пока нет». Then «Не найдены» (searched, absent) and «Не
    искали».
- **Which villages go into the table:**
  - **revisions and censuses before 1800 — all villages of the site** (every PLC page of
    the guberniya), each with what was found, not found or not searched; obligatory;
  - **after 1800** — in detail all villages of our volost / губа found in the delo (there
    are not many), if the compiler has the information; otherwise only our villages for now.
- **Village pages** keep only their record: «Полное описание» with archive, fond, opis,
  delo, leaf, the book named in plain words (no long title in «…»), the section heading
  of the губа, and a line «Полное название книги по описи, устройство записей, сканы и все
  деревни сайта в этом деле — на общей странице дела [A…]»; the scan file of the record;
  the record, residents, reading notes about this record, neighbours, comparison.
- Old deloes are converted when the user edits them (done: 1709 д. 8505; 1719 and others —
  later, on request).

## 2. Page skeleton

```markdown
---
source_id: A1292
source_type: archive          # archive | book | photo | website | map | letter …
title: "1709 РГАДА, ф. 1209, оп. 1, д. 8505: переписная книга дворцовых крестьян, Ильинская губа Вороницкого уезда, д. Пентехово Петрово Горелой Мост тож"
repository: "Российский государственный архив древних актов (РГАДА)"
collection: "1209"            # фонд; only fields that are known
inventory: "1"
record: "8505"
page: "185 об."
document_date: "1709"
family_list: [PLC1015]        # only for family lists, see «Previous / next known year» below
evidence_kind: "primary"      # primary | secondary | unknown
related_people: []            # IDs; empty if the user wants no links to people yet
accessed: "<today>"
---

# <title> (A1292)

**Полное описание:** <archive>, ф. …, оп. …, д. …, л. … <delo title, see 3>. <what part
of the delo / which village / which household>.

<one or two lines: what the record is about — only what the document shows>

Сканы есть у составителя в личной коллекции: папка `…/archive 5/`, файл
`2026-04-09 15-02-39.HEIC`, левая страница (л. 185 об.), верхняя половина.

## <sections: headings, the record, residents, notes, comparison>

## Связанные персоны
- [P…]
```

- **Title**: year first (`document_date`), then archive and reference, then what it is;
  neutral (the document, not the person's story). Exceptions: `W` and `DB` titles have no
  year in front. The H1 is the title plus ` (ID)`.
- **Archive codes** decoded into a readable citation; the original file code goes into
  «В личной библиотеке автора сайта документ хранится как файл `…`».
- The citation must stand on its own: name archive, fond, delo, book fully; «то же дело,
  что [A…]» only as an extra.
- **Previous / next known year** (`family_list:`). A page that gives the **list of families
  of a village** — confession list (исповедная роспись), census / переписная книга, revision
  tale (ревизская сказка), книга выбывших душ, похозяйственная книга — gets
  `family_list: [PLC…]` with every village whose households it lists (two villages →
  two IDs) — also when none of our people are there: it is the list of sources of the
  village. Order: by year; within one year by the kind of document alphabetically
  (Исповедная роспись before Ревизская сказка), then by ID. **Not** for metric books, maps, «Списки населённых мест», general delo pages
  (A1296-style) or pages that only mention a village in passing (a bride «из деревни X»).
  A guba-wide page (A1274) lists a village only if that village has no own page for that
  year. The hook `hooks/family_list_nav.py` then puts a card «← Предыдущий известный год /
  → Следующий известный год» (year · kind of document · ID, badge «Источник») above
  «## Связанные персоны» and recomputes it on every build, so a new in-between year
  updates its neighbours by itself — just set `family_list:` on the new page. Never
  write this block by hand. The kind is taken from the title (исповед → «Исповедная
  роспись», перепис → «Переписная книга», сказк/ревиз → «Ревизская сказка», похоз,
  выбывш; «(II ревизия)» is appended), so keep these words in the title.

## 2a. Shortening long titles (menu, page title, «Полное описание»)

Long delo or book titles list many uyezds, prigorods, gubas. Shorten them so that **our
place stays visible** — we look for it first (user, 2026-11-08: «нас же интересует
Вороничский»):

- **Page title and menu**: name the first place of the original and ours, then «и др.»:
  «переписные книги Псковского, Воронецкого и др. уездов»; on a village page, our
  section: «переписная книга дворцовых крестьян, Ильинская губа Вороницкого уезда, д. …».
  Never a title that names only other places (that reads as a mismatch with the village).
- **Quoted title in «…»** (bordeaux): keep the original words, cut the rest with «…»,
  keep our place: «Переписная книга дворцовых крестьян Псковского уезда и Псковских
  пригородов в уездах: … Воронецком … переписи стольника Кирилла Абрамовича Пестова …».
  The full title stays on the general delo page (§ 1a). Never retell in «…».

- **Town names in page title / menu: modern form** (user, 2026-11-09): «Опочки, Воронича и
  Велья», not «Вороноча»; the document's form («г. Вороноча») stays in «Полное описание»
  and quotes.

## 3. The delo title — verbatim, in «…», bordeaux

In «Полное описание», right after the reference, give the delo's title **verbatim in
guillemets** and say where it comes from: «название на обложке дела», «по архивной описи
фонда». The hook `hooks/delo_title.py` colours a «…» that follows «д. N» in bordeaux
(class `.delo-title`); if the title stands further away, wrap it yourself:
`<span class="delo-title">«…»</span>`. Inline `[…]{.class}` does **not** work on plain
text (it shows up raw on the page). **Never put your own paraphrase in «…»**: without a
real title, describe the delo in plain words, uncoloured. Facts read on the cover
(«Начато… Окончено… На 80 листах») are quoted as such.

## 4. Text and transcripts

- **Label every block** of quoted text on its own line, bold only the term from
  «Откуда взяты цитаты» (docs/sources/index.md): `Текст записи (**прочтение скана**):`,
  `Текст (**расшифровка составителя**):`, `Текст записи (**распознавание Яндекс Архива**):`,
  `**Текст недоступен:**`. After the user has checked it against the scan:
  `(**прочтение скана**, сверено составителем со сканом 2026-11-07; орфография оригинала)`.
- **Everything quoted goes inside `> `** (on «paper»; `document_age.py` ages pre-1800
  pages); tables too: `> | … |`.
- **Original spelling** (ъ ѣ і ѳ, old endings) in readings of pre-1918 scans; modern
  spelling only in the page's own prose.
- **Ellipsis never alone on a line** (user, 2026-11-08; same rule in genealogy-biography):
  a «…» at the end of a cut quote is glued to the last word, no space — «…переписи
  стольника Кирилла Абрамовича Пестова…»; where the space must stay (a placeholder for an
  omitted word, «Деревня …»), use a non-breaking space `&nbsp;…`. Same for any short
  piece that must not wrap away from its word.
- **Brackets**: `[?]` for a doubtful word, `[…]` for an illegible place, `[л. 380:]` for a
  page break inside a quote. Ordinary words under a titlo are written out without brackets
  («два сына», «сынъ»); a real contraction keeps the restored letters in brackets
  («Пре[с]вятыя Б[огороди]цы»).
- **Forms and lists as tables**, columns as in the original, one entry per row; group by
  household with `###` headings («### Деревня Горелик, двор 388 (л. 47 об.)»). Long lists:
  wrap in `<div class="dense-rows" markdown> … </div>` for tight rows.
- **Notes don't go into table cells** («[так в расшифровке…]» widens the column) — put
  them in «Пояснения к прочтению».
- **Headings of the book as written**: for a census or revision, quote the chain of
  headings that places the entry — uyezd, губа/засада, owner, village («Вороницкого уѣзду.
  Ильинской губѣ.», «Въ Богородицкой губѣ. Святогорской монастырь …»), with leaf and file.
- Show where the entry stops: the first words of the next entry («Деревня что была
  пустошь Захарина …»).
- **Whole village or only our household?** Usually only ours, plus a line that the compiler
  has the other households of that village for that year, with their numbers. The whole
  village only when neighbours are evidence (same people living together across years —
  A1048).

## 5. Explanations: facts versus guesses

- «Пояснения к прочтению»: abbreviations, numbers, empty columns, doubtful readings,
  what a phrase means.
- **Only what the document shows is stated as fact.** Background from general knowledge
  (what a census was for, an epidemic year, a war), the meaning of a formula («двор пуст»),
  identifications (this village = that one, this man = that one) and age arithmetic that
  depends on which record is right — either give a source or mark «по мнению составителя»,
  «по-видимому», «вероятно», «предположение составителя (не подтверждено)». Don't name an
  unverified identification as fact in titles or tables.
- **«Сравнение с другими документами» — required for censuses, revisions and confession
  lists of the 18th century** (model: A1294, Печохново 1719). These records give only names
  and ages, so identity rests on the comparison. Build it like this:
  - a table: one column per document (1709 / 1719 / 1745 …, each with its [ID]), one row per
    person of the household, cells quote the age or the words as written («голова Григорий
    Егоров», 51; «брат родной…»), last column «→ год рождения» (several years if the records
    disagree, e.g. «ок. 1699 (1709) / ок. 1694 (1719, 1745)»); a dash where the person is
    absent;
  - notes under the table: which ages agree and by how much; a later age that is exactly
    «previous + N years» repeats the earlier record and does not confirm it; who is missing
    from a household and should be there (a son 15 years old in 1719 not written in); a
    namesake in the same book and why he is not ours;
  - the conclusion in one sentence, marked as the compiler's: «Поэтому … — это [Имя](P…).
    Это вывод составителя по именам, отчествам, деревне и возрасту.»
  - **1709, 1711 and 1719 (user, 2026-11-09; only these three years):** every village page
    of these three documents carries the same comparison table with all three columns
    (1709 / 1711 / 1719, each with its [ID]), every person of the village in any of them as
    a row, cells quoted as written; a dash = absent (for a partly read record say «в
    прочитанном нет»). Notes may differ per page.
    **Exception (user, 2026-11-10):** if in one of the three records our people are not
    found — the entry is not read / not recognised (faded text) — that record gets **no
    column**: there is nothing to put in it. The pages of the other years take the nearest
    readable document instead (e.g. 1745) and end the section with one paragraph:
    «**Перепись 1711 г.** Запись деревни есть — [A…], но текст выцвел и прочитан не
    полностью; сравнение с 1711 г. пока не сделано.» The page of the unread record itself
    has no comparison table, only links to the other years. Model: Печохново — A1293
    (1709), A1294 (1719 / 1709 / 1745), A1302 (1711, no table). Adding it to a `verified:` page → remove
    `verified:`, uncheck. Model: Боровово — A1291, A1307, A1308.
- **Neighbouring entries as evidence** (censuses, revisions): in the full citation say
  which village comes before and after ours, and check them against the «Списки населённых
  мест» 1872–77 [B1011] order, the 1786 map [M1000] and other years' books. If the same
  neighbours recur, say so in one sentence with numbers («В 1872–77 гг. Печехново … тоже
  стоит рядом с Гузаревым (№ 7145, 7146) [B1011]»). The compiler finds this hard to see —
  always do it, don't wait to be asked. Details — place-page skill, «Check the neighbours».
- **Patronymics added by the compiler** in a residents table: write each added patronymic
  in *italics* (`Федор *Меркульев*`); a patronymic written in the document stays plain
  (also when the document gives it as «Самсоновы дѣти» — say so in one clause). Right
  under the table (not above it), always the same words: «Отчества, выделенные курсивом,
  в оригинале не записаны: в вышеуказанном списке жителей они добавлены составителем по
  имени отца.» (one added — «Отчество, выделенное курсивом, … оно добавлено …»). Don't
  list the patronymics in the note instead of italics (user, 2026-11-10; model A1295).
- **No history of the reading on the page**: don't write how a word was read before
  («в черновом просмотре было прочитано как …»); corrections go to the check list only.
- A compiler's conclusion about the place lives on the place page under its own heading
  with an anchor; link to it («Доводы составителя — на странице …»; not «доказательства» — a
  conclusion is not a proof).

## 6. Maps (`M`) and pictures

- File in `docs/sources/maps/M1000-<slug>.md`, nav group «Карты», index type «Карта».
- Image (≤ 1 MB) in `docs/assets/images/sources/maps/`, shown with
  `![alt](../../assets/images/sources/maps/<file>.png)` and a caption («снимок экрана
  составителя»). Map labels quoted as written on the map, in the nominative
  («Красихина», «Сухобреева»).
- If the site refuses automated reading, say so and give only what the user saw.

## 7. Register and check

1. `docs/sources/index.md`: row `| [A1292] | Архивная запись | <title> |`, sorted by year,
   then by ID.
2. `mkdocs.yml` → `nav:` under the matching group, same order.
3. `internal/checks/documents_check_list.md`: `- [ ] A1292 — <title> — создано <date>
   (<scan files, what is uncertain>)`; update the counters «Всего» and the section count.
4. `internal/checks/reviewed_documents.md`: the review, with frames and → [ID].
5. `research_open_questions.md`: doubts, contradictions, TODOs.
6. `cd family_tree_github && .venv/bin/mkdocs build --strict` — fix every warning.

## Old pages and corrections

- The user corrects a reading from the scan → change the text silently (no «было/стало» on
  the page) and add «изменено <date> по скану составителем: …» to the page's line in
  `documents_check_list.md`.
- Editing a page marked `verified:` → remove `verified:`, turn `[x]` into `[ ]`, say exactly
  what changed.
- A page is marked checked (`verified:` + `[x]`) only when the user says so.
- When the user checks an old page, bring it up to these rules (labels, delo title,
  guesses marked).
