# ArkuszaAI — Instrukcje projektu

## Pierwszeństwo dokumentów
Czytaj PRZED wszystkim innym: `D:\Dydaktyka\PROTOKOL_WSPOLPRACY.md`
Ten dokument jest Konstytucją projektu — nadrzędny wobec wszystkich innych instrukcji.

## Główna funkcja
Tworzenie kart pracy (arkuszy) do egzaminu E8 z pytaniami dostosowanymi do wybranych fragmentów lektur obowiązkowych.

---

## Przepływ pracy (OBOWIĄZKOWY)

### KROK 1 — Przed draftem: czytam CSV
Otwieram `statystyki_arkuszy.csv` i sprawdzam:
- które fragmenty tej lektury były już użyte → wybieram inny
- jakie typy pytań (zad. 3–7) były użyte w ostatnim arkuszu → wybieram inne

### KROK 2 — Wybieram fragment
- Nieprzekoroczony limit stron (dramat/wiersz: 2 str. A4; proza: 1 str. A4)
- Fragment ORYGINALNY z pliku tekstowego lektury, bez zmian

### KROK 3 — Draftuję pytania
- Wzorując się na banku pytań (S1–S5), NIE cytuję bezpośrednio
- Stosuję rotację typów dla zad. 3–7 (patrz tabela rotacji)

### KROK 4 — Pre-flight checklist (PRZED pokazaniem użytkownikowi)
Weryfikuję SAMODZIELNIE każdy punkt:
```
☐ Fragment mieści się w limicie stron?
☐ Zad. 1 = P/F, Zad. 2 = Wielokrotny wybór?
☐ Zad. 3–5 używają innych typów niż w poprzednim arkuszu tej lektury?
☐ Zad. 6 pochodzi z Podstawy programowej (I. Kształcenie literackie)?
   — Dramat z didaskaliami w fragmencie → tekst poboczny
   — Dramat bez didaskaliów / wiersz / proza → inne zagadnienie z PP
☐ Zad. 7 dotyczy CAŁEGO utworu, bez wydarzeń z użytego fragmentu?
☐ Żadne pytanie nie zawiera sugestii ani podpowiedzi co do odpowiedzi?
☐ Tytuły utworów w pytaniach są kursywą?
☐ Terminologia zgodna z projektem (osoba mówiąca / narrator, NIE podmiot liryczny)?
☐ Klucz odpowiedzi jest POMINIĘTY (podajemy tylko na polecenie)?
```

### KROK 5 — Pokazuję draft + komentarz weryfikacyjny
Format:
> **[PRE-FLIGHT: OK / UWAGA]** + co sprawdziłem i czy coś wzbudziło wątpliwość

Czekam na akceptację użytkownika.

