# Panduan untuk agen

Berkas ini menjelaskan cara mengubah Lugas tanpa merusak paket atau prompt-nya.

## Isi repo

Lugas adalah skill agen yang ditulis dalam Markdown, ditambah satu pemeriksa Python. `skills/lugas/SKILL.md` adalah prompt yang dibaca agen. Repo ini tidak punya langkah build.

Jaga agar skill tetap portabel. Jangan menulis instruksi yang hanya berlaku untuk satu atau dua alat agen.

## Berkas utama

- `skills/lugas/SKILL.md` adalah sumber kebenaran dan satu-satunya berkas skill. Isinya metadata YAML, aturan tetap, cara kerja, dan katalog pola bernomor dalam lima kelompok.
- `skills/lugas/scripts/periksa.py` menandai pola yang bisa dikenali dari kata. Nomor polanya harus sama dengan katalog di `SKILL.md`.
- `skills/lugas/agents/openai.yaml` berisi nama tampilan, deskripsi singkat, dan prompt bawaan untuk agen yang kompatibel dengan OpenAI, seperti Codex.
- `README.md` menjelaskan pemasangan, pemakaian, dan daftar pola.
- `CHANGELOG.md` berisi catatan rilis, yang terbaru di atas. Catatan lama tetap memakai nomor pola pada rilis itu.
- `.claude-plugin/plugin.json` dan `.claude-plugin/marketplace.json` untuk Claude Code.
- `.cursor-plugin/plugin.json` untuk Cursor.
- `scripts/validate-package.py` memeriksa berkas paket dan nilai yang harus sama di beberapa berkas.
- `tests/` berisi tes unit pemeriksa. `contoh/` berisi teks yang dipakai tes.
- `evaluasi/` berisi hasil uji kualitas. Jangan ubah hasil lama; tambahkan uji baru di folder bertanggal.

## Aturan perubahan

Jaga `SKILL.md` dan `README.md` tetap sejalan.

- **Pola:** Pola dinomori dari 1 tanpa lompatan. Pola baru hanya layak ditambahkan kalau tidak tercakup pola yang sudah ada; lebih baik gabungkan ke pola yang ada. Kalau Anda menambah, menghapus, atau menomori ulang pola, perbarui tabel README, judul bagian "## N pola" di README, nomor pola di `periksa.py`, dan tesnya. Validator memeriksa jumlah dan nama pola.
- **Versi:** Pakai versi yang sama di `metadata.version` pada `SKILL.md`, judul pertama `CHANGELOG.md`, `.claude-plugin/plugin.json`, dan `.cursor-plugin/plugin.json`.
- **Deskripsi:** Semua manifest memakai kalimat pertama deskripsi di `SKILL.md`.
- **Panjang:** Setiap kata di `SKILL.md` dibaca setiap kali skill dipakai. Validator membatasinya 5.500 kata. Tambahan kata harus sepadan manfaatnya.
- **Contoh:** Contoh "sesudah" tidak boleh berisi fakta yang tidak ada di teks "sebelum". Model meniru contoh.
- **Pemeriksa:** Setiap regex baru butuh satu kasus di `TestPolaTerdeteksi`. Frasa wajar yang hampir mirip masuk ke `TestTidakSalahTandai`.
- **Riwayat:** Tambahkan catatan singkat di `CHANGELOG.md` untuk setiap perubahan perilaku.
- **Pengecekan:** Sebelum merilis, jalankan:

  ```bash
  python3 scripts/validate-package.py
  python3 -m unittest discover -s tests
  claude plugin validate .
  npx skills add . --list
  ```

## Gaya tulisan

Tulis komentar kode, prompt, dokumentasi, dan pesan validasi dalam bahasa yang lugas. Lugas harus lolos pemeriksaannya sendiri.

- Sampaikan pokoknya lebih dulu.
- Pakai kata yang umum dan kalimat aktif.
- Buat kalimat dan paragraf pendek.
- Pakai satu istilah untuk satu hal.
- Jangan ubah identifier, perintah, path, kutipan, dan contoh yang menentukan perilaku.
