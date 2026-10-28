---
name: lugas
description: |
  Menulis ulang teks Bahasa Indonesia yang terdengar seperti buatan AI supaya terdengar
  seperti penulisnya, tanpa mengubah isinya. Pakai saat menyunting atau memeriksa tulisan
  berbahasa Indonesia: pembuka "Di era digital ini", "tidak hanya... tetapi juga", kata
  "tentunya" dan "penting untuk dicatat", idiom terjemahan, kata mubazir, register yang
  tercampur, tanda pisah panjang, label tebal, emoji, atau penutup "Semoga bermanfaat!".
  Juga untuk permintaan seperti "biar nggak kayak AI", "humanize teks ini", "lugaskan",
  "periksa pola AI", atau "kedengarannya kayak ChatGPT".
license: MIT
metadata:
  version: "0.2.0"
---

# Lugas: hilangkan pola tulisan AI dari Bahasa Indonesia

Tulis ulang teks supaya terdengar seperti penulisnya, bukan seperti chatbot. Pertahankan isinya. Jangan mengarang apa pun.

## Aturan tetap

1. **Isi tidak berubah.** Fakta, angka, tanggal, nama, kutipan langsung, tautan, kode, dan istilah teknis tetap persis sama. Kalimat yang jelas hanya hiasan boleh dihapus, tapi jangan ganti dengan klaim baru. Kalimat yang bisa jadi fakta ("Stok terbatas", "biaya pendaftarannya terjangkau") dibiarkan; kalau perlu bukti, sebutkan di catatan.
2. **Jangan menambah.** Tidak ada contoh, data, atau pendapat baru. Kalau teks butuh fakta yang tidak ada, biarkan saja, atau sebutkan di catatan.
3. **Pertahankan register.** Tentukan dulu gayanya, lalu ikuti sampai akhir:
   - **Formal:** saya, Anda, kalimat baku (surat resmi, makalah, rilis pers).
   - **Semiformal:** saya/aku dan Anda/kamu, kalimat rapi tapi luwes (blog, newsletter, dokumentasi).
   - **Santai:** aku/kamu, partikel "sih", "kok", "ya", "deh" (media sosial, chat, catatan pribadi).
   - **Gaul:** gue/lo, campur bahasa Inggris (konten anak muda, Twitter/X).
   Kalau penulis mencampur bahasa Inggris dengan sengaja, biarkan. Itu gaya, bukan pola AI.
4. **Potong lebih dulu, baru ubah.** Sebagian besar pola AI hilang dengan dihapus, jadi teks hasil biasanya lebih pendek. Teks yang sudah bersih boleh dikembalikan dengan sedikit perubahan atau tanpa perubahan; jangan menyunting hanya supaya terlihat bekerja.
5. **Bagian yang tidak disentuh:** blok kode, kutipan langsung, nama produk, judul karya, dan teks di dalam tanda kutip yang dikutip dari orang lain.
6. **Ikuti kebiasaan genre.** Emoji penanda (📍 alamat, 🕒 jam buka, 🧵 thread, ✅ daftar fitur di marketplace), tagar, judul bagian rilis pers, kop dan salam surat resmi adalah bentuk tulisan itu, bukan pola AI. Hapus hanya yang berlebihan untuk genrenya.
7. **Jaga kalimat yang membawa makna.** Pembatasan seperti "Bukan berarti nggak boleh, tapi..." mengubah isi saran, jadi tetap. Kalau pengguna meminta gaya tertentu (puitis, persuasif), ciri gaya itu boleh tetap selama tidak berulang.

## Cara kerja

1. **Baca seluruh teks.** Catat register, kata ganti yang dipakai, dan untuk siapa teks itu ditulis.
2. **Jalankan pemeriksa** kalau teksnya ada di berkas atau lebih dari beberapa paragraf. Skrip ada di folder `scripts` di samping berkas ini:
   ```bash
   python3 -I <folder skill ini>/scripts/periksa.py <berkas>
   ```
   Untuk teks yang ditempel, simpan dulu ke berkas sementara. Pemeriksa hanya mengenal frasa yang ada di daftarnya, dan pola 6, 7, 9, 12, 14, 15, dan 28 tidak diperiksa sama sekali. Nol temuan tidak berarti teks sudah bersih, jadi tetap baca ulang dengan katalog. Temuan pemeriksa juga perlu dinilai: label tebal di daftar definisi, atau kata ganti yang sengaja disebut sebagai contoh, boleh tetap.
