"""Search the OCR text of a scan collection; print delo, frame and the matching line.

  python3 -I hits.py <_ocr dir> <frames.tsv> '<regex>'

<regex> is case-insensitive; search by word fragments and letter variants,
e.g. 'глазк|глазов|[оа][зс][иі]нск'. frames.tsv comes from delos.py.
"""
import os
import re
import sys

ocr, tsv, pat = sys.argv[1], sys.argv[2], sys.argv[3]
d = {}
for l in open(tsv, encoding='utf-8'):
    a, b, c = l.rstrip('\n').split('\t')
    d[(a, b)] = c
rx = re.compile(pat, re.I)
for (a, b), c in sorted(d.items(), key=lambda x: (x[1], x[0])):
    t = open(os.path.join(ocr, f'{a}__{b}.txt'), encoding='utf-8').read()
    for line in t.split('\n'):
        if rx.search(line):
            print(f'д.{c}\t{a}/{b}\t{line.strip()[:110]}')
