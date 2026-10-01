import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

doc = fitz.open(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\TUGAS AKHIR (Revisii).pdf")
print(f"Total pages in TUGAS AKHIR (Revisii).pdf: {len(doc)}")
for i in range(min(15, len(doc))):
    text = doc[i].get_text()
    if any(k in text.lower() for k in ["daftar isi", "kata pengantar", "halaman judul"]):
        print(f"=== Page {i+1} ===")
        print(text[:1500])