### KROK 6 — Po akceptacji: agent `generator_arkuszy` (Opus)
Generuje docx → zapisuje w `ArkuszeAI\` → aktualizuje CSV → zwraca potwierdzenie.

---

## Format karty
- **Nagłówek fragmentu**: autor, *tytuł kursywą*, akt/rozdział/część
- **7–8 zadań**: P/F → Wielokrotny wybór → Krótkie odpowiedzi → Cały utwór
- **Marginesy**: 1,27 cm (wszystkie)
- **Czcionka**: Times New Roman 12pt
- **Linie odpowiedzi**: `'_' * 90`
- **Interlinia fragmentu poetyckiego/dramatycznego**: Pt(14) ≈ 120%
- **Margines dolny akapitu**: space_after=Pt(2)
- **Format**: A4, czarno-biały (do druku)
- **Limit fragmentu**: dramat/wiersz → max 2 str. A4 | proza → max 1 str. A4

## Format cytatów literackich
- **Cytaty ORYGINALNE** — bez zmian, parafrazy ani adaptacji
- **Proza**: zwykły tekst, TNR 12pt
- **Dramat wierszowany**: wiersze, didaskalia *kursywą*, postacie WERSALIKAMI + bold
- **Wiersze**: TNR 12pt

---

## Rotacja pytań

### Zad. 1–2: STAŁE
| Nr | Typ |
|----|-----|
| 1 | Prawda/Fałsz |
| 2 | Wielokrotny wybór |

### Zad. 3–5: ROTACJA (inne typy niż w poprzednim arkuszu z tej lektury)
| Nr | Opcje |
|----|-------|
| 3 | `CYTAT` / `FRAZEOLOGIZM` / `SLOWNIK` |
| 4 | `SRODEK` / `INTERPUNKCJA` / `SKLADNIA` |
| 5 | `CECHY` / `INNA_LEKTURA` / `NARRACJA` |

### Zad. 6: ZAWSZE z Podstawy programowej — I. Kształcenie literackie
| Gatunek | Pytanie 6 |
|---------|-----------|
| Dramat z didaskaliami w fragmencie | Tekst poboczny — nazwa, funkcja, 2 przykłady |
| Dramat bez didaskaliów w fragmencie | Zagadnienie z PP (gatunek, osoba mówiąca, tematyka) |
| Epika / proza | Narrator i jego funkcja — z PP |
| Wiersz / utwór synkretyczny | Narrator, budowa (wers, strofa, rym) — z PP |

**NIGDY**: kreatywna forma pisemna → należy do Części II E8

### Zad. 7: ROTACJA — ZAWSZE cały utwór, NIGDY tylko fragment
| Opcje |
|-------|
| `CALOSC` — wiedza o całości (opisz, wyjaśnij) |
| `CHRONOLOGIA` — zdarzenia z całego dzieła, **z pominięciem tych z fragmentu** |
| `POWIAZANIE` — powiązanie z innymi wątkami / postaciami |

---

## Terminologia (OBOWIĄZUJE W CAŁYM PROJEKCIE)
| Gatunek | Termin |
|---------|--------|
| Dramat | **osoba mówiąca** |
| Epika / proza | **narrator** (1-osobowy lub 3-osobowy) |
| Pan Tadeusz, Świtezianka, Reduta Ordona | **narrator** |
| **ZAKAZANE** | ~~podmiot liryczny~~ |

- Pytanie o didaskalia → użyj **tekst poboczny** w treści pytania (nigdy „didaskalia" jako podpowiedź)
- **Tytuły utworów zawsze kursywą** — w pytaniach, poleceniach i treści arkusza
- **NIGDY** sugestii ani podpowiedzi w treści pytania

---

## Zasady tworzenia pytań
- Każdy fragment = nowe pytania wzorowane na banku, NIE cytowane z bazy
- Klucz odpowiedzi — tylko na polecenie użytkownika
- Zadanie 5 (INNA_LEKTURA) — dokładna formuła:
  > *Spośród lektur obowiązkowych — innych niż [tytuł] — wybierz tę, w której [kryterium]. Podaj tytuł lektury i imię bohatera. Uzasadnij wybór, przywołując konkretną sytuację z tekstu.*
  > Tytuł i bohater: `______` Uzasadnienie: `______` (×3)

---

## Statystyki (CSV)
`D:\Dydaktyka\ArkuszeAI\statystyki_arkuszy.csv`

| Kiedy | Co robię |
|-------|----------|
| **PRZED draftem** | Czytam CSV → sprawdzam użyte fragmenty i typy pytań |
| **PO zapisie docx** | Dodaję wiersz z typami zad. 3–7, datą, uwagami |

---

## Szablony pytań
`D:\Dydaktyka\Bank_Pytan\S*\`
- **S1**: Tekst literacki | **S2**: Grafika/Plakat | **S3**: Tekst nieliteracki + Gramatyka
- **S4**: Krótka forma | **S5**: Długa forma

---

## Dostępne narzędzia zewnętrzne
- **Gemini CLI** — alternatywny model, duże okno kontekstu (przydatny do analizy długich PDF)
- **NotebookLM** — analiza dokumentów, synteza wiedzy
- **GitHub** — wersjonowanie, backup projektu
- Używaj ich proaktywnie gdy zadanie tego wymaga — nie czekaj na polecenie

---

## Ważne ścieżki
- Szablony: `D:\Dydaktyka\Bank_Pytan\S*\bank_pytan_S*.txt`
- Arkusze finalne: `D:\Dydaktyka\ArkuszeAI\`
- Statystyki: `D:\Dydaktyka\ArkuszeAI\statystyki_arkuszy.csv`
- Lektury (teksty): `D:\Dydaktyka\Lektury\Fragmenty\`
- Podstawa programowa: `D:\Dydaktyka\E8_Dokumentacja\Podstawa_Programowa\Podstawa programowa język polsk. Klasy IV-VI.txt`
- Kluczowe info E8: `D:\Dydaktyka\_projekt\KLUCZOWE_INFORMACJE_E8.txt`
- Pełne wytyczne E8: `D:\Dydaktyka\E8_Dokumentacja\Informator_E8\` (PDF — gdy KLUCZOWE_INFORMACJE nie wystarczą)
- Błędy i lekcje: `D:\Dydaktyka\_projekt\gotchas.md`
- Agent Opus: `D:\Dydaktyka\.claude\agents\generator_arkuszy.md`
