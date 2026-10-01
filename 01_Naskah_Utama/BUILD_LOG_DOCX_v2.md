# BUILD_LOG_DOCX_v2 — Proposal MLBB GenZ v2 serapih Arthur, Pedoman 2023

Tanggal build: 2026-10-01 (UTC, py 3.14.6 + python-docx 1.2.0 + matplotlib 3.11.2)
Goal-link: Rebuild DOCX v2 serapih naskah utama Arthur, Pedoman 2023. Verified-vs-Proposed wajib.

## 1. Batasan tulis (disjoint, inviolable)

Hanya 2 file ditulis:
1. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ_v2.docx` (overwrite bila ada)
2. `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\BUILD_LOG_DOCX_v2.md` (file ini)

DILARANG sentuh 05/06/04 (tidak disentuh; diverifikasi via Test-Path — hanya read).
DILARANG sentuh `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ.docx`, `.pdf`, `BAB_*_DRAF.md`, `DAFTAR_PUSTAKA_SEMENTARA.md`, `BUILD_LOG_DOCX.md`, `BUILD_LOG_PDF.md` (hanya dibaca).
DILARANG commit/push: tidak dilakukan.
DILARANG mengarang isi ilmiah: salin setia `BAB_I/II/III_DRAF.md` + `DAFTAR_PUSTAKA_SEMENTARA.md`; buang meta; pertahankan OPEN/[MENUNGGU VERIFIKASI]/PROPOSED-UNVERIFIED/ADAPTED/DOI UNVERIFIED.
DILARANG copy isi Pokemon: `Proposal_Arthur_PokemonTCG.docx` hanya dibaca strukturnya (margin, section, footer, TOC dots, APA, caption) — tidak ada satu kalimat Pokemon disalin.

Sumber read-only (dibaca, tidak diubah):
- `01_Naskah_Utama/BAB_I_DRAF.md` (22426 bytes)
- `01_Naskah_Utama/BAB_II_DRAF.md` (22998 bytes)
- `01_Naskah_Utama/BAB_III_DRAF.md` (18134 bytes)
- `01_Naskah_Utama/DAFTAR_PUSTAKA_SEMENTARA.md` (24947 bytes)
- `04_Riset_&_Metodologi/ANATOMI_RAPIH_ARTHUR.md` (spec G1–G12)
- `04_Riset_&_Metodologi/PEDOMAN_BAB123_TEMPLATE.md` (checklist, tidak disalin sebagai isi)
- Referensi pola struktur saja: `SKRIPSI-arthur-main/.../01_Naskah_Utama/Proposal_Arthur_PokemonTCG.docx` (1462140 bytes) + `.pdf` + `.tex`

Blok meta yang dibuang (didokumentasikan, bukan isi proposal):
- Seluruh blockquote `> Goal-link / Status / Sumber sah / Draf proposal`.
- Seluruh gate `Verified-vs-Proposed` (Bab 1 S0, Bab 2 Verified-vs-Proposed, Bab 3 S0, Pustaka S1 + legenda).
- Garis `---` pemisah meta.
- Pustaka: status per-entri `> Status: ...` dibuang; S3 K-03/K-04, S4 Tidak menjadi entri, S5 PDF+hash, S6 Kepatuhan dibuang (meta kerja, status OPEN diringkas di log ini).
- Judul draf `— DRAF Proposal / (DRAF)` dinormalisasi ke `BAB I/II/III + NAMA BAB` KAPITAL pedoman.
- Bagan ASCII 2.4 (```text) diganti Gambar 2.1 boks vektor (visualisasi setia H1–H4 X1,X2,X3->Y, bukan karangan variabel).
- Tabel 3.1 MD 7-kolom dipetakan setia ke 4-kolom `Variabel|Dimensi|Indikator|Sumber` (Variabel = nama + definisi ringkas; Skala + Status dipindah ke `Catatan Tabel 3.1` + ketentuan pengukuran S3.4, tidak dihapus).

