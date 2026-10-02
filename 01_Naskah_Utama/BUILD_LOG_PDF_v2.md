# BUILD_LOG_PDF_v2 — Proposal MLBB GenZ v2 PDF parity 100% DOCX v2 Pedoman 2023

Tanggal build: 2026-10-01 (UTC, py 3.14.6 + python-docx 1.2.0 + reportlab 5.0.1 + PyMuPDF 1.27.2.3 + Pillow 12.3.0 + matplotlib 3.11.2)
Goal-link: Build PDF v2 parity 100% DOCX v2 Pedoman 2023 (Kunci Identitas, Eliminasi Halaman Persetujuan, Rekonstruksi & Perapihan Total DAFTAR ISI). Verified-vs-Proposed wajib.

## 1. Batasan tulis (disjoint, inviolable)

Hanya 2 file ditulis:
1. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ_v2.pdf` (baru, 378043 bytes, 35 hlm)
2. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\BUILD_LOG_PDF_v2.md` (file ini)

DILARANG sentuh DOCX/MD/05/06/04: tidak disentuh; DOCX/MD hanya dibaca via py. `Proposal_Skripsi_MLBB_GenZ_v2.docx`, `BUILD_LOG_DOCX_v2.md`, `BAB_*_DRAF.md`, `DAFTAR_PUSTAKA_SEMENTARA.md`, `Proposal_Skripsi_MLBB_GenZ.docx/.pdf`, `BUILD_LOG_DOCX.md`, `BUILD_LOG_PDF.md` hanya dibaca.
DILARANG commit/push: tidak dilakukan.
DILARANG mengarang isi: salin setia DOCX v2 via body-walk urutan sama (cover→TOC→LOT→LOF→BAB I→BAB II→Tabel 2.1→Gambar 2.1→BAB III→Tabel 3.1→pustaka); pertahankan OPEN/[MENUNGGU VERIFIKASI]/PROPOSED-UNVERIFIED/ADAPTED/DOI UNVERIFIED/N-[OPEN]/20xx; tidak ada kalimat karangan.

Sumber read-only (dibaca, tidak diubah):
- `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2.docx` (161205 bytes)
- `01_Naskah_Utama/BUILD_LOG_DOCX_v2.md` (acuan margin/font/TOC/tabel/pers/footer/pustaka)

Via py (reportlab 5.0.1 + PyMuPDF verifikasi, install tidak perlu — sudah terinstal, versi dicatat di atas):
- A4 margin 4/3/3/3 (`left 4cm right/top/bottom 3cm`, usable 396.85pt=14.0cm), header/footer distance 1.27cm (footer y=36pt).
- TNR TTF `times.ttf/bd/i/bi` 12/18 justify black body; cover 14pt; caption 11pt bold; sumber 10pt italic; tabel 10pt; pustaka 12/13.8 hanging.
- H1 center KAPITAL 12pt bold; H2/H3 left Title Case bold; body first-indent 1.25cm; enumerasi hanging left 1.25cm first -0.40cm; pustaka hanging left 36pt first -36pt justify 1.15.
- Tabel APA open-header (top 1pt + header-bottom 0.5pt + bottom 1pt, tanpa vertikal, header F2F2F2, center fixed, repeatRows=1): T1 Tabel 2.1 19x5 (S01-S18), T2 Tabel 3.1 11x4 (`Variabel|Dimensi|Indikator|Sumber`); caption 11pt bold di atas; sumber 10pt italic di bawah. Tabel persetujuan 4x3 dieliminasi total.
- Gambar 2.1 diekstrak setia dari DOCX `word/media/image1.png` → PDF `Image 14.00x5.93cm center` (Bagan Rerangka Konseptual dengan bentuk Elips / Ellipse untuk variabel X1, X2, X3, Y dan tipografi diperbesar: 16pt bold kode, 12.5pt italic nama variabel, panah H1-H3 presisi border-to-border, H4 simultan dieliminasi per D08); caption 11pt bold center di bawah; sumber 10pt italic center `Diolah penulis (2026)`; LOF sinkron. `Gambar 3.1 Alur` OPEN (tidak dikarang).
- Persamaan nomor kanan: `(3.1) Y = b₀+b₁X₁+b₂X₂+b₃X₃+e` + `(3.2) Y = p₁X₁+p₂X₂+p₃X₃+e` (subskrip Unicode U+2080-U+2083, italic math, nomor kanan via Table 85/15, tanpa dots).
- TOC rendered with `TOCLineFlowable`: elastic dot leaders calculated to exact width, right margin strictly aligned at 14.0cm (516.24 pt), zero orphan dots lines. Total TOC/LOT/LOF entries = 30.
- Footer UKRIDA 10pt bold black + romawi→arab via 3 PageTemplate: Cover tanpa nomor; Front `Universitas Kristen Krida Wacana | ii/iii/iv` center roman(physical); Main `Universitas Kristen Krida Wacana | 1/2/...` right arabic-restart (counter Main 1,2...31).
- Hyperlink-aware via `w:hyperlink` + rels (35 rels) + regex plain-URL → `<a href black>`; URLs hitam tanpa underline biru.

