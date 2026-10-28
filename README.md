# Lugas

[![Uji](https://github.com/Adamfatur/lugas/actions/workflows/uji.yml/badge.svg)](https://github.com/Adamfatur/lugas/actions/workflows/uji.yml) [![Lisensi: MIT](https://img.shields.io/badge/lisensi-MIT-blue.svg)](LICENSE) [![Versi](https://img.shields.io/github/v/tag/Adamfatur/lugas?label=versi)](CHANGELOG.md)

Lugas menyunting teks Bahasa Indonesia yang terdengar seperti buatan AI supaya terdengar seperti ditulis penulisnya sendiri. Isinya tidak berubah: fakta, angka, nama, dan tautan tetap sama. Lugas bekerja sebagai skill di Claude Code, Codex, Cursor, Claude.ai, dan agen lain yang mendukung skill.

**Sebelum:**
> Di era digital ini, keamanan data tentunya memegang peranan yang sangat penting. Fitur terbaru kami tidak hanya melindungi data Anda, tetapi juga memberikan pengalaman yang mulus dan tak terlupakan. Dengan enkripsi end-to-end, cadangan otomatis, dan kontrol akses yang komprehensif, kami membawa keamanan ke level berikutnya. Semoga bermanfaat!

**Sesudah:**
> Fitur terbaru kami melindungi data Anda dengan enkripsi end-to-end, cadangan otomatis, dan kontrol akses.

Lugas terinspirasi dari [Humanizer](https://github.com/blader/humanizer), yang dibuat untuk bahasa Inggris. Pola tulisan AI dalam Bahasa Indonesia berbeda, jadi katalog Lugas disusun dari nol: pembuka "Di era digital ini", kata "tentunya" di hampir tiap paragraf, idiom terjemahan seperti "membawa ke level berikutnya", sampai "saya" dan "aku" yang tercampur dalam satu tulisan.

Dalam uji buta pada 10 teks AI sehari-hari, juri memilih hasil Lugas sebagai versi yang lebih siap dipakai di 9 dari 10 pasangan. Sisanya seri, dan Lugas tidak pernah kalah. Metode, teks, dan batasan ujinya ada di [`evaluasi/`](evaluasi/).

Lugas menyunting untuk pembaca manusia. Mengelabui detektor AI bukan tujuannya.

## Lima pola paling kentara

1. **Pembuka era:** "Di era digital ini…", "Seiring perkembangan teknologi…"
2. **Tidak hanya X, tetapi juga Y:** "Aplikasi ini tidak hanya cepat, tetapi juga hemat baterai."
3. **Kata pengisi:** "tentunya", "penting untuk dicatat bahwa", "tidak dapat dipungkiri"
4. **Penutup wajib:** "Semoga bermanfaat!", "Jadi, tunggu apa lagi?"
5. **Terjemahan harfiah:** "ke level berikutnya", "memainkan peran penting", "yang di mana"

Lugas memeriksa [31 pola](#31-pola) secara keseluruhan.

## Pemasangan

### Claude Code

```text
/plugin marketplace add Adamfatur/lugas
/plugin install lugas@lugas
```

Atau dari terminal:

```bash
claude plugin marketplace add Adamfatur/lugas
claude plugin install lugas@lugas
```

Setelah dipasang, skill ini bisa dipanggil dengan `/lugas:lugas`.

### Dari salinan lokal dengan GitHub CLI

Cara ini berguna kalau Anda ingin mengubah katalognya sendiri.

```bash
gh repo clone Adamfatur/lugas
claude plugin marketplace add ./lugas
claude plugin install lugas@lugas
```

Perubahan di folder itu langsung terpakai. Naikkan `version` di `.claude-plugin/plugin.json`, lalu jalankan `claude plugin update lugas@lugas`.

### Codex

```bash
npx skills add Adamfatur/lugas --global --agent codex
```

Di Codex, panggil dengan `$lugas`.

### Cursor

```bash
npx skills add Adamfatur/lugas --global --agent cursor
```

### Claude.ai dan Claude Desktop

Unduh repositori ini sebagai ZIP (**Code → Download ZIP**) dan ekstrak. Kompres folder `skills/lugas` menjadi ZIP tersendiri, lalu unggah sebagai skill di Settings.

### Agen lain

```bash
npx skills add Adamfatur/lugas --global --agent '*'
```

Perintah ini memasang Lugas untuk semua agen yang dikenal Skills CLI, termasuk Gemini CLI, GitHub Copilot, dan Windsurf. Hapus `--global` di perintah mana pun di atas untuk memasang Lugas hanya di project yang sedang dibuka. Untuk agen yang tidak dikenal Skills CLI, salin folder `skills/lugas` ke folder skill agen itu.

## Pemakaian

Panggil skill-nya langsung:

```
/lugas:lugas

[tempel teks di sini]
```

Atau minta dengan kalimat biasa:

```
Tolong buat tulisan ini nggak kedengaran kayak AI: [teks]
```

Untuk menyunting berkas, sebutkan path-nya: "lugaskan `draf/rilis-pers.md`". Lugas akan menyunting berkas itu langsung dan melaporkan apa saja yang diubah.

Kalau Anda hanya ingin tahu masalahnya, minta Lugas memeriksa saja: "periksa artikel ini, ada pola AI-nya nggak?". Lugas akan mendaftar temuannya tanpa menulis ulang.

## Cara kerja

1. Lugas membaca seluruh teks dan menentukan register penulis: formal, semiformal, santai, atau gaul.
2. Pemeriksa otomatis menandai pola yang bisa dikenali dari kata.
3. Lugas menulis ulang memakai katalog 31 pola. Bagian yang hanya hiasan dihapus, bukan diganti dengan kalimat baru.
4. Hasilnya dibaca ulang dan diperiksa sekali lagi sebelum diserahkan.

Ada tiga aturan yang tidak pernah dilanggar. Lugas tidak menambah fakta, contoh, atau pendapat. Lugas tidak mengubah register: tulisan santai tetap santai. Lugas juga tidak menyentuh blok kode, kutipan langsung, dan nama produk.

Lugas juga mengikuti kebiasaan tiap genre. Emoji 📍 untuk alamat di Instagram, 🧵 di thread, ✅ di daftar produk marketplace, dan kop surat resmi dianggap bagian dari bentuk tulisan, jadi tidak dihapus. Teks yang sudah bersih dikembalikan dengan sedikit perubahan atau tanpa perubahan.

## Pemeriksa

`periksa.py` bisa dipakai tanpa agen. Pemeriksa ini hanya butuh Python 3.9 atau lebih baru, tanpa pustaka tambahan.

```bash
python3 skills/lugas/scripts/periksa.py draf.md
cat draf.txt | python3 skills/lugas/scripts/periksa.py -
python3 skills/lugas/scripts/periksa.py --json draf.md
```

Contoh keluaran:

```text
== draf.md (24 kata, 6 temuan)
           1:1  [ 1] pembuka era: "Di era digital ini"  → Hapus. Mulai dari pokok persoalan.
          1:35  [16] kata pengisi: "tentunya"  → Hapus; kalimatnya tetap berdiri.
          1:44  [ 2] pentingnya dilebih-lebihkan: "memegang peranan yang sangat penting"  → Sebut apa yang sebenarnya terjadi, atau hapus.
          2:11  [21] nominalisasi: "melakukan pengecekan"  → Pakai kata kerja langsung (mis. 'mengecek', 'membeli').
          2:32  [19] di mana sebagai penghubung: "yang di mana"  → Pakai 'yang', 'tempat', atau pecah kalimatnya.
          2:69  [13] penutup wajib: "Semoga bermanfaat"  → Akhiri di kalimat terakhir yang berisi informasi.
```

Pemeriksa melewati blok kode dan kode sebaris. Tiap temuan tetap perlu dinilai: label tebal di daftar definisi atau emoji penanda genre, misalnya, boleh tetap ada. Pemeriksa hanya mengenal frasa di daftarnya, dan pola yang butuh penilaian (6, 7, 9, 12, 14, 15, dan 28) tidak diperiksa sama sekali. Nol temuan tidak berarti teksnya sudah bersih.

## 31 pola

| No | Pola | Contoh |
|---:|------|--------|
| | **Isi dan klaim** | |
| 1 | Pembuka era | "Di era digital ini" |
| 2 | Pentingnya dilebih-lebihkan | "memegang peranan yang sangat penting" |
| 3 | Bahasa promosi | "solusi terbaik", "pengalaman tak terlupakan" |
| 4 | Atribusi kabur | "Studi menunjukkan", "Banyak ahli berpendapat" |
| 5 | Ragu berlapis | "dapat dikatakan bahwa", "bisa jadi mungkin" |
| 6 | Kesimpulan kosong | "Hal ini menunjukkan betapa pentingnya…" |
| 7 | Definisi yang tidak diminta | "Media sosial adalah sebuah platform digital yang…" |
| | **Struktur** | |
| 8 | "Tidak hanya X, tetapi juga Y" | "bukan sekadar X, melainkan Y" |
| 9 | Tiga serangkai paksa | "efektif, efisien, dan inovatif" |
| 10 | Pembuka bertahap | "Jujur saja,", "Faktanya?", "Begini," |
| 11 | Pertanyaan yang dijawab sendiri | "Mengapa ini penting? Karena…" |
| 12 | Membantah lawan bicara yang tidak ada | "Saya tidak mengatakan X, tapi…" |
| 13 | Penutup wajib | "Semoga bermanfaat!", "Kesimpulannya," |
| 14 | Ritme seragam | Semua kalimat dan paragraf sama panjang |
| 15 | Poin untuk hal yang seharusnya prosa | Sebab-akibat dipecah jadi poin |
| | **Kosakata dan tata bahasa** | |
| 16 | Kata pengisi | "tentunya", "penting untuk dicatat bahwa" |
| 17 | Kosakata favorit AI | "holistik", "komprehensif", "menavigasi", "lanskap" |
| 18 | Terjemahan harfiah dari bahasa Inggris | "ke level berikutnya", "di penghujung hari" |
| 19 | "Yang di mana" dan "di mana" sebagai penghubung | "aplikasi yang di mana pengguna…" |
| 20 | Kata mubazir | "adalah merupakan", "agar supaya", "demi untuk" |
| 21 | Nominalisasi | "melakukan pengecekan" |
| 22 | Pasif bertumpuk | "Telah dilakukannya pengembangan…" |
| 23 | "Hal ini" dan "tersebut" berulang | Rujukan kabur di hampir tiap kalimat |
| 24 | Istilah asing yang tidak perlu | "insight", "leverage", "impact" |
| | **Nada dan register** | |
| 25 | Sapaan chatbot | "Tentu! Berikut adalah…", "Jangan ragu untuk bertanya" |
| 26 | Pujian kosong | "Pertanyaan yang sangat bagus!" |
| 27 | Kata ganti tercampur | "saya" dan "aku" dalam satu tulisan |
| 28 | Register tidak cocok | Bahasa surat dinas di unggahan Instagram |
| | **Format** | |
| 29 | Tanda pisah panjang (—) | "Hasilnya — seperti dugaan — buruk." |
| 30 | Label tebal dan judul berlebihan | Tiap poin dibuka dengan **Label:** |
| 31 | Emoji dan tanda seru | 🚀✨ dan tanda seru di tiap kalimat |

Penjelasan dan cara memperbaiki tiap pola ada di [`skills/lugas/SKILL.md`](skills/lugas/SKILL.md).

## Struktur repositori

```text
.claude-plugin/        manifest plugin dan marketplace Claude Code
.cursor-plugin/        manifest plugin Cursor
skills/lugas/
  SKILL.md             katalog pola dan instruksi untuk agen
  scripts/periksa.py   pemeriksa otomatis
  agents/openai.yaml   metadata untuk Codex dan agen kompatibel OpenAI
scripts/               validator paket
evaluasi/              uji kualitas buta per versi
contoh/                teks sebelum dan sesudah untuk tes
tests/                 tes unit pemeriksa
AGENTS.md              panduan untuk agen yang mengubah repo ini
```

## Berkontribusi

Pola baru, contoh yang lebih baik, dan laporan salah tandai sangat membantu. Untuk melaporkan masalah dari terminal:

```bash
gh issue create --repo Adamfatur/lugas
```

Kalau Anda menambah atau mengubah pola:

1. Tambahkan penjelasannya di `SKILL.md` dan barisnya di tabel README.
2. Kalau pola itu bisa dikenali dari kata, tambahkan regex-nya di `periksa.py` dan satu kasus di `tests/test_periksa.py`.
3. Pastikan frasa yang wajar tidak ikut tertandai. Tambahkan contohnya di `TestTidakSalahTandai`.
4. Jalankan tes dan validator paket:

   ```bash
   python3 -m unittest discover -s tests -v
   python3 scripts/validate-package.py
   ```

5. Kirim pull request:

   ```bash
   gh pr create --repo Adamfatur/lugas
   ```

Contoh "sesudah" tidak boleh berisi fakta yang tidak ada di teks "sebelum". Model meniru contoh, jadi contoh yang mengarang akan mengajari agen untuk ikut mengarang.

## Riwayat versi

Lihat [CHANGELOG.md](CHANGELOG.md).

## Lisensi

[MIT](LICENSE)