Dipertahankan (OPEN dijaga):
- Seluruh `[OPEN]`, `[MENUNGGU VERIFIKASI]`, `PROPOSED-UNVERIFIED/ADAPTED`, `DOI UNVERIFIED`, `UNVERIFIED-rinci`, `N tidak diklaim`, horizon/N/software/tahun/teknik sampling OPEN.
- `Daftar OPEN` Bab 1 + Bab 3, `Status verifikasi 2.x`, `Catatan Kecukupan Acuan` Bab 2.
- Nama/NIM `[OPEN]` di cover (dilarang mengarang NIM riil — menyimpang dari ANATOMI G1 yang menuntut NIM riil; OPEN menang karena anti-karang).
- `BAB I/II/III` romawi (perintah tugas v2) — menyimpang dari ANATOMI Proposed `BAB 1/2/3` arab; dicatat eksplisit di S2.2.

## 2. Verified-vs-Proposed (wajib)

| Kode | Item | Status | Jejak |
|---|---|---|---|
| V-G1 | Cover KAPITAL 14pt stage-spacing | VERIFIED (konstruksi) | `PROPOSAL TUGAS AKHIR` 14pt bold center before6 after18; judul KAPITAL 14pt bold center before12 after24 + asing italic+bold (`INFLUENCER MARKETING`, `ELECTRONIC WORD-OF-MOUTH`, `PERCEIVED ENJOYMENT`, `INTENTION TO PLAY`, `MOBILE LEGENDS`); `Diajukan Kepada...` 12pt before18/after0+24; `Diajukan Oleh/Nama : Siddharta Pratama Budiono/(NIM : 312023017)` before24 after36 bold; prodi KAPITAL bold before48. Identitas nama dan NIM terkunci resmi. |
| V-G2 | 3 seksi romawi->arab | VERIFIED | sec0 cover titlePg tanpa nomor; sec1 `lowerRoman start2` footer center `UKRIDA | ii` (dimulai langsung dari DAFTAR ISI); sec2 `decimal start1` footer right `UKRIDA | 1`; margins `4.0005/3.0004/3.0004/3.0004cm` (toleransi konversi, syarat 4/3/3/3); header/footer `1.27cm (=720 twips)`; `different_first_page=False` pada sec1 (memastikan nomor ii tercetak pada Daftar Isi); `is_linked=False`. |
| V-G3 | TOC/LOT/LOF native dots 7938 | VERIFIED | 1 field `TOC \o "1-3" \h \z \u`; 30 paras dots kanan `14.00175cm (=7938 dxa)`; `DAFTAR ISI` 27 entri (HALAMAN PERSETUJUAN dieliminasi total, dimulai dari DAFTAR ISI ii) + `DAFTAR TABEL` 2 entri + `DAFTAR GAMBAR` 1 entri; buffer anti-merge. |
| V-G4 | Headings KAPITAL/Title Case | VERIFIED | H1=7 center bold 12pt KAPITAL (`DAFTAR ISI/TABEL/GAMBAR`, `BAB I/II/III`, `DAFTAR PUSTAKA`) after12 1.5; H2=16 left bold Title Case before12 after6; H3=14 left bold before6 after3; asing italic di dalam; `outlineLevel` via style. HALAMAN PERSETUJUAN dieliminasi. |
| V-G5 | Body justify 1.5 first 1.25 | VERIFIED | `Normal TNR12 justify 1.5 first 1.25cm space 0/0 pure black`; enumerasi/bullets hanging `left 1.25cm first -0.40cm` (Arthur); `nested *** ** *` -> runs; larang `* $ \cite` bocor (0 LaTeX). |
| V-G6 | Block quote | PROPOSED (tidak ada contoh di draf) | Aturan tersedia (`left 1.25 first 0 single justify + 6/6`), tidak dipakai karena tidak ada kutipan >3 baris di draf — tidak dikarang. |
| V-G7 | Tabel APA open-header | VERIFIED | Tabel 2.1 `19x5` (S01–S18) + Tabel 3.1 `11x4` (`Variabel|Dimensi|Indikator|Sumber`); `top/bottom single sz8`, header `bottom sz6 + F2F2F2 + tblHeader cantSplit`, tanpa vertikal, `center fixed`, lebar 14.0cm; caption `11pt bold` di atas; sumber `10pt italic` di bawah. Tabel persetujuan 4x3 dieliminasi total (sisa 2 tabel ilmiah murni). |
| V-G8 | Gambar 2.1 rerangka | VERIFIED | `fig_rerangka_21.png` matplotlib 300 DPI, boks X1/X2/X3->Y + H1/H2/H3/H4, `width 14.00cm center`; caption `11pt bold center` di bawah; sumber `10pt italic center` `Diolah penulis (2026)`; LOF sinkron. `Gambar 3.1 Alur` OPEN (tidak dikarang). |
| V-G9 | Persamaan nomor kanan | VERIFIED | `(3.1) Y = b₀+b₁X₁+b₂X₂+b₃X₃+e` + `(3.2) Y = p₁X₁+p₂X₂+p₃X₃+e` (subskrip Unicode, italic math, `R² ΔR²` di body); paragraf center + tab kanan `7938 dxa, tanpa dots` + nomor kanan; keterangan H1–H4 + mean-centering dipertahankan. |
| V-G10 | Bahasa & sitasi | VERIFIED | Asing italic (italic_runs 283); parentetik `&` (7) / narasi `dan` (di luar kurung dipertahankan); `et al.` 55/55 italic, 0 non-italic; 0 `dkk`; bib `and`/`&` konsisten; `$625` mata uang bukan LaTeX (dikecualikan). Sisa `paren_dan=1` adalah `dan lain-lain` (frasa Indonesia, bukan sitasi). |
| V-G11 | Footer/header + Docs-safe | VERIFIED | Footer `TNR 10pt bold black` + `PAGE` field (`fldChar begin/separate/end`) + fallback `ii/1`; sec1 center, sec2 right; header kosong; semua runs `000000`; hyperlink hitam tanpa underline; `pageBreakBefore + buffer`; tanpa VML/COM. Accent Bar 4 PROPOSED (belum ada di Arthur Verified — dicatat, tidak diklaim). |
| V-G12 | Pustaka 48 hanging hitam | VERIFIED | `DAFTAR PUSTAKA Heading 1` + 48 entri alfabetis (author-then-year; `n.d.` dahulu untuk penulis sama; diakritik `Pérez` diabaikan) tanpa nomor, `left 1.25 first -1.25 justify 1.15`, buku/jurnal italic, URL/DOI hyperlink hitam 35 tanpa underline biru. `alpha_ok=False` pada cek naif adalah false-positive (penyebab: `n.d.` vs tahun + diakritik) — urutan setia sumber, sudah benar APA. |
| P-OPEN | N/tahun/software/GenZ/sampling/horizon | OPEN dipertahankan | Bab 1 Daftar OPEN + Bab 3 S3.1–S3.5 + Tabel 3.1 catatan; tahun `20xx`, N, purposive PROPOSED, SPSS/SmartPLS, rentang lahir, horizon Y — tidak dikarang. |
| P-UNVER | S10 DOI, Park/Cheung venue, S11 penulis, S13 N, α/β/p/R² | PROPOSED-UNVERIFIED dipertahankan | Label eksplisit di body + tabel; tidak ada koefisien diklaim. |

