# ANATOMI RAPIH ARTHUR — Verified-vs-Proposed + Spec G1–G12 + Gap Draf MLBB

> Goal-link: Buat skripsi serapih naskah utama Arthur. Verified-vs-Proposed wajib.
> Tanggal ukur: 2026-10-01 (UTC). Metode: `py` + `python-docx 1.2.0` + `Get-ChildItem`. DILARANG menebak angka.
> File ini SATU-SATUNYA output yang boleh ditulis (disjoint). DILARANG sentuh `01/05/06` lain. DILARANG commit/push.

**Sumber read-only (tidak diubah):**

- `Z:\SKRIPSII\SKRIPSI ARTHUR\SKRIPSI-arthur-main\SKRIPSI-arthur-main\01_Naskah_Utama\Proposal_Arthur_PokemonTCG.docx` + `.pdf` + `.tex`
- `directives/generate_thesis_word_document.md` (6460 bytes, versi Arthur-main) + `execution/build_proposal_word.py` (165742 bytes, 3398 baris)
- `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama\Proposal_Skripsi_MLBB_GenZ.docx` (draf pembanding)
- Catatan: `directives/generate_thesis_word_document.md` + `execution/build_proposal_word.py` di workspace `skripsi siddharta` = 0 bytes (placeholder). Pola dibaca dari arsip Arthur-main (secukupnya, via `Select-String`).

---

## 0. Bukti ukur (tanpa tebak)

### 0.1 Get-ChildItem (ukuran file)

| File | Length (bytes) | Sumber |
|---|---|---|
| `Proposal_Arthur_PokemonTCG.docx` | 1462140 | `Get-ChildItem 01_Naskah_Utama` Arthur-main |
| `Proposal_Arthur_PokemonTCG.pdf` | 1068259 | sama |
| `Proposal_Arthur_PokemonTCG.tex` | 107740 | sama |
| `Proposal_Skripsi_MLBB_GenZ.docx` | 69567 | `Get-ChildItem 01_Naskah_Utama` siddharta |
| `Proposal_Skripsi_MLBB_GenZ.pdf` | 263674 | sama |
| `build_proposal_word.py` (Arthur-main) | 165742 | `Get-Item` |
| `generate_thesis_word_document.md` (Arthur-main) | 6460 | `Get-Item` |
| `build_proposal_word.py` + directive (siddharta) | 0 + 0 | `Get-ChildItem` — placeholder, jangan dipakai |

Rasio kasar: docx Arthur ~21x lebih besar dari draf (1462140 vs 69567) — konsisten dengan isi 378 paras + 5 tabel + 6 gambar vs 265 paras + 3 tabel + 0 gambar (ukur `python-docx`, lihat 0.2).

### 0.2 python-docx — ringkasan struktur

| Metrik (ukur `docx.Document`) | Arthur (Verified) | MLBB / Draf kita (Verified) |
|---|---|---|
| `len(paragraphs)` | 378 | 265 |
| `len(tables)` | 5 | 3 |
| `len(sections)` | 3 | 1 |
| `inline_shapes` / `image_rels` | 6 / 6 | 0 / 0 |
| `H2 / H3 count` | 16 / 24 | 16 / 10 |
| `OMML paras` (`oMathPara/oMath`) | 7 | 0 |
| `numbered-eq plain` regex `\(\d+\.\d+\)$` | 0 | 2 (`(3.1)`, `(3.2)` plain text, `hasOMML=False`) |
| `italic_runs` | 459 | 248 |
| `paren cites` estimasi | ~54 | ~10 |
| `nonblack runs` | 0 (pure black) | 0 (pure black) |
| `TOC_like paras` (`TOC1/2/3` + tab dots) | 56 | 0 native; manual `Normal` + `—` placeholder |
| `TOC field` (`instrText TOC`) | 0 `TOC \o` field aktif di body docx final (TOC disuntik statis + `TOC1/2/3` + `_add_dot_tab`); 1 field di MLBB: `TOC \o "1-3" \h \z \u` | MLBB: 1 field `TOC \o "1-3"` |
| `PAGE/PAGENUM fields` di body | 0 (nomor di footer via `w:instr PAGE`, bukan body) | 0 |
| `hyperlinks` biru | 0 (bib `HYPERLINK=False`, URL plain hitam) | 0 biru, tapi URL plain + meta bocor |

Skrip ukur disimpan di luar workspace (tidak melanggar disjoint): `C:\Users\...\Temp\opencode\measure*.py` + `measure*_out.txt`.

---

## 1. Verified-vs-Proposed (wajib)

