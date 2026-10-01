# SEARCH_LOG — Fase 1 Master Directive (Fenomena Riil)

> Topik: Pengaruh Influencer Marketing, eWOM, Perceived Enjoyment terhadap Intention To Play Mobile Legends pada Gen Z Indonesia nasional, kuantitatif kuesioner, belum ada data awal.
> Prinsip: kumpulkan KANDIDAT sumber resmi, BUKAN angka hafalan. Setiap angka = [ANGKA MENUNGGU VERIFIKASI FETCH] kecuali sudah fetch isi penuh dan dikutip dengan halaman/definisi.
> Aturan tulis: hanya 2 file IN-SCOPE yang boleh ditulis pada fase ini. File ini + VERIFIED_EMPIRICAL_DATA.md. DILARANG sentuh SoT/Dashboard/Log/struktur lain. DILARANG commit/push.
> Aturan URL: setiap URL di bawah adalah hasil WebSearch/WebFetch pada 2026-10-01, atau ditandai UNVERIFIED / BELUM DIAKSES. Tidak ada URL karangan.
> Tanggal akses seragam: 2026-10-01 (UTC).

## 1. Metode pencarian

- Alat: WebSearch (2026) + WebFetch verifikasi HTTP.
- Status verifikasi yang dipakai:
  - `FETCH OK 200` = WebFetch berhasil mengembalikan isi (terverifikasi ada/respons 200 pada 2026-10-01).
  - `BELUM DIAKSES` = URL dari hasil WebSearch tetapi WebFetch belum berhasil / belum dilakukan fetch isi penuh.
  - `FETCH GAGAL (kode)` = WebFetch dicoba tetapi non-200 / transport error; diperlakukan sebagai BELUM DIAKSES.
  - `UNVERIFIED (sekunder)` = media sekunder/agregator; tidak boleh jadi bukti fenomena tanpa dokumen primer.
- Kebijakan angka: JANGAN kutip angka statistik di file ini. Tulis `[ANGKA MENUNGGU VERIFIKASI FETCH]` dan jelaskan langkah fetch berikutnya + definisi metrik yang harus dicek.

## 2. Log query WebSearch (2026-10-01)

| # | Query | Hasil relevan (URL) |
|---|-------|---------------------|
| Q1 | Newzoo Global Games Market Report 2026 Indonesia mobile gaming | https://newzoo.com/reports/newzoo-s-global-games-market-report-2026 ; https://newzoo.com/articles/2026-global-games-market-key-numbers |
| Q2 | DataReportal Digital 2026 Indonesia internet mobile gaming | https://datareportal.com/reports/digital-2026-indonesia ; https://datareportal.com/digital-in-indonesia |
| Q3 | APJII survei penetrasi internet Indonesia 2024 2025 resmi | https://survei.apjii.or.id/home (uji fetch → 404) ; https://survei.apjii.or.id/ ; https://apjii.or.id/download_survei/1b5d0968-ccc7-4f21-bed5-ac9962cb17f1 ; https://www.cnnindonesia.com/teknologi/20260521122201-213-1360738/survei-pengguna-internet-indonesia-tumbuh-6-juta-di-2026 ; https://inet.detik.com/telecommunication/d-8047759/survei-apjii-pengguna-internet-indonesia-2025-tembus-229-juta-jiwa |
| Q4 | BPS Indonesia statistik generasi Z Gen Z demografi 2025 | https://www.bps.go.id/id/publication/2026/06/30/bdc814f38edf0a941f4f9d34/penduduk-dan-indikator-kependudukan-hasil-survei-penduduk-antar-sensus-2025.html ; https://www.bps.go.id/id/publication/2025/01/31/29a40174e02f20a7a31b5bc3/statistik-demografi-indonesia--hasil-sensus-penduduk-2020-.html |
| Q5 | kanal resmi Moonton / Mobile Legends Bang Bang | https://www.mobilelegends.com/en ; https://en.moonton.com/about/index.html |
| Q6 | MPL Indonesia official viewership 2025 2026 | https://id-mpl.com/ ; https://id-mpl.com/en/mpljourney ; https://en.moonton.com/news/318.html ; https://escharts.com/tournaments/mobile-legends/mpl-indonesia-season-17 ; https://esportsinsider.com/2025/06/mpl-indonesia-records-4m-peak-viewership-season-15 ; https://esportsinsider.com/2025/11/onic-win-mpl-indonesia-season-16 |
| Q7 | Mobile Legends Google Play / App Store listing resmi | https://play.google.com/store/apps/details?gl=UK&hl=en&id=com.mobile.legends ; https://apps.apple.com/ge/app/mobile-legends-bang-bang/id1160056295 |
| Q8 | Sensor Tower Indonesia mobile games downloads 2025 MLBB | https://sensortower.com/blog/southeast-asia-mobile-gaming-2025 ; https://app.sensortower.com/overview/com.mobile.legends?country=id |
| Q9 | MPL Indonesia official site id-mpl.com | https://id-mpl.com/ ; https://id-mpl.com/en/mpljourney ; https://id-mpl.com/teams |

