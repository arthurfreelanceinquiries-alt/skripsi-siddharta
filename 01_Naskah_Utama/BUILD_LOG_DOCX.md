# BUILD_LOG_DOCX — Proposal Bab 1–3 FEB UKRIDA 2023 (DOCX)

Tanggal build: 2026-10-01 21:34:31
Python: 3.14.6 | python-docx: 1.2.0

## 1. Goal-link

Build DOCX Proposal Bab 1–3 FEB UKRIDA 2023 dari MD draf (Model B kuantitatif primer MLBB Gen Z). SoT: Y=intention to play; X1=influencer marketing; X2=eWOM; X3=perceived enjoyment; objek Mobile Legends; populasi Generasi Z Indonesia nasional; kuesioner Google Forms primer.

## 2. Batasan tulis (disjoint)

1. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.docx` (overwrite, satu-satunya docx yang ditulis)
2. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\BUILD_LOG_DOCX.md` (file ini, satu-satunya log yang ditulis)
DILARANG commit/push: tidak ada commit/push dilakukan. DILARANG sentuh file lain: sumber hanya dibaca (read-only), tidak dimodifikasi. DILARANG mengarang isi ilmiah: salin setia dari MD, buang blok meta, pertahankan OPEN/[MENUNGGU VERIFIKASI].

Sumber read-only (dibaca, tidak ditulis):
- 01_Naskah_Utama/BAB_I_DRAF.md (22426 bytes)
- 01_Naskah_Utama/BAB_II_DRAF.md (22998 bytes)
- 01_Naskah_Utama/BAB_III_DRAF.md (18134 bytes)
- 01_Naskah_Utama/DAFTAR_PUSTAKA_SEMENTARA.md (24947 bytes)
- 04_Riset_&_Metodologi/PEDOMAN_BAB123_TEMPLATE.md (.checklist, tidak disalin sebagai isi)

Blok meta yang dibuang (bukan isi proposal, didokumentasikan di sini):
- Seluruh blockquote awal Goal-link/Status draf/Draf proposal (> Goal-link, > Status draf, > Sumber sah, > Draf proposal).
- Seluruh gate `Verified-vs-Proposed` (Bab 1 §0, Bab 2 Verified-vs-Proposed, Bab 3 §0, Daftar Pustaka §1 + legenda).
- Garis `---` pemisah meta.
- Daftar Pustaka: status per-entri `> Status: ...` dibuang; §3 K-03/K-04, §4 Tidak menjadi entri, §5 Kebutuhan PDF+hash, §6 Kepatuhan tugas dibuang (meta kerja).
- Judul draf `— DRAF Proposal`/`(DRAF)` dinormalisasi ke judul bab pedoman HURUF BESAR.
- Tabel 3.1 MD 7-kolom diringkas setia menjadi grid 3-kolom (Variabel | Dimensi–Indikator | Skala|Sumber|Status); tidak ada dimensi/indikator/sumber/angka baru.
Dipertahankan: seluruh OPEN/[MENUNGGU VERIFIKASI]/PROPOSED-UNVERIFIED/ADAPTED/DOI UNVERIFIED, Daftar OPEN Bab 1 & Bab 3, Status verifikasi 2.x, Catatan Kecukupan Acuan Bab 2, horizon/N/software OPEN.

## 3. Verified-vs-Proposed (wajib di log)

