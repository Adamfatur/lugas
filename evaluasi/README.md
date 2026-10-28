# Evaluasi

Folder ini mencatat uji kualitas Lugas. Setiap versi yang diuji punya foldernya sendiri. Hasil lama tidak diubah.

## Metode

1. **Teks asli.** Satu sesi Claude menjawab 10 permintaan sehari-hari dalam Bahasa Indonesia, seperti asisten AI pada umumnya: rilis pers, caption Instagram, pembuka artikel, email ke dosen, README, thread X, deskripsi produk, pengumuman BEM, ringkasan rapat, dan surat lamaran. Sesi itu tidak diberi tahu bahwa jawabannya akan diuji. Hasilnya ada di [`asli/`](asli/).
2. **Tulis ulang.** Sesi terpisah membaca `SKILL.md` versi yang diuji dan menerapkannya pada kesepuluh teks. Sesi ini tidak melihat hasil versi lain.
3. **Penilaian buta.** Sesi juri ketiga menerima pasangan Teks A dan Teks B. Urutan asli dan hasil Lugas diacak per pasangan, dan juri tidak tahu mana yang mana. Juri memilih versi yang lebih manusiawi dan versi yang lebih siap dipakai.
4. **Cek fakta.** Setiap hasil dibandingkan dengan aslinya untuk mencari fakta yang hilang atau ditambahkan.

## Hasil

| Versi | Lebih manusiawi | Lebih siap pakai | Fakta ditambahkan |
|-------|-----------------|------------------|-------------------|
| [0.1.1](v0.1.1/penilaian.md) | 6/10 | 6/10 (1 seri) | 0 |
| [0.2.0](v0.2.0/penilaian.md) | 7/10 (1 kalah, 2 seri) | 9/10 (1 seri, 0 kalah) | 0 |

## Batasan

Penulis teks, penulis ulang, dan juri semuanya model Claude. Juri memakai model yang berbeda (Sonnet), tapi penilaian manusia tetap lebih kuat. Sepuluh teks juga terlalu sedikit untuk kesimpulan statistik. Anggap hasil ini sebagai petunjuk arah, bukan bukti.
