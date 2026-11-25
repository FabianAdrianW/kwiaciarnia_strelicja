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

## Kombinacja v2 (redesign 25.11.2026, na prośbę Fabiana: mniej szablonowo, bez karteczek i krzywizn, płynnie)
| Oś | Wybór |
|---|---|
| Układ | jedno płótno bez granic sekcji; kolor tła interpoluje się przy scrollu (len → szałwia → noc → len) |
| Typografia | Fraunces (duże, redakcyjne nagłówki, italic w kolorze liścia) + Inter |
| Źródło koloru | logo i szyld |
| Hero | „otwierane okno”: hasło na środku, pod nim wąskie okno ze strelicją; przy scrollu okno rośnie do pełnego ekranu i przechodzi w zdjęcie pracowni → galeria |
| Sygnatura | rysunkowe motywy kwiatów w tle (strelicja, liść, eukaliptus, róża, gerbera, pnącze), rysowane kreską przy scrollu z paralaksą + zegar 24h przy kwiatomatach |

**Złamana konwencja:** kwiatomaty jako pełna nocna scena z zegarem dobowym (pierwszy link w menu), a nie dopisek w stopce.
**Świadome wyjątki od listy zakazanej:** kremowe tło + terakota CTA, Inter (decyzja Fabiana 24.11.2026).

## Tokeny
| Token | Jasny | Ciemny | Rola |
|---|---|---|---|
| `--ink` / `--text` | #1E3533 | #F1ECE2 | tekst |
| `--accent` | #2B765C | #6CC3A0 | nagłówki italic, linki, motywy |
| `--cta` | #B8471A | #B8471A | wyłącznie CTA |
| `--muted` | #5E716C | #B9C6C1 | tekst pomocniczy |
| `--bg-paper` | #F8F3EA | #172A2B | tło: hero, galeria, pracownia, kontakt |
| `--bg-sage` | #ECEEE3 | #1B3130 | tło: okazje, opinie |
| `--bg-night` | #16282A | #0F1E1F | kwiatomaty, stopka |
| `--bloom` | #E8912A | #E8912A | kropki, wskaźniki, motywy (nigdy tekst na jasnym) |

## Sekcje
1. **Hero** (sticky 210vh): status na żywo, hasło, jedno CTA „Kwiatomaty 24/7” (telefon jest w navbarze); okno (proporcje zdjęcia 4:5) rośnie do pełnego ekranu wyłącznie przez `transform: scale` z kontr-skalą wnętrza (GPU), a przewijanie jest wygładzane (lerp 0,16 w pętli rAF), więc animacja jest płynna także przy skokowym kółku myszy. Crossfade na zdjęcie pracowni, podpis „Zobacz, co wiążemy”.
2. **Galeria** (v4, redakcyjne rozkładówki): siatka 12 kolumn, po 5 zdjęć na rozkładówkę w dwóch lustrzanych układach (duży kadr + mniejsze z przesunięciami i pustą przestrzenią) i kafel z prawdziwym cytatem z opinii; mobile: układ 6-kolumnowy. Odsłanianie maską od dołu z zoomem, hover: przygaszenie pozostałych zdjęć, przybliżenie, podpis z kategorią, kursor systemowy zoom-in, 2 kafle z cytatami na rozkładówkę (10 prawdziwych opinii). 10 zdjęć + „Pokaż więcej zdjęć (n)”. Filtry: Bukiety, Okazje, Święta, Pracownia. Lightbox FLIP z miniatury, strzałki, klawiatura, swipe, licznik.
3. **Okazje** (v4): 5 rozsuwanych paneli ze zdjęciami; zamknięty panel pokazuje pionowy tytuł i ikonę strelicji, najechanie/fokus/klik rozsuwa panel (flex 1 → 4,6), zdjęcie wyostrza się i odzoomowuje, wjeżdża tytuł, opis i CTA. Mobile: panele w pionie (76 px → 440 px).
4. **Kwiatomaty** (noc, v5, problem → rozwiązanie): nagłówek „Kwiaciarnia zamknięta? Kwiatomat nie.”, duże „24/7”. Komponent scenariuszy: lista sytuacji (Teraz — na żywo, 6:40 urodziny w pracy, 21:30 zapomniana rocznica, niedziela 11:00 imieniny mamy, 23:10 późny powrót) i scena z dużą godziną, statusem kwiaciarni (zamknięta/otwarta, liczone z prawdziwych godzin) i świecącym „Kwiatomaty: otwarte”, problemem klienta i rozwiązaniem z adresami + przyciski nawigacji. Autoodtwarzanie co 6 s z paskiem postępu, pauza na hover, klik/strzałki. Pod spodem 2 panele z mapą, 3 kroki, opinia o kwiatomacie.
5. **Pracownia** (v5): mieści się w jednym ekranie — u góry zdanie o Iwonie + 4 fakty i CTA, pod spodem pas 3 zdjęć (lada, dostawa, witryna) o szerokościach wg proporcji, każde z inną paralaksą i podpisem.
6. **Opinie**: „4,9” w dużej skali, rotator jednej opinii (7 s, pasek postępu, pauza na hover/focus, strzałki), taśma krótkich cytatów (pauza na hover).
7. **Kontakt**: duży numer, kopiowanie, godziny z podświetleniem dzisiejszego dnia, mapa.

## Ruch
Skala v4: wszystkie wymiary CSS ×0,85 (odpowiednik 85% zoomu), tekst min. 15 px, cele dotykowe min. 44 px. Wydajność: kolor tła na trzech warstwach `position:fixed` przenikanych przez `opacity` (bez repaintu całej strony), navbar bez `backdrop-filter`, okno hero tylko `transform`, zdjęcie hero w pełnych proporcjach (bez przycięcia).
Kicker sekcji: ikona strelicji (maska SVG, kolor kwiatu) zamiast kreski.
Jedna pętla rAF na scroll: tło, hero, galeria, motywy, zegar, paralaksa, wskaźnik menu. Navbar: fixed, stała wysokość; po scrollu pojawia się tło w aktualnym kolorze strony i linia; nad nocą przechodzi w jasny tekst i ciemną wersję logo; hover linku: tekst wysuwa się w górę, a z dołu wjeżdża italic w kolorze kwiatu; aktywna sekcja = linia pod linkiem przesuwana płynnie. `prefers-reduced-motion`: bez przypięć i animacji, motywy narysowane.

## Pliki
`src/index.src.html` + `tools/build.py` (galeria z `tools/gallery.json`, motywy SVG) → `index.html`. `python3 tools/build.py --preview OUT.html` daje plik z osadzonymi zasobami.

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
