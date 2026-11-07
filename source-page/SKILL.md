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
- Find the **delo's own title**: on its cover (photograph of the cover/first frames) or,
  if the cover has none, in the archive inventory (e.g. `sources/opisi/1209-opis_1-2.pdf`;
  `pypdf` in a scratch venv extracts the text). A delo may hold several books with
  different titles by leaf ranges — take the book the cited leaves belong to.

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
- Comparison with other records (e.g. 1709 vs 1719): a table plus notes; when ages
  disagree, say both and that it is not settled; a later age copied as «previous + N
  years» does not confirm the earlier one.
- A compiler's conclusion about the place lives on the place page under its own heading
  with an anchor; link to it («Читать доказательства — на странице …»).

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