## 3. Kandidat sumber resmi (metadata tanpa angka)

### 3a. Laporan industri game

**S1 — Newzoo Global Games Market Report 2026 (Free Edition)**
- Penerbit: Newzoo. Tahun/edisi: 2026 (rilis free edition 2026).
- Metrik yang diklaim tersedia: prospek pasar game global, forecast pemain & pendapatan per platform (PC/konsol/mobile), data region/country 100 pasar (pada edisi full/berbayar).
- URL: https://newzoo.com/reports/newzoo-s-global-games-market-report-2026
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: cakupan GLOBAL (bukan Indonesia-spesifik pada free preview); angka Indonesia hanya ada pada full subscription country-level; definisi revenue/player mengikuti model Newzoo (estimasi + consumer research + laporan perusahaan publik); bukan sensus.
- Langkah fetch berikut: unduh free 33-halaman via form, catat halaman definisi metodologi; untuk klaim Indonesia butuh akses full country-level atau kutip explisit sebagai tidak tersedia di free edition.

**S2 — Newzoo 2026 Global Games Market Key Numbers (artikel ringkasan)**
- Penerbit: Newzoo. Tahun: 2026-08-25.
- Metrik yang diklaim tersedia: ringkasan forecast revenue & pemain global per platform.
- URL: https://newzoo.com/articles/2026-global-games-market-key-numbers
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: GLOBAL, bukan bukti fenomena Indonesia; hanya ringkasan artikel, metodologi penuh ada di laporan. Nilai = [ANGKA MENUNGGU VERIFIKASI FETCH] bila kelak dikutip — wajib sertakan tanggal artikel + catatan forecast vs realisasi.
- Langkah berikut: tidak dipakai sebagai bukti fenomena nasional; hanya konteks global bila perlu.

**S3 — Sensor Tower Southeast Asia Mobile Game Market Insights 2025**
- Penerbit: Sensor Tower (Donny Kristianto). Tahun: Mei 2025 (data Q1 2025).
- Metrik yang diklaim tersedia: estimasi download & IAP revenue SEA per negara, sorotan Indonesia sebagai pemimpin download, studi hyper-localization MLBB.
- URL: https://sensortower.com/blog/southeast-asia-mobile-gaming-2025
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: cakupan SEA kuartalan (Q1 2025), berbasis estimasi App Store + Google Play (eksklusi pre-install, re-download, third-party Android); definisi download ≠ pemain unik/MAU; angka Indonesia Q1 = [ANGKA MENUNGGU VERIFIKASI FETCH] — baca dari laporan penuh via tombol VIEW THE REPORT.
- Langkah berikut: akses laporan penuh gratis, catat footnotes definisi; bedakan estimasi Sensor Tower (pihak ketiga independen) vs klaim Moonton.

