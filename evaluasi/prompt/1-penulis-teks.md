# Prompt penulis teks asli

Dipakai sekali untuk membuat [`asli/`](../asli/). Model: Claude Opus 5.5, sesi terpisah tanpa konteks uji. Teks yang sama dipakai di semua putaran.

```text
Kamu adalah asisten AI biasa. Jawab 10 permintaan pengguna di bawah ini, masing-masing seperti kamu menjawab di aplikasi chat pada umumnya. Tulis dalam Bahasa Indonesia. Panjang tiap jawaban 80 sampai 200 kata. Jangan menambahkan komentar tentang tulisanmu sendiri.

Simpan tiap jawaban (hanya teks jawabannya, tanpa permintaan) ke berkas terpisah dengan Write tool:
/Users/reysonic/Desain/Skill/lugas/evaluasi/asli/01.md sampai 10.md

Permintaan:
01. "Tolong buatkan rilis pers singkat: startup kami, Kirimin, meluncurkan layanan kirim paket same-day di Surabaya mulai 1 November, tarif mulai Rp9.000, sudah ada 120 kurir."
02. "Bikinin caption Instagram buat kafe aku yang baru buka di Jogja, namanya Kopi Senja, ada promo beli 1 gratis 1 sampai Minggu."
03. "Tulis paragraf pembuka artikel blog tentang kenapa UMKM perlu mulai pakai QRIS."
04. "Buatkan email formal ke dosen pembimbing untuk minta jadwal bimbingan skripsi minggu depan, saya Rina, NIM 2021045, bab 3 sudah selesai."
05. "Tulis bagian 'Instalasi' di README untuk CLI bernama tarik, dipasang lewat npm, butuh Node 20 ke atas, lalu jalankan tarik init."
06. "Bikin thread X gaya anak Jaksel soal tips biar nggak boros pas gajian, 4 poin aja."
07. "Tulis deskripsi produk Tokopedia untuk tumbler stainless 500 ml, tahan panas 12 jam, tahan dingin 24 jam, ada 4 warna."
08. "Buat pengumuman resmi dari BEM kampus: pendaftaran panitia ospek dibuka 4-10 November lewat formulir online, terbuka untuk angkatan 2023 dan 2024."
09. "Ringkas hasil rapat ini jadi satu paragraf: tim sepakat rilis aplikasi diundur ke 15 Desember karena bug pembayaran, Dika perbaiki bug, Sari siapkan pengumuman ke pengguna."
10. "Buatkan paragraf pembuka surat lamaran kerja untuk posisi desainer grafis di agensi kreatif, saya lulusan DKV dengan pengalaman 2 tahun freelance."

Setelah selesai, laporkan hanya daftar berkas yang dibuat.
```
