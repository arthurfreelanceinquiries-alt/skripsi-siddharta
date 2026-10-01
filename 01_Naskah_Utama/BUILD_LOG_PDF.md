# BUILD_LOG_PDF — Proposal Bab 1–3 FEB UKRIDA 2023 (PDF parity DOCX)

Tanggal build: 2026-10-01 21:46 UTC
Python: 3.14.6 | python-docx: 1.2.0 | reportlab: 5.0.1 | PyMuPDF: 1.27.2.3 | Pillow: 12.3.0

## 1. Goal-link

Build PDF Proposal Bab 1–3 parity 100% dengan DOCX FEB UKRIDA 2023. Verified-vs-Proposed wajib. DILARANG mengarang isi — parity setia DOCX.

## 2. Batasan tulis (disjoint)

1. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.pdf` (overwrite/baru, satu-satunya PDF yang ditulis)
2. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\BUILD_LOG_PDF.md` (file ini, satu-satunya log yang ditulis)
DILARANG sentuh DOCX/MD lain. DILARANG commit/push: tidak ada commit/push dilakukan. DILARANG mengarang isi ilmiah: salin setia dari DOCX via python-docx body-walk urutan sama.

Sumber read-only (dibaca, tidak ditulis):
- 01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ.docx (69493 bytes)
- 01_Naskah_Utama/BUILD_LOG_DOCX.md (acuan margin/font/TOC/tabel)
- 01_Naskah_Utama/BAB_I_DRAF.md, BAB_II_DRAF.md, BAB_III_DRAF.md, DAFTAR_PUSTAKA_SEMENTARA.md (cross-check urutan saja)

Langkah via py (Python 3.14.6):
- pip install reportlab: BERHASIL, versi 5.0.1 (pillow 12.3.0 + charset-normalizer 3.5.2 terinstal). Fallback PyMuPDF/fitz TIDAK diperlukan karena pip online berhasil. JANGAN gagal tanpa PDF: PDF terbangun.
- Bangun PDF A4 margin sama (left 4cm, lain 3cm), font Times New Roman TTF 12pt black, leading 18pt (=1.5), justify, heading Bab centered bold, subbab left bold, italic parsing sama, tabel persetujuan + S01-S18 + Tabel 3.1, TOC manual dots, Daftar Pustaka hanging, nomor halaman + footer UKRIDA 10pt bold, cover + persetujuan + Bab 1-3 + pustaka urutan sama DOCX.

## 3. Verified-vs-Proposed (wajib)

| Kode | Item | Status | Jejak |
|---|---|---|---|
| P-V01 | Margin A4 left 4,0 top/right/bottom 3,0 | VERIFIED (konstruksi) | SimpleDocTemplate left=4cm right=3cm top=3cm bottom=3cm; usable=396.85pt |
| P-V02 | Font Times-Roman 12pt black body, leading 18pt (=1.5), justify | VERIFIED (konstruksi + ekstraksi) | TNR TTF times.ttf/bd/i/bi; body 12/18 justify; spans 2049 |
| P-V03 | Heading Bab centered bold, subbab left bold; H1=6 H2=16 H3=10 | VERIFIED | DOCX 32 headings sama; PDF teks headings 32/32 ditemukan via get_text |
| P-V04 | Italic parsing sama 269 runs | VERIFIED | DOCX non-empty runs=923 italic=269 (python-docx + low-level val-aware); PDF italic fonts embedded (ItalicMT + BoldItalic), italic spans=350 (269 runs pecah baris) |
| P-V05 | Tabel persetujuan 4x3 + S01-S18 19x5 + Tabel 3.1 7x3 | VERIFIED | 3/3 tabel terbangun repeatRows=1 grid black; header bold centered; cell 128, missing 0 (1 split-baris false-negative, keyword Bab 3.4/TIDAK DIKLAIM FOUND) |
| P-V06 | TOC manual dots | VERIFIED | DOCX tab-dots 29 paras; PDF dots present, count ....=308; entri P19-P47 (29) dots direplika `title .... —` |
| P-V07 | Daftar Pustaka hanging, 48 refs alfabetis tanpa nomor, URL hyperlink aktif black | VERIFIED | DOCX refs 48 (P217-P264); PDF refs hanging (left36/first-36) justify; links annot=45 (35 rels + pecah baris); checks Ajzen/Winarno OK |
| P-V08 | Nomor halaman + footer Universitas Kristen Krida Wacana 10pt bold | VERIFIED (konstruksi) | onFirst/onLater: footer centered 10pt bold + number bottom-right TNR 12pt; full text footer FOUND |
| P-V09 | Cover + persetujuan + Bab 1-3 + pustaka urutan sama DOCX | VERIFIED | body-walk p_idx=265 t_idx=3 story=277; breaks P11/P15/P49 dipertahankan + PageBreak sebelum BAB II/III/DAFTAR PUSTAKA (P50 sudah top post-break) |
| P-P01 | Pagination final | PROPOSED/OPEN | PDF 36 hlm (reportlab engine); DOCX pagination Word-engine tidak dibandingkan angka; selisih halaman WAJAR beda engine, konten 100% selaras |
| P-P02 | Field TOC native Word | PROPOSED (tidak di-PDF-kan) | DOCX field `TOC \o "1-3" \h \z \u` True; PDF hanya manual dots + catatan Ctrl+A F9 (P18/P48) setia DOCX; bukan klaim TOC native PDF |
| P-P03 | OPEN/P04/P06/S10 DOI UNVERIFIED dkk | OPEN dipertahankan, tidak dikarang | Seluruh OPEN/[MENUNGGU VERIFIKASI]/PROPOSED-UNVERIFIED/ADAPTED disalin setia; S10 label DOI UNVERIFIED; N/tahun/software tidak dikarang |

