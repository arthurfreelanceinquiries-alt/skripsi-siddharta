import sys, os, re, fitz, docx
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DOCX_PATH = Path(r"01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2.docx")
DOCX_UPDATED = Path(r"01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2_updated.docx")
if DOCX_UPDATED.exists():
    if not DOCX_PATH.exists() or DOCX_UPDATED.stat().st_mtime > DOCX_PATH.stat().st_mtime:
        DOCX_PATH = DOCX_UPDATED
PDF_PATH = Path(r"01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2.pdf")

errors = []

def check(condition, desc):
    if condition:
        print(f"[PASS] {desc}")
    else:
        print(f"[FAIL] {desc}")
        errors.append(desc)

print("="*60)
print("ACADEMIC DOCUMENT VERIFICATION AUDIT — S1 MANAJEMEN FEB UKRIDA")
print("="*60)

# 1. Existence and size
check(DOCX_PATH.exists() and DOCX_PATH.stat().st_size > 50000, f"DOCX exists ({DOCX_PATH.stat().st_size if DOCX_PATH.exists() else 0} bytes)")
check(PDF_PATH.exists() and PDF_PATH.stat().st_size > 100000, f"PDF exists ({PDF_PATH.stat().st_size if PDF_PATH.exists() else 0} bytes)")

doc_docx = docx.Document(str(DOCX_PATH))
doc_pdf = fitz.open(str(PDF_PATH))

# 2. Page 1 (Cover) Identity & UKRIDA Logo Verification
docx_cover_text = "\n".join([p.text for p in doc_docx.paragraphs[:8]])
pdf_p1 = doc_pdf[0].get_text()

check("Siddharta Pratama Budiono" in docx_cover_text, "DOCX Cover: 'Siddharta Pratama Budiono' found")
check("312023017" in docx_cover_text, "DOCX Cover: '312023017' found")
check("NIM :" not in docx_cover_text, "DOCX Cover: 'NIM :' eliminated")
check("Siddharta Pratama Budiono" in pdf_p1, "PDF Cover: 'Siddharta Pratama Budiono' found")
check("312023017" in pdf_p1, "PDF Cover: '312023017' found")
check("NIM :" not in pdf_p1, "PDF Cover: 'NIM :' eliminated")
check("(S.M.)" not in docx_cover_text, "DOCX Cover: '(S.M.)' eliminated")
check("(S.M.)" not in pdf_p1, "PDF Cover: '(S.M.)' eliminated")
check("Nama :" not in docx_cover_text, "DOCX Cover: 'Nama :' eliminated")
check("Nama :" not in pdf_p1, "PDF Cover: 'Nama :' eliminated")
check("(NIM" not in docx_cover_text, "DOCX Cover: Bracketed '(NIM' eliminated")
check("(NIM" not in pdf_p1, "PDF Cover: Bracketed '(NIM' eliminated")
check("KONSENTRASI MANAJEMEN PEMASARAN" not in docx_cover_text, "DOCX Cover: 'KONSENTRASI MANAJEMEN PEMASARAN' eliminated")
check("KONSENTRASI MANAJEMEN PEMASARAN" not in pdf_p1, "PDF Cover: 'KONSENTRASI MANAJEMEN PEMASARAN' eliminated")
check("PROGRAM STUDI MANAJEMEN" in docx_cover_text, "DOCX Cover: 'PROGRAM STUDI MANAJEMEN' found without S1")
check("PROGRAM STUDI MANAJEMEN" in pdf_p1, "PDF Cover: 'PROGRAM STUDI MANAJEMEN' found without S1")
check("PROGRAM STUDI S1" not in docx_cover_text, "DOCX Cover: 'PROGRAM STUDI S1' eliminated")
check("PROGRAM STUDI S1" not in pdf_p1, "PDF Cover: 'PROGRAM STUDI S1' eliminated")

# Logo UKRIDA verification on Page 1
docx_logo_found = len(doc_docx.paragraphs[0]._p.xpath('.//a:blip')) == 1
pdf_logo_found = len(doc_pdf[0].get_images()) >= 1
check(docx_logo_found, "DOCX Cover: UKRIDA Logo embedded at paragraph 0")
check(pdf_logo_found, "PDF Cover: UKRIDA Logo rendered on Page 1")