Konvensi: **Verified** = hasil `python-docx` / `Select-String` atas file di atas. **Proposed** = yang harus ditiru builder v2 (dari `.tex` + directive + `build_proposal_word.py`).

### 1.1 Kertas & margin

- **Verified Arthur:** `sec0/1/2` semua `L=4.00cm R=3.00cm T=3.00cm B=3.00cm`, `pgSz 11906x16838` (A4), `pgMar left 2268 twips (=4.0cm) right/top/bottom 1701 (=3.0cm)`, `header/footer dist 720 twips`. Efektif teks `21.0-4.0-3.0=14.0cm`.
- **Verified MLBB:** sama `4.00/3.00/3.00/3.00`, `pgSz` sama, `header/footer 850` (bukan 720) — selisih kecil tapi menandakan template beda.
- **Verified .tex:** `left=4cm, right=3cm, top=3cm, bottom=3cm, a4paper`, `documentclass[12pt,a4paper]`.
- **Verified directive:** `Paper ISO A4 (21.0x29.7cm)`, `Left 4.0 Right 3.0 Top 3.0 Bottom 3.0 (Area teks efektif = 14.0cm)`.
- **Proposed builder v2:** kunci `Cm(4.0/3.0/3.0/3.0)`, `target_right=Cm(14.0)`, jangan pakai `850`.

### 1.2 Cover (kapital, logo, NIM, spasi)

- **Verified Arthur cover (p0–p5, `align=CENTER`):**
  - p1 `PROPOSAL SKRIPSI` — `14.0pt bold`, `space_before 6pt after 18pt`.
  - p2 judul panjang — `14.0pt bold`, `before 12pt after 24pt`, istilah asing `italic+bold` (`HEDONIC MOTIVATION`, `DESIRE FOR COMPLETENESS`, `SPECULATIVE MOTIVE`, `IMPULSIVE BUYING`, `SELF-CONTROL`).
  - p3 `Diajukan Kepada... / Untuk Menyusun...` — `before 18pt after 24pt`.
  - p4 `Diajukan Oleh: / Arthur Reezan / (312023002)` — `before 24pt after 36pt`, nama+NIM `bold`.
  - p5 `PROGRAM STUDI... / FAKULTAS... / UNIVERSITAS... / JAKARTA 2026` — `before 48pt`, semua `bold`, KAPITAL.
  - Logo: `shape0 w=3.20cm h=3.20cm` (ukur), `image_rels` pertama. `.tex`: `\includegraphics[width=3.2cm]{images/ukrida_pentagram.pdf}`. Builder: `add_picture(..., width=Cm(3.2))`, `p_logo space_before 0 after 18pt center`.
- **Verified MLBB cover (p0–p6, `align=CENTER`, `ls=1.5` semua):**
  - p0 `PROPOSAL TUGAS AKHIR` — `12.0pt bold` (bukan 14pt), `after 12pt`.
  - p1 judul — `12.0pt bold`, tanpa stage spacing.
  - p2 `Disusun untuk... Model B...` (kalimat tambahan, tidak ada di Arthur).
  - p3/p4 `Nama : [OPEN]` / `NIM : [OPEN]` (placeholder, bukan nama/NIM riil).
  - p5/p6 prodi ganda, tidak KAPITAL penuh.
  - Logo: `0 shapes` — tanpa logo.
- **Proposed:** tiru Arthur persis — `14pt bold center` untuk label + judul, NIM riil (bukan `[OPEN]`), logo `3.2cm center`, spasi bertahap `6/18/12/24/18/24/24/36/48` (bukan `1.5` rata), KAPITAL prodi/fakultas/univ/kota+tahun.

### 1.3 Frontmatter (persetujuan, TOC native + LOT/LOF, romawi, judul tak bernomor)

- **Verified Arthur:**
  - `DAFTAR ISI` p7 `Normal center bold` (judul tak bernomor, tanpa `BAB`).
  - `DAFTAR TABEL` / `DAFTAR GAMBAR` masing-masing `Heading 1` halaman sendiri (`p54`, `p60`), + entri `TOC 11` (`Tabel 1.1...7`, `Gambar 1.1...1` dst, 5+5 entri).
  - `DAFTAR PUSTAKA` `Heading 1` p323 (tak bernomor).
  - `BAB 1/2/3` sebagai `Heading 1` + `addcontentsline{toc}{section}{BAB...}` di `.tex`; frontmatter headings tidak pakai nomor Bab.
  - Sectioning: `sec0 titlePg` (cover, tanpa nomor), `sec1 pgNumType lowerRoman start=1` + footer `Universitas Kristen Krida Wacana | i`, `sec2 pgNumType decimal start=1` + footer `... | 1`, `different_first_page=True`, `header/footer is_linked=False` untuk sec1/2. `.tex`: `\pagenumbering{roman}` → `\pagenumbering{arabic}`.
  - Footer runs: teks + `PAGE` field terpisah (ukur `pagenum=True` di footer xml, `Footer style 10.0pt`).
