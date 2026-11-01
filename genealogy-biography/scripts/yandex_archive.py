#!/usr/bin/env python3
"""Read machine-recognized text from Yandex Archive (stdlib only).

Usage:
  python3 yandex_archive.py page <url>        # recognized lines + archive/fond/opis/delo of a scan page
  python3 yandex_archive.py search <query>    # search results with snippets (structured markup)

Page text is automatic handwriting recognition: quote it, but mark it as such and
expect errors (names, numbers, dates). Columns of a metric-book table come out as
separate lines, so dates/ages may need to be matched to columns by position.
"""
import html
import json
import re
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def next_data(page):
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', page, re.S)
    return json.loads(m.group(1)) if m else {}


def cmd_page(url):
    page = fetch(url)
    m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', page)
    if m:
        print("Документ:", html.unescape(m.group(1)))
    crumbs = re.findall(r'"@type":"ListItem","position":\d+,"name":"([^"]+)"', page)
    if crumbs:
        print("Каталог:", " / ".join(crumbs))
    print()
    lines = re.findall(r'RegionsListItem_Readonly[^"]*">(.*?)</p>', page, re.S)
    if not lines:
        print("(распознанного текста на странице нет или страница не загрузилась)")
    for i, line in enumerate(lines):
        print(i, html.unescape(re.sub("<[^>]+>", "", line)).strip())


def cmd_search(query):
    url = "https://yandex.ru/archive/search?" + urllib.parse.urlencode({"text": query})
    props = next_data(fetch(url)).get("props", {}).get("pageProps", {})
    print("Найдено:", props.get("totalDocs"))
    for it in props.get("items", []):
        snippet = (it.get("snippet") or "").replace("\u0007", "")
        print("- https://yandex.ru/archive/catalog/%s  (%s)\n  %s" % (it.get("parentId"), it.get("name"), snippet))


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("page", "search"):
        sys.exit(__doc__)
    (cmd_page if sys.argv[1] == "page" else cmd_search)(" ".join(sys.argv[2:]))


if __name__ == "__main__":
    main()