# 3. Elimination of HALAMAN PERSETUJUAN
docx_hp_count = sum(1 for p in doc_docx.paragraphs if "HALAMAN PERSETUJUAN" in p.text.upper())
for t in doc_docx.tables:
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                if "HALAMAN PERSETUJUAN" in p.text.upper():
                    docx_hp_count += 1

pdf_full_text = "".join([p.get_text() for p in doc_pdf])
pdf_hp_count = pdf_full_text.upper().count("HALAMAN PERSETUJUAN")

check(docx_hp_count == 0, f"DOCX: 'HALAMAN PERSETUJUAN' count == 0 (found {docx_hp_count})")
check(pdf_hp_count == 0, f"PDF: 'HALAMAN PERSETUJUAN' count == 0 (found {pdf_hp_count})")

# 4. Total Page Count of PDF
total_pages = len(doc_pdf)
check(total_pages == 34, f"PDF Total Pages == 34 (exact reduction from 36 to {total_pages})")

# 5. Right Margin Alignment of TOC, LOT, LOF
toc_pages = [1, 2, 3] # 0-indexed: Page 2 (DAFTAR ISI), Page 3 (DAFTAR TABEL), Page 4 (DAFTAR GAMBAR)
misaligned_entries = []
entry_count = 0

for p_idx in toc_pages:
    page = doc_pdf[p_idx]
    lines = [l.strip() for l in page.get_text().split("\n") if l.strip() and "Universitas Kristen" not in l and l not in ["DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR"]]
    entry_count += len(lines)
    words = page.get_text("words")
    from collections import defaultdict
    line_words = defaultdict(list)
    for w in words:
        if "Universitas" in w[4] or w[4] in ["DAFTAR", "ISI", "TABEL", "GAMBAR"]:
            continue
        line_words[round(w[3], 1)].append(w)
    for y, ws in line_words.items():
        if y > 750 or any("Kristen" in x[4] for x in ws) or any("Krida" in x[4] for x in ws):
            continue
        last_w = ws[-1]
        x1 = last_w[2]
        if abs(x1 - 516.24) > 0.5:
            misaligned_entries.append((last_w[4], x1))

check(entry_count == 30, f"TOC/LOT/LOF total entries checked == 30 (found {entry_count})")
check(len(misaligned_entries) == 0, f"TOC/LOT/LOF right alignment: 0 errors at 14.0cm (errors={misaligned_entries})")

# 6. Check for Orphan Dots in PDF TOC
orphan_dot_lines = []
for p_idx in toc_pages:
    page = doc_pdf[p_idx]
    lines = [l.strip() for l in page.get_text().split("\n") if l.strip()]
    for l in lines:
        if l.startswith("....") or l.startswith("..."):
            orphan_dot_lines.append(l)

check(len(orphan_dot_lines) == 0, f"Orphan dot lines == 0 (found {len(orphan_dot_lines)}: {orphan_dot_lines})")

# 7. Front matter and Main matter footers
pdf_p2_text = doc_pdf[1].get_text()
pdf_p3_text = doc_pdf[2].get_text()
pdf_p4_text = doc_pdf[3].get_text()
pdf_p5_text = doc_pdf[4].get_text()
pdf_p34_text = doc_pdf[33].get_text()

check("Universitas Kristen Krida Wacana | ii" in pdf_p2_text, "Page 2 Footer: 'Universitas Kristen Krida Wacana | ii'")
check("Universitas Kristen Krida Wacana | iii" in pdf_p3_text, "Page 3 Footer: 'Universitas Kristen Krida Wacana | iii'")
check("Universitas Kristen Krida Wacana | iv" in pdf_p4_text, "Page 4 Footer: 'Universitas Kristen Krida Wacana | iv'")
check("Universitas Kristen Krida Wacana | 1" in pdf_p5_text, "Page 5 Footer: 'Universitas Kristen Krida Wacana | 1'")
check("Universitas Kristen Krida Wacana | 30" in pdf_p34_text, "Page 34 Footer: 'Universitas Kristen Krida Wacana | 30'")