3. **Tulis ulang** dengan memakai katalog di bawah.
4. **Periksa ulang.** Tanyakan: "Kalimat mana yang masih terdengar seperti AI?" Perbaiki. Jalankan pemeriksa lagi pada hasilnya kalau tadi dipakai.
5. **Serahkan hasilnya.** Lihat bagian Keluaran.

## Mode

- **Tulis ulang** (bawaan): kembalikan teks yang sudah disunting.
- **Periksa saja**: kalau pengguna minta "periksa", "cek", atau "ada pola AI-nya nggak?", jangan menulis ulang. Daftar temuan dengan kutipan pendek, nomor pola, dan saran perbaikan, diurutkan dari yang paling mengganggu.
- **Berkas**: kalau diberi path, sunting berkasnya langsung, lalu laporkan ringkas apa yang diubah.

## Keluaran

Kembalikan teks hasil saja, tanpa pengantar seperti "Berikut hasilnya". Sesudahnya, tambahkan paling banyak tiga baris catatan hanya kalau ada yang perlu diketahui pengguna, misalnya klaim tanpa sumber yang Anda biarkan, atau bagian yang maknanya ambigu. Untuk beberapa berkas sekaligus, batas tiga baris itu berlaku per berkas.

Kalau teks masih terbungkus jawaban chatbot (pengantar, tawaran bantuan, saran untuk pengguna), keluarkan teksnya saja. Saran yang berguna bagi pengguna, misalnya "isi alamat dan jam buka", dipindah ke catatan, jangan dibuang. Label yang membedakan beberapa pilihan teks ("Opsi 1", "Opsi 2") tetap ada.

---

## Katalog pola

### A. Isi dan klaim

**1. Pembuka era.** "Di era digital ini", "Di zaman serba cepat seperti sekarang", "Seiring perkembangan teknologi", "Dalam dunia yang terus berkembang".
Hapus. Mulai dari pokok persoalan.

**2. Pentingnya dilebih-lebihkan.** "memegang peranan yang sangat penting", "sangat krusial", "tonggak sejarah", "revolusioner", "tak terbantahkan", "mengubah segalanya".
Ganti dengan apa yang sebenarnya terjadi. *"Fitur ini sangat krusial bagi bisnis Anda"* → *"Fitur ini memangkas waktu rekap dari dua jam ke sepuluh menit"* (hanya kalau angka itu ada di teks; kalau tidak ada, hapus klaimnya).

**3. Bahasa promosi.** "solusi terbaik", "pengalaman tak terlupakan", "dirancang khusus untuk Anda", "nikmati kemudahan", "mulus", "tanpa batas".
Hapus kata sifatnya, sisakan faktanya.

**4. Atribusi kabur.** "Banyak ahli berpendapat", "Studi menunjukkan", "Menurut para pakar", "Tidak sedikit orang yang".
Kalau sumbernya disebut di teks, pakai sumber itu. Kalau tidak, hapus atribusinya atau beri catatan.

**5. Ragu berlapis.** "dapat dikatakan bahwa", "bisa jadi mungkin", "cenderung relatif", "secara umum biasanya".
Satu kata ragu sudah cukup, atau tidak sama sekali.

**6. Kesimpulan kosong.** "Hal ini menunjukkan betapa pentingnya...", "Ini mencerminkan komitmen kami terhadap...", "Dengan demikian, jelas bahwa...".
Hapus kalimatnya. Pembaca sudah menangkap maksudnya dari kalimat sebelumnya.

**7. Definisi yang tidak diminta.** "Media sosial adalah sebuah platform digital yang memungkinkan penggunanya untuk..." di tulisan untuk pembaca yang jelas sudah tahu.
Hapus, kecuali pembacanya memang awam.

### B. Struktur

**8. "Tidak hanya X, tetapi juga Y".** Juga "Bukan sekadar X, melainkan Y" dan "Ini bukan soal X, ini soal Y". Sekali dalam satu tulisan masih wajar. Dua kali sudah pola.
*"Aplikasi ini tidak hanya cepat, tetapi juga hemat baterai"* → *"Aplikasinya cepat dan hemat baterai."*

**9. Tiga serangkai paksa.** "cepat, aman, dan andal", "efektif, efisien, dan inovatif". Daftar tiga hal yang muncul karena irama, bukan karena memang ada tiga.
Pertahankan yang didukung isi. Sering tinggal satu.

**10. Pembuka bertahap.** "Faktanya?", "Jujur saja,", "Begini,", "Yang menarik adalah", "Pertanyaannya:", "Inilah kuncinya:".
Hapus dan langsung sampaikan isinya.

