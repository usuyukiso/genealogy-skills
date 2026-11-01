"""Map OCR frames to delo numbers via microfilm cards; write frames->delo TSV.

  python3 -I delos.py <_ocr dir> <frames.tsv> > cards.txt

A frame whose text has «МИКРОФОТОКОП…» or «ГОСУДАРСТВЕН…» + «ФОНД» is a microfilm
card that starts a new delo. Delos are numbered in order inside each subfolder,
starting from the first number in the folder name («592-33-1361_1370» → 1361;
«592-19-205_212 (с 206)» → 206). cards.txt lists every card with the number OCR
read on it; «<-- check» = unread or different — verify that card by eye when a
find lands in that delo. If a folder has more cards than delos (duplicate cards),
numbers after the duplicate drift: check the card of every delo you cite.
Output TSV columns: folder, frame, delo.
"""
import os, re, sys, json

ocr = sys.argv[1]
out = sys.argv[2]
files = sorted(os.listdir(ocr))
by_folder = {}
for f in files:
    if not f.endswith('.txt'):
        continue
    folder, frame = f[:-4].split('__', 1)
    by_folder.setdefault(folder, []).append(frame)

rows = []
report = []
for folder in sorted(by_folder):
    m = re.match(r'592-(\d+)-(\d+)', folder)
    start = int(m.group(2))
    m2 = re.search(r'\(с (\d+)\)', folder)  # «592-19-205_212 (с 206)»: first delo is 206
    if m2:
        start = int(m2.group(1))
    frames = sorted(by_folder[folder])
    delo = None
    seq = start - 1
    for fr in frames:
        t = open(os.path.join(ocr, f'{folder}__{fr}.txt'), encoding='utf-8').read()
        if 'МИКРОФОТОКОП' in t.upper() or ('ГОСУДАРСТВЕН' in t.upper() and 'ФОНД' in t.upper()):
            seq += 1
            nums = re.findall(r'\d{3,5}', re.sub(r'[\[\]/|]', '', t))
            nums = [int(n) for n in nums if start - 2 <= int(n) <= start + 15]
            ocrnum = nums[0] if nums else None
            report.append((folder, fr, seq, ocrnum))
            delo = seq
        rows.append((folder, fr, delo))

with open(out, 'w', encoding='utf-8') as fh:
    for r in rows:
        fh.write(f'{r[0]}\t{r[1]}\t{r[2]}\n')
for r in report:
    flag = '' if r[3] == r[2] else '  <-- check'
    print(*r, flag)
