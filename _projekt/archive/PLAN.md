# ArkuszaAI — Plan architektury i działania
*Ostatnia aktualizacja: 2026-03-21*

---

## Stan obecny

### Gotowe
- [x] CLAUDE.md — pełne instrukcje projektu z pre-flight checklistą
- [x] gotchas.md — 10 udokumentowanych błędów (G01–G10) z regułami
- [x] statystyki_arkuszy.csv — 5 wierszy (Balladyna, Chłopcy, Zemsta, Dziady×2)
- [x] agent generator_arkuszy.md (Opus) — roboczy, do zastąpienia dedykowanymi
- [x] arkusz_utils.py — DO STWORZENIA (wspólne funkcje formatowania)
- [x] Szablon S1 (dramat wierszowany): Balladyna, Zemsta, Dziady cz. II (×2)
- [x] Przepływ: CSV przed draftem → draft+komentarz → akceptacja → Opus generuje

### W toku / następny krok
- [ ] Pierwsza proza (S1c) — lektura do ustalenia z użytkownikiem
- [ ] Refaktor agenta na dedykowane narzędzia (patrz architektura poniżej)

---

## Docelowa architektura narzędzi

### Agenci Opus (.claude/agents/)

```
s1a_dramat_wierszowany.md     Balladyna, Dziady cz. II, Zemsta
s1b_epika_wierszowana.md      Pan Tadeusz, Świtezianka, Reduta Ordona
s1c_proza.md                  Opowieść wigilijna, Kamienie na szaniec,
                              Chłopcy z Placu Broni, Mały Książę,
                              Quo vadis, Syzyfowe prace, Latarnik,
                              Hobbit, Narnia, Akademia Pana Kleksa itd.
s2_grafika_plakat.md          Plakaty, okładki, karty do gry, obrazy
s3_tekst_nieliteracki.md      Teksty popularnonaukowe, publicystyczne
                              + pytania gramatyczne
s4a_ogloszenie.md             Krótka forma: ogłoszenie (3 pkt)
s4b_zaproszenie.md            Krótka forma: zaproszenie (3 pkt)
s5a_opowiadanie.md            Długa forma: opowiadanie (20 pkt)
s5b_rozprawka.md              Długa forma: rozprawka (20 pkt)
s5c_przemowienie.md           Długa forma: przemówienie (20 pkt)
```

### Wspólna biblioteka
```
D:\Dydaktyka\Narzędzia\arkusz_utils.py
```
Funkcje: `para()`, `poem()`, `speaker()`, `blank()`, `answer_line()`,
`task_header()`, `setup_document()`, `save_and_confirm()`
Wszystkie agenty ją importują — formatowanie w jednym miejscu.

---

## Różnice między narzędziami S1a / S1b / S1c

| Cecha | S1a Dramat | S1b Epika wiersz. | S1c Proza |
|-------|-----------|-------------------|-----------|
| Limit fragmentu | 2 str. A4 | 2 str. A4 | 1 str. A4 |
| Formatowanie | Speaker BOLD+CAPS, didaskalia italic | Strofy, wcięcia chóru | Akapity, narracja ciągła |
| Terminologia | osoba mówiąca | narrator | narrator (1. lub 3. os.) |
| Zad. 6 (PP) | tekst poboczny (jeśli didaskalia w fragm.) | narrator + budowa wiersza | narrator i jego funkcja |
| Zad. 4 rotacja | SRODEK / INTERPUNKCJA / SKLADNIA | SRODEK / SRODEK_wierszowy / SKLADNIA | SRODEK / INTERPUNKCJA / SKLADNIA |
| Zad. 7 | całość dramatu | całość poematu | całość powieści/noweli |

## Różnice S4a / S4b

| Cecha | S4a Ogłoszenie | S4b Zaproszenie |
|-------|---------------|-----------------|
| Wymagane elementy | Tytuł OGŁOSZENIE, nadawca, temat, kiedy/gdzie, 2 argumenty | Tytuł ZAPROSZENIE, adresat, okazja, kiedy/gdzie, 2 argumenty (1 dot. tematyki), podpis |
| Punktacja | 0–3 pkt (treść 0–2, język 0–1) | 0–3 pkt (treść 0–2, język 0–1) |

## Różnice S5a / S5b / S5c

| Cecha | S5a Opowiadanie | S5b Rozprawka | S5c Przemówienie |
|-------|----------------|---------------|-----------------|
| Struktura | wstęp+akcja+kulminacja+zakończenie | teza+argumenty+konkluzja | wstęp+argumenty+wezwanie |
| Elementy twórcze | narracja, dialog, opis, punkt kulminacyjny | argumenty z faktów/logiki/emocji | perswazja, argumenty, retoryka |
| Punktacja | 0–20 pkt (8 kryteriów) | 0–20 pkt (8 kryteriów) | 0–20 pkt (8 kryteriów) |

---

## Kolejność budowania narzędzi (priorytet)

1. **arkusz_utils.py** — fundament, wszystko inne go używa
2. **s1c_proza.md** — następny arkusz to proza
3. **s1a_dramat_wierszowany.md** — refaktor obecnego generator_arkuszy.md
4. **s1b_epika_wierszowana.md** — Pan Tadeusz, Świtezianka, Reduta
5. **s2_grafika_plakat.md**
6. **s3_tekst_nieliteracki.md**
7. **s4a_ogloszenie.md** + **s4b_zaproszenie.md**
8. **s5a_opowiadanie.md** + **s5b_rozprawka.md** + **s5c_przemowienie.md**

---

## Zasady niezmienne (skrót)

- CSV: czytaj PRZED draftem, aktualizuj PO zapisie
- Rotacja zad. 3–7: inne typy niż w poprzednim arkuszu tej lektury
- Zad. 6: zawsze z Podstawy programowej I. Kształcenie literackie
- Zad. 7: zawsze cały utwór, bez wydarzeń z fragmentu
- Klucz: tylko na polecenie użytkownika
- Draft pokazuj z komentarzem weryfikacyjnym (pre-flight)
- Tytuły: zawsze kursywą
- Terminologia: osoba mówiąca / narrator — NIE podmiot liryczny
- Pytania: zero podpowiedzi i sugestii odpowiedzi
- Gotchas: czytaj przed każdą generacją

---

## Dostępne narzędzia zewnętrzne
- Gemini CLI, NotebookLM, GitHub — używać proaktywnie
