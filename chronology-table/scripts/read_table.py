#!/usr/bin/env python3
"""Dump a chronology table (.ods, .xlsx, .csv/.tsv) as Markdown, using only the stdlib.

Usage: python3 read_table.py <file> [--sheet NAME]

Every sheet is printed as a Markdown table, followed by any cell comments/notes
and hyperlinks found in the sheet (these often hold source references).
"""
import csv
import re
import sys
import zipfile
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
import xml.etree.ElementTree as ET

ODS_NS = {
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "xlink": "http://www.w3.org/1999/xlink",
}
X_NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
MAX_REPEAT = 200  # guard against "repeat this empty column 16000 times"


def _q(ns, tag):
    p, t = tag.split(":")
    return "{%s}%s" % (ns[p], t)


def _ods_text(el, links):
    """Collect text of an ODS cell, keeping line breaks and recording hyperlinks."""
    parts = []
    for p in el.findall(_q(ODS_NS, "text:p")):
        buf = []

        def walk(node):
            if node.text:
                buf.append(node.text)
            for ch in node:
                if ch.tag == _q(ODS_NS, "text:s"):
                    buf.append(" " * int(ch.get(_q(ODS_NS, "text:c"), "1")))
                elif ch.tag == _q(ODS_NS, "text:line-break"):
                    buf.append("\n")
                elif ch.tag == _q(ODS_NS, "text:tab"):
                    buf.append("\t")
                elif ch.tag == _q(ODS_NS, "office:annotation"):
                    pass  # handled separately
                else:
                    if ch.tag == _q(ODS_NS, "text:a"):
                        href = ch.get(_q(ODS_NS, "xlink:href"))
                        if href:
                            links.append(href)
                    walk(ch)
                if ch.tail:
                    buf.append(ch.tail)

        walk(p)
        parts.append("".join(buf))
    return "\n".join(parts)


def read_ods(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("content.xml"))
    sheets = []
    for tbl in root.iter(_q(ODS_NS, "table:table")):
        name = tbl.get(_q(ODS_NS, "table:name"))
        rows, notes, links = [], [], []
        for r_i, row in enumerate(tbl.iter(_q(ODS_NS, "table:table-row"))):
            rrep = min(int(row.get(_q(ODS_NS, "table:number-rows-repeated"), "1")), MAX_REPEAT)
            cells = []
            for cell in row:
                if cell.tag not in (_q(ODS_NS, "table:table-cell"), _q(ODS_NS, "table:covered-table-cell")):
                    continue
                crep = min(int(cell.get(_q(ODS_NS, "table:number-columns-repeated"), "1")), MAX_REPEAT)
                cell_links = []
                txt = _ods_text(cell, cell_links)
                if not txt:
                    # dates/numbers sometimes only live in attributes
                    txt = cell.get(_q(ODS_NS, "office:date-value")) or cell.get(_q(ODS_NS, "office:value")) or ""
                for ann in cell.findall(_q(ODS_NS, "office:annotation")):
                    note = "\n".join("".join(p.itertext()) for p in ann.findall(_q(ODS_NS, "text:p")))
                    if note.strip():
                        notes.append((len(rows) + 1, len(cells) + 1, note.strip()))
                for h in cell_links:
                    links.append((len(rows) + 1, len(cells) + 1, h))
                cells.extend([txt] * crep)
            for _ in range(rrep):
                rows.append(list(cells))
        sheets.append((name, rows, notes, links))
    return sheets


def _col_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1


