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
| Hero (v8) | hasło po lewej, po prawej duże zdjęcie kompozycji ze strelicją (#47) wtopione w tło maską gradientu, podpis „Strelicja: kwiat, od którego wzięliśmy nazwę”; taśma bukietów przeniesiona nad stopkę (Instagram) |
| Sygnatura | linie „problem? → Kwiatomat: otwarte.” + mapa „Gdzie masz najbliżej?” z czasem dojazdu |

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
1. **Hero** (v7): status na żywo, hasło, zaproszenie, 2 CTA, ocena 4,9 i link do kwiatomatów, taśma bukietów (marquee 70 s, maska na krawędziach, `prefers-reduced-motion` = stop).
2. **Dwie drogi**: karta pracowni (zdjęcie lady, godziny, dowóz) i bursztynowa karta kwiatomatu (24/7, adresy). Hover: zoom zdjęcia, strzałka.
3. **Kwiatomaty** (v7): „Kwiaciarnia zamknięta? Kwiatomat nie.”; 6 linii pytanie → „Kwiatomat: otwarte.” (pierwsza na żywo z aktualną godziną; odpowiedź wjeżdża po wejściu w widok); ciemna karta 24/7 z adresami; **wyszukiwarka „Gdzie masz najbliżej?”**: mapa Leaflet (lokalnie w `vendor/leaflet`, kafle OpenStreetMap (bez klucza API, ocieplone filtrem CSS), atrybucja i link „Zgłoś błąd mapy” w rogu) z pinezkami pracowni i 2 kwiatomatów, przycisk geolokalizacji (dane zostają w przeglądarce) ; lista sortowana po odległości z czasem dojazdu autem (szacunek: odległość w linii prostej × 1,35, 28/45/60 km/h), statusem otwarcia, plakietką „najbliższy kwiatomat” i „Prowadź” do Map Google; opinia o kwiatomacie.
4. **Pracownia**: kolaż 3 zdjęć, „Bukiet związany przy Tobie.”, o Iwonie, 4 fakty, „Zamów” + „Jak dojechać”; okazje jako 5 rozsuwanych paneli.
5. **Galeria**: rozkładówki z 2 cytatami z opinii (bez przygaszania zdjęć na hover), filtry-pigułki, „Pokaż więcej”, lightbox FLIP.
6. **Opinie**: 4,9 + rotator z paskiem postępu.
7. **Kontakt**: ciemna karta z dużym numerem, godzinami (dziś podświetlony) i przyciskiem do mapy.

## Ruch
Tylko: fade-up przy wejściu w widok (raz), rysowanie motywów kwiatowych (raz), wolna taśma bukietów w hero, wjazd „Kwiatomat: otwarte.” w liniach, hover kart/zdjęć, przelot mapy do wybranego punktu, rotator opinii z paskiem postępu. Brak przypinania, paralaksy i zmiany koloru tła. `prefers-reduced-motion`: wszystko statyczne.

## Pliki
`src/index.src.html` + `tools/build.py` (galeria z `tools/gallery.json`, motywy SVG; poprzednia wersja v5 w historii git) → `index.html`. `python3 tools/build.py --preview OUT.html` daje plik z osadzonymi zasobami.

## Zdjęcia
Realizacje z Instagrama @kwiaciarniastrelicjaid. **Zgoda właścicielki: potwierdzona przez Fabiana (24.11.2026).** WebP 480/960, bez EXIF. Galeria: 24 zdjęcia, WebP 640/1280. Motywy kwiatowe to rysunki wektorowe (tools/build.py), tylko dekoracja tła. Brak zdjęć generowanych przez AI i stocków.

## Do uzupełnienia
- [ ] Kafle OSM (tile.openstreetmap.org) zgodnie z polityką OSMF: dozwolone przy małym ruchu, wymagana atrybucja; przy dużym ruchu przejść na własne kafle/komercyjnego dostawcę (URL w `initMap()`)
- [ ] Zdjęcia kwiatomatów (noc + z bliska) → do galerii i sekcji kwiatomatów
- [ ] Niedziela: szyld 10–14, Google brak; na stronie „zamknięte”
- [ ] Potwierdzić, że bukiet w wazonie z wodą to stała opcja
- [ ] Przejąć profil Google kwiatomatu w Jelczu-Laskowicach
- [ ] Wektor logo
- [ ] Podpis „Strona: Adrian Wojtasik” do potwierdzenia z firmą
- [ ] Domena

## v8 (27.11.2026)
- Hero: zdjęcie strelicji wtopione w tło zamiast taśmy (taśma nad stopką jako pasek Instagrama).
- Kwiatomaty: dwie kolumny (intro + 5 linii), usunięta ciemna karta 24/7 i powtórzony cytat; sekcja ok. 38% niższa na desktopie.
- Mobile (27.11): karta kwiatomatu wjeżdża na przyklejoną kartę pracowni; pytania jako jedna rotująca linia nad stałym „Kwiatomat: otwarte.”; okazje jako przyklejona scena (pozycja przewinięcia wybiera otwarty panel, nic nie da się przeskoczyć).
- Mapa usunięta (Leaflet wyrzucony z repo); „Dojazd” to lista 3 punktów z czasem dojazdu po „Użyj mojej lokalizacji”.
- Przycisk „Prowadź” (pasek mobilny obok „Zadzwoń”, navbar na desktopie): najbliższy punkt otwarty teraz; bez zgody na lokalizację → Kwiatomat Oława; poza godzinami „Do kwiatomatu”. iOS: panel wyboru Mapy Apple / Google Maps (comgooglemaps://) / Waze; Android i desktop: Google Maps od razu.
