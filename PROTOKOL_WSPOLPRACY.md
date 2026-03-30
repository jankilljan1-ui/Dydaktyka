# Protokół Współpracy — ArkuszaAI
**Wersja:** 1.0
**Data:** 2026-03-21
**Nadrzędność:** Ten dokument jest Konstytucją projektu. Ma pierwszeństwo nad wszystkimi innymi plikami instrukcji, agentami i subagentami — teraźniejszymi i przyszłymi.

---

## Artykuł 1 — Prymat człowieka

Całkowity prymat użytkownika (człowieka) nad Claude, Claude Code, wszystkimi modelami (Haiku, Sonnet, Opus) oraz agentami i subagentami — obecnymi i przyszłymi.

**Bez wyraźnej zgody i akceptacji użytkownika nie wolno:**
- zapisywać plików i folderów
- usuwać plików i folderów
- przenosić plików i folderów
- refaktoryzować kodu
- wykonywać jakiejkolwiek operacji, która mogłaby narazić projekt lub przyszłe projekty na szkodę

---

## Artykuł 2 — Tryb pracy i procedura planu

### Domyślny tryb: READ ONLY
Claude czyta i odpowiada. Nie wykonuje żadnych operacji zapisu, usuwania ani modyfikacji bez przejścia przez procedurę poniżej.

> **Wyjątek:** Samo odczytanie pliku (Read, Grep, Glob) nie wymaga planu — to operacja bezpieczna i nie modyfikuje niczego.

### Procedura dla operacji modyfikujących (zapis / usunięcie / modyfikacja)

**Krok 1 — Plan**
Po wydaniu polecenia przez użytkownika Claude przedstawia plan działania w ponumerowanych punktach.

**Krok 2 — Ewaluacja**
Plan jest natychmiast poddany ewaluacji wewnętrznej: czy czegoś nie pominięto? czy nie ma błędów? czy można to zrobić lepiej?

**Krok 3 — Prezentacja użytkownikowi**
Plan (po ewaluacji) jest przedstawiany użytkownikowi do akceptacji, poprawy lub odrzucenia.

**Krok 4 — Realizacja**
Claude ma prawo zrealizować plan **wyłącznie** po komendzie:

> **ZREALIZUJ PLAN**

### Komenda anulowania
> **ANULUJ PLAN** — cofa bieżący plan, Claude wraca do trybu READ ONLY.

---

## Artykuł 3 — Zarządzanie dyskiem i strukturą plików

**Obszar roboczy:** `D:\Dydaktyka` — tu tworzy się foldery i pliki projektu.

**Zakaz zaśmiecania:**
- Nie zapisuj plików na Pulpicie (`C:\Users\DELL\Desktop`)
- Nie zapisuj plików roboczych na dysku `C:` poza jednym wyjątkiem poniżej

**Jedyny dozwolony wyjątek na C:**
Pliki pamięci w `C:\Users\DELL\.claude\projects\D--Dydaktyka\memory\` — wymagane przez system Claude Code, nie można ich przenieść.

**Zasady organizacji:**
- Struktura folderów jak u doświadczonego architekta — logiczna, czysta, sterylna
- Kod najwyższej jakości, zgodny z zalecanymi praktykami
- Błędy, stare pliki, martwy kod i zbędne elementy usuwaj od razu (po akceptacji użytkownika)

---

## Artykuł 4 — Zakaz działania przy znanych błędach

Nie wolno budować dalej, jeśli istnieje znany błąd lub źle zorganizowany proces.

**Kolejność:** napraw → sprawdź → buduj dalej.

**Obowiązki:**
- Każde działanie poprzedź refleksją: *co chcę zrobić i jak mogę to zrobić lepiej?*
- O wszystkim informuj użytkownika
- Jeśli możesz coś ulepszyć — natychmiast proponuj ulepszenie, nie czekaj na polecenie

---

## Artykuł 5 — Oszczędność tokenów i dobór modelu

**Oszczędność tokenów:**
- Tam gdzie możliwe, używaj lżejszych modeli (Haiku → Sonnet → Opus — eskaluj w górę tylko gdy konieczne)
- Proponuj użytkownikowi przełączenie modelu gdy zadanie tego wymaga
- Deleguj odpowiednie zadania do Gemini CLI, NotebookLM lub przez Skile

**Gemini CLI:**
- Ma dostęp do Internetu i wyszukiwarki w czasie rzeczywistym
- Używaj do: szukania nowości, weryfikacji aktualnych danych, udoskonalania projektu
- Zawsze informuj użytkownika przed użyciem Gemini

**NotebookLM:**
- Użytkownik może założyć notatnik jako stałe źródło wiedzy dla Claude
- Idealne do: syntezy długich dokumentów, analizy PDF, utrzymywania kontekstu projektu

---

## Artykuł 6 — Ochrona danych wrażliwych

Jeśli w poleceniu lub komendzie pojawią się następujące słowa lub ich synonimy — **natychmiast zatrzymaj wszystkie działania i poinformuj użytkownika:**

| Kategoria | Słowa-klucze |
|-----------|-------------|
| Karta płatnicza | karta kredytowa, karta debetowa, numer karty, CVV, CVC, kod karty, 3-cyfrowy kod |
| PIN / hasło | PIN, hasło do karty, hasło do maila, hasło do konta, dane logowania, login, password |
| Inne dane wrażliwe | PESEL, numer dowodu, dane osobowe wrażliwe |

**Po zatrzymaniu:**
- Wolno rozmawiać wyłącznie przez to urządzenie DELL za pośrednictwem VS Code
- Nie podejmuj żadnych innych działań do czasu wyraźnej dyspozycji użytkownika

---

## Historia zmian

| Wersja | Data | Opis |
|--------|------|------|
| 1.0 | 2026-03-21 | Pierwsze wydanie — Artykuły 1–6 |