**11. Pertanyaan yang dijawab sendiri.** "Mengapa ini penting? Karena..."
Ubah jadi pernyataan: *"Ini penting karena..."*, atau langsung ke alasannya.

**12. Membantah lawan bicara yang tidak ada.** "Saya tidak mengatakan X, tapi...", "Ini bukan berarti Y salah, namun..."
Hapus bantahannya, sisakan klaimnya.

**13. Penutup wajib.** "Semoga bermanfaat!", "Kesimpulannya,", "Pada akhirnya,", "Jadi, tunggu apa lagi?", "Mari kita bersama-sama...", "Yuk, mulai sekarang!".
Akhiri di kalimat terakhir yang berisi informasi. Ajakan bertindak boleh tetap ada kalau memang tujuan teksnya, tapi tulis spesifik: *"Daftar sebelum 30 November di tautan ini."* Penutup yang khas genrenya, seperti "Save dan RT kalau berguna" di thread atau salam penutup surat resmi, tetap. "Mari kita bahas" di akhir pembuka artikel adalah jembatan ke isi berikutnya; ganti dengan kalimat biasa atau hapus.

**14. Ritme seragam.** Semua kalimat sepanjang 15–25 kata, semua paragraf tiga kalimat, tiap paragraf dibuka dengan kalimat topik dan ditutup dengan ringkasan.
Variasikan. Gabungkan kalimat pendek yang terpotong-potong, pecah kalimat yang terlalu panjang, biarkan sebagian paragraf hanya satu kalimat.

**15. Poin untuk hal yang seharusnya prosa.** Penjelasan sebab-akibat yang dipecah jadi poin-poin, atau daftar berisi kalimat lengkap yang saling bergantung.
Jadikan paragraf. Poin hanya untuk hal yang memang setara dan berdiri sendiri: langkah, syarat, spesifikasi.

### C. Kosakata dan tata bahasa

**16. Kata pengisi.** "tentunya", "pastinya", "sejatinya", "pada dasarnya", "secara keseluruhan", "dalam hal ini", "perlu diingat bahwa", "penting untuk dicatat bahwa", "tidak dapat dipungkiri bahwa", "tak bisa dimungkiri".
Hapus. Kalimatnya hampir selalu tetap berdiri.

**17. Kosakata favorit AI.** "esensial", "holistik", "komprehensif", "signifikan" (tanpa angka), "optimal", "inovatif", "menavigasi", "lanskap", "ekosistem", "sinergi", "memberdayakan", "mengeksplorasi", "menyelami", "permadani", "ranah", "spektrum", "dinamika", "transformatif", "katalis".
Ganti dengan kata biasa: "penting", "lengkap", "besar", "mencoba", "melihat", "bidang". Atau hapus.

**18. Terjemahan harfiah dari bahasa Inggris.** "membawa ke level berikutnya", "di penghujung hari", "memainkan peran penting", "membuat perbedaan", "dalam rangka untuk", "bagaimanapun juga" (untuk *however*), "itu adalah" (untuk *it is*), "mari kita menyelam lebih dalam".
Pakai ungkapan Indonesia: *"memainkan peran penting dalam"* → *"berperan dalam"* atau *"menentukan"*; *"di penghujung hari"* biasanya cukup dihapus.

**19. "Yang di mana" dan "di mana" sebagai penghubung.** *"Aplikasi di mana pengguna bisa..."*, *"sistem yang di mana..."*.
Pakai "yang", "tempat", atau pecah kalimatnya. "Di mana" hanya untuk menanyakan atau menyebut tempat.

**20. Kata mubazir.** "adalah merupakan", "agar supaya", "demi untuk", "sangat... sekali", "para hadirin-hadirin", "mulai sejak", "saling bantu-membantu", "seperti misalnya", "dan lain sebagainya" di akhir daftar yang sudah lengkap.
Pilih satu.

**21. Nominalisasi.** "melakukan pengecekan", "melakukan pembelian", "memberikan penjelasan", "mengadakan perbaikan".
Pakai kata kerja langsung: "mengecek", "membeli", "menjelaskan", "memperbaiki".

**22. Pasif bertumpuk.** "Telah dilakukannya pengembangan sistem oleh tim", "Pelaksanaan kegiatan dilakukan pada...".
Sebutkan pelakunya: *"Tim mengembangkan sistem"*, *"Kegiatan berlangsung pada..."*.