**S4 — Sensor Tower App Overview MLBB (dashboard)**
- Penerbit: Sensor Tower. Edisi: berjalan (dashboard).
- Metrik yang diklaim tersedia: peringkat Top Free/Grossing MLBB di Indonesia, estimasi download & revenue bulanan.
- URL: https://app.sensortower.com/overview/com.mobile.legends?country=id
- Status: BELUM DIAKSES (URL dari WebSearch; dashboard enterprise, butuh login; belum WebFetch isi).
- Keterbatasan: estimasi pihak ketiga, metodologi tertutup sebagian, butuh verifikasi definisi country=rank/chart.
- Langkah berikut: coba akses via browser terautentikasi / minta demo; jika gagal, jangan kutip angka; gunakan hanya sebagai petunjuk arah, bukan bukti.

### 3b. Kanal resmi Moonton / MLBB + MPL Indonesia

**S5 — MOONTON About Us (profil resmi perusahaan)**
- Penerbit: MOONTON Games. Tahun: halaman berjalan (memuat journey s.d. 2026).
- Metrik yang diklaim tersedia: profil instalasi kumulatif & MAU global MLBB, histori milestone (M-series, MPL, SEA Games, Asian Games), klaim peringkat top-played per negara.
- URL: https://en.moonton.com/about/index.html
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: klaim PENYELENGGARA (self-reported, global, bukan Indonesia-spesifik); definisi instalasi vs MAU vs registered accounts tidak dirinci di halaman; nilai = [ANGKA MENUNGGU VERIFIKASI FETCH] bila kelak dikutip — wajib label "klaim Moonton".
- Langkah berikut: arsipkan tanggal akses + screenshot; cari dokumen pendukung independen (store intelligence / esports charts) untuk triangulasi; jangan pakai klaim global sebagai proksi Gen Z Indonesia.

**S6 — Mobile Legends: Bang Bang Official Website**
- Penerbit: Moonton. Edisi: berjalan.
- Metrik yang diklaim tersedia: TIDAK ada metrik populasi/download di halaman depan; hanya konten hero/patch/berita + tautan kebijakan & kontak resmi.
- URL: https://www.mobilelegends.com/en
- Status: FETCH OK 200 pada 2026-10-01 (konten JS-heavy, teks minimal).
- Keterbatasan: bukan sumber angka; hanya bukti kanal resmi + kontak resmi (mobilelegendsgame@moonton.com).
- Langkah berikut: telusuri sub-halaman news dengan ID berita spesifik bila butuh pengumuman resmi; catat newsid + tanggal.

**S7 — MPL Indonesia Official Site (id-mpl.com)**
- Penerbit: MOONTON (MPL Indonesia). Edisi: Season 18 berjalan (jadwal s.d. Okt 2026 terlihat saat fetch).
- Metrik yang diklaim tersedia: jadwal, tim, tiket, statistik, berita liga (struktur kompetisi, bukan angka populasi game).
- URL: https://id-mpl.com/
- Status: FETCH OK 200 pada 2026-10-01 (isi terpotong karena JS, tetapi jadwal terbaca).
- Keterbatasan: klaim penyelenggara; angka viewership TIDAK ada di homepage — butuh sub-halaman Statistics / News atau sumber Esports Charts.
- Langkah berikut: fetch https://id-mpl.com/en/mpljourney dan sub-halaman Statistics; catat definisi viewership bila ada; jika tidak ada, rujuk ke pihak ketiga independen dengan label jelas.