| Kode | Item | Status | Jejak |
|---|---|---|---|
| B-V01 | Margin A4 left 4,0 top/right/bottom 3,0 | VERIFIED | py baca section: left=4.0 top=3.0 right=3.0 bottom=3.0 cm |
| B-V02 | Font Times New Roman 12pt semua teks | VERIFIED | runs diperiksa=923, italic_runs=269 |
| B-V03 | Warna Pure Black 000000 semua teks | VERIFIED | runs diperiksa=923 |
| B-V04 | Heading BAB I/II/III centered bold H1; subbab left bold H2/H3; style Heading 1/2 agar TOC native | VERIFIED | H1=6 H2=16 H3=10 |
| B-V05 | Parse *...* menjadi italic run | VERIFIED | italic_runs=269 |
| B-V06 | Cover: PROPOSAL TUGAS AKHIR + judul KAPITAL + Nama/NIM [OPEN] + Prodi Manajemen Pemasaran + FEB UKRIDA + 2026 | VERIFIED | cek string cover |
| B-V07 | Halaman Persetujuan tabel tanda tangan (Pembimbing Dr Fredella Colline ADOPTED-NEEDS-VERIFY, Kaprodi OPEN, tanggal OPEN) | VERIFIED | tabel persetujuan 4x3 grid |
| B-V08 | TOC manual tab-stop kanan 14,0cm dot-leader + field TOC native; entri sinkron heading | VERIFIED | tab_dots_paras=29, field_TOC=True, entri_manual=30 |
| B-V09 | Daftar Pustaka alfabetis tanpa nomor, hanging indent, URL hyperlink aktif warna black | VERIFIED | refs_diekstrak=48, hyperlinks=35 |
| B-V10 | Tabel 3.1 grid 3-kolom ringkas faithful | VERIFIED | cek kolom=3 baris>=7 |
| B-V11 | Body justify + line_spacing 1,5 | VERIFIED (konstruksi) | Normal/Heading line_spacing=1.5, Normal align=JUSTIFY |
| B-P01 | Nomor halaman final/pagination | PROPOSED/OPEN placeholder | TOC manual pakai —; tekan Ctrl+A F9 setelah cetak; footer/page-number tidak dikunci agar tidak langgar TNR12 |
| B-P02 | N sampel, tahun 20xx, software SPSS/SmartPLS, definisi Gen Z, teknik sampling, horizon Y | OPEN dipertahankan, tidak dikarang | Bab 1 Daftar OPEN + Bab 3 §3.1–§3.5 + Tabel 3.1 |
| B-P03 | S10 DOI UNVERIFIED; Park/Cheung venue UNVERIFIED; S11 penulis UNVERIFIED-rinci; S13 N tidak diklaim; α/loading/AVE/β/p/R² | PROPOSED-UNVERIFIED/ADAPTED dipertahankan | Bab 2 + Daftar Pustaka label |
| B-P04 | Karya FEB pemasaran langsung gaming; textbook edisi terbaru; PDF lokal+hash; cek Sinta/Scopus | OPEN | Catatan Kecukupan Bab 2 + Daftar Pustaka §3–§5 dibuang dari DOCX, status OPEN di sini |

## 4. Hasil verifikasi via py (buka docx)