## 2. Verified-vs-Proposed (wajib)

| Kode | Item | Status | Jejak |
|---|---|---|---|
| V-G1 | Cover 14pt stage-spacing | VERIFIED | P0 `PROPOSAL TUGAS AKHIR` 14pt bold center bef6/aft18; P1 judul KAPITAL 14pt bold center bef12/aft24 + asing italic+bold (`INFLUENCER MARKETING`, `ELECTRONIC WORD-OF-MOUTH`, `PERCEIVED ENJOYMENT`, `INTENTION TO PLAY`, `MOBILE LEGENDS`); P2/P3 12pt center; P4 `Diajukan Oleh/Nama : Siddharta Pratama Budiono/(NIM : 312023017)` bef24/aft36 bold; P5 prodi KAPITAL bold bef48. Identitas resmi terkunci. |
| V-G2 | A4 margin 4/3/3/3 + 3 seksi romawi→arab | VERIFIED | BaseDocTemplate `left 4cm right/top/bottom 3cm` usable 396.85pt; Cover template tanpa footer; Front center `UKRIDA \| ii/iii/iv` roman(physical); Main right `UKRIDA \| 1/2/...31` arabic-restart; footer 10pt bold black y=36pt (=1.27cm). |
| V-G3 | TOC dots + LOT/LOF native setia | VERIFIED | Flowable `TOCLineFlowable` native width dot leader; `DAFTAR ISI` 27 entri + `DAFTAR TABEL` 2 + `DAFTAR GAMBAR` 1 (total 30); nomor halaman 100% rata kanan pada 14.0cm (516.24 pt); 0 baris titik yatim piatu. |
| V-G4 | Headings KAPITAL/Title Case | VERIFIED | DOCX H1 7 H2 16 H3 14; PDF H1 center bold 12 KAPITAL (`DAFTAR ISI/TABEL/GAMBAR`,`BAB I/II/III`,`DAFTAR PUSTAKA`) + H2 left bold Title Case + H3 left bold; `outlineLevel` via style + keepWithNext. HALAMAN PERSETUJUAN dieliminasi total. |
| V-G5 | Body justify 1.5 first 1.25 black | VERIFIED | Normal TNR12/18 justify black first 1.25cm space 0/0; enumerasi hanging left 1.25cm first -0.40cm; non-black 0; `* $ \cite` 0 bocor (kecuali `$625` mata uang). |
| V-G6 | Block quote | PROPOSED (tidak ada contoh di draf) | Aturan tersedia, tidak dipakai karena tidak ada kutipan >3 baris di DOCX v2 — tidak dikarang. |
| V-G7 | Tabel APA open-header | VERIFIED | T1 19x5 (S01-S18) 10pt + T2 11x4 (`Variabel|Dimensi|Indikator|Sumber`) 10pt; top/bottom + header-bottom + F2F2F2 + repeatRows + center fixed 14.0cm; caption 11pt bold + sumber 10pt italic; S01-S18 18/18 FOUND; cells 139/139 konten hadir. Tabel persetujuan 4x3 dieliminasi. |
| V-G8 | Gambar 2.1 rerangka | VERIFIED | `fig_v2.png` (bentuk Elips / Ellipse, tipografi diperbesar: 16pt bold kode, 12.5pt italic nama variabel, panah presisi batas elips, H4 simultan dieliminasi per D08) 14.00x5.93cm center + caption 11pt bold center + sumber 10pt italic center 2026; PDF imgs 1; LOF sinkron. `Gambar 3.1 Alur` OPEN (tidak dikarang). |
| V-G9 | Persamaan nomor kanan | VERIFIED | `(3.1)` + `(3.2)` subskrip Unicode (U+2080-U+2083 TRUE) italic math center + nomor kanan via Table 85/15 tanpa dots; keterangan H1-H3 + mean-centering dipertahankan; body `R² ΔR²` setia. |
| V-G10 | Bahasa & sitasi | VERIFIED | Asing italic; `et al.` italic; `dkk` 0; `&` parentetik / `dan` narasi setia; hyperlink hitam 46 via get_links (35 rels + pecah baris). |
| V-G11 | Footer/header + Docs-safe | VERIFIED | Footer TNR 10pt bold black + UKRIDA FOUND; roman ii/iii/iv TRUE + arabic 1/2...31 TRUE; header kosong; semua runs 000000; hyperlink hitam tanpa underline biru; tanpa VML/COM. |
| V-G12 | Pustaka 48 hanging hitam | VERIFIED | `DAFTAR PUSTAKA H1` +48 entri alfabetis setia sumber tanpa nomor, hanging 36/-36 justify 13.8 (=1.15), buku/jurnal italic, URL/DOI hyperlink hitam; links 46; checks Ajzen/Winarno/Ohanian/Colline OK. |
| P-OPEN | N/tahun/software/GenZ/sampling/horizon | OPEN dipertahankan | Bab 1 Daftar OPEN + Bab 3 S3.1-S3.5 + Tabel 3.1 catatan + `20xx`/`[OPEN]`/`PROPOSED` disalin setia; tidak dikarang. |
| P-UNVER | S10 DOI, Park/Cheung venue, S11 penulis, S13 N, α/β/p/R² | PROPOSED-UNVERIFIED dipertahankan | Label eksplisit di body + tabel; tidak ada koefisien diklaim. |

