"""Append rows of raw (document-spelling) forms to people_all.xlsx → sheet people_all2.

Usage: python3 to_people_all.py SRC OUT [--estate=крестьянин|военный] raw_form.xlsx …
Without --estate: военный for paths containing "part.1", else крестьянин (the 1900 batches).
"""
import copy, re, sys, openpyxl

args = [a for a in sys.argv[1:] if not a.startswith('--estate=')]
ESTATE = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--estate=')), None)
SRC, OUT, *FORMS = args
SHEET = 'people_all2'
DETAILED = 'Сповідний розпис Предтечінської церкви села Станичного Валківського повіту Харьківської губ'
FOD = 'Ф-40, оп.-110, спр.-914, арк. 191-270'
VILLAGE = {'Хутор Винников': 'Винники', 'Хутор Брижанев': 'Брижанев', 'Хутор Лычев': 'Лычев', 'Хутор Пивнев': 'Пивнев'}

wb = openpyxl.load_workbook(SRC)
base = wb['people_all']
# род: the user's own surname→род pairs from people_all first
user_rod = {}
for r in base.iter_rows(min_row=3, values_only=True):
    # only feminine forms of the same surname (not maiden names of wives)
    if (r[0] == 1900 and r[4] == 'Винники' and r[11] and r[13] and r[11] != r[13]
            and r[13].startswith(r[11][:4])):
        user_rod[r[13]] = r[11]

rows = []  # (form_row, estate)
for path in FORMS:
    ws = openpyxl.load_workbook(path).active
    estate = ESTATE or ('военный' if 'part.1' in path else 'крестьянин')
    rows += [(r, estate) for r in ws.iter_rows(min_row=2, values_only=True) if any(r)]

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


FILECOL = 26  # Z: FileName (added by the user to people_all2)
if SHEET in wb.sheetnames and wb[SHEET].max_row > 2:
    # sheet already has data (and maybe the user's edits) — append, never rebuild
    ws = wb[SHEET]
    have = {(r[13], r[14], r[15], str(r[5]), r[FILECOL - 1])
            for r in ws.iter_rows(min_row=3, values_only=True)}
    rows = [(r, e) for r, e in rows
            if (r[0], r[1], r[2], str(page(r[8].split('914, ')[1])), r[9]) not in have]
    start = ws.max_row + 1
else:
    if SHEET in wb.sheetnames:
        del wb[SHEET]
    ws = wb.create_sheet(SHEET, index=1)
    for key, dim in base.column_dimensions.items():
        ws.column_dimensions[key].width = dim.width
        ws.column_dimensions[key].hidden = dim.hidden
    for rn in (1, 2):
        ws.row_dimensions[rn].height = base.row_dimensions[rn].height
        for c in base[rn]:
            n = ws.cell(row=rn, column=c.column, value=c.value)
            n._style = copy.copy(c._style)
            if c.comment:
                n.comment = copy.copy(c.comment)
    ws.cell(row=2, column=FILECOL, value='FileName')._style = copy.copy(base.cell(row=2, column=1)._style)
    start = 3
body_style = {c.column: copy.copy(c._style) for c in base[1856]}  # a 1900 Винники row

for i, (r, estate) in enumerate(rows, start=start):
    sur, name, pat, _by, _t, _y, place, _d, arch, fname, comment = r[:11]
    num = r[11] if len(r) > 11 else None  # "M1751" / "F1729" → Муж / жен
    dvor = r[12] if len(r) > 12 else None  # → Family # / Двор №
    flags = (r[13] if len(r) > 13 else None) or ''  # S / P → italic фамилия / Отчество
    info, age = split_age(comment or '')
    leaf = arch.split('914, ')[1]
    vals = {1: 1900, 2: 'Confession_book', 3: DETAILED, 4: FOD, 5: VILLAGE[place.split(',')[0]],
            6: page(leaf), 11: estate, 12: rod(sur), 13: info or None, 14: sur, 15: name, 16: pat,
            17: age, FILECOL: fname}
    vals[18] = f'=A{i}-Q{i}' if isinstance(age, int) else (f'=A{i}' if age else None)
    if num:
        vals[9 if num[0] == 'M' else 10] = int(num[1:])
    if dvor:
        vals[8] = dvor
    italic = {14} if 'S' in flags else set()
    if 'P' in flags:
        italic.add(16)
    for col in range(1, FILECOL + 1):
        c = ws.cell(row=i, column=col, value=vals.get(col))
        c._style = copy.copy(body_style.get(col, body_style[15]))
        if col in italic:
            f = copy.copy(c.font)
            f.i = True
            c.font = f
ws.freeze_panes = 'A3'
ws.auto_filter.ref = f'A2:{openpyxl.utils.get_column_letter(FILECOL)}{ws.max_row}'
wb.save(OUT)
print(len(rows), 'rows ->', OUT, '| rod map:',
      sorted({(r[0], rod(r[0])) for r, _ in rows if rod(r[0]) != r[0]}))
