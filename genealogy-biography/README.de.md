# Genealogy Biography — ein Skill für Familiengeschichte aus Dokumenten

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

**Ein Agent Skill für Claude Code, der die Biografie eines Vorfahren aus Archivdokumenten schreibt und sie als Seite einer Website zur Familiengeschichte veröffentlicht.** Als Eingabe dient meist eine chronologische Tabelle (eine Zeile pro Lebensereignis: Geburten, Ehen, Todesfälle, Volkszählungen, Beichtlisten, Patenschaften, Umzüge, Standeswechsel), aber auch Notizen, Links oder Scans sind möglich. Das Ergebnis ist eine gut lesbare Lebensgeschichte, in der jede Tatsache eine Quelle hat und jedes Zitat wörtlich ist, dazu eine eigene Seite für jedes Dokument.

Der Skill wurde für eine russischsprachige [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/)-Website über Familien aus dem Russischen Kaiserreich und der UdSSR entwickelt. Die Anweisungen sind auf Englisch; den Text für die Website schreibt er auf Russisch (oder in der gewünschten Sprache), und Zitate aus Dokumenten behalten die ursprüngliche vorrevolutionäre Rechtschreibung.

---

## Was er tut

- **Biografieseite.** Eine Erzählung des Lebens nach Abschnitten, eine Familienliste, eine Chronologie, Anmerkungen zu Widersprüchen zwischen Dokumenten und ein eigener Block mit Forschungsnotizen für Hypothesen.
- **Quellenseiten.** Eine Seite pro Dokument: vollständige Archivsignatur (Archiv, Fonds, Findbuch, Akte, Blatt), Ablageort des Scans, Spaltenüberschriften des Formulars, wörtlicher Text des Eintrags und Erläuterungen zu unsicheren Lesungen. Ein Dokument hat genau eine Seite, auch wenn mehrere Biografien es zitieren.
- **Wörtliche Zitate.** Einträge werden exakt und in der Originalschreibung zitiert. Auf der Quellenseite steht, woher der Text stammt: eigene Lesung des Scans, Transkription des Verfassers, von anderen Forschenden veröffentlichte Transkription (mit Link) oder Texterkennung von Yandex Archive. Unsichere Wörter sind mit `[?]` markiert, unleserliche Stellen mit `[…]` oder `[неразборчиво]`.
- **Hilfsskript für Yandex Archive.** `scripts/yandex_archive.py` holt den erkannten Text und die Archivsignatur eines Scans und durchsucht das Archiv. Der erkannte Text gilt als Entwurf: Er wird mit dem Scan abgeglichen, Korrekturen werden sichtbar gemacht.
- **Feste Kennungen.** Jede Seite hat eine dauerhafte ID (`P1000` Person, `A1000` Archiveintrag, `B` Buch, `F` Foto, `W` Webseite, `PLC` Ort…). `scripts/next_id.py` liefert die nächste freie ID und prüft, ob ein Dokument bereits eine Seite hat, damit nichts doppelt angelegt wird.
- **Namensregister.** Jede Person, die in einem Eintrag genannt wird — Verwandte, Paten, Trauzeugen, Nachbarn, Priester —, erhält eine Zeile im gemeinsamen Register; Frauen unter jedem bekannten Nachnamen.
- **Orte.** Personen werden mit Ortsseiten verknüpft; die Verwaltungsgliederung vor 1917 wird nach Dokumenten mit dem Jahr der Quelle angegeben.
- **Strenger Build.** Am Ende wird die Website im strikten Modus gebaut: Ein defekter Link oder eine unbekannte ID stoppt die Arbeit, bis der Fehler behoben ist.

## Welche Regeln er befolgt

- **Nichts erfinden.** Keine Namen, Daten, Verwandten, Signaturen oder Zitate, die nicht in den Eingabedaten stehen. Wo die Dokumente schweigen, steht das so im Text.
- **Jede Tatsache mit Beleg,** und der Link führt zum konkreten Eintrag, nicht zu einer Übersichtsseite.
- **Schlussfolgerungen sind gekennzeichnet.** Eine Hypothese steht in den Forschungsnotizen und beginnt mit «Предположение (не подтверждено документами)» („Vermutung, nicht durch Dokumente belegt“), mit Argumenten dafür und dagegen und mit dem, was sie bestätigen könnte.
- **Verwandtschaft Glied für Glied.** Jede Eltern-Kind- und Ehebeziehung hat eigene Belege; ein entfernter Vorfahr gilt nur dann als belegt, wenn jedes Glied der Kette belegt ist. Kopien desselben Eintrags sind eine einzige Quelle. Ein Vatersname nennt den Vornamen des Vaters, zeigt aber nicht, um welchen Mann es sich handelt; gleicher Nachname, gleiches Dorf oder gleicher Hof beweisen keine Verwandtschaft.
- **Namensvettern bleiben getrennt.** Zwei Personen mit gleichem Vor- und Vatersnamen aus einem Dorf werden nicht zusammengeführt, bis Dokumente sie unterscheiden.
- **Widersprüche werden gezeigt, nicht verborgen.** Beide Fassungen stehen nebeneinander, mit Angabe, wer die Auskunft wann gegeben hat.
- **Ein fehlender Eintrag ist kein Beweis,** dass das Ereignis nicht stattfand; die Seite nennt die durchgesehenen Bücher und Jahrgänge.
- **Jede Archivdurchsicht wird protokolliert,** auch ohne Fund, in einem internen Register (`internal/checks/reviewed_documents.md`), damit Jahre später nichts doppelt gesucht wird.
- **Die Arbeitstabelle wird auf der Website nie erwähnt:** Leser sehen nur echte Quellen.