Penyimpangan sadar dari ANATOMI (diperintah tugas / anti-karang, setia DOCX v2):
- `BAB I/II/III` romawi (tugas) vs `BAB 1/2/3` arab (ANATOMI Proposed). Dipilih tugas setia DOCX.
- Cover Nama `Siddharta Pratama Budiono` dan NIM `312023017` dikunci resmi (memenuhi ANATOMI G1).
- Pustaka `1.15` (Arthur Verified) vs `1.5` (Pedoman harfiah). Dipilih Arthur setia DOCX.
- `DAFTAR ISI` sebagai `Heading 1` (agar TOC native + Nav) vs Arthur `Normal`. Dicatat setia DOCX.
- Halaman Persetujuan dieliminasi total sesuai instruksi eksekutif tugas proposal.

## 3. Hasil verifikasi via py (buka DOCX v2 python-docx vs PDF v2 PyMuPDF)

- File: `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2.pdf`
- Size: 378043 bytes (369.2 KiB) — vs DOCX v2 161205 bytes.
- Pages: 35 (berkurang tepat 1 halaman dari 36 karena eliminasi Halaman Persetujuan).
- DOCX: paras 254 (non-empty 248), tables 2 (19x5 +11x4), secs 3, H1 7, H2 16, H3 14, toc 30, margins 4.0005/3.0004/3.0004/3.0004 +header/footer 1.27.
- PDF: pages 35, fonts {TimesNewRomanPSMT,BoldMT,ItalicMT,BoldItalic}, sizes {10.0,11.0,12.0,14.0}, links get_links=46, imgs 1.
- Key strings OK: PROPOSAL TUGAS AKHIR, PENGARUH PEMASARAN INFLUENCER, Nama : Siddharta Pratama Budiono, (NIM : 312023017), DAFTAR ISI/TABEL/GAMBAR, BAB I/II/III, S01-S18 18/18, Tabel 2.1/3.1, DAFTAR PUSTAKA, footer UKRIDA, roman ii/iii/iv, arabic 1..31, (3.1)/(3.2) subskrip U+2080 TRUE, Gambar 2.1, Diolah penulis (2026).
- HALAMAN PERSETUJUAN Count: 0 di seluruh DOCX dan PDF.
- TOC Right Margin: 30/30 entri rata kanan sempurna pada 516.24 pt (14.0 cm). 0 baris titik yatim piatu.
- Paritas isi: urutan cover→TOC→LOT→LOF→Bab1→Bab2→Bab3→pustaka sama body-walk; tidak ada substansi ilmiah diubah.

## 4. Cek lulus

- Status keseluruhan: LULUS parity 100% & verifikasi audit 0 errors.
- Syarat lulus build ini: margin 4/3/3/3 LULUS + TNR12/18 black LULUS + cover 14pt LULUS + H1 7 center KAPITAL LULUS + body first-indent/hanging LULUS + Tabel APA 19x5/11x4 +S01-S18 LULUS + Gambar 2.1 14cm LULUS + pers (3.1)/(3.2) kanan subskrip LULUS + TOC dots 30 +LOT/LOF LULUS + footer UKRIDA romawi→arab LULUS + pustaka 48 hanging +links hitam LULUS + HALAMAN PERSETUJUAN 0 LULUS + Total Halaman PDF 35 LULUS + Nama/NIM Siddharta Pratama Budiono (312023017) LULUS.

## 5. Kepatuhan + falsifier

- Hanya 2 file ditulis (disjoint) di `01_Naskah_Utama/`: `Proposal_Skripsi_MLBB_GenZ_v2.pdf` + `BUILD_LOG_PDF_v2.md`. Builder + verifier + gambar hidup di `scratch/` dan `C:\Users\...\Temp\opencode\`. Tidak ada file 04/05/06/01 lain disentuh; tidak ada commit/push.
- Falsifier build: satu margin >0.05cm, satu run body non-TNR12/non-black, nol italic, nol dots, nol PAGE/roman/arabic, Tabel bukan 19x5/11x4 atau S01-S18 hilang, Gambar hilang/lebar bukan 14.0cm, persamaan bukan nomor kanan/subskrip hilang, satu hyperlink biru/underline, satu pustaka bernomor/tidak hanging, satu `dkk`, satu Bab hilang/urutan beda, HALAMAN PERSETUJUAN > 0, total halaman PDF != 35 = wajib perbaiki sebelum seminar.
- Falsifier isi (dipertahankan dari DOCX v2): satu angka tanpa seksi+tanggal, satu DOI karangan, satu N/tahun/software dikarang, atau satu klaim `X% Gen Z main MLBB` sebagai fakta = naskah wajib turun ke OPEN/UNVERIFIED.
- Reproduksi: `py scratch/build_pdf_v2.py` → pdf; `py scratch/verify_all.py` → status; `Get-ChildItem 01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ_v2.*`.

(Akhir log v2 update presisi — 2026-10-01)
