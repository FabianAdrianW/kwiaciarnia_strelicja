# Strelicja — design.md (dla strony)

Źródło prawdy: `brandbook.config.json` + `Strelicja_Brand_Book_v1`.

## Reguły wyglądu
- Tło len `#F8F3EA`; tekst ink `#1E3533`; akcent liść `#2B765C`; CTA terakota `#B8471A`.
- `#E8912A` (kwiat) tylko jako linia/kropka/dekor — nigdy tekst na jasnym (2,2:1).
- Czerwień róż wyłącznie na zdjęciach.
- Fraunces 400 (nagłówki, druga linia italic w kolorze liścia), Inter 400/600 (tekst, etykiety, przyciski). Bez fontów odręcznych.
- Radius 3px, linie 1px `#DDD5C6`, grid 12 kolumn, max 70ch.
- Schemat sekcji: eyebrow → h2 → lead → 1 CTA.

## Motyw: pnącze
SVG z logo (linia ink + listki liść + 2 kropki kwiat). Wystąpienia: separator sekcji, podkreślenie h2, hover menu (rysowanie od lewej), hover kafelka okazji, rysowanie przy wejściu w viewport (stroke-dashoffset, 600–900 ms, listki +80 ms).

## Interakcje
- Navbar: przezroczysty na hero → ink po scrollu (300 ms). „Zadzwoń” zawsze widoczny; mobile: sticky bar u dołu.
- Kafelki: zdjęcie scale 1.04, border liść, linia pnącza pod tytułem.
- Przyciski: terakota → `#9E3C15`, ikona telefonu +2 px.
- `prefers-reduced-motion`: wszystko statyczne.

## Struktura strony
Hero → Kwiatomaty 24h (2 adresy + mapa, terakota) → Okazje (5–6 kart) → Pracownia i Iwona → Opinie (4,9★, 78) → Dojazd i godziny → Stopka.
Kwiatomaty muszą być widoczne bez przewijania na 375 px (min. przycisk/link w hero).

## Dostępność
AA dla wszystkich par tekst/tło (tabela w rozdz. 07). Linki tel: na każdym CTA. Alt dla zdjęć realizacji opisowy, krótki.

## Decyzje (D)
- Niebieski z logo usunięty z palety (trzecia rodzina barw).
- Kościoły bez wyróżnienia.
- Brak stocków i AI; tylko realizacje z IG + sesja do zrobienia (kwiatomat noc/z bliska, ręce Iwony, bukiet w wazonie, witryna).
- Logo raster → potrzebny wektor przed drukiem i oklejeniem.

## TODO przed stroną
- [ ] zdjęcia kwiatomatów
- [ ] potwierdzić niedzielę 10–14
- [ ] przejąć profil Google kwiatomatu Jelcz-Laskowice (Oławska 27)
- [ ] wektor logo
