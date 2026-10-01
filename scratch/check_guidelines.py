import fitz
import sys

# Set standard output to UTF-8
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def inspect(path, name):
    doc = fitz.open(path)
    print(f"==================== {name} ({len(doc)} pages) ====================")
    for i, page in enumerate(doc):
        text = page.get_text()
        for kw in ["proposal tugas akhir", "format tugas akhir", "bagian awal", "daftar isi", "halaman persetujuan"]:
            if kw in text.lower():
                print(f"--- Page {i+1} mentions '{kw}' ---")
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                for l in lines[:15]:
                    print("  ", l[:120])
                break

inspect(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\Buku Pedoman Penyusunan Tugas Akhir 2023.pdf", "Buku Pedoman 2023")
