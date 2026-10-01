import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

doc = fitz.open(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\Buku Pedoman Penyusunan Tugas Akhir 2023.pdf")
print("=== BU KU PEDOMAN 2023: DAFTAR ISI RULES ===")
for p in range(len(doc)):
    text = doc[p].get_text()
    if "lampiran" in text.lower() and "daftar isi" in text.lower():
        print(f"--- Page {p+1} ---")
        print(text[:1500])
    elif "2.1. Bagian Awal" in text:
        print(f"--- Page {p+1} ---")
        print(text[:1500])
