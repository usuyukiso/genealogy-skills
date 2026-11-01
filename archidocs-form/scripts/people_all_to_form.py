"""Build an Archidocs form from verified rows of people_all.xlsx / people_all2, modernizing names.

Usage: python3 people_all_to_form.py people_all.xlsx TEMPLATE_FORM.xlsx OUT.xlsx scan_file_1.jpg [scan_file_2.jpg …]
Rows are taken from people_all2 whose FileName is one of the given scan files, in sheet order.
people_all keeps the document spelling; only the form gets modern names (modern_names.py).
"""
import copy
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modern_names import modern_name, modern_patronymic  # noqa: E402

SRC, TEMPLATE, OUT, *FILES = sys.argv[1:]
DOC = 'Исповедная роспись Предтеченской церкви села Станичного Валковского уезда Харьковской губ за 1900 год'
ARCH = 'Государственный архив Харьковской области (ДАХО), фонд 40, опись 110, дело 914, '
TAIL = ', Караванская волость, Валковский уезд, Харьковская губерния'
PLACE = {'Винники': 'Хутор Винников', 'Брижанев': 'Хутор Брижанев', 'Лычев': 'Хутор Лычев',
         'Пивнев': 'Хутор Пивнев', 'Ляшев': 'Хутор Ляшев'}


def age_str(n):
    if isinstance(n, str):
        return f'возраст {n}'
    if n % 10 == 1 and n % 100 != 11:
        w = 'год'
    elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        w = 'года'
    else:
        w = 'лет'
    return f'возраст {n} {w}'


def leaf(page):
    p = str(page)
    return f'лист {p[:-2]} об.' if p.endswith('об') else f'лист {p}'


src = openpyxl.load_workbook(SRC)['people_all2']
head = [c.value for c in src[2]]
fcol = head.index('FileName')
rows = [r for r in src.iter_rows(min_row=3, values_only=True) if r[fcol] in FILES]

wb = openpyxl.load_workbook(TEMPLATE)
ws = wb.active
style_row = [copy.copy(c._style) for c in ws[2]]
height = ws.row_dimensions[2].height
ws.delete_rows(2, ws.max_row)
unknown = set()
for i, r in enumerate(rows, start=2):
    year, place, page, info, sur, name, patr, age = r[0], r[4], r[5], r[12], r[13], r[14], r[15], r[16]
    new_p, ok = modern_patronymic(patr)
    if not ok:
        unknown.add(patr)
    parts = [x for x in (info, age_str(age) if age not in (None, '') else None) if x]
    by = None if age in (None, '') else (year if isinstance(age, str) else year - age)
    vals = [sur, modern_name(name), new_p, by, 'Исповедная роспись', str(year),
            PLACE.get(place, place) + TAIL, DOC, ARCH + leaf(page), r[fcol], '; '.join(parts)]
    for j, v in enumerate(vals, start=1):
        c = ws.cell(row=i, column=j, value=v)
        c._style = copy.copy(style_row[j - 1])
    ws.row_dimensions[i].height = height
wb.save(OUT)
print(len(rows), 'rows ->', OUT)
if unknown:
    print('UNKNOWN patronymics (kept as in document, add to modern_names.PATR):', sorted(unknown))
