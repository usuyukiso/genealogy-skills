# Genealogie-Skills

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

**Eine Sammlung von Agent Skills für Claude Code für die dokumentenbasierte Familienforschung zum Russischen Kaiserreich und zur UdSSR:** Archivscans und Kirchenbücher lesen, sie in eine Tabelle und ein Upload-Formular für Archidocs übertragen und Biografien von Vorfahren mit Quellenbelegen für eine Website zur Familiengeschichte schreiben.

Jeder Skill ist ein Ordner mit einer `SKILL.md` (Anweisungen für den Agenten), Hilfsskripten und einem eigenen README. Sie müssen nichts von Hand starten: Sie beschreiben Ihre Aufgabe in einfachen Worten, und Claude startet den passenden Skill. Die Skills geben Arbeit aneinander weiter, daher hilft es, die Kette unten zu kennen.

---

## Die Skills

| Skill | Was er tut | Zum Beispiel fragen |
|---|---|---|
| [archive-scan-search](archive-scan-search/README.de.md) | Durchsucht einen großen Ordner mit Archivscans (Tausende Aufnahmen, viele Akten): Texterkennung jeder Aufnahme, Zuordnung Aufnahme → Akte anhand der Mikrofilmkarten, Suche nach Wortteilen, Prüfung jedes Treffers am Scan, Ortsregister | „Suche das Dorf Glazki in den Akten der Bauernlandbank für den Kreis Rschew“ |
| [metric-book-index](metric-book-index/README.de.md) | Liest ein ganzes Kirchenbuch Aufnahme für Aufnahme und erstellt ein internes Register aller Geburten, Ehen und Todesfälle, mit ★ bei den gesuchten Personen; lässt sich fortsetzen | „Lies die Kirchenbücher von Drogatschewo für 1892 zu Ende“ |
| [scans-to-people-all](scans-to-people-all/README.de.md) | Überträgt eine Beichtliste oder ein Register in `people_all.xlsx` (Blatt `people_all`), eine Zeile pro Person, in der Schreibweise des Dokuments; Zweifelhaftes gelb markiert; hält dann für Ihre Prüfung an | „Trage die Scans 078–081 in people_all ein“ |
| [archidocs-form](archidocs-form/README.de.md) | Erstellt das Archidocs-Upload-Formular aus den von Ihnen geprüften Zeilen, mit modernen Vor- und Vatersnamen; gleicht frühere Teile mit Ihren späteren Korrekturen ab | „Erstelle das Archidocs-Formular für Teil 4“ |
| [chronology-table](chronology-table/README.de.md) | Liest eine chronologische Tabelle (eine Zeile pro Lebensereignis, `.ods/.xlsx/.csv`) zu einer bereinigten Faktenliste mit Quellen, Kommentaren und Links | wird von genealogy-biography genutzt; oder „Prüfe die Tabelle zu Lapina“ |
| [genealogy-biography](genealogy-biography/README.de.md) | Schreibt die Personenseite der Website: Lebensgeschichte mit wörtlichen Zitaten, eine Seite pro Quelle, Namensregister, Verknüpfung mit Orten; baut die Website und prüft die Links | „Schreibe eine Biografie von Jakow Pissarew“ |
| [source-page](source-page/README.de.md) | Erstellt oder korrigiert eine Quellenseite: Jahr vorn im Titel, die Akte wie auf dem Umschlag oder im Archivverzeichnis benannt (in Bordeaux), Lage des Scans, wörtlicher Text mit Herkunftsvermerk, Vermutungen als solche gekennzeichnet; trägt sie in Register, Menü und Prüflisten ein | „Lege eine Quellenseite zur Volkszählung 1709, Dorf Borowowo, an“ |
| [place-page](place-page/README.de.md) | Erstellt oder ordnet eine Dorfseite zeitlich: Kirchengemeinde nach Zeiträumen, Gliederung vor 1917 nach Zeiträumen, alle Erwähnungen in Dokumenten nach Jahren, Schlüsse des Verfassers mit Ankern | „Liste auf der Seite von Gorelik alle Erwähnungen nach Jahren auf“ |
| [replica-birth-certificate-1936](replica-birth-certificate-1936/README.de.md) | Gesetzte Kopie (HTML/CSS nach dem Formular) einer Geburtsurkunde der späten 1930er (Standesamt beim NKWD), auch Zweitschriften nach Kirchenbuch; auf einer Dokumentseite mit wörtlicher Abschrift | „Zeichne die Geburtsurkunde der 1930er nach dem Formular nach“ |
| [replica-birth-certificate-1940s](replica-birth-certificate-1940s/README.de.md) | Dasselbe für eine Geburtsurkunde der Kriegsjahre (etwa 1941–1946, gefaltetes Blatt mit Umschlag) | „Zeichne die Geburtsurkunde von 1944 nach“ |
| [replica-marriage-certificate-1940s](replica-marriage-certificate-1940s/README.de.md) | Dasselbe für eine Heiratsurkunde der 1940er (Standesamtsstempel, Siegel, Namen nach der Ehe) | „Zeichne die Heiratsurkunde von 1945 nach“ |
| [replica-school-certificate-1930s](replica-school-certificate-1930s/README.de.md) | Dasselbe für ein Schulzeugnis der 1930er (Fächer und Noten, Ornamentrahmen) | „Zeichne das Schulzeugnis von 1934 nach“ |

