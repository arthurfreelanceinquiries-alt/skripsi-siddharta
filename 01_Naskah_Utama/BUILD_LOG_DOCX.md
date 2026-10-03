# BUILD_LOG_DOCX — Proposal Skripsi MLBB GenZ FEB UKRIDA 2023 (DOCX)

Tanggal build: 2026-10-03 (UTC, py 3.14.6 + python-docx 1.2.0 + matplotlib 3.11.2)
Goal-link: Build tunggal DOCX Proposal Skripsi Bab 1–3 FEB UKRIDA 2023 serapih Arthur, Pedoman 2023. Verified-vs-Proposed wajib.

## 1. Batasan Berkas (Tunggal & Kanonik)

Satu-satunya dokumen Word naskah utama:
- `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.docx` (478895 bytes)

Seluruh variasi penamaan versi (v1, v2, v2_updated) telah dieliminasi total sehingga seluruh build dan pembaruan mengarah langsung ke satu dokumen kanonik ini.

Sumber draf acuan:
- `01_Naskah_Utama/BAB_I_DRAF.md`
- `01_Naskah_Utama/BAB_II_DRAF.md`
- `01_Naskah_Utama/BAB_III_DRAF.md`
- `01_Naskah_Utama/DAFTAR_PUSTAKA_SEMENTARA.md`
- `04_Riset_&_Metodologi/ANATOMI_RAPIH_ARTHUR.md` (G1–G12)
- `04_Riset_&_Metodologi/PEDOMAN_BAB123_TEMPLATE.md`

## 2. Verified-vs-Proposed (Kepatuhan Spesifikasi)

| Kode | Item | Status | Realisasi |
|---|---|---|---|
| V-G1 | Cover KAPITAL 14pt stage-spacing | VERIFIED | `PROPOSAL TUGAS AKHIR` 14pt bold center; judul KAPITAL 14pt bold center + asing italic+bold (`INFLUENCER MARKETING`, `ELECTRONIC WORD-OF-MOUTH`, `PERCEIVED ENJOYMENT`, `INTENTION TO PLAY`, `MOBILE LEGENDS`); Nama: `Siddharta Pratama Budiono` dan NIM: `312023017` (label NIM: dan kurung dieliminasi); Prodi KAPITAL bold tanpa S1. |
| V-G2 | 3 Seksi Romawi -> Arab | VERIFIED | sec0 cover tanpa nomor; sec1 `lowerRoman start2` footer kanan `UKRIDA \| ii` (dimulai langsung dari DAFTAR ISI); sec2 `decimal start1` footer kanan `UKRIDA \| 1`; margins `4.0/3.0/3.0/3.0 cm`; header/footer `1.27 cm`. |
| V-G3 | TOC/LOT/LOF native dots 7938 | VERIFIED | 1 field `TOC \o "1-3" \h \z \u`; 30 baris dot leader rata kanan pada `14.0 cm (=7938 dxa)`; HALAMAN PERSETUJUAN dieliminasi total. |
| V-G4 | Headings KAPITAL/Title Case | VERIFIED | H1 center bold 12pt KAPITAL (`DAFTAR ISI/TABEL/GAMBAR`, `BAB I/II/III`, `DAFTAR PUSTAKA`); H2/H3 left bold Title Case; asing italic di dalam heading; outline level sinkron. |
| V-G5 | Body justify 1.5 first 1.25 cm | VERIFIED | TNR 12pt justify 1.5 spasi, first line indent 1.25 cm, pure black (`000000`); enumerasi hanging indent; asing miring. Notasi sampel N= dikonversi menjadi narasi mengalir. |
| V-G6 | Block quote | PROPOSED | Sesuai pedoman bila ada kutipan langsung panjang. |
| V-G7 | Tabel APA open-header | VERIFIED | Tabel 2.1 (S01–S18) dan Tabel 3.1 (Operasionalisasi Variabel); top/bottom border + header bottom border tanpa garis vertikal; caption 11pt bold di atas; sumber 10pt italic di bawah. |
| V-G8 | Gambar 2.1 Rerangka | VERIFIED | `fig_rerangka_21.png` / `fig_v2.png` 300 DPI, bentuk elips untuk variabel X1, X2, X3, Y dengan tipografi besar 16pt/12.5pt, panah H1–H3 langsung, H4 simultan dieliminasi. |
| V-G9 | Persamaan nomor kanan | VERIFIED | Persamaan (3.1) dan (3.2) subskrip Unicode matematis miring center dengan nomor kanan. |
| V-G10 | Bahasa & Sitasi APA 7th | VERIFIED | Parentetik `&` / naratif `dan`; `et al.` miring; 0 dkk; 48 entri daftar pustaka bebas ghost citations. |
| V-G11 | Footer UKRIDA Rata Kanan | VERIFIED | Format `Universitas Kristen Krida Wacana \| nomor` 10pt bold black di margin kanan. |
| V-G12 | Pustaka 48 Entri Hanging | VERIFIED | Hanging indent 1.25 cm, spasi 1.15, alfabetis, hyperlink hitam tanpa garis bawah biru. |

## 3. Hasil Audit Verifikasi

- File target: `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ.docx`
- Ukuran: 478.895 bytes
- Status Audit `scratch/verify_all.py`: **PASS (52/52 checks, 0 errors)**.