**S8 — MOONTON News: MPL Indonesia Season 17 begins (siaran resmi)**
- Penerbit: MOONTON Games. Tanggal: 2026-03-25 (dari cuplikan search).
- Metrik yang diklaim tersedia: narasi liga (9 tim, periode regular season, positioning pasca-M7) — bukan angka populasi.
- URL: https://en.moonton.com/news/318.html
- Status: BELUM DIAKSES (hanya cuplikan WebSearch; belum WebFetch isi penuh).
- Keterbatasan: siaran pers penyelenggara; nilai viewership M7 di artikel = [ANGKA MENUNGGU VERIFIKASI FETCH].
- Langkah berikut: WebFetch URL di atas, arsipkan tanggal + kutipan definisi M7/PCV bila ada.

**S9 — Esports Charts: MPL Indonesia Season 17 (pihak ketiga independen)**
- Penerbit: Esports Charts. Edisi: Season 17.
- Metrik yang diklaim tersedia: peak viewers, average viewers, hours watched, jadwal/hasil.
- URL: https://escharts.com/tournaments/mobile-legends/mpl-indonesia-season-17
- Status: FETCH GAGAL 403 pada 2026-10-01 → diperlakukan BELUM DIAKSES.
- Keterbatasan: metodologi tracking streaming pihak ketiga (sampel platform ter-track, definisi PCV/avg); angka = [ANGKA MENUNGGU VERIFIKASI FETCH].
- Langkah berikut: ulang fetch via browser / gunakan halaman schedule yang tidak diblokir; catat definisi metrik Charts; jangan campur dengan klaim Moonton.

**S10 — Esports Insider: MPL Indonesia Season 15 records peak viewers (media esports, mengutip Esports Charts)**
- Penerbit: Esports Insider (mengutip Esports Charts). Tahun: 2025-06.
- Metrik yang diklaim tersedia: peak viewers grand final, average viewers, hours watched, platform breakdown (YouTube/TikTok Live).
- URL: https://esportsinsider.com/2025/06/mpl-indonesia-records-4m-peak-viewership-season-15
- Status: FETCH GAGAL (transport error) pada 2026-10-01 → BELUM DIAKSES.
- Keterbatasan: media sekunder yang mengutip pihak ketiga; angka = [ANGKA MENUNGGU VERIFIKASI FETCH]; butuh verifikasi silang ke halaman Esports Charts asli.
- Langkah berikut: ulang WebFetch + cari URL Esports Charts turnamen S15 sebagai primer.

**S11 — Esports Insider: ONIC win MPL Indonesia Season 16 (media esports)**
- Penerbit: Esports Insider. Tahun: 2025-11 (dari search).
- Metrik yang diklaim tersedia: peak/average/hours watched S16, prize pool, narasi juara.
- URL: https://esportsinsider.com/2025/11/onic-win-mpl-indonesia-season-16
- Status: BELUM DIAKSES (hanya hasil WebSearch; belum WebFetch).
- Keterbatasan: sama dengan S10; angka = [ANGKA MENUNGGU VERIFIKASI FETCH].
- Langkah berikut: WebFetch + silang ke Esports Charts S16.

### 3c. Listing toko aplikasi resmi MLBB

**S12 — Google Play: Mobile Legends: Bang Bang (com.mobile.legends)**
- Penerbit: listing resmi MOONTON (developer: YoungJoy Technology Limited) di Google Play.
- Metrik yang diklaim tersedia: tier download (bukan angka presisi), rating & jumlah ulasan, update terakhir, kategori, kontak developer.
- URL: https://play.google.com/store/apps/details?gl=UK&hl=en&id=com.mobile.legends
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: cakupan GLOBAL (bukan Indonesia-spesifik); tier download = bucket, bukan sensus pemain; rating fluktuatif; nilai = [ANGKA MENUNGGU VERIFIKASI FETCH] bila kelak dikutip — wajib sertakan region store (gl=UK) + tanggal akses.
- Langkah berikut: buka dengan gl=ID untuk konteks Indonesia (tetap bukan angka nasional); arsipkan tanggal + tier yang tampil.

