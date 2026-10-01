# Panduan 1-Menit: Impor Referensi Skripsi ke Mendeley Reference Manager
### *Khusus untuk Arthur Reezan — Memenuhi Arahan Pembimbing (Dr. Fredella Colline)*

> [!SUMMARY] Ringkasan Cepat & Target Mutlak
> - **Tujuan:** Memasukkan seluruh **tepat 54 referensi** proposal skripsi Pokémon TCG ke aplikasi **Mendeley Reference Manager** dalam 1 kali klik, dan mengambil tangkapan layar (*screenshot*) untuk ditunjukkan kepada Ibu Dr. Fredella Colline.
> - **Target Notifikasi Mendeley:** Toast hijau di kanan bawah wajib menampilkan: **"1 file uploaded, 54 references generated"**.
> - **Berkas yang Digunakan:** `06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris`.
> - **Waktu yang Dibutuhkan:** Kurang dari 1 menit.

---

## ⚠️ Langkah Pra-Syarat: Bersihkan Library Lama (Cegah Duplikat)
Jika sebelumnya Anda sudah pernah mengimpor file yang menampilkan 52, 55, 56, atau 71 referensi:
1. Klik pada daftar referensi di Mendeley, tekan tombol **`Ctrl + A`** pada keyboard untuk memilih semua.
2. Klik kanan lalu pilih **`Delete`** atau **`Move to Trash`**.
3. Pastikan daftar kepustakaan Anda bersih.

---

## Langkah 1: Impor Berkas RIS 54 Referensi (Sekali Klik)

### Opsi A (Melalui Menu — Sangat Direkomendasikan):
1. Klik tombol **`+ Add new`** berwarna biru di pojok kiri atas aplikasi Mendeley.
2. Arahkan kursor ke **`Import library`**.
3. Pilih **`RIS (*.ris)`**.
4. Cari dan pilih berkas:
   ```text
   06_Referensi_Jurnal_PDF/Mendeley_Library_Arthur_PokemonTCG.ris
   ```
5. Klik **`Open`**.

### Opsi B (Drag & Drop Langsung):
1. Buka folder `06_Referensi_Jurnal_PDF` di Windows Explorer.
2. Tarik (*drag*) berkas `Mendeley_Library_Arthur_PokemonTCG.ris` dan lepaskan (*drop*) langsung ke jendela aplikasi Mendeley Anda.

---

## Langkah 2: Verifikasi Notifikasi Hijau (Tepat 54 Referensi)
Perhatikan notifikasi *toast* hijau di pojok kanan bawah aplikasi Mendeley Anda:
> **"1 file uploaded, 54 references generated"**

Jika angka menunjukkan tepat **54**, maka paritas kepustakaan antara Mendeley dan Naskah Skripsi Arthur sudah **100% klop sempurna**!

---

## Langkah 3: Buat Koleksi Khusus (Opsional tapi Sangat Rapi)
1. Di panel sebelah kiri bawah **Collections**, klik **`+ New Collection`**.
2. Beri nama: **`Skripsi Arthur - Pokemon TCG`**.
3. Pilih seluruh referensi yang baru diimpor (`Ctrl + A`), lalu seret (*drag*) ke dalam koleksi tersebut.

---

## Langkah 4: Ambil Bukti Screenshot untuk Dosen
1. Klik koleksi **`Skripsi Arthur - Pokemon TCG`** sehingga terlihat daftar jurnal dan data industri (seperti *Aiken & West*, *Colline (2024)*, *The Pokémon Company (2024)*, *Statista (2024)*, *ICv2 (2024)*, *PSA (2024)*, dll.).
2. Tekan tombol **`Windows + Shift + S`** pada keyboard untuk mengambil *screenshot* rapi dari jendela Mendeley Anda.
3. Kirimkan tangkapan layar tersebut di WhatsApp saat mengirimkan naskah revisi ke Ibu Fredella Colline.

---

## 💡 Pengetahuan Tambahan (*Root Cause Lesson Learned*)
* **Mengapa dulu pernah muncul hanya 52 referensi?**
  Mendeley Reference Manager tidak mengenali tag `TY  - ELEC` (Electronic Web Citation) dan secara diam-diam melewatinya tanpa error. Akibatnya 4 data Pokémon tidak masuk ($40\text{ Jurnal} + 11\text{ Buku} + 1\text{ Konferensi} = 52$).
* **Bagaimana masalah tersebut dicegah selamanya?**
  Sistem naskah Arthur kini dilengkapi generator cerdas yang secara otomatis memetakan seluruh data industri ke tag resmi `TY  - RPRT` (*Report*), serta test suite otomatis `execution/verify_mendeley_integrity.py` yang memblokir tag tidak dikenal sebelum file dibagikan.
