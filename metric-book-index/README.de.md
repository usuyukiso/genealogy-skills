# metric-book-index

Sprachen: [English](README.md) / [Русский](README.ru.md) / [Українська](README.uk.md) / [Deutsch](README.de.md)

Teil der Sammlung [genealogy-skills](../README.de.md).

Liest ein ganzes Kirchenbuch einer Pfarrei (Geburten, Ehen, Todesfälle) anhand der Scans, Aufnahme für Aufnahme, und schreibt **jeden** Eintrag auf — nicht nur die gesuchten. So entsteht ein internes Register: Fragen wie „Wer war Pate?“ oder „Wann starb dieses Kind?“ lassen sich später daraus beantworten, ohne die Scans erneut zu öffnen. Gesuchte Personen sind mit ★ markiert.

## Wie starten

Der Skill startet von selbst, wenn Ihre Bitte zu ihm passt — beschreiben Sie die Aufgabe einfach in Claude Code, zum Beispiel:

- „Die Kirchenbücher von Drogatschewo sollen gelesen und digitalisiert werden“
- „Lies die Kirchenbücher von Drogatschewo ab 1892 zu Ende“
- „Finde in diesem Buch alle Charlamows und alle mit dem Vatersnamen Anissimowitsch“

Oder direkt starten: `/metric-book-index <Buch oder Ordner>`.

Lange Bücher werden in Abschnitten gelesen. Wenn Sie aufhören, sagen Sie beim nächsten Mal „weiter“ — der Skill setzt bei der Aufnahme fort, an der er stehen blieb.

## Was Sie bekommen

- Eine Registerdatei: ein Abschnitt pro Jahr, Tabellen der Geburten, Ehen und Todesfälle — Aufnahme, Blatt, Eintragsnummer, Datum, Dorf, Eltern bzw. Brautpaar, Paten bzw. Trauzeugen, Todesursache — mit Querverweisen („gestorben … (Aufnahme 260)“).
- Eine Notizdatei: wonach gesucht wurde, was gefunden wurde (★) nach Familien, Widersprüche zwischen Einträgen, was erneut zu lesen oder als Nächstes zu beschaffen ist.
- Monats- und Jahressummen, abgeglichen mit der Übersicht am Ende des Buches.
- Einträge im Durchsichtsprotokoll und in der Liste offener Fragen. Die Website wird nicht verändert.

## Was er braucht

- Die Scans in einem Ordner; macOS zum Zuschneiden und Vergrößern der Scans (Swift, Skript enthalten).

Die Anweisungen für den Agenten stehen in [SKILL.md](SKILL.md).