**S13 — App Store: Mobile Legends: Bang Bang (id1160056295)**
- Penerbit: listing resmi MOONTON di Apple App Store.
- Metrik yang diklaim tersedia: rating, chart kategori, ukuran, bahasa, versi/what's new, privacy.
- URL: https://apps.apple.com/ge/app/mobile-legends-bang-bang/id1160056295
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: cakupan per storefront (contoh GE), bukan Indonesia; tidak ada angka download publik; bukan bukti populasi.
- Langkah berikut: buka storefront ID bila perlu; hanya untuk bukti eksistensi resmi + klasifikasi usia 13+.

### 3d. Demografi & penetrasi internet Indonesia

**S14 — DataReportal Digital 2026: Indonesia**
- Penerbit: DataReportal / Kepios (Simon Kemp), bermitra Meltwater & We Are Social. Edisi: Digital 2026 (data Okt 2025, rilis Nov 2025).
- Metrik yang diklaim tersedia: populasi (UN), koneksi seluler (GSMA Intelligence), pengguna internet (Kepios), user media sosial & ad-reach per platform (Google/Meta/TikTok/dll), kecepatan koneksi (Ookla).
- URL: https://datareportal.com/reports/digital-2026-indonesia
- Status: FETCH OK 200 pada 2026-10-01 (fetch penuh berhasil).
- Keterbatasan: agregator multi-sumber (bukan sensus tunggal); definisi berbeda per metrik (internet users vs ad reach vs connections); periode acuan Okt 2025 untuk laporan 2026; revisi/koreksi platform dapat mengubah tren; nilai = [ANGKA MENUNGGU VERIFIKASI FETCH] — baca dari halaman + catat sumber primer tiap baris (UN/GSMA/Kepios/Ookla) sebelum dikutip di skripsi.
- Langkah berikut: unduh slide deck penuh via embed; catat halaman + sumber primer tiap metrik; jangan hitung ulang tren antar edisi tanpa baca catatan metodologi.

**S15 — APJII Survei Profil Internet Indonesia 2026 (dilaporkan via CNN Indonesia)**
- Penerbit primer: APJII. Penerbit sekunder pelapor: CNN Indonesia. Tahun: survei 2026 (diumumkan 2026-05-19/21).
- Metrik yang diklaim tersedia: penetrasi & jumlah pengguna internet nasional, breakdown pulau/urban-rural/generasi (Gen Z/Milenial disebut tertinggi), perangkat utama smartphone, durasi akses, alasan belum terkoneksi, fixed broadband.
- URL sekunder terverifikasi: https://www.cnnindonesia.com/teknologi/20260521122201-213-1360738/survei-pengguna-internet-indonesia-tumbuh-6-juta-di-2026
- Status: FETCH OK 200 pada 2026-10-01 (isi artikel terbaca penuh).
- Keterbatasan: ARTIKEL SEKUNDER — dokumen primer APJII belum di-fetch; angka di artikel = [ANGKA MENUNGGU VERIFIKASI FETCH] sampai dokumen APJII dibaca; metodologi survei (sampling, n, populasi acuan) harus diambil dari laporan APJII, bukan dari artikel.
- Langkah berikut: dapatkan PDF/laporan resmi APJII 2026 via https://survei.apjii.or.id/ ; catat n responden, teknik sampling, definisi penetrasi & generasi.

**S16 — APJII Survei Profil Internet Indonesia 2025 (dilaporkan via detikInet)**
- Penerbit primer: APJII. Pelapor sekunder: detikInet. Tahun: survei 2025 (rilis 2025-08-06).
- Metrik yang diklaim tersedia: penetrasi & pengguna nasional, tren tahunan, breakdown pulau/gender/generasi (komposisi Gen Z/Milenial/Alpha/X), metode multistage random sampling dengan n responden.
- URL sekunder terverifikasi: https://inet.detik.com/telecommunication/d-8047759/survei-apjii-pengguna-internet-indonesia-2025-tembus-229-juta-jiwa
- Status: FETCH OK 200 pada 2026-10-01.
- Keterbatasan: sekunder; angka = [ANGKA MENUNGGU VERIFIKASI FETCH] sampai PDF primer dibaca.
- Langkah berikut: bandingkan definisi generasi APJII vs BPS (rentang tahun lahir); catat perbedaan sebelum dipakai untuk sampling Gen Z.

