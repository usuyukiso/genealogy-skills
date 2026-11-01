"""Build an Archidocs upload form (.xlsx) from transcribed confession-list rows.

Usage: python3 build_form.py rows.json OUT.xlsx

rows.json:
{
  "template": "path/to/previous/form_output_....xlsx",   # styles + header are copied from it
  "year": 1900,
  "doc_type": "Исповедная роспись",
  "doc_title": "Исповедная роспись Предтеченской церкви ... за 1900 год",
  "arch_prefix": "Государственный архив ... дело 914, ",
  "place": "Хутор Винников, Караванская волость, ...",      # default for rows
  "pages": {"076": ["лист 228 об.", "..._scan076_page228ob.jpg"]},
  "rows": [
    ["076", "Розова", "Поликарп", "Севастианов", 6, "дети их (...)"],
    ["077", "Прасол", "Петр", "Никитин", 73, "вдовец по 1 браку", "Хутор Брижанев, ...", "M1757", 431, "SP"]   # 7th = place override (or null), 8th = number in the document: M… / F…, 9th = двор (or null), 10th = "S"/"P"/"SP": surname / patronymic not written in the document for this person (→ italic in people_all)
  ]
}
The comment column gets "<note>; возраст N лет" (or just the age part if note is empty);
birth year = year - age.
"""
import copy
import json
import sys

import openpyxl


def age_str(n):
    if isinstance(n, str):  # under a year, as in the original: "5 недель"
        return f'возраст {n}'
    if n % 10 == 1 and n % 100 != 11:
        w = 'год'
    elif n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        w = 'года'
    else:
        w = 'лет'
    return f'возраст {n} {w}'


def main(spec_path, out_path):
    with open(spec_path, encoding='utf-8') as f:
        spec = json.load(f)
    year = spec['year']
    wb = openpyxl.load_workbook(spec['template'])
    ws = wb.active
    style_row = [copy.copy(c._style) for c in ws[2]]
    height = ws.row_dimensions[2].height
    ws.delete_rows(2, ws.max_row)
    for i, row in enumerate(spec['rows'], start=2):
        scan, sur, name, pat, age, note = row[:6]
        place = row[6] if len(row) > 6 and row[6] else spec['place']
        leaf, fname = spec['pages'][scan]
        comment = f'{note}; {age_str(age)}' if note else age_str(age)
        vals = [sur, name, pat, year if isinstance(age, str) else year - age, spec.get('doc_type', 'Исповедная роспись'), str(year),
                place, spec['doc_title'], spec['arch_prefix'] + leaf, fname, comment]
        # raw-form extras for people_all (cols L–N): 8th = document number "M1751"/"F1729",
        # 9th = двор number (only on the row where the document gives it),
        # 10th = flags: "S" surname not written for this person, "P" patronymic not written → italic
        extra = list(row[7:10]) + [None] * (3 - len(row[7:10]))
        if any(extra):
            vals += extra
            for col, title in ((12, '№ в документе'), (13, 'Двор'), (14, 'Не в документе')):
                ws.cell(row=1, column=col, value=title)
        for j, v in enumerate(vals, start=1):
            c = ws.cell(row=i, column=j, value=v)
            c._style = copy.copy(style_row[min(j, len(style_row)) - 1])
        ws.row_dimensions[i].height = height
    wb.save(out_path)
    print(len(spec['rows']), 'rows ->', out_path)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
