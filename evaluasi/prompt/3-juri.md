# Prompt juri

Model: Claude Sonnet, satu sesi baru per putaran. Juri hanya bisa membaca folder berisi pasangan Teks A dan Teks B, di luar repo. Tiap berkas pasangan berbentuk:

```markdown
# Pasangan 01

## Teks A

[teks]

## Teks B

[teks]
```

Urutan asli dan hasil Lugas diacak per pasangan dengan `random.SystemRandom`. Kuncinya ada di `kunci-acak.json` di folder tiap versi.

## Prompt

Putaran 0.2.0 memakai prompt yang sama dengan satu kalimat tambahan (ditandai di bawah), karena satu pasangan identik. Path folder berbeda per putaran (`buta` lalu `buta2`).

```text
Kamu juri penulisan Bahasa Indonesia. Di folder <folder pasangan> ada 10 berkas (01.md–10.md). Tiap berkas berisi dua versi teks untuk keperluan yang sama: Teks A dan Teks B.

Baca HANYA berkas di folder itu. Jangan membuka berkas atau folder lain mana pun.

Untuk tiap pasangan, jawab:
1. **Lebih manusiawi:** versi mana yang lebih terdengar seperti ditulis orang Indonesia sungguhan untuk keperluan itu? (A / B / seri)
2. **Lebih siap pakai:** kalau kamu pemilik teks ini, versi mana yang akan kamu kirim atau unggah? (A / B / seri)
3. **Keyakinan:** rendah / sedang / tinggi.
4. **Alasan:** satu kalimat.

Nilai tiap pasangan secara terpisah. Jangan berasumsi ada pola atau jumlah tertentu untuk A atau B. [0.2.0 saja: Kalau kedua versi identik, jawab seri.]

Kembalikan hasil sebagai tabel Markdown dengan kolom: No | Lebih manusiawi | Lebih siap pakai | Keyakinan | Alasan. Setelah tabel, tulis satu paragraf pendek tentang pola umum yang kamu lihat.
```

Jawaban lengkap juri, sebelum kunci dibuka, ada di `jawaban-juri.md` di folder tiap versi.
