# README_PEDOMAN — 05_Pedoman_&_Referensi (skripsi siddharta)

Tanggal: 01-Okt-2026 (perintah user)
Sumber read-only: `Z:\SKRIPSII\SKRIPSI ARTHUR\SKRIPSI-arthur-main\SKRIPSI-arthur-main\05_Pedoman_&_Referensi\`
Tujuan: `Z:\SKRIPSII\SKRIPSI ARTHUR\skripsi siddharta\05_Pedoman_&_Referensi\`
Metode: `Get-ChildItem` + `Copy-Item` + `Test-Path`. Tanpa karang URL/DOI/angka.

## 1. Daftar file VERIFIED copy (bytes via Get-ChildItem, identik sumber↔tujuan)

| File tujuan | Bytes | Status |
|---|---:|---|
| Buku Pedoman Penyusunan Tugas Akhir 2023.pdf | 481009 | VERIFIED copy |
| Buku Pedoman Penyusunan Tugas Akhir 2023.md | 60205 | VERIFIED copy |
| Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.pdf | 577799 | VERIFIED copy (pembanding) |
| Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md | 59133 | VERIFIED copy (pembanding) |
| TUGAS AKHIR (Revisii).pdf | 1558989 | VERIFIED copy (contoh kakak tingkat) |
| TUGAS AKHIR (Revisii).md | 138543 | VERIFIED copy (contoh kakak tingkat) |
| lampiran_2_preview.png | 58097 | VERIFIED copy |
| README_PEDOMAN.md (file ini) | — | NEW |
| README_PLACEHOLDER.md (lama, tidak dihapus) | 184 | PRE-EXISTING |

Total sumber (8 file, termasuk PRD yang tidak dicopy): 2947987 bytes (via Measure-Object Sum).

Verifikasi:
- `Test-Path` tiap 7 file tujuan = True (lihat §4).
- Bytes tujuan identik dengan sumber (tabel di atas = hasil `Get-ChildItem` kedua sisi).
- Tidak ada file `.env` / `*token*` di sumber (hasil `Get-ChildItem -Filter` kosong) → tidak ada yang perlu dikecualikan.
- File sumber `PRD_AI_Dosen_Pembimbing_Skripsi_v2.md` (14212 bytes) ada di sumber tetapi TIDAK dicopy (di luar ruang lingkup minimal perintah).

## 2. Cara pakai (diringkas dari Buku Pedoman 2023.md — sudah Read, bukan tebakan)

Acuan utama: `Buku Pedoman Penyusunan Tugas Akhir 2023.pdf/.md`.
Pengesahan: SK Dekan FEB UKRIDA No. 350a/SK/UKKW/FEB/D/VI/2023, wajib bagi sivitas FEB UKRIDA.

Format naskah (Bab 3 pedoman, baris ±414–430):
- Margin: kiri 4 cm (termasuk 1 cm penjilidan), kanan 3 cm, atas 3 cm, bawah 3 cm.
- Font: Times New Roman 12, justify (rata kiri-kanan). Kata asing miring.
- Spasi: 1,5 untuk seluruh naskah. Kutipan langsung > 3 baris: alinea baru, diawali/diakhiri 2 tanda kutip, 1 spasi, indentasi 5 ketukan ke kanan dan kiri.
- Sampul hardcover: huruf tinta kuning emas, spasi 1,5, center, tanpa singkatan (kecuali PT/UD/CV/PSAK/UU), tanpa kalimat tanya. Logo UKRIDA 5 cm x 5 cm warna emas.
- Nomor halaman: awal = tengah tepi bawah; isi = kanan bawah dengan label Universitas Kristen Krida Wacana (TNR 10 bold).

Sitasi / referensi (Bab 1 + Bab 3):
- Wajib mensitasi karya ilmiah dosen FEB UKRIDA sesuai topik.
- Khusus Tugas Akhir Skripsi: minimal 5 artikel jurnal terindeks Sinta dan/atau jurnal internasional.
- Tinjauan pustaka: minimal 20 acuan (jurnal, tesis, disertasi doktoral 5 tahun terakhir, textbook edisi terbaru yang relevan).
- Skripsi mahasiswa TIDAK boleh dijadikan referensi.
- Kutipan tanpa catatan kaki; memakai endnotes nama + tahun (contoh pola: Kwik (2010), Harsono (2011)).
- Daftar Pustaka: minimal 20 referensi, abjad nama pengarang tanpa nomor urut, tanpa tanda baca akhir, baris kedua indent 5 spasi dari margin kiri, spasi 1,5. Dianjurkan terbitan 5 tahun terakhir (kecuali teori konvensional). Kutipan dari Tugas Akhir/diktat/fotokopi/catatan kuliah dilarang masuk Daftar Pustaka.
- Minimal 50 halaman (BAB 1–BAB 5). Jangka waktu penyusunan maksimal 2 semester sejak pendaftaran.

Lampiran pedoman (untuk template halaman): lampiran 1 (judul proposal), 2 (persetujuan proposal), 3 (sampul/judul hardcover), 4 (orisinalitas), 5 (persetujuan pembimbing), 6 (pengesahan penguji), 7 (persetujuan publikasi), 8–9 (abstrak ID/EN), 10 (anatomi TA). File `lampiran_2_preview.png` = pratinjau lampiran 2.

Pembanding: `Buku Pedoman 2022` dipakai hanya bila 2023 tidak mengatur hal detail; bila konflik, 2023 menang (SK 2023).

## 3. Jurnal kakak tingkat — VERIFIED vs OPEN

- VERIFIED (contoh kakak tingkat, bukan jurnal standalone):
  - `TUGAS AKHIR (Revisii).pdf` (1558989 bytes) / `.md` (138543 bytes)
  - Isi terverifikasi via Read head: "PENGARUH KUALITAS PRODUK DAN KEPERCAYAAN MEREK TERHADAP LOYALITAS PELANGGAN GLAD2GLOW DI JAKARTA BARAT DENGAN KEPUASAN PELANGGAN SEBAGAI VARIABEL MEDIASI", diajukan oleh JEDDY (312022015), Fakultas Ekonomi dan Bisnis UKRIDA, Jakarta 2026.
  - Fungsi: contoh struktur BAB 1–5 + sitasi, agar serapih Arthur.
- OPEN (belum ada file jurnal standalone kakak tingkat di sumber maupun tujuan):
  - Pencarian `Get-ChildItem` sumber hanya menemukan 8 file di atas; tidak ada file `*jurnal*.pdf/md`.
  - Tindak lanjut: bila ada PDF jurnal kakak tingkat, taruh di folder ini dan catat bytes + status VERIFIED di tabel §1.

## 4. Checklist Test-Path tujuan (VERIFIED)

- [x] `Buku Pedoman Penyusunan Tugas Akhir 2023.pdf` = True
- [x] `Buku Pedoman Penyusunan Tugas Akhir 2023.md` = True
- [x] `Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.pdf` = True
- [x] `Buku Pedoman Penyusunan Skripsi FEB Ukrida 2022.md` = True
- [x] `TUGAS AKHIR (Revisii).pdf` = True
- [x] `TUGAS AKHIR (Revisii).md` = True
- [x] `lampiran_2_preview.png` = True

## 5. Kode K-01..K-07 — OPEN (tidak dikarang)

- Hasil `rg -n "K-0"` pada `Buku Pedoman 2023.md` dan `Buku Pedoman 2022.md` = kosong (tidak ditemukan).
- Maka daftar K-01..K-07 diperlakukan sebagai OPEN / menunggu definisi dari pemilik topik; tidak diisi tebakan di file ini.
- Bila K-01..K-07 merujuk pada daftar lampiran 1–10 di atas, petakan eksplisit dulu sebelum diklaim VERIFIED.

---
DILARANG commit/push dari tugas ini. Klaim bytes/status di atas berasal dari `Get-ChildItem`/`Test-Path`/`Read`, bukan tebakan. Tidak ada URL/DOI yang dikarang.