**S17 — Portal Survei APJII (sumber primer yang dituju)**
- Penerbit: APJII. Edisi: 2025/2026 berjalan.
- Metrik yang diklaim tersedia: unduhan laporan survei penetrasi & perilaku, segmentasi pasar ISP.
- URL: https://survei.apjii.or.id/ (varian /home diuji → 404, jangan dipakai)
- Status: BELUM DIAKSES (daftar dari WebSearch; fetch /home gagal 404; root belum fetch isi penuh).
- Keterbatasan: struktur situs berubah; butuh navigasi manual.
- Langkah berikut: WebFetch root + sub-halaman /survei/group/11 ; unduh PDF resmi; catat nomor publikasi/tanggal rilis/metodologi.

**S18 — PDF Survei APJII (tautan unduhan dari hasil search)**
- Penerbit: APJII (diduga).
- URL: https://apjii.or.id/download_survei/1b5d0968-ccc7-4f21-bed5-ac9962cb17f1
- Status: BELUM DIAKSES (belum WebFetch; belum verifikasi isi/PDF).
- Keterbatasan: belum konfirmasi tahun/edisi/n responden dari dokumen.
- Langkah berikut: fetch + verifikasi header PDF (judul, tahun, n, metode); jika gagal, tandai UNVERIFIED dan jangan kutip.

**S19 — BPS SUPAS 2025: Penduduk dan Indikator Kependudukan**
- Penerbit: BPS. Rilis: 2026-06-30. Cakupan: 664.640 rumah tangga (dari abstraksi halaman).
- Metrik yang diklaim tersedia: indikator demografi (fertilitas, mortalitas, mobilitas, ageing) — BUKAN tabel proporsi generasi di halaman ini.
- URL: https://www.bps.go.id/id/publication/2026/06/30/bdc814f38edf0a941f4f9d34/penduduk-dan-indikator-kependudukan-hasil-survei-penduduk-antar-sensus-2025.html
- Status: FETCH OK 200 pada 2026-10-01 (abstraksi + metadata katalog terverifikasi).
- Keterbatasan: halaman ini abstraksi; komposisi Gen Z nasional TIDAK ada di halaman ini — butuh tabel publikasi / direktori SUPAS 2025 atau publikasi Sensus 2020; angka generasi = [ANGKA MENUNGGU VERIFIKASI FETCH].
- Langkah berikut: akses https://direktori.web.bps.go.id/supas2025 (tautan dari halaman) + unduh PDF publikasi (26.21 MB) via tombol Unduh; cari tabel generasi/kelompok umur.

**S20 — BPS Statistik Demografi Indonesia Hasil Sensus Penduduk 2020**
- Penerbit: BPS. Rilis: 2025-01-31 (dari search).
- Metrik yang diklaim tersedia: komposisi penduduk per generasi/umur berbasis Sensus 2020 (basis historis sebelum SUPAS 2025).
- URL: https://www.bps.go.id/id/publication/2025/01/31/29a40174e02f20a7a31b5bc3/statistik-demografi-indonesia--hasil-sensus-penduduk-2020-.html
- Status: BELUM DIAKSES (hanya hasil WebSearch; belum WebFetch isi).
- Keterbatasan: basis 2020 (kedaluwarsa untuk klaim 2026); definisi generasi BPS harus dicek (rentang tahun lahir) karena berbeda antar publikasi/sekunder.
- Langkah berikut: WebFetch + unduh PDF; catat definisi generasi resmi BPS; jadikan pembanding historis, bukan dasar klaim Gen Z 2026.

