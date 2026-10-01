import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

doc = fitz.open(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\TUGAS AKHIR (Revisii).pdf")
print("=== DAFTAR ISI FROM TUGAS AKHIR (Revisii).pdf ===")
# Pages 11, 12, 13
for p in range(10, 14):
    print(f"--- Page {p+1} ---")
    print(doc[p].get_text())
