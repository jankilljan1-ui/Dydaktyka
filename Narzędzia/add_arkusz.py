"""
add_arkusz.py — Narzędzie do dodawania arkuszy do statystyki_arkuszy.csv

Użycie:
    python add_arkusz.py \
        --lektura "Balladyna" \
        --autor "Juliusz Słowacki" \
        --fragment "Akt IV scena 2 — ..." \
        --zad3 CYTAT \
        --zad4 SRODEK \
        --zad5 CECHY \
        --zad6 TEKST_POBOCZNY \
        --zad7 CALOSC \
        [--uwagi "opcjonalne uwagi"]

Typy pytań:
    zad3: CYTAT | FRAZEOLOGIZM | SLOWNIK
    zad4: SRODEK | INTERPUNKCJA | SKLADNIA
    zad5: CECHY | INNA_LEKTURA | NARRACJA
    zad6: dowolny string (np. TEKST_POBOCZNY, PP_narrator, DIDASKALIA...)
    zad7: CALOSC | CHRONOLOGIA | POWIAZANIE
"""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "ArkuszeAI" / "statystyki_arkuszy.csv"

VALID_ZAD3 = {"CYTAT", "FRAZEOLOGIZM", "SLOWNIK"}
VALID_ZAD4 = {"SRODEK", "INTERPUNKCJA", "SKLADNIA"}
VALID_ZAD5 = {"CECHY", "INNA_LEKTURA", "NARRACJA"}
VALID_ZAD7 = {"CALOSC", "CHRONOLOGIA", "POWIAZANIE"}

FIELDNAMES = [
    "id", "lektura", "autor", "fragment_opis", "data_generacji",
    "zad_1_typ", "zad_2_typ", "zad_3_typ", "zad_4_typ",
    "zad_5_typ", "zad_6_typ", "zad_7_typ", "uwagi"
]


def load_csv():
    if not CSV_PATH.exists():
        print(f"BŁĄD: Nie znaleziono pliku CSV: {CSV_PATH}", file=sys.stderr)
        sys.exit(1)
    rows = []
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows


def next_id(rows):
    if not rows:
        return 1
    return max(int(r["id"]) for r in rows) + 1


def validate(args):
    errors = []
    if args.zad3.upper() not in VALID_ZAD3:
        errors.append(f"zad3='{args.zad3}' — dozwolone: {', '.join(sorted(VALID_ZAD3))}")
    if args.zad4.upper() not in VALID_ZAD4:
        errors.append(f"zad4='{args.zad4}' — dozwolone: {', '.join(sorted(VALID_ZAD4))}")
    if args.zad5.upper() not in VALID_ZAD5:
        errors.append(f"zad5='{args.zad5}' — dozwolone: {', '.join(sorted(VALID_ZAD5))}")
    if args.zad7.upper() not in VALID_ZAD7:
        errors.append(f"zad7='{args.zad7}' — dozwolone: {', '.join(sorted(VALID_ZAD7))}")
    if errors:
        print("BŁĄD WALIDACJI:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


def check_rotation(rows, args):
    lektura_rows = [r for r in rows if r["lektura"].lower() == args.lektura.lower()]
    if not lektura_rows:
        return
    last = lektura_rows[-1]
    warnings = []
    if last["zad_3_typ"].upper() == args.zad3.upper():
        warnings.append(f"zad3={args.zad3} był użyty w ostatnim arkuszu tej lektury (id={last['id']})")
    if last["zad_4_typ"].upper() == args.zad4.upper():
        warnings.append(f"zad4={args.zad4} był użyty w ostatnim arkuszu tej lektury (id={last['id']})")
    if last["zad_5_typ"].upper() == args.zad5.upper():
        warnings.append(f"zad5={args.zad5} był użyty w ostatnim arkuszu tej lektury (id={last['id']})")
    if last["zad_7_typ"].upper() == args.zad7.upper():
        warnings.append(f"zad7={args.zad7} był użyty w ostatnim arkuszu tej lektury (id={last['id']})")
    if warnings:
        print("OSTRZEŻENIE — naruszenie rotacji:", file=sys.stderr)
        for w in warnings:
            print(f"  ⚠ {w}", file=sys.stderr)
        answer = input("Kontynuować mimo to? [t/N] ").strip().lower()
        if answer != "t":
            print("Anulowano.", file=sys.stderr)
            sys.exit(0)


def append_row(rows, args, new_id):
    new_row = {
        "id": new_id,
        "lektura": args.lektura,
        "autor": args.autor,
        "fragment_opis": args.fragment,
        "data_generacji": date.today().isoformat(),
        "zad_1_typ": "PF",
        "zad_2_typ": "WW",
        "zad_3_typ": args.zad3.upper(),
        "zad_4_typ": args.zad4.upper(),
        "zad_5_typ": args.zad5.upper(),
        "zad_6_typ": args.zad6,
        "zad_7_typ": args.zad7.upper(),
        "uwagi": args.uwagi or "",
    }
    with open(CSV_PATH, encoding="utf-8", newline="", mode="a") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=";")
        writer.writerow(new_row)
    return new_row


def print_commit_message(row):
    lektura_slug = row["lektura"].replace(" ", "_")
    msg = (
        f"arkusz: {row['lektura']} id={row['id']} | "
        f"zad3={row['zad_3_typ']} zad4={row['zad_4_typ']} "
        f"zad5={row['zad_5_typ']} zad7={row['zad_7_typ']} | "
        f"{row['data_generacji']}"
    )
    print("\n✅ Dodano do CSV.")
    print(f"\nGotowy komunikat git commit (skopiuj i wklej):")
    print(f'  git commit -m "{msg}"')


def main():
    parser = argparse.ArgumentParser(description="Dodaj arkusz do statystyki_arkuszy.csv")
    parser.add_argument("--lektura", required=True, help="Tytuł lektury")
    parser.add_argument("--autor", required=True, help="Autor lektury")
    parser.add_argument("--fragment", required=True, help="Opis użytego fragmentu")
    parser.add_argument("--zad3", required=True, help="Typ zad. 3: CYTAT | FRAZEOLOGIZM | SLOWNIK")
    parser.add_argument("--zad4", required=True, help="Typ zad. 4: SRODEK | INTERPUNKCJA | SKLADNIA")
    parser.add_argument("--zad5", required=True, help="Typ zad. 5: CECHY | INNA_LEKTURA | NARRACJA")
    parser.add_argument("--zad6", required=True, help="Typ zad. 6: np. TEKST_POBOCZNY, PP_narrator...")
    parser.add_argument("--zad7", required=True, help="Typ zad. 7: CALOSC | CHRONOLOGIA | POWIAZANIE")
    parser.add_argument("--uwagi", default="", help="Opcjonalne uwagi")
    args = parser.parse_args()

    rows = load_csv()
    validate(args)
    check_rotation(rows, args)
    new_id = next_id(rows)
    new_row = append_row(rows, args, new_id)
    print_commit_message(new_row)


if __name__ == "__main__":
    main()