- **Verified MLBB:**
  - `HALAMAN PERSETUJUAN` + `DAFTAR ISI` sebagai `Heading 1 center`, tapi `DAFTAR TABEL/GAMBAR` **tidak ada** sebagai heading (gap fatal).
  - `DAFTAR ISI` isi manual: `Normal` + `—` placeholder halaman (p19–p44), catatan `tekan Ctrl+A lalu F9...` + `Catatan TOC: entri manual... tanda — adalah placeholder` (bocor ke naskah).
  - `sections=1`, `pgNumType NOT FOUND`, `titlePg NOT FOUND`, tanpa footer/header sama sekali.
  - `DAFTAR PUSTAKA` p47 sebagai `Normal` (bukan Heading), diikuti meta bocor (lihat 1.11).
- **Proposed:** 3 section (cover / romawi / arab), `lowerRoman` → `decimal`, footer UKRIDA + nomor (lihat 1.10), `DAFTAR ISI/TABEL/GAMBAR` masing-masing halaman baru `page_break_before=True` + buffer anti-merge (directive), `LOT/LOF` sebagai `TOC 1` + `_add_dot_tab_7938`, judul frontmatter tak bernomor tapi masuk TOC via `addcontentsline`.

### 1.4 TOC dots `14.0cm / 7938 dxa`

- **Verified Arthur paras:** `w:pos="7927"` + `w:leader="dot"` + `w:val="right"` di semua `toc1/2/3` (ukur `tab_pos_vals=['7927']`). `7927 dxa = 13.98cm` (selisih 11 dxa dari 7938, toleransi render).
- **Verified builder:** `parse_xml('<w:tab w:val="right" w:leader="dot" w:pos="7938"/>')`, fungsi `_add_dot_tab_7938`, `target_right=Cm(14.0)`, komentar `21.0-4.0-3.0=14.0cm=7938 dxa`.
- **Verified directive:** `Right + Dot Leader pada 14.0cm=7938 dxa`, formula `Tab Stop = 13.8cm - Left Indent` (L1 `13.8/14.0`, L2 `13.2`, L3 `12.6`) agar tidak melewati margin di Word/WPS/Google Docs.
- **Verified MLBB:** `TOC styles` tidak ada (`TOC 1/2/3 missing`), tab dots hanya di catatan manual, field tunggal `TOC \o "1-3"` tanpa `7938`.
- **Proposed:** pakai `7938` di builder (`_add_dot_tab_7938`), `right_indent=0`, terapkan per-level sesuai formula directive. `7927` di file final adalah artefak render Word, bukan untuk ditiru mentah — builder tetap tulis `7938`.

### 1.5 Isi — Bab centered bold KAPITAL, subbab Title Case bold

- **Verified Arthur:** `Heading 1 bold=True align=CENTER ls=1.5 after 12pt`, teks `BAB 1\nPENDAHULUAN`, `BAB 2\nKAJIAN PUSTAKA...`, `BAB 3\nMETODE PENELITIAN` (arab, KAPITAL, 2 baris). `.tex`: `\titleformat{\section}[block]{\normalfont\fontsize{12}{14}\bfseries\centering\MakeUppercase}` + `\titlespacing*{18pt}{12pt}`. Builder: `parse_markdown_runs(..., Pt(12), bold=True)` + `outline level` untuk Nav/Docs Tabs.
- **Verified MLBB:** `Heading 1 align=CENTER` juga, tapi teks `BAB I/II/III` (romawi, bukan arab) + `HALAMAN PERSETUJUAN`/`DAFTAR ISI`/`DAFTAR PUSTAKA` campur.
- **Subbab Verified Arthur:** `Heading 2/3` `bold=True ls=1.5` (`H2 before 12 after 6`, `H3 before 6 after 3` via style default), contoh `1.1 Latar Belakang Penelitian`, `1.4.1 Manfaat Teoretis`, `2.1.1 Landasan Teoretis: Pendekatan Keuangan Perilaku (Behavioral Finance)` — Title Case, asing italic di dalam. `xml_has_TOC=True` (masuk Nav). `.tex`: `\titleformat{\subsection}[block]{\bfseries}` + spacing `12/6`, `subsubsection 10/4`.
- **Verified MLBB H2/H3:** `align=LEFT ls=1.5 sz=12 bold=True`, contoh sama struktur tapi tanpa italic konsisten + ada `Daftar OPEN (wajib dikunci...)` bocor sebagai H2.
- **Proposed:** Bab `Heading 1 center bold KAPITAL arab (BAB 1/2/3)`, subbab `Heading 2/3 left bold Title Case 12pt`, asing italic di dalam judul, `outlineLevel` diset untuk Google Docs Tabs.

