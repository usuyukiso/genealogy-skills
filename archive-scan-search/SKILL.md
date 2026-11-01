---
name: archive-scan-search
description: Search a large folder of archive scans (thousands of frames, many delos — e.g. RGIA f. 592 Peasant Land Bank photos from velikie.org, or any microfilmed fond) for villages, surnames or volosts — machine-recognize every frame (macOS Vision OCR), map frames to delo numbers by the microfilm cards, search by word fragments, verify every hit on the scan by eye, build a per-delo index of places, and log the review (including negative results) in reviewed_documents.md. Use when the user asks to look for a village/person/surname in a scan collection, to read a new uyezd/opis, or to list settlements mentioned in such scans.
---

# Archive scan search

A collection is one folder of photographed delos, usually split into subfolders by delo
range (`592-33-1361_1370/`, `592-19-205_212 (с 206)/`), each delo starting with a
microfilm card («ЦГИА СССР / Фонд № / Опись № / Дело №») and then the cover. Most text is
handwritten: OCR finds where to look, it never replaces reading the scan.

Before anything else, check `family_tree_github/internal/checks/reviewed_documents.md`:
if the collection or the delos were already reviewed for this question, say so and build
on it instead of redoing it.

Scripts (in `scripts/`, Python 3 stdlib + macOS Swift; run Python with `-I`):

| Script | What it does |
|---|---|
| `run_ocr.sh "<collection>" [N]` | OCR every frame (jpg/png/jxl) in N parallel workers into `<collection>/_ocr/<subfolder>__<frame>.txt`; skips done frames; waits until finished |
| `ocr.swift` | the OCR worker (Vision, ru, frames scaled to 2000 px) used by `run_ocr.sh` |
| `delos.py <_ocr> <frames.tsv>` | frame → delo map by microfilm cards; prints the card list with `<-- check` marks |
| `hits.py <_ocr> <frames.tsv> '<regex>'` | every OCR line matching the regex, with delo and frame |
| `idx.py <_ocr> <frames.tsv>` | raw per-delo list of товарищества, volosts, «при …», «дер. …» |
| `crop.swift` | crop a scan at full resolution (`<in> <out> x0 x1 [y0 y1]` as fractions) |

Paths below: `$SK=.claude/skills/archive-scan-search/scripts`, `$C=<collection folder>`.

## 1. OCR the collection

```bash
$SK/run_ocr.sh "$C" 4          # run in background; ~0.8 s/frame/worker → ~7000 frames ≈ 30 min
```

- Run it with `run_in_background` and wait for its completion notification. Never wait
  with a loop on `pgrep -f …ocr`: the loop's own command line matches and it never ends.
- Re-running is safe: frames that already have a `.txt` are skipped (resume after a stop).
- Then write `$C/_ocr/README.md` (see the Rzhev/Gomel ones for the form): what was
  recognized, date, method, file naming, that it is a search index and not a
  transcription, where the frame→delo map and the review log are.

## 2. Map frames to delos

```bash
python3 -I $SK/delos.py "$C/_ocr" "$C/_ocr_frames_to_delo.tsv" > /tmp/cards.txt
grep -c . /tmp/cards.txt; grep check /tmp/cards.txt
```

- Number of cards should match the number of delos (folder ranges). `<-- check` lines
  with `None` are just unread numbers; a different number may be an OCR misread *or* a
  duplicate/missing card that shifts every later delo in that folder. Look at those cards
  (crop the frame) when a find lands near them, and always confirm the delo number on
  the card of any delo you cite.
- Folder names: `592-19-205_212 (с 206)` → first delo 206; `592-19-300` → single delo;
  `592-33-1720_1728 (по 1722)` → ends at 1722. A folder with photos named by time
  (`20250918_154335.jpg`) may hold several takes of one card — check the count.
- Keep the TSV next to the collection (`_ocr_frames_to_delo.tsv`), not only in /tmp.

## 3. Search

Build the patterns from what is known about the target — read the place page
(`docs/places/PLC…`) and person pages first: volost, parish, neighbouring villages, the
estate or landowner, surnames.

```bash
python3 -I $SK/hits.py "$C/_ocr" "$C/_ocr_frames_to_delo.tsv" 'глазк|глазов|лазко|[кн][оа][зс][иі]нск|язвиц'
```

- Search by **fragments**, not whole words, and with letter variants OCR confuses:
  `[оа]`, `[зс3]`, `[иіu]`, `[еѣ]`, `ъ/ь` at ends, dropped first letter
  («азинск» for Казинск), pre-reform endings (-аго, -ѣ).
- Search the **volost** too: a village may be absent from OCR while the volost line on
  the decision page («…уѣзда, Казинской волости, при сельцѣ Корытовѣ») is readable.
- Expect noise: officials' names (a bank member «А. Г. Озерскій» is not a peasant
  Ozersky), common words containing the fragment («разины», «новинности»). Filter them
  out by reading the hit line, then by the frame.
- Surnames of buyers sit in handwritten lists that OCR reads badly; a negative surname
  search covers only the typed/clearer parts — say so.

## 4. Verify every hit on the scan

For each candidate delo, look at the frames themselves: the cover (2nd frame after the
card), the decision («Постановленіе … Отдѣленія»), the inspection report («Докладъ /
Объ осмотрѣ и оцѣнкѣ»), the buyers list («Списокъ членовъ … товарищества»).

```bash
swiftc -O $SK/crop.swift -o /tmp/scan_crop     # once
/tmp/scan_crop "<frame>" /tmp/v.jpg 0.07 0.93          # whole spread without margins
/tmp/scan_crop "<frame>" /tmp/z.jpg 0.15 0.70 0.25 0.45  # zoom on one entry
```

- Read the image, not the OCR line. Note frame file names for every fact (they become the
  source reference later: folder + `IMG_xxxx`).
- Uncertain readings: «?» in the text, never silently normalised.
- Record what the delo is: year, the товарищество/общество and size, seller, land
  location (volost, «при сельцѣ/дер./имѣніи …»), buyers' villages, whether there is a
  name list.

## 5. Places index

```bash
python3 -I $SK/idx.py "$C/_ocr" "$C/_ocr_frames_to_delo.tsv" > /tmp/idx.txt
```

Turn the raw list into `family_tree_github/internal/checks/kpb_<uyezd>_places.md`
(internal, not on the site; see `kpb_rzhev_places.md`, `kpb_gomel_places.md`):
- header: document (archive, fond, opis, delo range, scan folder), how it was made,
  limitations (how many delos gave no names; absence ≠ not there);
- first, the search the user asked for: a table of checked delos with year, what, buyers'
  villages, frames, ✓ = checked by eye;
- then the index by volost and the places without volost (при сельцѣ/дер./пустошь,
  товарищества), names in modern spelling, «?» for doubtful readings.

## 6. Log and report

- Add or update the collection's entry in `reviewed_documents.md`: scans path, date, how
  reviewed (OCR of all frames; which delos by eye), what was searched (exact fragments),
  result — found → delos/frames (and [A…] if a source page was made), not found →
  «искали …, не нашли», with the OCR limitation; what remains unreviewed.
- A find about a family member becomes a site source page only when the user asks; then
  copy that delo's frames into a separate folder named as in the
  velikie-org rule (`<year>_krestyan_pozemeln_bank_<place>_<person>_RGIA-592-<op>-<delo>`)
  and write the page with the genealogy-biography skill («прочтение скана»; never quote OCR).
- Report to the user: what was found (delo, year, one line each, key frames), what was
  not found and why it may still exist, how many delos/frames were checked by eye, the
  next useful step. Offer the most promising unchecked lists.