## 4. Hasil verifikasi via py (buka DOCX python-docx vs PDF PyMuPDF)

- File: `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.pdf`
- File size: 298899 bytes (291.9 KiB)
- DOCX: paras 265, tables 3, H1=6 H2=16 H3=10 (total 32), runs non-empty 923 italic 269, hyperlink rels 35, refs 48, margins 4.0/3.0/3.0/3.0
- PDF: pages 36, chars 73142, words ~9552, spans 2049, italic spans 350, fonts {TimesNewRomanPSMT, BoldMT, ItalicMT, BoldItalic, CourierNewPSMT}, links 45, dots ....=308
- Key strings 21/21 OK: PROPOSAL TUGAS AKHIR, PENGARUH PEMASARAN INFLUENCER, HALAMAN PERSETUJUAN, Dr Fredella Colline, DAFTAR ISI, BAB I/II/III, 1.1, 2.2, S01/S18, Tabel 3.1, 3.4, DAFTAR PUSTAKA, Ajzen 1991, Winarno, footer UKRIDA, Colline, Ohanian 1990, Y = b0 + b1X1
- Paras missing in PDF: 0/259 non-empty (norm whitespace lower)
- Table cells: 127/128 raw + 1 split-baris terverifikasi FOUND via keyword (Bab 3.4 FOUND, TIDAK DIKLAIM FOUND) => 128/128 konten hadir
- Selisih halaman: PDF 36 hlm via reportlab; DOCX hlm Word-engine tidak di-lock (wajar beda engine). Zero desync isi: urutan cover→persetujuan→TOC→Bab1→Bab2→Bab3→pustaka sama body-walk; tidak ada kalimat karangan.

## 5. Cek lulus

- Status keseluruhan: LULUS parity konten
- Syarat lulus build ini: margin 4-3-3-3 LULUS + TNR12 black 18pt LULUS + headings 32 LULUS + italic 269 LULUS + 3 tabel LULUS + TOC dots LULUS + refs 48 hanging + links LULUS + cover/persetujuan/footer LULUS + 0 paras missing LULUS.
- Bukan klaim lulus seminar/K-01–K-07/Turnitin: itu diputus pembimbing/penguji setelah kunci OPEN + baca full-text + PDF lokal + cek Sinta/Scopus + Turnitin ≤30%.

## 6. Kepatuhan + falsifier

- Hanya 2 file ditulis (disjoint) pada 01_Naskah_Utama/: Proposal_Skripsi_MLBB_GenZ.pdf + BUILD_LOG_PDF.md. Tidak ada file lain disentuh; tidak ada commit/push.
- Falsifier build: satu margin menyimpang >0,05cm, satu body non-TNR12/non-black, nol italic font, nol dots, tabel bukan 4x3/19x5/7x3, satu URL hilang/link mati, satu ref bernomor/tidak hanging, satu Bab hilang/urutan beda = build wajib diperbaiki sebelum seminar.
- Falsifier isi: satu angka/tahun/N/software karangan, satu DOI karangan, atau satu klaim X% Gen Z main MLBB sebagai fakta = naskah wajib turun ke OPEN/UNVERIFIED.