### 1.6 Body — justify TNR12 1.5 indent 5 ketukan

- **Verified Arthur body (p70, p75–76):** `align=JUSTIFY ls=1.5 first=1.250597cm`, `Normal TNR 12.0pt 000000`, `space 0/0`. `.tex`: `\onehalfspacing`, `\parindent 1.25cm`, `\parskip 0pt`. Directive: `Body 12pt 1.5 justify first 1.25cm, 0pt before/after`.
- **Verified MLBB body:** `align=JUSTIFY ls=1.5` tapi `first=None` (tanpa indent) di p13/p18/p48; `Normal TNR 12.0pt 000000` benar tapi indent hilang → terlihat rapat/mepet.
- **Proposed:** `Normal TNR12 justify 1.5 first=Cm(1.25) space 0/0`, `make_run_pure_black` tiap run.

### 1.7 Kutipan >3 baris (block quote)

- **Verified Arthur:** tidak ditemukan block quote single-spasi murni di docx final. Paras `left=1.25cm` semuanya `ls=1.5` bullets/enumerasi (`•` + `1.` dengan `first -0.40/-0.62cm`, `left 1.25cm`, `justify`) — bukan kutipan langsung. `.tex`/directive tidak mencontohkan block quote panjang di sampel ini.
- **Verified MLBB:** sama — `left>=0.9cm` hanya bib `1.27/-1.27` (hanging), bukan quote.
- **Proposed (dari prompt + UKRIDA, untuk builder v2):** kutipan >3 baris = `Normal` turunan `left=Cm(1.25) (atau 1.0 per pedoman) first=0 ls=1.0 (single) justify TNR12`, tanpa tanda kutip, spasi atas/bawah 6pt. Tandai `G6` sebagai Proposed murni (belum ada contoh Verified di kedua docx) — jangan klaim sudah Verified.

### 1.8 Tabel — APA grid + judul di atas + sumber di bawah

- **Verified Arthur (5 tabel):**
  - Borders: `tblBorders top single sz8 bottom single sz8` (=1pt), `header row bottom single sz6` (=0.75pt), `insideV/H False`, tanpa vertikal. Header `shd fill F2F2F2`, `tblHeader + cantSplit`, `jc center`, `tblLayout fixed`.
  - Contoh `table0 8x5`, `table1 11x5`, `table2 6x3`, `table3 28x5`, `table4 11x8`.
  - Judul di atas: `Tabel 1.1: Matriks...` `11.0pt bold` (`Research Gap` italic di dalam), `align` kiri/ragged (p101). LOT: `TOC 11` `Tabel 1.1...7` dst.
  - Sumber di bawah: `Sumber: Data diolah... (2026).` italic (p102, `runs italic True`, size inherit).
  - Builder: `apply_apa7_table_borders()` + `sz8/sz6/000000` + `F2F2F2` + caption `Pt(11) bold` + sumber `Pt(10) italic`.
- **Verified MLBB (3 tabel):** `style TableGrid` (grid penuh + vertikal), `has_top/bottom 0` (bukan APA), caption hilang — hanya `Tabel berikut merangkum 18 studi...` (`Normal center`, bukan `Tabel X.X:`), tanpa `Sumber:` di bawah, tanpa LOT.
- **Proposed:** APA open 3 garis, tanpa vertikal, judul `11pt bold` di atas, sumber `10pt italic` di bawah, `LOT` native.

### 1.9 Gambar — bus sentral/elips + caption di bawah

