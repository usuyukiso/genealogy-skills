---
name: replica-school-certificate-1930s
description: Make a typed replica (HTML/CSS copy laid out like the blank form, not a scan) of a Soviet school-leaving certificate of the 1930s («Свидетельство об окончании … школы», form of an oblast education department — «РСФСР, Народный Комиссариат по Просвещению, … облоно», with a numbered list of subjects and marks, social work, discipline, issue date, head of school and school council secretary) and publish it as a document page (D-ID) of the family-history MkDocs site, with a verbatim transcript, reading notes and a footer naming this skill. Use when the user asks to draw / отрисовать / сделать копию бланка of a 1930s school certificate («школьное свидетельство 1930-х», «свидетельство об окончании школы»). Other forms have their own replica-* skills.
---

# Replica: school-leaving certificate of the 1930s

Reference page: [assets/example-D1009.md](assets/example-D1009.md) (D1009, Western
oblast form, issued 7 September 1934). Styles: [assets/replica.css](assets/replica.css).

## The form

- Portrait sheet, yellow paper, no grid (`.replica--school`). Frame: thick line, a chain
  of diamonds (SVG `border-image` on `.rp-sborder`), thin line inside.
- Head in two columns (`.rp-shead`): **left** (`.rp-sleft`) — «РСФСР / Народный
  Комиссариат по Просвещению / … ОБЛОНО» (`.rp-sobl`), then «_____ школа», «Адрес ____»
  on lines (`.rp-sl` + `.rp-fill`); **right** (`.rp-sright`) — motto (`.rp-smotto`),
  big «Свидетельство» (`.rp-stitle`), «ОБ ОКОНЧАНИИ … ШКОЛЫ» (`.rp-ssub`).
- Body (`.rp-sbody`), each printed line a `.rp-sl` flex row: «Пред’явитель сего ___
  (фамилия, имя)» (caption under the line: `.rp-under`), «родивш__ в 19__ году,
  поступил__ в школу в 19__ году, окончил__ ее в 19__ году», «проявил__ следующую
  успеваемость:», the subjects list (`.rp-subj`, one `<p>` per subject: label + `.rp-fill`
  with the mark), «За время пребывания в школе ___ (фамилия) выполнял__ общественную
  работу ___», «дисциплинирован ___ и проявляет склонность к ___», «Выдано ___ 193_ г.»,
  footer (`.rp-sfoot`: М. П. with a faded stamp `.rp-sstamp`, «Зав. школой», «Секретарь
  школьного совета» in `.rp-ssign`), printer's line under the frame (`.rp-styp`).
- Short blank lines: `.rp-w` with an inline width; a handwritten digit on a printed
  «19__»: `.rp-h.rp-u`; handwriting: `.rp-h` (Marck Script), usually violet
  (`--rp-pen: #5b3fa0`).
- Transcript paper: `paper: yellow` (class `doc-paper-yellow`; italics blue).

## Reading and dating hints