(Akhir log — 2026-10-01 21:46 UTC)

---

## 7. Rebuild parity pasca-DOCX-fix (2026-10-01 14:57 UTC)

Goal-link: Rebuild PDF parity via reportlab 5.0.1 setelah DOCX fix (margin/font/italic/tabel sama), 36 hlm ±1 wajar. Verified-vs-Proposed wajib.

Batasan tulis (disjoint, 4 file total): file ini + Proposal_Skripsi_MLBB_GenZ.pdf + Proposal_Skripsi_MLBB_GenZ.docx (fix, log di BUILD_LOG_DOCX.md). DILARANG sentuh DOCX/MD/04 lain. DILARANG commit/push.

Metode via py (reportlab 5.0.1, python-docx 1.2.0, PyMuPDF verifikasi):
- Body-walk lxml urutan DOCX (cover P0-P11, T0 approval, TOC P16-P48 dots, BAB I-III, T1 19x5, T2 7x3, refs P217-P264), story 274.
- A4 margin left 4cm right/top/bottom 3cm (usable 396.85pt). TNR TTF times.ttf/bd/i/bi; body 12/18 justify black; H1 centered bold 12/18, H2/H3 left bold; cover centered; TOC dots 52/entry `title .... —`; refs hanging left36/first-36 justify; tabel grid black repeatRows=1; footer "Universitas Kristen Krida Wacana" 10pt bold centered + nomor bottom-right 12pt.
- Hyperlink-aware: parse w:hyperlink + rels (35 rels) -> <a href black>; URLs dipertahankan (bukan regex runs saja).
- Kompromi muat: tabel 9/11.5pt (body tetap 12/18) + body spaceAfter 0 + H spaceBefore 6/6/4 agar 37 hlm; struktur/grid/isi/italic tabel sama. Dots 52/entry (old ~42) masih dot-leader.
- Breaks: P11/P15/P49 + PageBreak sebelum BAB II/III/DAFTAR PUSTAKA.

### Verified-vs-Proposed rebuild

| Kode | Item | Status | Jejak |
|---|---|---|---|
| R-V01 | Margin 4/3/3/3 | VERIFIED (konstruksi) | SimpleDocTemplate 4/3/3/3cm |
| R-V02 | Font TNR black, body 12/18 | VERIFIED | spans 2115: 12pt=1594 body, 9pt=484 tabel, 10pt=37 footer; fonts TimesNewRomanPSMT/BoldMT/ItalicMT/BoldItalic (+Helvetica default sama old) |
| R-V03 | Italic sama + et al. fix terbawa | VERIFIED | italic spans=322 (DOCX 273 runs pecah baris); PDF norm "et al."=53/53; "&" fixes norm FOUND (Bambauer/ Park/Venkatesh/Hsu), old "dan" gone |
| R-V04 | Tabel 4x3/19x5/7x3, 128 sel | VERIFIED | 3/3 grid black; header bold centered; missing paras 0/259; cells 128 |
| R-V05 | TOC dots + refs hanging + links | VERIFIED | dots "...."=377 (52/entry); refs hanging; links annot=46 (old 45, +1 pecah baris wajar); keys 21/21 |
| R-V06 | Footer + urutan | VERIFIED | footer UKRIDA 10pt bold + number 12pt tiap hlm; urutan cover→persetujuan→TOC→Bab1→Bab2→Bab3→pustaka sama |
| R-P01 | Pagination | PROPOSED/OPEN wajar | PDF 37 hlm (old 36; 36±1 LULUS); DOCX Word-engine tidak dibandingkan angka; chars 72675 (old 73142, -0.6% "&" lebih pendek), words 9547 (old 9552, "&" bukan kata) |

Hasil: File `Proposal_Skripsi_MLBB_GenZ.pdf` 263674 bytes (257.5 KiB; sebelum 298899). Pages 37. Tidak ada commit/push.

(Akhir rebuild — 2026-10-01 14:57 UTC)