- **Verified Arthur:** `6 image_rels`, `shape w: 3.20 (logo), 13.50/13.50/13.50/14.00/13.00cm` (ukur). Builder: `fig11/12/13 width Cm(13.5)`, `rerangka Cm(14.0)`, `alur Cm(13.0)`. Caption body `center`: `Gambar 1.1...`, `Gambar 2.1 Model Rerangka Konseptual...`, `Gambar 3.1 Diagram Alur...` (`11pt bold` per builder; ukur p73/p78/p87/p205 `align CENTER`). Sumber di bawah caption `10pt italic` (`Sumber: Statista... / The Pokemon Company...`). LOF: `TOC 11` 5 entri. `.tex`: `\includegraphics[width=0.80\textwidth]` + `\captionsetup[figure]{position=bottom, justification=centering, font=small}` + `\figurename Gambar`.
- **Verified MLBB:** `0 shapes/images`, `0 Gambar captions`, `2.4 Rerangka Penelitian` tanpa gambar → bus/elips hilang.
- **Proposed:** gambar `center`, `300 DPI crop`, lebar `13.5` umum / `14.0 rerangka` / `13.0 alur`, caption `11pt bold center` di bawah gambar, sumber `10pt italic center` di bawah caption, masuk `LOF`.

### 1.10 Persamaan bernomor kanan

- **Verified Arthur:** `OMML_paras=7` (`oMathPara/oMath` via `pandoc -f latex -t docx`), `numbered_eq_like=0` (nomor section via `\numberwithin{equation}{section}` di PDF, bukan `(3.1)` plain di docx body). Builder: `latex_to_omml_pandoc()` + `add equation ... line_spacing 1.5` + fallback Unicode (`X₁ X₂ X₃ Y M R² ΔR² p<0,05 α n=30`).
- **Verified MLBB:** `OMML 0`, `2 plain`: `Y = b0+b1X1... (3.1)`, `Y = p1X1... (3.2)` (`hasOMML=False`, `Normal`, tanpa italic/subscript, nomor ketik manual).
- **Proposed:** OMML native (`m:oMathPara`) + nomor kanan `(3.x)` via tab kanan / tabel 2-kolom tanpa border (Word) dan `\numberwithin` (TeX). Inline math: `X₁ X₂ X₃ Y M` italic+subscript Unicode, `R² ΔR²`, `p α n`, `β₁–β₇`.

### 1.11 Bahasa — istilah asing italic, sitasi dan/&/et al.

- **Verified Arthur:** `italic_runs 459`, contoh cover + body `media franchise`, `HEDONIC MOTIVATION` (`bold+italic`), bib `Multiple Regression...`, `Journal of Retailing...` italic (judul buku/jurnal italic, sisanya regular). Sitasi: `;` + `et al.,` + `and` di bib (`Aiken, L. S. and West...`), in-text `(Shiller, 2000; Baur et al., 2018; ...)`, `(Qu et al., 2023; Amos et al., 2014)`. Tidak ada `&` mentah di body; `dan` di dalam kalimat Indonesia.
- **Verified MLBB:** `italic_runs 248` tapi tidak konsisten (`INFLUENCER MARKETING` all-caps, `multiplayer...` vs `intention to play`). Sitasi campur: `(Bambauer-Sachse & Mangold, 2011)` + `(Venkatesh dan Bala, 2008)` + `(Davis et al., 1992)` dalam satu naskah.
- **Proposed:** asing (`hedonic motivation`, `impulsive buying`, `self-control`, `media franchise`, `collectibles`, `grading`, dsb) selalu italic; sitasi: narasi pakai `dan` (`Venkatesh dan Bala, 2008`), parentetik pakai `&` (`(Bambauer-Sachse & Mangold, 2011)`), `et al.` untuk 3+ penulis, `;` antar sumber. Builder: `nested parsing *** ** *` → run Word murni, larang `* $ \cite` bocor (directive §3).

### 1.12 Footer/header — UKRIDA 10pt + nomor arab kanan-bawah + Accent Bar 4

- **Verified Arthur footer:** `Footer style 10.0pt` (ukur `doc.styles['Footer'].font.size`), isi `Universitas Kristen Krida Wacana | i` (sec1) / `| 1` (sec2) + `PAGE` field (`pagenum=True` di footer xml). `align=None` (inherit, bukan eksplisit kanan/tengah di xml) — prompt menyebut `romawi kecil tengah-bawah` untuk frontmatter dan `arab kanan-bawah` untuk isi; file Verified tidak menegaskan `RIGHT` di xml, jadi jangan klaim `RIGHT` Verified.
- **Verified Accent Bar:** `xml_has_accent=False`, `has_pBdr=False`, `has_shd=False` di kedua footer Arthur (ukur). Builder docstring menyebut `UKRIDA Accent Bar 4` + `Times New Roman 10pt Bold Black` + `GDocs fallback` + `PAGE field` — artinya Accent adalah **Proposed**, belum terwujud di docx final yang diukur.
- **Verified header:** kosong (hanya footer yang berisi).
- **Verified MLBB:** tanpa header/footer sama sekali (`sections=1`, tidak ada footer paras).
- **Proposed:** footer `TNR 10pt bold black 000000` `Universitas Kristen Krida Wacana | <PAGE>` + `Accent Bar 4` (kanan-bawah) + `PAGE` field dengan `rFonts TNR + color 000000` eksplisit + fallback teks untuk Google Docs. Frontmatter `lowerRoman` (`ii, iii, iv...`), isi `decimal` (`1,2,3...`), cover `titlePg` tanpa nomor.