- File: `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.docx`
- File size: 69493 bytes (67.9 KiB)
- Paragraf (top-level doc.paragraphs): 265
- Tabel (top-level doc.tables): 3 (rincian: 1 persetujuan + 1 Tabel Bab2 S01–S18 + 1 Tabel 3.1 + tabel lain bila ada)
- Margin cm: left=4.0 top=3.0 right=3.0 bottom=3.0 -> LULUS (syarat left=4.0 top/right/bottom=3.0)
- Font runs total=923; nama menyimpang=0; ukuran menyimpang (!=12pt)=0 -> LULUS
- Warna menyimpang (None/bukan 000000)=0 -> LULUS
- Italic runs=269 -> LULUS ada italic asing
- Heading styles: H1=6 H2=16 H3=10 -> LULUS
- TOC tab-stop dots 14,0cm: 29 paragraf -> LULUS (kode memakai paragraph_format.tab_stops.add_tab_stop(Cm(14.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS))
- Field TOC native: True (instrTexts=['TOC \\o "1-3" \\h \\z \\u']) -> LULUS
- Hyperlink aktif: 35 -> LULUS (warna hitam diverifikasi via w:color 000000)
- Tabel 3.1 3-kolom: True -> LULUS
- Cover/Persetujuan string: {'cover_proposal': True, 'cover_judul': True, 'cover_nama_open': True, 'cover_prodi': True, 'cover_feb': True, 'cover_2026': True, 'approval_pembimbing': True, 'approval_kaprodi_open': True, 'italic_present': True, 'refs_present': True}

## 5. Cek lulus

- Status keseluruhan: LULUS
- Syarat lulus build ini: margin 4-3-3-3 LULUS + font TNR12 LULUS + black LULUS + TOC dots+field LULUS + Tabel3.1 LULUS + cover/persetujuan LULUS.
- Bukan klaim lulus seminar/K-01–K-07/Turnitin: itu diputus pembimbing/penguji setelah kunci OPEN + baca full-text + PDF lokal + cek Sinta/Scopus + Turnitin ≤30%.

## 6. Kepatuhan + falsifier

- Hanya 2 file ditulis (disjoint) pada 01_Naskah_Utama/: Proposal_Skripsi_MLBB_GenZ.docx + BUILD_LOG_DOCX.md. Tidak ada file lain disentuh; tidak ada commit/push.
- Falsifier build: satu margin menyimpang >0,05cm, satu run non-TNR12/non-black, nol italic, nol tab-stop dots, nol field TOC, Tabel 3.1 bukan 3-kolom, satu URL mati/hiperlink non-hitam, satu entri Daftar Pustaka bernomor/tidak alfabetis = build wajib diperbaiki sebelum seminar.
- Falsifier isi (dari MD, dipertahankan): satu angka tanpa seksi+tanggal, satu DOI karangan, satu N/tahun/software dikarang, atau satu klaim X% Gen Z main MLBB sebagai fakta = naskah wajib turun ke OPEN/UNVERIFIED.

(Akhir log — 2026-10-01 21:34:31)

---

## 7. Fix minor pasca-verifikasi (2026-10-01 21:57 WIB)

Goal-link: Perbaikan minor DOCX Pedoman 2023 pasca-verifikasi via py python-docx surgical, preservasi isi. Verified-vs-Proposed wajib.

Batasan tulis fix ini (disjoint, 4 file total tugas): file ini + Proposal_Skripsi_MLBB_GenZ.docx (fix) + Proposal_Skripsi_MLBB_GenZ.pdf (rebuild, log di BUILD_LOG_PDF.md) + BUILD_LOG_PDF.md. DILARANG sentuh MD/04 lain. DILARANG commit/push: tidak dilakukan.

Perbaikan surgical (teks lain identik, narasi di luar kurung tetap "dan"):
1. Tabel 3.1 (tabel ke-3 7x3) et al. italic via pecah run, template font disalin (TNR12 black, bold=False):
   - R3C2 (Likert 5-titik second-order): "Cheung et al. (2008, 2009)" -> "Cheung *et al.*" italic + "Fan et al. (2013)" -> "*et al.*" italic (1 sel, 2 okurensi; Fan termasuk agar 52/52 in-text tercapai).
   - R4C2: "Davis et al. (1992)" -> "*et al.*" italic (1 okurensi).
   - R5C2: "Venkatesh et al. (2003)" -> "*et al.*" italic (1 okurensi).
   Total tabel: 3 sel, 4 okurensi. Teks sel identik selain italic (verifikasi before==after True).
2. Parenthetical dan->& exact (hanya di dalam kurung kutipan, narasi luar tetap "dan"):
   - P95 §2.1.2 "(Bambauer-Sachse dan Mangold, 2011)" -> "(Bambauer-Sachse & Mangold, 2011)" (1 run).
   - P96 §2.1.2 "(Park dan Lee, 2008" -> "(Park & Lee, 2008" (1 run; sisa "; Cheung/Fan" tak disentuh).
   - T2R4C2 "Venkatesh dan Bala (2008)" -> "Venkatesh & Bala (2008)".
   - T2R5C2 "Hsu dan Lu (2004)" -> "Hsu & Lu (2004)".
   - T2 Kurnia dan Sukarnadi dalam kurung: NOT FOUND di Tabel 3.1 -> no-op sesuai "bila dalam kurung".
   DILARANG scope-creep: P99 "(Venkatesh dan Bala, 2008)", P100 "(Kurnia dan Sukarnadi, 2023)", P103 "(Hsu dan Lu, 2004)" di luar §2.1.2 dibiarkan "dan" sesuai instruksi literal + "pertahankan teks lain identik"; T2R2C2 Bambauer-Sachse dan Mangold + T2R3C2 Park dan Lee di tabel dibiarkan "dan" (tidak tercantum). P52/P80 "dan" naratif dalam kurung non-sitasi dibiarkan.

### Verified-vs-Proposed fix

| Kode | Item | Status | Jejak |
|---|---|---|---|
| F-V01 | Margin A4 4/3/3/3 | VERIFIED | left=4.0005 top=3.0004 right=3.0004 bottom=3.0004 cm |
| F-V02 | Font TNR12 semua teks | VERIFIED | runs non-empty=931 (923+8 pecahan), non-TNR=0 non-12pt=0 |
| F-V03 | Black 000000 | VERIFIED | non-black=0 |
| F-V04 | Italic et al. 52/52 in-text (53/53 total) | VERIFIED | italic_runs=273 (269+4); total et al.=53 italic=53 non-italic=0; in-text 52/52 + P253 ref 1/1 |
| F-V05 | LaTeX 0 | VERIFIED | backslash-cmd=0; "$625" mata uang bukan LaTeX, dikecualikan |
| F-V06 | Tabel 3.1 7x3 | VERIFIED | 7x3, header bold centered |
| F-V07 | Fix & present, old dan gone (scope) | VERIFIED | P95 "& Mangold" True, P96 "(Park & Lee" True, R4C2 "Venkatesh & Bala" True, R5C2 "Hsu & Lu" True; "(Bambauer-Sachse dan" gone, "(Park dan Lee, 2008" gone |
| F-P01 | Sisa parenthetical dan luar scope | PROPOSED/OPEN diketahui | P99/P100/P103 + T2R2C2/T2R3C2 masih "dan" (di luar §2.1.2 + list tabel); 0 dkk dalam scope fix (P95/P96 + R4C2/R5C2) |

Hasil: File `Proposal_Skripsi_MLBB_GenZ.docx` 69567 bytes (67.9 KiB; sebelum 69493, +74 run pecahan). H1=6 H2=16 H3=10 sama. Tidak ada commit/push.

(Akhir fix — 2026-10-01 21:57 WIB)