**S21 — Klaim proporsi Gen Z dari SUPAS 2025 via media sekunder (DITANDAI UNVERIFIED)**
- Pelapor: Towa News & GoodStats Data (mengaku mengutip rilis BPS 2026-05-05 / SUPAS 2025).
- URL sekunder (BUKAN bukti resmi): https://towa.co.id/postingan/gen-z-jadi-kelompok-penduduk-terbesar-di-indonesia-capai-2493-persen-dari-total-populasi ; https://data.goodstats.id/statistic/gen-z-dominasi-penduduk-indonesia-pada-2025-qxbOL
- Status: UNVERIFIED sebagai bukti fenomena (belum ada URL bps.go.id rilis pers 2026-05-05 yang terfetch).
- Keterbatasan: definisi Gen Z antar sekunder inkonsisten (rentang tahun lahir berbeda); angka = [ANGKA MENUNGGU VERIFIKASI FETCH] dan DILARANG dikutip sebagai fakta BPS sampai dokumen BPS dibaca.
- Langkah berikut: cari siaran pers resmi di https://www.bps.go.id/id (press release Mei 2026) + tabel direktori SUPAS; cocokkan definisi generasi; jika tidak ketemu, tetap UNVERIFIED.

## 4. Sumber yang DITOLAK sebagai bukti fenomena (blog opini/SEO tanpa metodologi)

- https://gitnux.org/indonesia-gaming-industry-statistics — agregator SEO tanpa metodologi primer transparan; angka campur tahun; TOLAK sebagai bukti. Boleh dicatat hanya sebagai petunjuk pencarian, bukan sitasi.
- https://digitalinasia.com/indonesia-gaming-market/ — analisis sekunder yang berguna sebagai peta bacaan tetapi mengutip silang (Sensor Tower/Niko/Xsolla) tanpa dataset primer; TOLAK sebagai bukti langsung. Lacak ke sumber primer tiap klaim.
- Mirror APK (apkpure/apkMirror) & gizmodo download page — bukan kanal resmi Moonton; TOLAK untuk klaim populasi/rating resmi.
- GoodStats/Towa/Databoks/Katadata ringkasan — sekunder; TOLAK sebagai pengganti publikasi BPS/APJII. Wajib lacak ke bps.go.id / apjii.or.id.

## 5. Langkah fetch berikutnya (prioritas)

1. Unduh PDF APJII 2025 & 2026 via https://survei.apjii.or.id/ ; catat n, sampling, definisi penetrasi & generasi.
2. Unduh PDF BPS SUPAS 2025 (tombol Unduh Publikasi di S19) + buka direktori SUPAS; cari tabel generasi/umur; verifikasi definisi Gen Z resmi.
3. Cari press release BPS Mei 2026 tentang SUPAS/generasi di bps.go.id; jika tidak ada, S21 tetap UNVERIFIED.
4. Ulangi fetch S9–S11 (Esports Charts + Esports Insider) via browser; catat definisi PCV/avg/hours watched.
5. Akses laporan penuh Sensor Tower (VIEW THE REPORT di S3) + Newzoo free report (form di S1); catat halaman metodologi.
6. Buka Google Play dengan gl=ID dan App Store storefront ID untuk konteks; tetap label global/bukan nasional.
7. Setiap angka yang kelak dikutip di skripsi wajib: nilai + satuan + tahun acuan data + penerbit + halaman/URL + definisi metrik + tanggal akses. Jika satu unsur hilang → tetap [ANGKA MENUNGGU VERIFIKASI FETCH].

## 6. Catatan kepatuhan

- File disentuh pada fase ini: hanya file ini dan VERIFIED_EMPIRICAL_DATA.md (disjoint).
- Tidak menyentuh SoT/Dashboard/Log/struktur lain. Tidak commit/push.
- Tidak ada URL/DOI/angka/statistik karangan di file ini; semua URL di atas dari WebSearch/WebFetch 2026-10-01 atau diberi label BELUM DIAKSES/UNVERIFIED.