### 1.13 Pustaka — alfabetis hanging 1.25cm tanpa nomor + hyperlink hitam

- **Verified Arthur (p323 Heading + p324–377):** `left=1.250597cm first=-1.250597cm` (=1.25cm hanging, ukur), `align JUSTIFY`, `ls None` (inherit single/1.15 per directive §10; builder tulis `1.15`), tanpa nomor, alfabetis (`Aiken → Zheng`), judul buku/jurnal italic, `HYPERLINK=False` semua (URL `Tersedia di: https://...` plain hitam, bukan biru). Contoh: `Amos, C., Holmes... (2014). A meta-analysis... Journal of Retailing... 21(2):86–97.`
- **Verified MLBB (p215 Heading CENTER + p216–264):** `left=1.27cm first=-1.27cm` (selisih 0.02cm dari 1.25 — terlihat dari `1.27` eksplisit), `ls=1.5 align JUSTIFY`, alfabetis tapi tercemar: p216 `Daftar di bawah disalin setia dari DAFTAR_PUSTAKA_SEMENTARA.md §2...` + `> Status:` + `Verified-vs-Proposed/Goal-link` bocor ke naskah; URL `https://...` plain tapi tanpa `Tersedia di:` konsisten + `DOI` campur.
- **Verified .tex/bib:** `apalike` + `references.bib`, tanpa numbering.
- **Proposed:** `left=Cm(1.25) first=Cm(-1.25) justify` tanpa nomor, alfabetis nama belakang, `1.15` spasi (directive §10), `hyperlink hitam` (`000000`, `underline None`, bukan biru), hapus semua meta/legenda/status dari body.

### 1.14 TOC dots lanjutan + pure black + Google Docs-safe

- **Verified pure black:** `nonblack 0` di kedua docx; `Title style 17365D` + `Subtitle 4F81BD` ada di styles tapi tidak dipakai di runs body (runs `000000`). Builder: `make_run_pure_black(... 000000)` di level `python-docx` + `w:color` mentah.
- **Verified GDocs-safe:** Arthur memakai `python-docx` murni + `pandoc OMML` + `outlineLevel` untuk Nav/Docs Tabs (builder), tanpa `COM Interop` di file final (COM hanya disebut di directive sebagai proteksi `pageBreakBefore` + buffer anti-merge). MLBB catatan `Ctrl+A F9` menandakan field rapuh di Docs.
- **Proposed:** semua runs `000000`, hyperlink hitam (bukan `0000FF`), `outlineLevel` diset, `pageBreakBefore` untuk `DAFTAR TABEL/GAMBAR`, buffer paragraf setelah TOC, hindari `VML/COM-only`.

---

## 2. Spec checklist G1–G12 (siap eksekusi builder v2)

> Setiap G = inviolable. Builder v2 wajib lolos verifikator `verify_docx_typography.py` + `verify_pdf_docx_parity.py` sebelum disebut rapi.

