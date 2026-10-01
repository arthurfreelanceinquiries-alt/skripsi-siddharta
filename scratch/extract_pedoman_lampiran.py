import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

doc = fitz.open(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\Buku Pedoman Penyusunan Tugas Akhir 2023.pdf")
for p in range(35, len(doc)):
    print(f"--- Page {p+1} ---")
    print(doc[p].get_text()[:1200])