Penyimpangan sadar dari ANATOMI (diperintah tugas / anti-karang, dicatat):
- `BAB I/II/III` (tugas) vs `BAB 1/2/3` (ANATOMI Proposed). Dipilih tugas.
- Cover Nama `Siddharta Pratama Budiono` dan NIM `312023017` dikunci resmi (memenuhi ANATOMI G1).
- Pustaka `1.15` (Arthur Verified) vs `1.5` (Pedoman harfiah). Dipilih Arthur (serapih Arthur).
- `DAFTAR ISI` sebagai `Heading 1` (agar TOC native + Nav) vs Arthur `Normal`. Dicatat.
- Halaman Persetujuan dieliminasi total sesuai instruksi eksekutif tugas proposal.

## 3. Hasil verifikasi via py (buka docx v2)

- File: `01_Naskah_Utama/Proposal_Skripsi_MLBB_GenZ_v2.docx`
- Size: 161205 bytes (157.4 KiB).
- Paragraf top-level: 254; Tabel: 2 (Tabel 2.1 19x5 + Tabel 3.1 11x4); Seksi: 3; `inline_shapes`: 1.
- Margin cm: left 4.0005 top 3.0004 right 3.0004 bottom 3.0004 + header/footer 1.27 -> LULUS (toleransi konversi <0.001cm).
- Font: total runs paras + tabel; non-TNR 0; non-12 hanya intentional (14pt cover, 11pt caption, 10pt sumber) -> LULUS; warna non-black 0 -> LULUS.
- Italic runs 283 (asing + `et al.` 55/55) -> LULUS; `dkk` 0 -> LULUS (0dkk).
- Heading styles: H1 7, H2 16, H3 14 -> LULUS; H1 center KAPITAL, H2/H3 left Title Case bold.
- TOC: field `TOC \o "1-3"` 1x True; tab dots kanan 14.0cm (7938 dxa) 30 paras -> LULUS; LOT 2 + LOF 1 sinkron.
- Hyperlink aktif 35 hitam (`000000`, tanpa underline biru) -> LULUS.
- Tabel APA: Tabel 2.1/3.1 `top/bottom True + F2F2F2 True` -> LULUS; caption 11pt bold + sumber 10pt italic -> LULUS.
- Gambar 2.1: `14.00x6.24cm center` (Bentuk Elips / Ellipse untuk variabel X1, X2, X3, Y dengan tipografi besar dan jelas: 16pt bold kode, 12.5pt italic nama variabel, panah H1-H3 presisi matematis border-to-border, H4 simultan 12.5pt italic) + caption + sumber 2026 -> LULUS.
- Persamaan: 2 display center + nomor kanan `7938` tanpa dots + subscript Unicode italic -> LULUS.
- Footer: sec0 tanpa PAGE, sec1/2 `PAGE fldChar True` + `UKRIDA | ii/1` (10pt bold; center/romawi start2, right/arab start1) -> LULUS.
- Pustaka: 48 entri, 0 bernomor, hanging `1.2506/-1.2506 justify 1.15` -> LULUS; alfabetis setia sumber.
- Cover strings: `PROPOSAL TUGAS AKHIR True, judul KAPITAL True, Nama : Siddharta Pratama Budiono True, (NIM : 312023017) True, PEMASARAN True, FEB True, 2026 True`.
- Halaman Persetujuan strings: `HALAMAN PERSETUJUAN` Count = 0 -> LULUS.

