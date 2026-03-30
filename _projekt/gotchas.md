# Gotchas — Błędy i lekcje projektu ArkuszaAI

Zgodnie z zasadą Self-Improvement Loop (Anthropic Playbook):
> After ANY mistake → log it here. Convert mistakes into rules before starting next task.
> Review this file before generating each new worksheet.

---

## G01 — Kreatywna forma w Zadaniu 6
**Co poszło nie tak:** Zadanie 6 było poleceniem napisania monologu / wyznania / listu.
**Dlaczego to błąd:** Twórcze formy pisemne należą WYŁĄCZNIE do Części II arkusza E8. Część I sprawdza rozumienie tekstu.
**Reguła:** Zadanie 6 zawsze pochodzi z Podstawy programowej, punkt I. Kształcenie literackie. Nigdy forma twórcza.
**Arkusze, których dotyczy:** Balladyna (id=1), Dziady — Monolog Zosi (id=4) — oba naprawione.

---

## G02 — "Podmiot liryczny" w projekcie
**Co poszło nie tak:** Użycie terminu „podmiot liryczny" w pytaniu do dramatu.
**Dlaczego to błąd:** W dramacie używamy „osoba mówiąca", w epice i synkretykach — „narrator". „Podmiot liryczny" jest w tym projekcie zakazany.
**Reguła:** Patrz tabela terminologii w CLAUDE.md.

---

## G03 — Zadanie 7 z wydarzeń fragmentu
**Co poszło nie tak:** Pytanie o chronologię używało wydarzeń z samego fragmentu.
**Dlaczego to błąd:** Zadanie 7 sprawdza znajomość CAŁEGO utworu. Używanie wydarzeń z fragmentu czyni pytanie trywialnie łatwym — uczeń nie potrzebuje znać całej lektury.
**Reguła:** Zadanie 7 = zdarzenia z całego dzieła. Przy chronologii: pomijaj zdarzenia z użytego fragmentu.

---

## G04 — Podpowiedź w treści pytania
**Co poszło nie tak:** Pytanie o didaskalia zawierało słowo „didaskalia" — odpowiedź była podana w pytaniu.
**Dlaczego to błąd:** Pytanie testuje wiedzę ucznia, nie podpowiada mu odpowiedzi.
**Reguła:** Nigdy nie umieszczaj w pytaniu terminu, którego podania oczekujesz. Zamiast „didaskalia" użyj „tekst poboczny". Zamiast nazwy środka stylistycznego — opisz fragment i pytaj o nazwę.

---

## G05 — Zbyt duże odstępy w tekście poetyckim
**Co poszło nie tak:** Interlinia 150%–200% w fragmentach wierszowanych — za duże odstępy przy wydruku.
**Dlaczego to błąd:** Marnuje papier, fragment przekracza limit stron.
**Reguła:** Interlinia fragmentu poetyckiego/dramatycznego = Pt(14) ≈ 120%. space_after=Pt(2).

---

## G06 — Tytuły bez kursywy
**Co poszło nie tak:** Tytuły lektur pisane bez kursywy w treści pytań.
**Reguła:** Tytuły utworów zawsze kursywą — w pytaniach, poleceniach, komentarzach.

---

## G07 — CSV aktualizowany po, nie konsultowany przed
**Co poszło nie tak:** CSV był wypełniany dopiero po wygenerowaniu arkusza, zamiast być konsultowany PRZED draftem pytań.
**Dlaczego to błąd:** Rotacja typów pytań była intuicyjna zamiast oparta na danych — prowadziło to do powtarzania tych samych typów.
**Reguła:** KROK 1 przepływu pracy = czytaj CSV. Dopiero potem draftujesz pytania.

---

## G08 — Nieprofesjonalny opis didaskaliów w pytaniu
**Co poszło nie tak:** Użyto opisu „fragmenty zapisane kursywą w nawiasach ukośnych" zamiast profesjonalnego terminu.
**Reguła:** W pytaniu używaj terminu „tekst poboczny" — to jest właśnie ta wiedza, którą uczeń ma wykazać.

---

## G09 — Klucz odpowiedzi generowany bez polecenia
**Co poszło nie tak:** Klucz odpowiedzi był generowany automatycznie przy każdym drafcie.
**Dlaczego to błąd:** Niepotrzebne tokeny, zaśmiecanie draftu.
**Reguła:** Klucz odpowiedzi tylko na wyraźne polecenie użytkownika.

---

## G10 — Rotacja pytań bez sprawdzenia CSV
**Co poszło nie tak:** Typy pytań 3–7 powtarzały się (CYTAT/SRODEK/CECHY) w każdym arkuszu, bo rotacja była deklarowana, ale nie weryfikowana.
**Reguła:** Przed każdym draftem przeczytaj CSV i sprawdź jakie typy były użyte w ostatnich arkuszach tej lektury.

---

## G11 — Skrypty robocze na Pulpicie
**Co poszło nie tak:** Skrypty generujące arkusze (`gen_arkusz_dziady2.py`, `gen_tmp.py`) były zapisywane na `C:\Users\DELL\Desktop\` zamiast w obszarze roboczym projektu.
**Dlaczego to błąd:** Naruszenie Artykułu 3 Protokołu Współpracy — Pulpit i dysk C: są poza obszarem roboczym projektu.
**Reguła:** Wszystkie skrypty robocze trafiają do `D:\Dydaktyka\Narzędzia\` (płasko). Nigdy na Pulpit, nigdy na C:.

---

*Ostatnia aktualizacja: 2026-03-21*
*Plik do przeglądu przed każdym generowaniem arkusza.*
