# Prompt penulis ulang

Model: Claude Opus 5.5, satu sesi baru per putaran. Sesi ini hanya membaca `SKILL.md` versi yang diuji, pemeriksanya, dan teks asli.

## Putaran 0.1.1

```text
Baca dan ikuti skill di /Users/reysonic/Desain/Skill/lugas/skills/lugas/SKILL.md dengan cermat. Pemeriksanya ada di /Users/reysonic/Desain/Skill/lugas/skills/lugas/scripts/periksa.py (jalankan dengan `python3 -I <path> <berkas>`).

Terapkan skill itu dalam mode tulis ulang pada 10 berkas di /Users/reysonic/Desain/Skill/lugas/evaluasi/asli/ (01.md sampai 10.md). Kerjakan tiap berkas secara terpisah, persis seperti yang diminta SKILL.md, termasuk menjalankan pemeriksa sebelum dan sesudah menulis ulang.

Jangan ubah berkas di folder asli/. Simpan hasil tiap berkas (hanya teks hasil, tanpa catatan) ke /Users/reysonic/Desain/Skill/lugas/evaluasi/lugas/ dengan nama yang sama. Kalau SKILL.md menyuruh menambahkan catatan untuk pengguna, tulis catatan itu ke /Users/reysonic/Desain/Skill/lugas/evaluasi/lugas/catatan.md, dikelompokkan per nomor berkas.

Setelah selesai, laporkan secara singkat: berkas yang dibuat, dan bagian SKILL.md yang menurutmu tidak jelas atau sulit diikuti (kalau ada).
```

Folder `lugas/` kemudian dipindah ke [`v0.1.1/hasil/`](../v0.1.1/hasil/).

## Putaran 0.2.0

```text
Baca dan ikuti skill di /Users/reysonic/Desain/Skill/lugas/skills/lugas/SKILL.md dengan cermat. Pemeriksanya ada di /Users/reysonic/Desain/Skill/lugas/skills/lugas/scripts/periksa.py (jalankan dengan `python3 -I <path> <berkas>`).

Terapkan skill itu dalam mode tulis ulang pada 10 berkas di /Users/reysonic/Desain/Skill/lugas/evaluasi/asli/ (01.md sampai 10.md). Kerjakan tiap berkas secara terpisah, persis seperti yang diminta SKILL.md, termasuk menjalankan pemeriksa sebelum dan sesudah menulis ulang.

Hanya baca SKILL.md, pemeriksa, dan berkas di folder asli/. Jangan membuka folder lain di evaluasi/.

Jangan ubah berkas di folder asli/. Simpan hasil tiap berkas (hanya teks hasil) ke /Users/reysonic/Desain/Skill/lugas/evaluasi/v0.2.0/hasil/ dengan nama yang sama. Tulis catatan yang diminta SKILL.md ke /Users/reysonic/Desain/Skill/lugas/evaluasi/v0.2.0/hasil/catatan.md, dikelompokkan per nomor berkas.

Setelah selesai, laporkan singkat: berkas yang dibuat, dan bagian SKILL.md yang menurutmu tidak jelas atau sulit diikuti (kalau ada).
```
