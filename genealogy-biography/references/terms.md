# Archive codes and record terms

Extend this file as new archives and terms show up in the user's tables.

## Archives

| Code in table | Full name | Notes |
|---|---|---|
| GIASO, ГИАСО | Государственный исторический архив Сахалинской области (Южно-Сахалинск) | Metric books of Sakhalin churches, e.g. fond 23 (often written 23I / 23И) |
| RGIA_DV, РГИА ДВ | Российский государственный исторический архив Дальнего Востока (Владивосток) | Sakhalin administrative files and confession lists |
| GAPK, ГАПК | Государственный архив Приморского края | Primorye metric books (e.g. Шкотовская церковь) |
| RGIA, РГИА | Российский государственный исторический архив (СПб) | |
| GARF, ГАРФ | Государственный архив Российской Федерации | |
| ргБ, РГБ | Российская государственная библиотека | In Chekhov census rows "ргБ № 6864" is the number of the census card in the RSL manuscript collection |

Yandex Archive (`yandex.ru/archive/catalog/<id>/<page>`) hosts scans of archive files;
the last path segment is the scan page. Cite it as: "Скан: Яндекс Архив, <URL>".
Get the recognized text and the catalog path (фонд/опись/дело) with
`scripts/yandex_archive.py page <url>`. The "Лист N" in a page title is Yandex's scan
number. It may differ from the archival sheet (лист) number, so cite it as "л. N (по
нумерации Яндекс Архива)" when in doubt. The year in a recognized page header is often
misread (e.g. "1849" or "1897" for 1893/1895). Trust the table and the catalog instead.

## Reading reference codes

Codes are usually `<date>_<record no>_<event>_<place>_<names>_<archive>_<fond-opis-delo>[_page.N]`.

- `23I-2-9` / `F.23-2-24` / `1133-2-2253` → **ф.** (фонд) – **оп.** (опись) – **д.** (дело): `ф. 23И, оп. 2, д. 9`.
- `page.160`, `л. 160` → **л.** (лист): sheet 160.
- `No.10_No.6` → record numbers (e.g. birth record 10, with a second number for the other twin or another register part).
- Event words: `birth` — рождение/крещение; `wedding` — брак; `death` — смерть; `ispoved` — исповедная роспись; `became_peasant` — перечисление в крестьяне.
- `der.` — деревня/селение (village).

Citation pattern (Russian):
`<Архив>, ф. X, оп. Y, д. Z[, л. N]. <Тип документа> <церкви/учреждения>, <запись № …> от <дата>.`

The original code itself is shown on the source page as the file name in the author's library (see SKILL.md).

## Record types

- **Метрическая книга** — parish register of births/baptisms, marriages, deaths.
- **Исповедная роспись (ведомость)** — annual list of parishioners by household, with ages; shows who lived together.
- **Сахалинская перепись Чехова (1890)** — census of Sakhalin's population conducted personally by A. P. Chekhov, Sept–Oct 1890; card lines are numbered as Chekhov himself describes them in «Остров Сахалин», ch. III
  (https://azbyka.ru/fiction/ostrov-saxalin-iz-putevyx-zametok/3/):
  1 post/settlement; 2 house no. «по казенной подворной описи»; 3 status on Sakhalin
  (каторжный / поселенец / крестьянин из ссыльных / свободного состояния), not the former
  estate; 4 name **and relation to the household head** (хозяин/хозяйка, жена,
  сожительница, сын, работник, жилец; children marked as legitimate/illegitimate, own/adopted);
  5 age; 6 religion; 7 place of birth; 8 year of arrival on Sakhalin; 9 «главное занятие и
  ремесло»; 10 literacy («Умеешь ли читать?»); 11 marital status «женат, вдов, холост? Если
  женат, то где: на родине, на Сахалине?» («одинок» = formally married but living alone);
  12 «получает ли пособие от казны?».
  Popular retellings sometimes claim line 9 is the term of penal servitude and line 12 is
  cohabitation. That is wrong: cohabitation goes in line 4. When a Chekhov card is cited,
  add a line-by-line decoding table to the sources file. Its columns are: line, Chekhov's
  words, explanation, and the person's value.
- **Восприемник/восприемница** — godparent at a baptism; shows the person's social ties in the community.

## Status terms (звание)

- **Ссыльнокаторжный(ая)** — convict serving penal servitude (каторга).
- **Ссыльнопоселенец / поселенка, «поселка»** — exile-settler: after serving the term, released from prison to live in a settlement on the island but still not free to leave.
- **Крестьянин(ка) из ссыльных** — after (usually 10) years as a settler, could be enrolled as a peasant, gaining the right to leave Sakhalin for the mainland (often Primorye / Amur region).
- **Гражданин(ка)** — post-1917 designation replacing estate titles.
- **«Женат(а) на родине»** — census note: married back home; a spouse remained in European Russia. A later Sakhalin marriage usually required the earlier one to be dissolved (брак расторгнут).
- **Н[езаконнорожденный]** — born outside wedlock.

## Dates

Pre-1918 Russian records use the Julian calendar. A form like `17/30.06.1921` gives
Julian/Gregorian. Keep dates as in the source; mention the double date when given.

## Pskov archives and terms (added 2026-10-11)

| Code in table | Full name | Notes |
|---|---|---|
| GAPO, ГАПО | Государственный архив Псковской области | f. 39 — Псковская духовная консистория (исповедные росписи); f. 58 — Псковская казённая палата (ревизские сказки 1782–1858) |
| RGADA, РГАДА | Российский государственный архив древних актов (Москва) | f. 350 — ландратские книги и ревизские сказки (II–III ревизии, 1745, 1763) |

- **Ревизская сказка** — name list of tax-paying population at a revision (census) of the 18th–19th c.; before 1763 men only.
- **Дворцовая вотчина** (Вороницкая) — estate whose peasants belonged to the imperial family; from 1797 — **удельные** крестьяне (Департамент уделов); by the 1840s Makovitsy peasants are written «Государственных имуществ» (state peasants). **Губа** — district of the Voronich palace estate (Богородицкая, Ильинская, Спасская…). **Экономическая вотчина** — former church lands secularised in 1764.
- Old patronymic form: «Иван Давыдов» = Иван, сын Давыда (not yet a surname).