## Wie sie zusammenhängen

```
 Einträge finden                 digitalisieren                   veröffentlichen
 ───────────────                 ──────────────                   ───────────────
 archive-scan-search ─┐
   (große Scan-       │          scans-to-people-all
    Ordner)           │            (people_all)                   chronology-table
 metric-book-index  ──┤               │                                │
   (ein Kirchen-      │          Sie prüfen die Zeilen                 ▼
    buch)             │               ▼                          genealogy-biography
                      │          archidocs-form                  (Personen- und
                      │          (Upload-Formular)                Quellenseiten)
                      │                                                ▲
                      └──────── Fund zu einem Familienmitglied ────────┘
                                 (nur auf Ihren Wunsch)
```

- **Such-Skills ändern die Website nicht.** archive-scan-search und metric-book-index schreiben nur interne Dateien (Register, Notizen, das Durchsichtsprotokoll). Ein Fund wird nur auf Ihren Wunsch zur Website-Seite; dann schreibt sie genealogy-biography.
- **Zwischen den beiden Digitalisierungsschritten prüfen Sie die Tabelle.** scans-to-people-all hält nach dem Schreiben der Zeilen an; archidocs-form arbeitet nur mit geprüften Zeilen.
- **Alles Durchgesehene wird protokolliert,** auch Suchen ohne Fund, in `family_tree_github/internal/checks/reviewed_documents.md`. Jeder Skill liest dieses Protokoll vor der Suche und ergänzt es danach, damit keine Akte zweimal durchsucht wird.
- **Offene Fragen und Widersprüche** zwischen Dokumenten kommen in `research_open_questions.md`.

## Gemeinsame Regeln aller Skills

- Nichts wird erfunden: Namen, Daten, Verwandtschaft, Signaturen und Zitate stammen nur aus Dokumenten. Wo die Dokumente schweigen, steht das so im Text.
- Zitate wörtlich in der Originalschreibung; unsichere Wörter mit `[?]`, unleserliche Stellen mit `[…]`. Maschinell erkannter Text (OCR) dient nur dazu, die Stelle im Scan zu finden, und wird nie ohne Lesen des Scans zitiert.
- Verwandtschaft wird Glied für Glied belegt; Vatersname, gleicher Nachname oder gleiches Dorf sind kein Beweis; Namensvettern bleiben getrennte Personen, bis Dokumente sie unterscheiden.
- Ein fehlender Eintrag ist kein Beweis, dass das Ereignis nicht stattfand.
- Schlussfolgerungen sind als Vermutungen gekennzeichnet, mit dem, was sie bestätigen oder widerlegen könnte.

## Voraussetzungen

