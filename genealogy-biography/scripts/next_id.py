"""ID страниц сайта family_tree_github.

  python3 next_id.py next A [A ...]   — следующий свободный ID для префикса (A1010)
  python3 next_id.py find <текст>     — страницы, где встречается текст (шифр, URL, имя)
  python3 next_id.py list             — все занятые ID с файлами

Номера берутся из имён файлов в docs/ («A1006-….md»), начинаются с 1000
и никогда не переиспользуются. Путь к docs можно задать через DOCS=…
"""
import os
import re
import sys

PREFIXES = ("FAM", "PLC", "EV", "DB", "P", "F", "D", "A", "B", "W", "N", "L", "I", "M", "V", "O")
FILE_ID = re.compile(r"^(%s)(\d{4})-" % "|".join(PREFIXES))
HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.environ.get("DOCS") or os.path.normpath(
    os.path.join(HERE, "..", "..", "..", "..", "family_tree_github", "docs"))


def pages():
    for root, _, names in os.walk(DOCS):
        for n in sorted(names):
            m = FILE_ID.match(n)
            if m and n.endswith(".md"):
                yield m.group(1), int(m.group(2)), os.path.join(root, n)


def main(argv):
    if not os.path.isdir(DOCS):
        sys.exit(f"нет папки {DOCS}")
    cmd = argv[0] if argv else "list"
    if cmd == "next":
        used = {}
        for p, n, _ in pages():
            used.setdefault(p, set()).add(n)
        nxt = {}
        for p in argv[1:]:
            if p not in PREFIXES:
                sys.exit(f"неизвестный префикс {p}")
            nxt[p] = nxt.get(p, max(used.get(p, {999}) | {999}) ) + 1
            print(f"{p}{nxt[p]}")
    elif cmd == "find":
        needle = " ".join(argv[1:]).lower()
        for p, n, path in pages():
            if needle in open(path, encoding="utf-8").read().lower():
                print(f"{p}{n}\t{os.path.relpath(path, DOCS)}")
    else:
        for p, n, path in sorted(pages()):
            print(f"{p}{n}\t{os.path.relpath(path, DOCS)}")


if __name__ == "__main__":
    main(sys.argv[1:])