- **G1 — Cover:** `A4`, logo `Cm(3.2) center after 18pt`, `PROPOSAL SKRIPSI 14pt bold center (before6 after18)`, judul `14pt bold center (before12 after24)` + asing `italic+bold`, `Diajukan... (before18 after24)`, `Diajukan Oleh/Nama/(NIM riil) (before24 after36) bold`, `PRODI/FAKULTAS/UNIV/JAKARTA TAHUN KAPITAL bold (before48)`. Larang `[OPEN]`, larang `12pt`, larang `1.5` rata.
- **G2 — Section & pagination:** 3 section (`titlePg` cover tanpa nomor; `lowerRoman start1` frontmatter `ii...`; `decimal start1` isi `1...`), `header/footer is_linked=False`, `different_first_page=True`, `pgMar 4.0/3.0/3.0/3.0`, `header/footer dist 720`. `HALAMAN PERSETUJUAN` + `DAFTAR ISI/TABEL/GAMBAR` masing-masing halaman baru (`page_break_before=True` + buffer anti-merge).
- **G3 — TOC/LOT/LOF native:** `TOC 1 Pt11 bold Cm0`, `TOC 2/3` sesuai builder, `_add_dot_tab_7938` (`pos 7938 dot right`), `right_indent 0`, formula `13.8-LeftIndent` (L1 13.8/14.0, L2 13.2, L3 12.6). `DAFTAR ISI` + `DAFTAR TABEL` (5 entri) + `DAFTAR GAMBAR` (5 entri) + `BAB 1/2/3` + subbab masuk TOC. Judul tak bernomor tapi `addcontentsline`.
- **G4 — Headings:** `Heading 1 center bold 12pt KAPITAL arab (BAB 1/2/3 + PENDAHULUAN...) after12`, `Heading 2 left bold 12pt Title Case before12 after6`, `Heading 3 left bold 12pt before6/10 after3/4`, asing italic di dalam, `outlineLevel` untuk Nav/Docs Tabs. Larang `BAB I/II/III` romawi di isi.
- **G5 — Body:** `Normal TNR12 justify 1.5 first Cm(1.25) space 0/0 pure black`, `nested parsing *** ** *` → runs, larang `* $ \cite` bocor, inline math Unicode (`X₁ X₂ X₃ Y M R² ΔR² p α n β`).
- **G6 — Block quote (>3 baris):** turunan `Normal left Cm(1.25) first 0 ls 1.0 justify TNR12` + `space 6/6`, tanpa kutip. (Proposed murni — belum ada contoh Verified, jangan di-skip.)
- **G7 — Tabel APA:** `apply_apa7_table_borders()` (`top/bottom single sz8=1pt`, header `bottom sz6=0.75pt`, tanpa vertikal, `F2F2F2` header, `tblHeader cantSplit center fixed`), caption `11pt bold` di atas (`Tabel X.X: ...` + asing italic), sumber `10pt italic` di bawah, `LOT` sinkron, `14.0cm` lebar.
- **G8 — Gambar:** `center`, `Cm(13.5)` umum / `Cm(14.0)` rerangka / `Cm(13.0)` alur, `300 DPI`, caption `11pt bold center` di bawah, sumber `10pt italic center` di bawah caption, `LOF` sinkron. Wajib ada `Gambar 2.1 Rerangka` + `Gambar 3.1 Alur` (bus sentral/elips).
- **G9 — Persamaan:** `pandoc -f latex -t docx` → `m:oMathPara` native, display `1.5` + nomor kanan `(3.x)` (`\numberwithin{equation}{section}`), inline Unicode italic+subscript. Larang plain `Y = b0... (3.1)` ketik manual.
- **G10 — Bahasa & sitasi:** asing selalu italic, sitasi narasi `dan` / parentetik `&` / `et al.` + `;`, bib `and` (Inggris) konsisten, `Babin et al., 1994` style. Larang `&` + `dan` campur dalam satu naskah.
- **G11 — Footer/header + warna + Docs-safe:** footer `TNR 10pt bold 000000` `Universitas Kristen Krida Wacana | <PAGE>` + `Accent Bar 4` kanan-bawah + `PAGE` field (`rFonts TNR + 000000`) + fallback teks Docs, `make_run_pure_black` semua runs, hyperlink `000000` tanpa underline biru, `outlineLevel` + `pageBreakBefore` + buffer (lihat directive §5).
- **G12 — Pustaka:** `Heading 1 DAFTAR PUSTAKA` tak bernomor, entri `left Cm(1.25) first Cm(-1.25) justify 1.15` tanpa nomor alfabetis, buku/jurnal italic, URL `Tersedia di: https://...` plain hitam, hapus meta/legenda/`> Status:`/`Verified-vs-Proposed` dari body. Sumber hanya `references.bib`/`.bbl` formal.

---

## 3. Gap list draf kita (apa yang bikin jelek)

> Semua poin di bawah Verified via `python-docx` (bukan opini). Perbaiki berurutan G1→G12.

