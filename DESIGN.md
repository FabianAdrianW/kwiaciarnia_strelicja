# DESIGN.md — Kwiaciarnia Strelicja (Oława)

Źródło prawdy dla strony. Tokeny zgodne z `:root` w `index.html` i z `brandbook/brandbook.config.json`.

## Podmiot i cel
Kwiaciarnia Iwony Dąbrowy, ul. Wiejska 28A, Oława, i dwa kwiatomaty 24/7: Oława, Lipowa 1c oraz Jelcz-Laskowice, Oławska 27. Strona ma prowadzić do telefonu (880 056 918) i reklamować kwiatomaty, które są głównym przychodem.

## Wywołane skille
- `brand-book` (LITE): moodboard + brand book v1 (`brandbook/`)
- `generator-wizytowek`: proces, macierz, testy
- `ui-ux-pro-max`: `--design-system --variance 8 --motion 5 --density 4` + `--domain typography`. **Odrzucono:** brutalizm, róż jako CTA, lejek 3-krokowy (nie pasują do kwiaciarni). **Wzięto:** asymetrię, treści sezonowe (osobna karta „Święta i sezon”), dbałość o jakość zdjęć.
- Zestaw narzędzi `generator-wizytowek` (tools/, KOMBINACJE.md) był niedostępny w sesji, więc obróbkę zdjęć i testy zrobiłem ręcznie (Pillow + Playwright).

## Ziarna → oś strony
1. **Kwiatomat 24h** (dwa miasta) → szkło, przegródki, nocne światło → ciemna zieleń szyldu + bursztyn → ruch: przegródki „zapalają się” → słowo: *o każdej porze*.
2. **Strelicja** (nazwa i logo) → ostry płatek, pomarańcz → hasło w Fraunces italic.
3. **Pnącze z logo** → cienka linia z listkami → separator, podkreślenie, hover.
4. **Bukiet w wazonie z wodą** (opinie) → wyróżnik w sekcji Pracownia.
5. **Pani Iwona** (opinie po imieniu) → głos marki: na Ty, ciepło, konkretnie.

## Kombinacja v6 (przebudowa 25.11.2026: „Dwie drogi”)
Powód: v2–v5 były niespójne, przejścia agresywne (przeskok w tryb nocny, przypięty hero), a strona nie sprzedawała ani pracowni, ani kwiatomatów. v6: jedno ciepłe tło (len), zero zmian koloru strony przy scrollu, jedyny ruch to delikatne pojawianie się treści (fade-up 18 px), rysowanie motywów i hovery.

| Oś | Wybór |
|---|---|
| Układ | jedna szerokość treści (max 1320 px), rytm: hero → dwie drogi → panel kwiatomatów → pracownia → galeria → opinie → karta kontaktu |
| Typografia | Fraunces + Inter, nagłówki z drugą linią italic w kolorze liścia |
| Kolor | len (tło), szałwia (panel kwiatomatów), bursztyn (karta kwiatomatu, akcenty 24/7), butelkowa zieleń (scena scenariuszy, karta kontaktu), terakota tylko na „Zadzwoń/Zamów” |
| Hero | zapraszający: tekst + zdjęcie pracowni z wolnym Ken Burns, plakietka „24/7 kwiatomaty”, karta „Dziś: pracownia / kwiatomaty” z prawdziwymi godzinami |
| Sygnatura | dwie równorzędne karty „Wpadnij do pracowni” / „Kwiatomat zawsze otwarty” + scenariusze „Kiedy kwiatomat ratuje sytuację” |

**Świadome wyjątki od listy zakazanej:** kremowe tło + terakota CTA, Inter (decyzja Fabiana 24.11.2026).

## Tokeny
| Token | Wartość | Rola |
|---|---|---|
| `--ink` | #1E3533 | tekst, ciemne karty |
| `--accent` | #2B765C | italic w nagłówkach, linki |
| `--cta` | #B8471A | wyłącznie telefon (navbar, pracownia, okazje, kontakt, pasek mobilny) |
| `--paper` | #F8F3EA | tło całej strony |
| `--sage` | #ECEEE3 | panel kwiatomatów |
| `--bloom` / `--amber` | #E8912A / #F4B866 | kwiatomat, 24/7, ikony strelicji |
| `--muted` | #5E716C | tekst pomocniczy |
Promienie: 4 px (drobne), 14 px (karty, zdjęcia), 18–28 px (panele). Przyciski-pigułki.

## Sekcje
1. **Hero**: status na żywo, „Świeże kwiaty o każdej porze.”, zaproszenie do pracowni + informacja o kwiatomatach, CTA „Odwiedź pracownię” i „Znajdź kwiatomat” (telefon tylko w navbarze), 4,9 ★. Zdjęcie wnętrza pracowni, plakietka 24/7, karta dzisiejszych godzin.
2. **Dwie drogi**: karta pracowni (zdjęcie lady, godziny, dowóz) i bursztynowa karta kwiatomatu (24/7, adresy). Hover: zoom zdjęcia, strzałka.
3. **Kwiatomaty** (panel szałwiowy): „Kwiaciarnia zamknięta? Kwiatomat nie.”, 3 korzyści, scenariusze (Teraz na żywo, 6:40, 21:30, niedziela 11:00, 23:10) z ciemną sceną: godzina, status pracowni vs kwiatomatu, problem, rozwiązanie, przyciski nawigacji; 2 karty lokalizacji z mapą; opinia o kwiatomacie.
4. **Pracownia**: kolaż 3 zdjęć, „Bukiet związany przy Tobie.”, o Iwonie, 4 fakty, „Zamów” + „Jak dojechać”; okazje jako 5 rozsuwanych paneli.
5. **Galeria**: rozkładówki z 2 cytatami z opinii, filtry-pigułki, „Pokaż więcej”, lightbox FLIP.
6. **Opinie**: 4,9 + rotator z paskiem postępu.
7. **Kontakt**: ciemna karta z dużym numerem, godzinami (dziś podświetlony), mapą.

## Ruch
Tylko: fade-up przy wejściu w widok (raz), rysowanie motywów kwiatowych (raz), Ken Burns zdjęcia hero, hover kart/zdjęć, przełączanie scenariuszy i opinii z paskami postępu. Brak przypinania, paralaksy i zmiany koloru tła. `prefers-reduced-motion`: wszystko statyczne.

## Pliki
`src/index.src.html` + `tools/build.py` (galeria z `tools/gallery.json`, motywy SVG; poprzednia wersja v5 w historii git) → `index.html`. `python3 tools/build.py --preview OUT.html` daje plik z osadzonymi zasobami.

## Zdjęcia
Realizacje z Instagrama @kwiaciarniastrelicjaid. **Zgoda właścicielki: potwierdzona przez Fabiana (24.11.2026).** WebP 480/960, bez EXIF. Galeria: 24 zdjęcia, WebP 640/1280. Motywy kwiatowe to rysunki wektorowe (tools/build.py), tylko dekoracja tła. Brak zdjęć generowanych przez AI i stocków.

## Do uzupełnienia
- [ ] Zdjęcia kwiatomatów (noc + z bliska) → do galerii i sekcji kwiatomatów
- [ ] Niedziela: szyld 10–14, Google brak; na stronie „zamknięte”
- [ ] Potwierdzić, że bukiet w wazonie z wodą to stała opcja
- [ ] Przejąć profil Google kwiatomatu w Jelczu-Laskowicach
- [ ] Wektor logo
- [ ] Podpis „Strona: Adrian Wojtasik” do potwierdzenia z firmą
- [ ] Domena