- [Claude Code](https://claude.com/claude-code) (oder eine andere Umgebung mit Agent Skills).
- Python 3. Die Tabellen-Skills (scans-to-people-all, archidocs-form) brauchen `openpyxl`; die anderen nur die Standardbibliothek.
- macOS für archive-scan-search und das Zuschneiden von Scans (Swift und die systemeigene Texterkennung Vision).
- Die Projektstruktur, für die die Skills geschrieben sind (die Pfade stehen in den `SKILL.md`-Dateien; für ein anderes Projekt anpassen):

```
<projekt>/
  .claude/skills/          ← diese Skills
  family_tree_github/      ← Website mit MkDocs Material: docs/people, docs/sources, docs/places,
                             internal/checks (Durchsichtsprotokoll, Ortsregister),
                             internal/metrics (Kirchenbuchregister)
  sources/                 ← Scans und Tabellen (people_all.xlsx, Chronologien)
  research_open_questions.md
```

## Installation

Sie brauchen [Git](https://git-scm.com/downloads), Python 3 und [Claude Code](https://claude.com/claude-code) (oder Codex). Für die beiden Tabellen-Skills einmalig `openpyxl` installieren:

```bash
pip3 install openpyxl
```

1. **Repository herunterladen:**

   ```bash
   git clone https://github.com/usuyukiso/genealogy-skills
   ```

2. **Die benötigten Skills in den Ordner `skills` kopieren.** Jeder Skill ist ein Ordner (`genealogy-biography`, `metric-book-index`, …); kopieren Sie den ganzen Ordner.
   - Claude Code: `.claude/skills/` in Ihrem Projektordner (anlegen, falls er fehlt).
   - Codex: `~/.codex/skills/`.

   Kopieren Sie die Skill-Ordner selbst, nicht den ganzen Ordner `genealogy-skills`. genealogy-biography braucht chronology-table, source-page und place-page — kopieren Sie alle vier; source-page und place-page nutzen die Skripte von genealogy-biography.

3. **Claude Code neu starten.** Geben Sie `/` ein — die Skills erscheinen in der Liste. Wie jeder Skill gestartet wird und worum man ihn bittet, steht in seinem eigenen README (Links in der Tabelle oben).

Zum Aktualisieren `git pull` im heruntergeladenen Ordner ausführen und die Skills erneut kopieren.

## Verwendung

1. Öffnen Sie ein Terminal **im Projektordner** (dort, wo `family_tree_github/` und `sources/` liegen) und starten Sie Claude Code: `claude`.
2. Beschreiben Sie die Aufgabe in eigenen Worten, in jeder Sprache. Ein Skill startet von selbst, wenn Ihre Bitte zu ihm passt. Beispiele:
   - „Die Kirchenbücher sollen gelesen und digitalisiert werden“ → metric-book-index
   - „Suche das Dorf Glazki in den Akten der Bauernlandbank für den Kreis Rschew“ → archive-scan-search
   - „Trage die Scans 078–081 in people_all ein“ → scans-to-people-all; Sie prüfen die Zeilen; dann „Erstelle das Archidocs-Formular für Teil 4“ → archidocs-form
   - „Schreibe eine Biografie von Jakow Pissarew nach der Tabelle“ → genealogy-biography (mit chronology-table)
3. Um einen bestimmten Skill selbst zu starten, beginnen Sie die Nachricht mit `/` und seinem Namen: `/metric-book-index lies Drogatschewo zu Ende`.
4. Lange Aufgaben (Texterkennung von Tausenden Aufnahmen, ein ganzes Kirchenbuch) laufen in Schritten; die Skills speichern den Fortschritt in ihren Dateien, sodass Sie anhalten und später „weiter“ sagen können — die Arbeit setzt an derselben Stelle fort.
5. Lesen Sie am Ende den Bericht des Agenten: was gefunden wurde, was nicht, was Sie prüfen sollten. Auf der Website wird nichts veröffentlicht, solange Sie es nicht wünschen.

## Lizenz

[MIT](LICENSE): frei nutzbar, veränderbar und weitergebbar, auch kommerziell; der Urheberrechtshinweis muss erhalten bleiben.