def read_xlsx(path):
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        shared = []
        if "xl/sharedStrings.xml" in names:
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", X_NS):
                shared.append("".join(t.text or "" for t in si.iter(_q(X_NS, "m:t"))))
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        rid2target = {r.get("Id"): r.get("Target") for r in rels.findall("rel:Relationship", X_NS)}
        sheets = []
        for s in wb.find("m:sheets", X_NS).findall("m:sheet", X_NS):
            target = rid2target[s.get(_q(X_NS, "r:id"))].lstrip("/")
            target = target if target.startswith("xl/") else "xl/" + target
            ws = ET.fromstring(z.read(target))
            grid = {}
            for c in ws.iter(_q(X_NS, "m:c")):
                ref = c.get("r")
                r = int(re.search(r"\d+", ref).group(0)) - 1
                col = _col_index(ref)
                t = c.get("t")
                v = c.find("m:v", X_NS)
                if t == "s" and v is not None:
                    val = shared[int(v.text)]
                elif t == "inlineStr":
                    val = "".join(x.text or "" for x in c.iter(_q(X_NS, "m:t")))
                else:
                    val = v.text if v is not None else ""
                grid[(r, col)] = val
            rows = []
            if grid:
                maxr = max(k[0] for k in grid) + 1
                maxc = max(k[1] for k in grid) + 1
                rows = [[grid.get((r, c), "") for c in range(maxc)] for r in range(maxr)]
            # hyperlinks
            links = []
            srels_path = target.replace("worksheets/", "worksheets/_rels/") + ".rels"
            if srels_path in names:
                srels = ET.fromstring(z.read(srels_path))
                id2url = {r.get("Id"): r.get("Target") for r in srels.findall("rel:Relationship", X_NS)}
                hl = ws.find("m:hyperlinks", X_NS)
                if hl is not None:
                    for h in hl.findall("m:hyperlink", X_NS):
                        url = id2url.get(h.get(_q(X_NS, "r:id")))
                        if url:
                            ref = h.get("ref")
                            links.append((int(re.search(r"\d+", ref).group(0)), _col_index(ref) + 1, url))
            # comments
            notes = []
            for rel_target in (id2url.values() if srels_path in names else []):
                if "comments" in rel_target:
                    cpath = "xl/" + rel_target.replace("../", "")
                    if cpath in names:
                        for cm in ET.fromstring(z.read(cpath)).iter(_q(X_NS, "m:comment")):
                            ref = cm.get("ref")
                            txt = "".join(t.text or "" for t in cm.iter(_q(X_NS, "m:t")))
                            notes.append((int(re.search(r"\d+", ref).group(0)), _col_index(ref) + 1, txt.strip()))
            sheets.append((s.get("name"), rows, notes, links))
    return sheets


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        rows = list(csv.reader(f, dialect))
    return [("csv", rows, [], [])]


def trim(rows):
    rows = [r for r in rows]
    while rows and not any(c.strip() for c in rows[-1]):
        rows.pop()
    width = 0
    for r in rows:
        for i, c in enumerate(r):
            if c.strip():
                width = max(width, i + 1)
    return [(r + [""] * width)[:width] for r in rows]


NOISY_PARAMS = {"snippet", "text"}  # search-highlight params, not part of the document address


def clean_url(url):
    """Drop search-snippet query params so links stay short but still open the right page."""
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k not in NOISY_PARAMS]
    return urlunsplit(parts._replace(query=urlencode(query, safe=" +")))


def clean_urls_in(text):
    return re.sub(r"https?://\S+", lambda m: clean_url(m.group(0)), text)


def md_cell(s):
    return clean_urls_in(s).replace("|", "\\|").replace("\n", "<br>").strip()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    want = sys.argv[sys.argv.index("--sheet") + 1] if "--sheet" in sys.argv else None
    low = path.lower()
    if low.endswith(".ods"):
        sheets = read_ods(path)
    elif low.endswith((".xlsx", ".xlsm")):
        sheets = read_xlsx(path)
    elif low.endswith((".csv", ".tsv", ".txt")):
        sheets = read_csv(path)
    else:
        sys.exit("Unsupported format: %s (use .ods, .xlsx, .csv)" % path)

    for name, rows, notes, links in sheets:
        if want and name != want:
            continue
        rows = trim(rows)
        print("## Sheet: %s  (%d rows)\n" % (name, len(rows)))
        if not rows:
            print("(empty)\n")
            continue
        print("| # | " + " | ".join(md_cell(c) for c in rows[0]) + " |")
        print("|---|" + "---|" * len(rows[0]))
        for i, r in enumerate(rows[1:], start=2):
            if any(c.strip() for c in r):
                print("| %d | " % i + " | ".join(md_cell(c) for c in r) + " |")
        if notes:
            print("\n### Cell comments")
            for r, c, t in notes:
                print("- row %d, col %d: %s" % (r, c, t.replace("\n", " ")))
        if links:
            print("\n### Hyperlinks")
            for r, c, h in links:
                print("- row %d, col %d: %s" % (r, c, clean_url(h)))
        print()


if __name__ == "__main__":
    main()
