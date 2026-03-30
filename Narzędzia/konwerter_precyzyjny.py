import fitz  # PyMuPDF
import os

def konwertuj_wybrany_plik(nazwa_pliku):
    # Nowe ścieżki zgodnie z Twoją strukturą
    folder_zrodlowy = r"E:\Balice\Lektury"
    folder_docelowy = r"D:\Dydaktyka\Lektury\Lekturyfragmentytxt"
    
    # Tworzenie folderu docelowego, jeśli nie istnieje
    if not os.path.exists(folder_docelowy):
        os.makedirs(folder_docelowy)

    sciezka_pdf = os.path.join(folder_zrodlowy, nazwa_pliku)
    
    # Sprawdzanie czy plik istnieje w nowym miejscu na E:
    if not os.path.isfile(sciezka_pdf):
        print(f"Blad: Nie znaleziono pliku {nazwa_pliku} w lokalizacji E:\\Balice\\Lektury")
        return

    nazwa_txt = nazwa_pliku.replace('.pdf', '_TEKST.txt')
    sciezka_wyjsciowa = os.path.join(folder_docelowy, nazwa_txt)

    try:
        doc = fitz.open(sciezka_pdf)
        tekst_calosc = ""
        for strona in doc:
            # Wyciąganie tekstu z zachowaniem układu (ważne przy analizie wierszy i rytmiki)
            tekst_calosc += strona.get_text("text") + f"\n--- STRONA {strona.number + 1} ---\n"
        
        with open(sciezka_wyjsciowa, "w", encoding="utf-8") as f:
            f.write(tekst_calosc)
        print(f"Sukces! Plik zapisano w: {sciezka_wyjsciowa}")
    except Exception as e:
        print(f"Blad podczas konwersji: {e}")

if __name__ == "__main__":
    plik = input("Wklej pelna nazwe pliku PDF (np. Balladyna.pdf): ")
    konwertuj_wybrany_plik(plik)