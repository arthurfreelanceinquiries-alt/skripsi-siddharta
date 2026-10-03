import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

doc = fitz.open(r"z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.pdf")
print(f"Total pages in Proposal_Skripsi_MLBB_GenZ.pdf: {len(doc)}")
for i in range(min(7, len(doc))):
    text = doc[i].get_text()
    print(f"=== Page {i+1} ===")
    print(text[:1200])