**23. "Hal ini" dan "tersebut" berulang.** Rujukan kabur yang muncul di hampir tiap kalimat.
Sebut bendanya langsung, atau gabungkan kalimatnya.

**24. Istilah asing yang tidak perlu.** "insight", "leverage", "impact", "highlight", "concern" di tulisan formal atau semiformal yang selebihnya berbahasa Indonesia.
Ganti dengan padanan yang lazim ("wawasan", "memanfaatkan", "dampak", "sorotan", "kekhawatiran"). Di register gaul atau santai yang memang bercampur, biarkan.

### D. Nada dan register

**25. Sapaan chatbot.** "Tentu! Berikut adalah...", "Semoga membantu!", "Jangan ragu untuk bertanya", "Jika ada pertanyaan lain, silakan hubungi...", "Sebagai model bahasa...".
Hapus semuanya.

**26. Pujian kosong.** "Pertanyaan yang sangat bagus!", "Ide yang luar biasa!", "Anda benar sekali!".
Hapus.

**27. Kata ganti tercampur.** "saya" dan "aku" dalam satu tulisan, "Anda" lalu "kamu", "kami" dan "kita" tertukar.
Seragamkan sesuai pilihan penulis yang paling dominan. "Kami" tidak termasuk pembaca, "kita" termasuk.

**28. Register tidak cocok.** Kalimat baku yang kaku di konteks santai (*"Silakan Anda melakukan pendaftaran terlebih dahulu"* di unggahan Instagram), atau sebaliknya.
Sesuaikan dengan register teks: *"Daftar dulu, ya."*

### E. Format

**29. Tanda pisah panjang (—).** Penulis Indonesia jarang memakainya, apalagi beberapa kali dalam satu paragraf.
Ganti dengan koma, titik, titik dua, atau kurung.

**30. Label tebal dan judul berlebihan.** Tiap poin dibuka dengan **Label:**, atau teks tiga paragraf diberi empat subjudul.
Hapus label yang hanya mengulang isi poin. Teks pendek tidak butuh subjudul.

**31. Emoji dan tanda seru.** 🚀✨💡 di judul dan poin, tanda seru di akhir hampir tiap kalimat.
Hapus emoji yang hanya hiasan. Emoji penanda yang lazim di genrenya tetap (lihat aturan tetap 6). Di tulisan formal dan semiformal, satu tanda seru per tulisan sudah banyak; di media sosial, ikuti kebiasaan penulisnya.

---

## Contoh

**Formal (rilis pers)**

Sebelum:
> Di era transformasi digital ini, PT Sinar Data dengan bangga mengumumkan peluncuran platform terbarunya. Platform ini tidak hanya menawarkan kecepatan, tetapi juga keamanan yang komprehensif. Hal ini tentunya mencerminkan komitmen perusahaan dalam memberikan solusi terbaik bagi pelanggan. Dengan fitur enkripsi, cadangan otomatis, dan dasbor analitik, PT Sinar Data siap membawa bisnis Anda ke level berikutnya.

Sesudah:
> PT Sinar Data meluncurkan platform barunya. Platform ini dilengkapi enkripsi, cadangan otomatis, dan dasbor analitik.

**Santai (unggahan media sosial)**

Sebelum:
> Halo teman-teman! 👋 Pernahkah kalian merasa kewalahan dengan tugas kuliah? Jujur saja, saya juga pernah! Nah, di sini aku mau berbagi 3 tips yang sangat efektif, efisien, dan mudah diterapkan. Yuk, simak sampai habis! Semoga bermanfaat! ✨

Sesudah:
> Lagi kewalahan sama tugas kuliah? Aku juga pernah. Ini tiga tips yang gampang dipraktikkan.

**Semiformal (dokumentasi)**

Sebelum:
> Penting untuk dicatat bahwa sebelum melakukan instalasi, pengguna diharapkan untuk melakukan pengecekan terhadap versi Node.js yang di mana harus minimal versi 20. Hal ini dikarenakan beberapa fitur memerlukan API terbaru.

Sesudah:
> Sebelum memasang, cek versi Node.js Anda. Minimal versi 20, karena beberapa fitur memakai API yang baru ada di versi itu.

## Teks bahasa Inggris atau campuran

Untuk teks yang seluruhnya berbahasa Inggris, pakai skill `humanizer` kalau terpasang. Untuk teks campuran, terapkan katalog ini pada bagian berbahasa Indonesia dan jangan menerjemahkan bagian bahasa Inggrisnya.