- The oblast in «… облоно» and the address date the form (e.g. Западная область
  1929–1937; a district's transfer to another oblast). The printer's line («Тип.
  Политотдела МТС, п. Оленино») can date the printing too — MTS political departments
  existed 1933–1934. Such dating facts are general history: label them as context.
- The printed title («средней школы») is generic; do not infer the school type from it —
  give the years of study and age at leaving instead.
- Marks are abbreviated («удовлетвор.», «хор.», «отл.», «оч. хор.»); the same word may be
  written slightly differently in each line — transcribe uniformly and say so.
- In the transcript the subjects are a table inside the quote (`> | № | Предмет |
  Отметка |`), one row per subject — a line starting «1.» would become a Markdown list
  and run together; say in the notes that the column headings are the compiler's.
- Dashes in unused subjects are handwriting: `*—*` in the transcript.
- Subjects on a fold may be hard to read — list them for the user's check.
- Social work wording is abbreviated («участвовал в провед. с/хоз. полит. кампаний»):
  transcribe as written, expand in the notes.

## Workflow

Follow the shared steps below; the form-specific part is above.

1. **Read the scan.** Render a PDF on macOS with PDFKit (a short Swift script:
   `PDFDocument` → `page.draw(with:.mediaBox, to:)` into an `NSBitmapImageRep` at scale
   4–5) or use the TIFF/JPEG as is; `sips -c H W --cropOffset Y X in.png --out crop.png`
   cuts fragments. Read the whole sheet, then every handwritten field, stamp, signature
   and the printer's line at 2× crops. Nothing is guessed: unreadable → `[…]`,
   uncertain → `[?]`, and list these for the user.
2. **ID and duplicates.** `python3 .claude/skills/genealogy-biography/scripts/next_id.py D`
   gives the next free ID; grep `docs/sources/documents/` and the person pages for the
   scan file name — the document may already be mentioned as «скан у составителя».
3. **Write the page** `family_tree_github/docs/sources/documents/D####-<slug>.md`:
   - front matter: `source_id`, `source_type: document`, `title` (year first, person
     identifiable: «1934 Свидетельство об окончании школы Григ. Як. Писарева, Бобровская
     школа»), `document_date`, `evidence_kind`, `doc_replica: true`,
     `replica_skill: <this skill's name>`, `paper: <colour>`, `related_people`,
     `accessed`. Never add `verified:` — only the user verifies.
   - `# <title> (D####)`, then **Полное описание:** — what, on whose name, dates, the
     issuing school and education department, printer, ink, sheets, condition, where the
     original is, scan file name.
   - The sentence «Ниже — не скан, а копия, набранная по образцу бланка: …», saying what
     is not reproduced (signatures) and how seals are shown.
   - The replica HTML (copy the block from the example page and refill it).
   - The label line on its own, only the term from «Как подготовлены тексты источников» in bold:
     `Текст свидетельства (**прочтение скана**; вписанное от руки выделено курсивом,
     сомнительное отмечено «[?]»):`
   - The transcript as a quote: printed text plain, everything handwritten in `*italic*`.
     The `paper:` field puts the quote on coloured paper and shows the italics in blue
     ink — handwriting in a transcript is always italic and blue. Use `grey`, `white`,
     `pink`, `cream` or `yellow`; all of them colour italics blue.
   - `## Пояснения к прочтению` — dating, abbreviations, marks, empty fields, uncertain
     readings, how the document relates to other sources.
   - `## Связанные персоны` — `- [P####]` per person.
4. **Replica rules.** Same layout and line breaks as the form; printed text verbatim
   (old spelling, «Пред’явитель», «ее»); handwriting in `.rp-h` in the ink colour of the
   original. Never draw signatures: write `[подпись]`, or `[подпись: И. Фамилия]` only
   when the user confirmed the reading. Seals and stamps are faded circles; their text
   only if it is read. Crossed-out printed words in `<s>`. All sizes in `cqw`, so the
   sheet scales like a picture. If the user's sheet differs from the example (another
   oblast, another subject list), adapt the HTML; new CSS goes to `extra.css` under a new
   modifier class, and update `assets/replica.css` here.
5. **Register it.** Add the page to `mkdocs.yml` nav → «Источники» → «Документы»
   (sorted by year, then ID; «1930-е» goes before 1934); a row in
   `docs/sources/index.md` (same order); a `- [ ]` line in
   `family_tree_github/internal/checks/documents_check_list.md` (section «Документы (D)»,
   fix the counts). On every related person page: cite `[D####]` in the text, the
   chronology and «Источники», add it to `sources:` in the front matter, and remove
   «скан у составителя» / «не опубликован» wording for this document. A page with
   `verified:` you edit → remove `verified:`, uncheck its line, append «изменено …», and
   tell the user.
6. **Check.** Build the site (`.venv/bin/mkdocs build -d <scratch dir>`) and look at the
   page in a browser at the normal column width: no wrapped subject names, handwriting
   on its lines, the footer «Копия бланка сгенерирована с помощью скилла …» present.
7. **Report** to the user: the uncertain readings to check on the scan, every page
   touched, every `verified:` removed. Corrections the user confirms are applied
   silently (no «было/исправлено» on the page) and logged in the check list.

## Setting up on another site (once)

- Append `assets/replica.css` to the site's `extra.css`; load the fonts (Google Fonts:
  Marck Script, PT Sans Narrow 400/700, PT Serif 400/700/italic) in `overrides/main.html`.
- Copy `assets/document_age.py` (wraps pages by `paper:`) and `assets/replica_credit.py`
  (footer from `replica_skill:`) to `hooks/` and list both under `hooks:` in `mkdocs.yml`.
  The paper styles use the site's «old paper» blockquote variables (`--doc-paper-*`).
