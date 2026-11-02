---
name: replica-marriage-certificate-1940s
description: Make a typed replica (HTML/CSS copy laid out like the blank form, not a scan) of a Soviet marriage certificate on the NKVD USSR ZAGS form of the 1940s («Свидетельство о браке», landscape sheet: on the left the ZAGS office stamp, place and date of issue, on the right the fields «Гр. … и гр. …, вступили в брак …», surnames after marriage) and publish it as a document page (D-ID) of the family-history MkDocs site, with a verbatim transcript, reading notes and a footer naming this skill. Use when the user asks to draw / отрисовать / сделать копию бланка of a 1940s marriage certificate («свидетельство о браке 1940-х»). Other forms have their own replica-* skills.
---

# Replica: marriage certificate, NKVD ZAGS form of the 1940s

Reference page: [assets/example-D1008.md](assets/example-D1008.md) (D1008, issued
9 June 1945). Styles: [assets/replica.css](assets/replica.css) (needs both
`.replica--wide` and `.replica--marriage`).

## The form

- One landscape sheet, cream paper without grid, frame of a thick and a thin line
  (`.replica--wide.replica--marriage`).
- Top: «НАРОДНЫЙ КОМИССАРИАТ · [coat of arms] · ВНУТРЕННИХ ДЕЛ СССР» (`.rp-mhead`,
  arms as an empty dashed circle `.rp-emblem`), «ОТДЕЛ АКТОВ ГРАЖДАНСКОГО СОСТОЯНИЯ»
  (`.rp-msub`).
- Two columns (`.rp-mcols`): **left** (`.rp-mleft`) — the stamp of the ZAGS office
  (`.rp-cstamp`, faint grey), place of issue (`.rp-mplace`), date (`.rp-mdate`), number
  (`.rp-mno`); often a diagonal handwritten note (`.rp-diag`, e.g. a passport issue
  mark). **Right** (`.rp-mright`) — title «СВИДЕТЕЛЬСТВО О БРАКЕ № __», then «Гр. ___
  и гр. ___» (`.rp-two`), «вступили в брак ___ 19__ г., о чем в книге записей актов
  гражданского состояния о браке произведена соответствующая запись под № __» (`.rp-mtext`),
  «Фамилии после заключения брака: { мужа · жены }» (`.rp-grp`), М. П., signatures
  (Заведующий бюро ЗАГС, Делопроизводитель), date.
- Ink: usually violet (`--rp-pen: #5a3f9a`). Transcript paper: `paper: cream`.

## Reading and dating hints

- Stamps of 1940s selsovet / settlement ZAGS offices are often half printed: letters
  missing in a word are supplied by sense — say which in the notes, without brackets in
  the replica if the user prefers (ask).
- Read the round seal ring by ring; abbreviations inside the seal («депут.», «Хаб.
  края») are transcribed as printed.
- The bride is listed under her maiden surname; the surnames after marriage are a
  separate field.
- Compute both ages at marriage from their birth records and mention them.
- Empty fields («запись под №») stay empty; say so in the notes.

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
   - front matter: `source_id`, `source_type: document`, `title` (year first, both
     persons identifiable: «1945 Свидетельство о браке Пав. Ив. Давыдова и Люб. Ив.
     Почеревиной, № 15»), `document_date`, `evidence_kind`, `doc_replica: true`,
     `replica_skill: <this skill's name>`, `paper: <colour>`, `related_people`,
     `accessed`. Never add `verified:` — only the user verifies.
   - `# <title> (D####)`, then **Полное описание:** — what, on whose name, dates, the
     issuing office, form, ink, sheets, condition, where the original is, scan file name.
   - The sentence «Ниже — не скан, а копия, набранная по образцу бланка: …», saying what
     is not reproduced (signatures, coat of arms) and how seals are shown.
   - The replica HTML (copy the block from the example page and refill it).
   - The label line on its own, only the term from «Откуда взяты цитаты» in bold:
     `Текст свидетельства (**прочтение скана**; вписанное от руки выделено курсивом,
     неразборчивое отмечено «[…]»):`
   - The transcript as a quote: printed text plain, everything handwritten in `*italic*`.
     The `paper:` field puts the quote on coloured paper and shows the italics in blue
     ink — handwriting in a transcript is always italic and blue. Use `grey`, `white`,
     `pink`, `cream` or `yellow`; all of them colour italics blue.
   - `## Пояснения к прочтению` — dating, abbreviations, stamps and seals, empty fields,
     uncertain readings, how the document relates to other sources.
   - `## Связанные персоны` — `- [P####]` per person.
4. **Replica rules.** Same layout and line breaks as the form; printed text verbatim;
   handwriting in `.rp-hand` / `.rp-inline` (Marck Script) in the ink colour of the
   original. Never draw signatures: write `[подпись]`, or `[подпись: И. Фамилия]` only
   when the user confirmed the reading. Coats of arms are not drawn. Seals and stamps
   are faded circles/frames; their text only if it is read. Crossed-out printed words in
   `<s>`. All sizes in `cqw`, so the sheet scales like a picture. If the user's sheet
   differs from the example (another printing), adapt the HTML and add the CSS to
   `extra.css` under a new modifier class, and update `assets/replica.css` here.
5. **Register it.** Add the page to `mkdocs.yml` nav → «Источники» → «Документы»
   (sorted by year, then ID); a row in `docs/sources/index.md` (same order); a `- [ ]`
   line in `family_tree_github/internal/checks/documents_check_list.md` (section
   «Документы (D)», fix the counts). On every related person page (both spouses): cite
   `[D####]` in the text, «Муж»/«Жена», the chronology and «Источники», add it to
   `sources:` in the front matter, and remove «скан у составителя» / «не опубликован»
   wording for this document. A page with `verified:` you edit → remove `verified:`,
   uncheck its line, append «изменено …», and tell the user.
6. **Check.** Build the site (`.venv/bin/mkdocs build -d <scratch dir>`) and look at the
   page in a browser at the normal column width: no wrapped field labels, handwriting
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
