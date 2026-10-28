# Riwayat versi

## 0.2.1 (2026-10-28)

- Pemeriksa tidak lagi menandai frasa wajar seperti "Berikut contoh", "Berikut hasil", "Mari kita lihat", "Jangan sampai ketinggalan kereta", dan "Jika perlu, saya (juga) bisa datang". "Berikut" hanya ditandai bila diikuti "beberapa", "penjelasan", atau "ringkasan". Frasa chatbot yang ditambahkan di 0.2.0 tetap dikenali.
- `evaluasi/README.md` mencatat bahwa jawaban mentah juri tidak disimpan dan bahwa kriteria "siap pakai" sebagian mengukur pembuangan bungkus chatbot.

## 0.2.0 (2026-10-28)

- Dukungan Codex (`skills/lugas/agents/openai.yaml`) dan Cursor (`.cursor-plugin/plugin.json`).
- Cara pasang lewat `npx skills add` untuk Codex, Cursor, dan agen lain.
- `AGENTS.md`: panduan untuk agen yang mengubah repo ini.
- `scripts/validate-package.py` memeriksa versi, deskripsi, dan nama pola agar sama di semua berkas. Validator ini ikut dijalankan di CI.
- Aturan tetap baru: ikuti kebiasaan genre (emoji penanda, tagar, kop surat tetap ada) dan jaga kalimat yang membawa makna.
- Bungkus jawaban chatbot dibuang dari teks, tapi saran yang berguna dipindah ke catatan.
- Teks yang sudah bersih boleh dikembalikan tanpa perubahan.
- Pemeriksa mengenali "Berikut ringkasan", "Mari kita bahas", "Jangan sampai kelewatan", dan "Jika perlu, saya bisa".
- Nama pola di tabel README disamakan dengan `SKILL.md`.
- Uji kualitas buta di `evaluasi/`: hasil yang lebih siap pakai naik dari 6/10 (0.1.1) ke 9/10 (0.2.0).

## 0.1.1 (2026-10-28)

- Contoh "sesudah" di README dan SKILL.md tidak lagi menambahkan fakta yang tidak ada di teks aslinya.
- Saran pola 18 tidak lagi menyarankan "pada akhirnya", yang justru ditandai sebagai pola 13.
- SKILL.md menjelaskan bahwa temuan pemeriksa tetap perlu dinilai.
- Tes unit untuk pemeriksa dan workflow GitHub Actions.

## 0.1.0 (2026-10-28)

- Rilis pertama: katalog 31 pola, mode tulis ulang dan periksa saja, serta pemeriksa `periksa.py`.