## Voraussetzungen

- [Claude Code](https://claude.com/claude-code) oder eine andere Umgebung mit Unterstützung für Agent Skills.
- Python 3 (nur Standardbibliothek).
- Eine Website mit der erwarteten Struktur: `family_tree_github/` mit `docs/people/`, `docs/sources/{archives,books,photos,websites}/`, `docs/places/`, den Registern und `mkdocs.yml` sowie dem Hook für ID-Links (`hooks/id_links.py`). Die Pfade sind im Skill festgelegt; für eine andere Website passen Sie die Tabelle „Where the output goes“ in `SKILL.md` und den Pfad `DOCS` in `scripts/next_id.py` an (oder setzen die Umgebungsvariable `DOCS`).
- Optional: der Skill **chronology-table**, der chronologische Tabellen (`.ods`, `.xlsx`, `.csv`) liest und automatisch geladen wird, wenn die Eingabe eine Tabelle ist.

## Installation

Der Skill gehört zur Sammlung [genealogy-skills](https://github.com/usuyukiso/genealogy-skills). Klonen Sie die Sammlung und kopieren Sie diesen Ordner zusammen mit **chronology-table**, mit dem der Skill Tabellen liest (der Ordnername ist der Name des Skills):

```bash
git clone https://github.com/usuyukiso/genealogy-skills ~/genealogy-skills
cp -r ~/genealogy-skills/genealogy-biography ~/genealogy-skills/chronology-table <projekt>/.claude/skills/
```

oder in Ihre persönlichen Skills (`~/.claude/skills/`), um sie in allen Projekten zu nutzen. Die übrigen Skills und ihr Zusammenspiel beschreibt das README der Sammlung.

## Verwendung

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code (oder starten Sie ihn direkt mit `/genealogy-biography`), zum Beispiel:

- *«Напиши биографию Евдокии Лапиной по таблице `sources/people_all.xlsx`»*
- *„Aktualisiere die Seite von Grigori Pissarew: Füge die Verlustmeldung von 1943 mit Zitat hinzu.“*
- *„Schreibe eine Biografie anhand dieser drei Kirchenbuch-Scans in Yandex Archive.“*

Die Hilfsskripte lassen sich auch von Hand im Projektstamm ausführen:

```bash
python3 .claude/skills/genealogy-biography/scripts/next_id.py next A A P          # nächste freie IDs
python3 .claude/skills/genealogy-biography/scripts/next_id.py find "23И, оп. 2, д. 24"  # schon auf der Website?
python3 .claude/skills/genealogy-biography/scripts/yandex_archive.py page "<Scan-URL>"
python3 .claude/skills/genealogy-biography/scripts/yandex_archive.py search "Лапина Корсаковск"
```

Am Ende berichtet der Agent, welche Seiten er geschrieben und wiederverwendet hat, wie viele Personen ins Register aufgenommen wurden, welche Einträge nach Scans zitiert sind, welche keinen verfügbaren Text haben und welche Widersprüche geprüft werden sollten.

## Dateien

| Pfad | Zweck |
|---|---|
| `SKILL.md` | Die Anweisungen, denen der Agent folgt |
| `references/terms.md` | Auflösung von Archivabkürzungen (ГИАСО, РГИА ДВ…) und Fachbegriffen der Einträge; wird laufend ergänzt |
| `scripts/next_id.py` | Nächste freie ID, Dublettensuche, Liste aller IDs |
| `scripts/yandex_archive.py` | Erkannter Text und Signatur eines Yandex-Archive-Scans; Archivsuche |

## Einschränkungen

- Maschinell erkannter Text (Yandex Archive) enthält Fehler bei Namen, Zahlen und Daten; der Skill kennzeichnet ihn und verlangt den Abgleich mit dem Scan.
- Der Skill schreibt nur, was die Eingabedaten belegen. Selbst sucht er nur in Yandex Archive; das Auffinden neuer Einträge ist eine eigene Forschungsaufgabe.
- Lebende Personen: Die Website ist öffentlich, veröffentlichen Sie also nur, womit die Familie einverstanden ist.

## Lizenz

[MIT](LICENSE): frei nutzbar, veränderbar und weitergebbar, auch kommerziell; der Urheberrechtshinweis muss erhalten bleiben.
