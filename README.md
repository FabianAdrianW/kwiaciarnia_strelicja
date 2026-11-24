# Kwiaciarnia Strelicja — strona wizytówka

Statyczna strona (jeden `index.html`, bez frameworka) dla Kwiaciarni Strelicja w Oławie i jej dwóch kwiatomatów 24h.

- `index.html` — strona (CSS i JS w pliku)
- `img/` — zdjęcia realizacji (WebP 480/960), logo, faktury tła
- `fonts/` — Fraunces + Inter (OFL), hostowane lokalnie
- `brandbook/` — brand book v1, moodboard, `brandbook.config.json`, decyzje
- `DESIGN.md` — zasady projektu i tokeny, `RESEARCH.md` — dane i źródła
- `KOMBINACJE.md` — wpis do rejestru kombinacji

Podgląd lokalny: `python3 -m http.server` w katalogu repo, potem http://localhost:8000 (fonty nie ładują się z `file://`).
Wdrożenie: dowolny hosting statyczny (GitHub Pages, Netlify).