# Check all footers are right-aligned
check(doc_docx.sections[1].footer.paragraphs[0].alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT, "DOCX Section 1 (Frontmatter) Footer is right-aligned")
check(doc_docx.sections[2].footer.paragraphs[0].alignment == docx.enum.text.WD_ALIGN_PARAGRAPH.RIGHT, "DOCX Section 2 (Main matter) Footer is right-aligned")
p2_words = [w for w in doc_pdf[1].get_text('words') if w[1] > 750]
p2_max_x = max(w[2] for w in p2_words) if p2_words else 0
check(p2_max_x > 450, f"PDF Page 2 Footer right-aligned (ends at {p2_max_x:.1f} pt)")

# 8. Tables and Scientific Parity
docx_tables = len(doc_docx.tables)
check(docx_tables == 2, f"DOCX Tables count == 2 (Tabel 2.1 & 3.1, found {docx_tables})")

# Check S01-S18 in Tabel 2.1
s_codes = [f"S{i:02d}" for i in range(1, 19)]
s_found_docx = sum(1 for s in s_codes if s in doc_docx.tables[0]._tbl.xml)
s_found_pdf = sum(1 for s in s_codes if s in pdf_full_text)
check(s_found_docx == 18, f"DOCX Tabel 2.1: 18/18 empirical studies found (found {s_found_docx})")
check(s_found_pdf == 18, f"PDF Tabel 2.1: 18/18 empirical studies found (found {s_found_pdf})")

# Check Gambar 2.1
check("Gambar 2.1" in pdf_full_text and "Diolah penulis (2026)" in pdf_full_text, "Gambar 2.1 and caption/source found in PDF")

# Check Equations (3.1) and (3.2)
check("(3.1)" in pdf_full_text and "(3.2)" in pdf_full_text, "Equations (3.1) and (3.2) found in PDF")

# Check 48 References in Pustaka
pust_start = None
for i, p in enumerate(doc_docx.paragraphs):
    if p.text.strip() == "DAFTAR PUSTAKA":
        pust_start = i
        break
ref_count_docx = len(doc_docx.paragraphs) - pust_start - 1 if pust_start else 0
check(ref_count_docx == 48, f"DOCX DAFTAR PUSTAKA: 48 entries intact (found {ref_count_docx})")

# Check Key Authors in PDF
key_authors = ["Ajzen, I. (1991)", "Colline", "Winarno", "Ohanian, R. (1990)"]
check(all(a in pdf_full_text for a in key_authors), "Key bibliographic references found in PDF")

# 9. Verification of Simultaneous Effect (Simultan) & H4 Elimination
# Bab 1 Rumusan Masalah & Tujuan Penelitian
docx_full_text = "\n".join([p.text for p in doc_docx.paragraphs])
check("secara simultan berpengaruh positif terhadap niat bermain" not in docx_full_text, "DOCX: Rumusan/Tujuan simultan eliminated")
check("secara simultan berpengaruh positif terhadap niat bermain" not in pdf_full_text, "PDF: Rumusan/Tujuan simultan eliminated")

# Bab 2 Hipotesis: H4 eliminated
check("H4:" not in docx_full_text, "DOCX: 'H4:' eliminated")
check("H4:" not in pdf_full_text, "PDF: 'H4:' eliminated")
check("H4 (+)" not in docx_full_text, "DOCX: 'H4 (+)' eliminated")
check("H4 (+)" not in pdf_full_text, "PDF: 'H4 (+)' eliminated")

# Check H1, H2, H3 intact
check("H1:" in docx_full_text and "H2:" in docx_full_text and "H3:" in docx_full_text, "DOCX: H1, H2, H3 intact")
check("H1:" in pdf_full_text and "H2:" in pdf_full_text and "H3:" in pdf_full_text, "PDF: H1, H2, H3 intact")

# Rumusan masalah count in Bab 1: exactly 3 questions
check("4. Apakah" not in docx_full_text and "4. Apakah" not in pdf_full_text, "Bab 1: 4th question eliminated (only 1, 2, 3)")
check("4. Untuk menganalisis" not in docx_full_text and "4. Untuk menganalisis" not in pdf_full_text, "Bab 1: 4th objective eliminated (only 1, 2, 3)")

# 9. Final verdict
print("="*60)
if len(errors) == 0:
    print("FINAL STATUS: PASS (0 errors)")
    print("="*60)
    sys.exit(0)
else:
    print(f"FINAL STATUS: FAIL ({len(errors)} errors)")
    for e in errors:
        print(" -", e)
    print("="*60)
    sys.exit(1)
