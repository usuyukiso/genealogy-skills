"""Append rows of raw (document-spelling) forms to sources/people_all.xlsx → sheet «people_all».

Usage: python3 to_people_all.py SRC OUT [--estate=крестьянин|военный] raw_form.xlsx …
Without --estate: военный for paths containing "part.1", else крестьянин (the 1900 batches).

Sheets of people_all.xlsx (renamed by the user 2026-11-01):
  people_all      — the working sheet for confession-list data (was «people_all2»); rows go here;
  people_all_orig — the user's older master sheet (was «people_all»); read-only here.
Columns are found by their headers in row 2 (not by letter), so adding or removing a column
in the sheet does not break the script. Rows already in the sheet (same surname, name,
patronymic, page, file) are skipped: the sheet is never rebuilt — the user edits it.
"""
import copy
import re
import sys

import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

args = [a for a in sys.argv[1:] if not a.startswith('--estate=')]
ESTATE = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--estate=')), None)
SRC, OUT, *FORMS = args
SHEET = 'people_all'
ORIG = 'people_all_orig'
DETAILED = 'Сповідний розпис Предтечінської церкви села Станичного Валківського повіту Харьківської губ'
FOD = 'Ф-40, оп.-110, спр.-914, арк. 191-270'
VILLAGE = {'Хутор Винников': 'Винники', 'Хутор Брижанев': 'Брижанев', 'Хутор Лычев': 'Лычев',
           'Хутор Пивнев': 'Пивнев', 'Хутор Ляшев': 'Ляшев'}


def columns(ws):
    """header (row 2) → column number (1-based)"""
    return {c.value: c.column for c in ws[2] if c.value}


wb = openpyxl.load_workbook(SRC)
if SHEET not in wb.sheetnames:
    sys.exit(f'no sheet «{SHEET}» in {SRC} (sheets: {wb.sheetnames})')
ws = wb[SHEET]
col = columns(ws)
need = ['Год', 'DocType', 'detailed', 'фонд-опись-дело', 'нас.пункт', 'Page', 'Family # / Двор №',
        'Муж', 'жен', 'Сословие', 'род', 'additional info', 'фамилия', 'Имя', 'Отчество', 'age',
        'BirthYearCalculated', 'FileName']
missing = [h for h in need if h not in col]
if missing:
    sys.exit(f'headers not found in row 2 of «{SHEET}»: {missing}')
LAST = ws.max_column

# род: the user's own surname→род pairs (feminine form → family name), from both sheets
user_rod = {}
for name in (ORIG, SHEET):
    if name not in wb.sheetnames:
        continue
    s = wb[name]
    c = columns(s)
    if not all(h in c for h in ('Год', 'нас.пункт', 'род', 'фамилия')):
        continue
    for r in s.iter_rows(min_row=3, values_only=True):
        year, place, rd, sur = (r[c['Год'] - 1], r[c['нас.пункт'] - 1], r[c['род'] - 1], r[c['фамилия'] - 1])
        if year == 1900 and rd and sur and rd != sur and sur.startswith(rd[:4]):
            user_rod[sur] = rd

rows = []  # (form_row, estate)
for path in FORMS:
    f = openpyxl.load_workbook(path).active
    estate = ESTATE or ('военный' if 'part.1' in path else 'крестьянин')
    rows += [(r, estate) for r in f.iter_rows(min_row=2, values_only=True) if any(r)]

male_surnames = {r[0] for r, _ in rows if r[2] and not r[2].endswith('а')}


def rod(s):
    if s in user_rod:
        return user_rod[s]
    if s in male_surnames:
        return s
    if s.endswith('ова') and s[:-2] in male_surnames:  # Крамаренкова → Крамаренко
        return s[:-2]
    if s.endswith('кая'):
        return s[:-3] + 'кий'
    if s.endswith(('ова', 'ева', 'ина')):
        return s[:-1]
    return s


def page(leaf):
    m = re.match(r'лист (\d+)( об\.)?$', leaf)
    return f'{m.group(1)}об' if m.group(2) else int(m.group(1))


def split_age(comment):
    m = re.search(r'[;,]?\s*возраст (\d+) (?:год|года|лет)$', comment)
    if m:
        return comment[:m.start()].strip(), int(m.group(1))
    m = re.search(r'[;,]?\s*возраст (\d+ (?:недел[ьяи]|день|дня|дней|месяц|месяца|месяцев))$', comment)
    if m:  # under a year: keep as in the original
        return comment[:m.start()].strip(), m.group(1)
    return comment, None


def v(r, h):
    return r[col[h] - 1]


have = {(v(r, 'фамилия'), v(r, 'Имя'), v(r, 'Отчество'), str(v(r, 'Page')), v(r, 'FileName'))
        for r in ws.iter_rows(min_row=3, values_only=True)}
rows = [(r, e) for r, e in rows
        if (r[0], r[1], r[2], str(page(r[8].split('914, ')[1])), r[9]) not in have]

# style of new rows: copied from the last data row of the sheet (the user's own formatting)
last = ws.max_row
while last > 2 and not any(c.value for c in ws[last]):
    last -= 1
body_style = {c.column: copy.copy(c._style) for c in ws[last]}
start = last + 1
age_letter = get_column_letter(col['age'])

for i, (r, estate) in enumerate(rows, start=start):
    sur, name, pat, _by, _t, _y, place, _d, arch, fname, comment = r[:11]
    num = r[11] if len(r) > 11 else None  # "M1751" / "F1729" → Муж / жен
    dvor = r[12] if len(r) > 12 else None  # → Family # / Двор №
    flags = (r[13] if len(r) > 13 else None) or ''  # S / P → italic фамилия / Отчество
    info, age = split_age(comment or '')
    leaf = arch.split('914, ')[1]
    vals = {'Год': 1900, 'DocType': 'Confession_book', 'detailed': DETAILED, 'фонд-опись-дело': FOD,
            'нас.пункт': VILLAGE[place.split(',')[0]], 'Page': page(leaf), 'Сословие': estate,
            'род': rod(sur), 'additional info': info or None, 'фамилия': sur, 'Имя': name,
            'Отчество': pat, 'age': age, 'FileName': fname}
    vals['BirthYearCalculated'] = (f'=A{i}-{age_letter}{i}' if isinstance(age, int)
                                   else (f'=A{i}' if age else None))
    if num:
        vals['Муж' if num[0] == 'M' else 'жен'] = int(num[1:])
    if dvor:
        vals['Family # / Двор №'] = dvor
    italic = ({col['фамилия']} if 'S' in flags else set()) | ({col['Отчество']} if 'P' in flags else set())
    by_col = {col[h]: x for h, x in vals.items()}
    for cn in range(1, LAST + 1):
        c = ws.cell(row=i, column=cn, value=by_col.get(cn))
        c._style = copy.copy(body_style.get(cn, body_style[col['Имя']]))
        if c.fill.fill_type and c.fill.fgColor.rgb == 'FFFFFF00':  # a doubt mark of the style row
            c.fill = PatternFill(fill_type=None)
        f = copy.copy(c.font)
        f.i = cn in italic
        c.font = f

ws.freeze_panes = 'A3'
ws.auto_filter.ref = f'A2:{get_column_letter(LAST)}{ws.max_row}'
wb.save(OUT)
print(len(rows), 'rows ->', OUT, f'(sheet «{SHEET}», rows {start}–{start + len(rows) - 1})', '| rod map:',
      sorted({(r[0], rod(r[0])) for r, _ in rows if rod(r[0]) != r[0]}))
