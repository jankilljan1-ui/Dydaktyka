"""
sprawdz_fragment.py — Podgląd użytych fragmentów lektur z statystyki_arkuszy.csv

Użycie:
    python sprawdz_fragment.py                      # lista wszystkich lektur
    python sprawdz_fragment.py "Balladyna"          # fragmenty konkretnej lektury
    python sprawdz_fragment.py "Dziady cz. II"      # obsługuje spacje w tytule

Wyłącznie odczytowe — nie modyfikuje żadnych plików.
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

# Windows cp1250 fix
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CSV_PATH = Path(__file__).parent.parent / "ArkuszeAI" / "statystyki_arkuszy.csv"


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


def show_all_lektury(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["lektura"]].append(row)

    print(f"{'='*60}")
    print(f"  STATYSTYKI ARKUSZY — {CSV_PATH.name}")
    print(f"{'='*60}")
    print(f"  Łącznie arkuszy: {len(rows)}\n")

    for lektura, arkusze in sorted(grouped.items()):
        print(f"  >> {lektura} ({len(arkusze)} ark.)")
        for a in arkusze:
            print(f"     id={a['id']:>2} | {a['data_generacji']:<12} | {a['fragment_opis'][:55]}")
        print()


def show_lektura(rows, szukana):
    pasujace = [r for r in rows if r["lektura"].lower() == szukana.lower()]

    if not pasujace:
        dostepne = sorted({r["lektura"] for r in rows})
        print(f"Nie znaleziono lektury: '{szukana}'")
        print(f"\nDostępne lektury w CSV:")
        for l in dostepne:
            print(f"  - {l}")
        sys.exit(0)

    print(f"\n{'='*60}")
    print(f"  {pasujace[0]['lektura']} — {pasujace[0]['autor']}")
    print(f"  Użyte fragmenty ({len(pasujace)}):")
    print(f"{'='*60}\n")

    for a in pasujace:
        print(f"  id={a['id']:>2}  [{a['data_generacji']}]")
        print(f"  Fragment: {a['fragment_opis']}")
        print(f"  Typy:  zad3={a['zad_3_typ']:<15} zad4={a['zad_4_typ']:<15}")
        print(f"         zad5={a['zad_5_typ']:<15} zad6={a['zad_6_typ']:<15}")
        print(f"         zad7={a['zad_7_typ']}")
        if a.get("uwagi"):
            print(f"  Uwagi: {a['uwagi']}")
        print()

    # Podsumowanie typów — co zostało użyte ostatnio
    last = pasujace[-1]
    print(f"{'-'*60}")
    print(f"  OSTATNI ARKUSZ (id={last['id']}) — typy ZAKAZANE w następnym:")
    print(f"    zad3 != {last['zad_3_typ']:<14}  |   zad4 != {last['zad_4_typ']}")
    print(f"    zad5 != {last['zad_5_typ']:<14}  |   zad7 != {last['zad_7_typ']}")
    print(f"{'-'*60}\n")


def main():
    rows = load_csv()

    if len(sys.argv) < 2:
        show_all_lektury(rows)
    else:
        szukana = " ".join(sys.argv[1:])
        show_lektura(rows, szukana)


if __name__ == "__main__":
    main()