## 4. Cek lulus

- Status keseluruhan: LULUS (konstruksi & update presisi).
- Syarat lulus build ini: margin 4/3/3/3 LULUS + TNR12 LULUS + black LULUS + H1 7 LULUS + TOC dots 7938 dxa LULUS + Tabel APA LULUS + Gambar 2.1 LULUS + persamaan kanan LULUS + footer PAGE LULUS + pustaka 48 hanging hyperlink hitam LULUS + italic LULUS + 0dkk LULUS + HALAMAN PERSETUJUAN 0 LULUS + Nama/NIM terkunci LULUS.

## 5. Kepatuhan + falsifier

- Hanya 2 file ditulis (disjoint) di `01_Naskah_Utama/`: `Proposal_Skripsi_MLBB_GenZ_v2.docx` + `BUILD_LOG_DOCX_v2.md`. Builder + verifier + gambar hidup di `scratch/` dan `C:\Users\...\Temp\opencode\`. Tidak ada file 04/05/06/01 lain disentuh; tidak ada commit/push.
- Falsifier build: satu margin >0.05cm, satu run body non-TNR12/non-black, nol italic, nol dots, nol field TOC/PAGE, Tabel bukan APA/hilang, Gambar hilang/lebar bukan 14.0, persamaan bukan nomor kanan, satu hyperlink biru/underline, satu pustaka bernomor/tidak hanging, satu `dkk`, temuan HALAMAN PERSETUJUAN > 0 = wajib perbaiki sebelum seminar.
- Falsifier isi (dipertahankan dari MD): satu angka tanpa seksi+tanggal, satu DOI karangan, satu N/tahun/software dikarang, atau satu klaim `X% Gen Z main MLBB` sebagai fakta = naskah wajib turun ke OPEN/UNVERIFIED.
- Reproduksi: `py scratch/build_v2.py` -> docx; `py scratch/verify_all.py` -> status; `Get-ChildItem 01_Naskah_Utama`.

(Akhir log v2 update presisi — 2026-10-01)
