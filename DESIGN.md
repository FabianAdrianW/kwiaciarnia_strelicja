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

## Kombinacja (macierz)
| Oś | Wybór |
|---|---|
| Układ | jedna historia przewijana „dzień → noc → dzień” |
| Typografia | szeryf redakcyjny Fraunces + Inter |
| Źródło koloru | logo i szyld (liść, kwiat strelicji, ciemna zieleń szyldu) |
| Hero | duży kadr zdjęcia strelicji przycięty przy krawędzi + typografia |
| Sygnatura | żywy status otwarcia (Europe/Warsaw) + kwiatomat z przegródkami, które się podświetlają; navbar przechodzi w tryb nocny nad sekcją kwiatomatów |

**Złamana konwencja:** kwiaciarnie stawiają sklep na pierwszym miejscu, a automat chowają. Tu kwiatomaty mają własną nocną scenę i są pierwszym linkiem w menu.

**Świadome wyjątki od listy zakazanej:** kremowe tło + terakota CTA i Inter. Decyzja Fabiana z 24.11.2026: zostaje jak w brand booku. Kolory pochodzą z logo, nie z trendu.

## Tokeny
| Token | Jasny | Ciemny | Rola | Źródło |
|---|---|---|---|---|
| `--ink` | #1E3533 | tekst #F1ECE2 | tekst, noc | szyld |
| `--accent` | #2B765C | #6CC3A0 | linki, etykiety, ikony | liść w logo |
| `--cta` | #B8471A | #B8471A | wyłącznie CTA | kwiat strelicji + czerwień róż |
| `--muted` | #5E716C | #B9C6C1 | tekst pomocniczy | szałwia |
| `--paper` / `--bg` | #F8F3EA | #172A2B | tło | len |
| `--bloom` | #E8912A | #E8912A | kropki, linie, nocne akcenty (nigdy tekst na jasnym) | kwiat strelicji |
| `--night` | #16282A | — | sekcja kwiatomatów, stopka | szyld nocą |

Kontrast (AA): ink/len 11,8:1, accent/len 4,9:1, muted/len 4,7:1, biały/cta 5,3:1, bloom/night ≥5,3:1.

## Typografia
Fraunces 400/400i/600 (nagłówki), Inter 400/600 (tekst). OFL, hostowane lokalnie w `fonts/` (latin + latin-ext). Hero `clamp(44px,6.6vw,104px)`, h2 `clamp(34px,5.2vw,68px)`, body 16/1.6.

## Kompozycja (łamanie schematu)
- Każda sekcja ma własne wcięcia: hero `7vw` lewo, okazje `12vw` lewo, noc wyrównana do prawej, pracownia `9vw` prawo, opinie `6vw`.
- Nakładanie: zdjęcie róż w hero zwisa na sekcję okazji, mapa wchodzi na opinie (−110 px), ogromne „4,9” wychodzi poza ekran.
- 4 przejścia z kształtem: fala płatka (hero→okazje), zęby jodły/świerku (okazje→noc), miękka fala (noc→dzień), ząbkowany brzeg bibuły (pracownia→opinie).
- Tła graficzne: faktura lnu (hero), cienie liści strelicji (okazje), nocne niebo z bursztynową poświatą (kwiatomaty), znak strelicji (hero). Wszystkie proceduralne (Pillow), tylko jako faktura.
- Okazje jako bileciki zawieszone na pinezce, różne szerokości i obroty (−2°…+2,2°), ciemny bilecik = CTA.

## Ruch i interakcje
- Navbar: fixed, stała wysokość 72 px. Po scrollu rysuje się linia dolna + cień. Nad sekcją kwiatomatów płynnie przechodzi w tryb nocny (tło, kolor, wersja logo). Kropka w kolorze kwiatu przesuwa się pod aktywnym linkiem, a podkreślenie linku rysuje się od lewej.
- Pnącze pod nagłówkiem okazji rysuje się raz (stroke-dashoffset), listki pojawiają się z opóźnieniem.
- Bileciki po najechaniu: prostują się, unoszą, zdjęcie przybliża się o 6%, pod tytułem rysuje się pnącze.
- Kwiatomat: co 2,6 s zapalają się losowo dwie przegródki; najechanie podświetla przegródkę bursztynem i pokazuje nazwę.
- Przyciski: CTA ciemnieje, słuchawka się obraca.
- `prefers-reduced-motion`: wszystko statyczne. Brak wjeżdżania sekcji.

## CTA
| Sekcja | Akcja główna | Druga |
|---|---|---|
| Navbar | Zadzwoń: 880 056 918 | — |
| Hero | Zadzwoń | Gdzie są kwiatomaty |
| Okazje | ciemny bilecik → Zadzwoń | każdy bilecik = tel: |
| Kwiatomaty | Prowadź (Mapy Google) ×2 | — |
| Pracownia | Jak do nas trafić | — |
| Opinie | Wszystkie opinie w Google | — |
| Dojazd | duży numer, Zadzwoń, Kopiuj numer | Wyznacz trasę |
| Mobile | dolny pasek „Zadzwoń” po przewinięciu | — |

## Zdjęcia
Realizacje z Instagrama @kwiaciarniastrelicjaid. **Zgoda właścicielki: potwierdzona przez Fabiana (24.11.2026).** WebP 480/960, bez EXIF. Rysunek kwiatomatu to ilustracja CSS ze zdjęciami realnych bukietów, podpisana jako „rysunek poglądowy”. Brak zdjęć generowanych przez AI i stocków.

## Do uzupełnienia
- [ ] Zdjęcia kwiatomatów (noc + z bliska) → zastąpią rysunek poglądowy
- [ ] Niedziela: szyld 10–14, Google brak; na stronie „zamknięte”
- [ ] Potwierdzić, że bukiet w wazonie z wodą to stała opcja
- [ ] Przejąć profil Google kwiatomatu w Jelczu-Laskowicach
- [ ] Wektor logo
- [ ] Podpis „Strona: Adrian Wojtasik” do potwierdzenia z firmą
- [ ] Domena
