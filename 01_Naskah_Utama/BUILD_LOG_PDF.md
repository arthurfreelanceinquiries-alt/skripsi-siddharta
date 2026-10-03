# BUILD_LOG_PDF — Proposal Skripsi MLBB GenZ FEB UKRIDA 2023 (PDF)

Tanggal build: 2026-10-03 (UTC, py 3.14.6 + reportlab 5.0.1 + PyMuPDF 1.27.2.3 + Pillow 12.3.0 + matplotlib 3.11.2)
Goal-link: Build tunggal PDF Proposal Skripsi Bab 1–3 FEB UKRIDA 2023 dengan paritas 100% dari DOCX.

## 1. Batasan Berkas (Tunggal & Kanonik)

Satu-satunya dokumen PDF naskah utama:
- `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.pdf` (769406 bytes, 34 halaman)

Seluruh variasi penamaan versi (v1, v2, v2_updated) telah dieliminasi total sehingga seluruh build dan pembaruan mengarah langsung ke satu dokumen kanonik ini.

Sumber konversi:
- `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ.docx`
- `01_Naskah_Utama/BUILD_LOG_DOCX.md`

## 2. Verified-vs-Proposed (Kepatuhan Spesifikasi)

| Kode | Item | Status | Realisasi |
|---|---|---|---|
| V-G1 | Cover 14pt stage-spacing | VERIFIED | Layout proporsional judul 14pt bold center; nama dan NIM resmi terkunci tanpa kurung/label NIM:; logo UKRIDA tajam di paragraph 0. |
| V-G2 | A4 Margin 4/3/3/3 cm | VERIFIED | Usable width 396.85 pt (14.0 cm); header/footer distance 1.27 cm (footer y=36 pt). |
| V-G3 | TOC Dot Leader 516.24 pt | VERIFIED | Rata kanan presisi pada 14.0 cm; 0 orphan dot lines; total 30 entri (Daftar Isi, Tabel, Gambar). |
| V-G4 | Headings KAPITAL/Title Case | VERIFIED | H1 center 12pt bold KAPITAL; H2/H3 left Title Case bold; outline level PDF terdaftar. |
| V-G5 | Body Justify 1.5 Spasi | VERIFIED | First line indent 1.25 cm; enumerasi hanging indent; pure black 000000; asing miring. |
| V-G7 | Tabel APA Open-Header | VERIFIED | Tabel 2.1 (S01–S18) dan Tabel 3.1; border horizontal APA standar; header abu-abu F2F2F2; tanpa garis vertikal. |
| V-G8 | Gambar 2.1 Rerangka | VERIFIED | Gambar elips proporsional 14.0 cm center; caption dan sumber sinkron dengan Daftar Gambar. |
| V-G9 | Persamaan Matematika Kanan | VERIFIED | Persamaan (3.1) dan (3.2) nomor kanan tanpa titik leader, variabel miring dengan subskrip Unicode. |
| V-G10 | Bahasa & Sitasi APA 7th | VERIFIED | 0 dkk; et al. miring; hyperlink hitam tanpa garis bawah biru. |
| V-G11 | Footer UKRIDA Rata Kanan | VERIFIED | Romawi pada bagian awal (ii s.d. iv) dan Arab pada isi (1 s.d. 30); seluruh nomor rata kanan. |
| V-G12 | Pustaka 48 Entri Hanging | VERIFIED | 48 entri hanging indent, alfabetis, URL/DOI aktif. |

## 3. Hasil Audit Verifikasi

- File target: `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ.pdf`
- Ukuran: 769.406 bytes
- Jumlah Halaman: **34 Halaman** (eliminasi Halaman Persetujuan & perapihan naskah).
- Status Audit `scratch/verify_all.py`: **PASS (52/52 checks, 0 errors)**.