1. **TOC manual (G3):** `1 field TOC \o "1-3"` + puluhan `Normal —` placeholder + catatan `Ctrl+A F9` bocor (p18/p48). Arthur: `56 TOC1/2/3` + dots `7927` + `TOC 11` LOT/LOF. Dampak: nomor tidak update, dots tidak presisi, gagal Nav/Docs Tabs.
2. **Tabel 3-kolom ringkas + `TableGrid` (G7):** `3 tabel TableGrid` bergrid vertikal, caption bukan `Tabel X.X:` (`Tabel berikut merangkum 18 studi... center`), tanpa `Sumber:` di bawah, tanpa LOT. Arthur: `5 tabel APA open sz8/sz6 F2F2F2` + caption `11pt bold` + sumber italic.
3. **Tanpa LOT/LOF (G3/G7/G8):** tidak ada `Heading DAFTAR TABEL/GAMBAR`, tidak ada `TOC 11` entri, tidak ada `Tabel X.X`/`Gambar X.X` body. Arthur: `DAFTAR TABEL/GAMBAR Heading 1` + `5+5 TOC 11`.
4. **Tanpa romawi/arab split (G2):** `sections=1`, `pgNumType NOT FOUND`, tanpa footer/header. Arthur: `3 sections lowerRoman→decimal + footer | i / | 1`.
5. **Tanpa header/footer (G11):** draf `0 footer paras`; Arthur `Footer 10pt + PAGE field + UKRIDA`. Juga `header/footer dist 850` vs `720` (template salah).
6. **Tanpa gambar rerangka (G8):** `0 shapes/images`; `2.4 Rerangka` teks saja. Arthur `6 images 13.5/14.0/13.0cm` + `Gambar 2.1/3.1` + LOF.
7. **Persamaan plain (G9):** `2 plain (3.1)(3.2) hasOMML=False` (`Y = b0...`, `Y = p1...` tanpa italic/subscript). Arthur `7 OMML` + Unicode `X₁ M* β ΔR²`.
8. **Cover jelek (G1):** `12pt` (bukan 14pt), `1.5` rata (bukan stage `6/18/12/24/36/48`), tanpa logo (`0 shapes`), `NIM : [OPEN]`, kalimat `Disusun untuk...` tambahan, prodi ganda tidak KAPITAL.
9. **Body tanpa indent (G5):** `first=None` di body (p13/p18/p48) vs `1.250597cm` Arthur. Ditambah `H1 BAB I (romawi)` vs `BAB 1 (arab)`, `H2 Daftar OPEN...` bocor.
10. **Sitasi campur (G10):** `&` + `dan` + `et al.` campur (`& Mangold` vs `dan Bala`), all-caps `INFLUENCER MARKETING` vs italic kalimat. Arthur konsisten `and` di bib + `et al.;` in-text.
11. **Pustaka bocor + hanging salah (G12):** p216 meta `Disalin setia dari DAFTAR_PUSTAKA_SEMENTARA.md §2... > Status:...` masuk naskah; `hanging 1.27/-1.27` (bukan `1.250597`), `ls 1.5` (bukan `1.15`/single), `DAFTAR PUSTAKA Normal` (bukan Heading). Arthur `1.250597/-1.250597 justify` tanpa nomor/meta.
12. **Dots & style hilang (G3/G11):** `TOC 1/2/3 styles missing` di draf, `Footer/Header styles missing/size None`; Arthur `Footer 10pt` + `Heading1 center bold` + `TOC dots`. Ditambah `Accent Bar 4` belum ada di kedua file — wajib Proposed di builder v2 (jangan klaim sudah ada).

**Prioritas eksekusi builder v2:** G2 (section) → G3 (TOC/LOT/LOF 7938) → G1 (cover+logo+NIM) → G11 (footer 10pt+Accent+PAGE) → G4/G5 (headings/body indent) → G7/G8 (tabel/gambar) → G9 (OMML) → G10/G12 (sitasi/pustaka hitam) → G6 (quote) → verifikator.

---

## Lampiran — perintah ukur ulang (repro)

```powershell
Get-ChildItem -LiteralPath "Z:\SKRIPSII\SKRIPSI ARTHUR\SKRIPSI-arthur-main\SKRIPSI-arthur-main\01_Naskah_Utama" | Format-Table Name, Length -AutoSize
Get-ChildItem -LiteralPath "Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\01_Naskah_Utama" | Format-Table Name, Length -AutoSize
py "C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\measure_anatomi.py"
py "C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\measure2.py"
py "C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\measure3.py"
py "C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\measure4.py"
py "C:\Users\Arthur Reezan\AppData\Local\Temp\opencode\measure5.py"
Get-Content -LiteralPath "Z:\SKRIPSII\SKRIPSI ARTHUR\SKRIPSI-arthur-main\SKRIPSI-arthur-main\execution\build_proposal_word.py" | Select-String -Pattern "7938|Accent|pure black|OMML" -CaseSensitive:$false
```

> Jangan tulis file lain. Jangan commit/push. Builder v2 hanya boleh membaca sumber di atas + `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` bila perlu, tanpa mengubahnya.
