#!/usr/bin/env python3
"""Tandai pola tulisan khas AI dalam teks Bahasa Indonesia.

Pemakaian:
  python3 periksa.py berkas.md [berkas lain ...]
  cat teks.txt | python3 periksa.py -
  python3 periksa.py --json berkas.md

Nomor pola mengikuti katalog di SKILL.md. Skrip ini hanya menemukan pola yang
bisa dikenali dari kata; pola yang butuh penilaian (tiga serangkai, ritme,
definisi yang tidak diminta) tidak diperiksa di sini.
"""

import argparse
import json
import re
import sys

# (nomor pola, nama, regex, saran)
POLA = [
    (1, "pembuka era",
     r"\b(di|pada) (era|zaman|masa) (digital|modern|teknologi|globalisasi|serba [a-z]+|sekarang|transformasi digital)( ini| seperti sekarang)?\b"
     r"|\bseiring (dengan )?(perkembangan|kemajuan) (teknologi|zaman)\b"
     r"|\bdalam dunia yang (terus|semakin) (berkembang|berubah)\b",
     "Hapus. Mulai dari pokok persoalan."),
    (2, "pentingnya dilebih-lebihkan",
     r"\bmemegang peran(an)? (yang )?(sangat )?(penting|krusial|vital)\b"
     r"|\b(sangat|amat) (krusial|vital)\b|\btonggak sejarah\b|\brevolusioner\b"
     r"|\btak terbantahkan\b|\bmengubah segalanya\b|\bmengubah permainan\b",
     "Sebut apa yang sebenarnya terjadi, atau hapus."),
    (3, "bahasa promosi",
     r"\bsolusi (terbaik|terdepan|lengkap)\b|\bpengalaman (yang )?(tak|tidak) terlupakan\b"
     r"|\bdirancang khusus untuk (anda|kamu)\b|\bnikmati kemudahan\b"
     r"|\b(secara |dengan )?mulus\b|\btanpa batas\b",
     "Hapus kata sifatnya, sisakan faktanya."),
    (4, "atribusi kabur",
     r"\b(banyak|para) (ahli|pakar|peneliti)( berpendapat| mengatakan| menyebutkan)?\b"
     r"|\b(studi|penelitian|riset) (menunjukkan|membuktikan)\b|\bmenurut para (ahli|pakar)\b"
     r"|\btidak sedikit (orang|yang)\b",
     "Sebut sumbernya kalau ada di teks; kalau tidak, hapus."),
    (5, "ragu berlapis",
     r"\bdapat dikatakan bahwa\b|\bbisa jadi mungkin\b|\bmungkin saja bisa\b"
     r"|\bcenderung relatif\b|\bsecara umum biasanya\b",
     "Satu kata ragu cukup."),
    (8, "tidak hanya X, tetapi juga Y",
     r"\btidak (hanya|cuma|sekadar)\b[^.!?\n]{0,100}?\b(tetapi|tapi|namun|melainkan)( juga)?\b"
     r"|\bbukan (hanya|cuma|sekadar)\b[^.!?\n]{0,100}?\b(melainkan|tetapi|tapi)\b"
     r"|\bini bukan (soal|tentang)\b[^.!?\n]{0,80}?\b(soal|tentang)\b",
     "Nyatakan langsung. Sekali per tulisan masih wajar."),
    (10, "pembuka bertahap",
     r"(^|[.!?]\s+)(faktanya\?|jujur saja,|begini,|yang menarik adalah|pertanyaannya:|inilah kuncinya:|nah,)",
     "Hapus dan langsung ke isi."),
    (11, "pertanyaan dijawab sendiri",
     r"\b(mengapa|kenapa|apa) [^.!?\n]{0,60}\?\s+(karena|sebab|jawabannya)\b",
     "Ubah jadi pernyataan."),
    (13, "penutup wajib",
     r"\bsemoga (bermanfaat|membantu|artikel ini)\b|\bkesimpulannya,|\bpada akhirnya,"
     r"|\bjadi,? tunggu apa lagi\b|\bmari kita (bersama|mulai|bahas|simak)\b|\byuk,? (mulai|simak)\b"
     r"|\bjangan sampai (kelewatan|ketinggalan)(,? ya)?[!.]",
     "Akhiri di kalimat terakhir yang berisi informasi."),
    (16, "kata pengisi",
     r"\b(tentunya|pastinya|sejatinya|pada dasarnya|secara keseluruhan|dalam hal ini)\b"
     r"|\b(perlu diingat|penting untuk (dicatat|diketahui|diingat)) bahwa\b"
     r"|\btidak dapat dipungkiri\b|\btak (bisa|dapat) di(p|m)ungkiri\b",
     "Hapus; kalimatnya tetap berdiri."),
    (17, "kosakata favorit AI",
     r"\b(esensial|holistik|komprehensif|optimal|inovatif|menavigasi|lanskap|sinergi"
     r"|memberdayakan|mengeksplorasi|menyelami|permadani|ranah|spektrum|transformatif|katalis)\b",
     "Pakai kata biasa atau hapus."),
    (18, "terjemahan harfiah",
     r"\bke level (berikutnya|selanjutnya)\b|\bdi penghujung hari\b|\bmemainkan peran\b"
     r"|\bmembuat (sebuah )?perbedaan\b|\bdalam rangka untuk\b|\bmenyelam lebih dalam\b",
     "Pakai ungkapan Indonesia."),
    (19, "di mana sebagai penghubung",
     r"\byang di ?mana\b|\b[a-z]{3,} di ?mana (pengguna|kita|kami|anda|kamu|mereka|ia|dia|setiap|semua)\b",
     "Pakai 'yang', 'tempat', atau pecah kalimatnya."),
    (20, "kata mubazir",
     r"\badalah merupakan\b|\bagar supaya\b|\bdemi untuk\b|\bsangat [a-z]+ sekali\b"
     r"|\bmulai sejak\b|\bseperti misalnya\b|\bpara ([a-z]+)-\1\b",
     "Pilih satu."),
    (21, "nominalisasi",
     r"\b(melakukan|memberikan|mengadakan) (pe[a-z]+an|pen[a-z]+an|pem[a-z]+an|peng[a-z]+an|per[a-z]+an)\b",
     "Pakai kata kerja langsung (mis. 'mengecek', 'membeli')."),
    (22, "pasif bertumpuk",
     r"\b(telah |sudah )?dilakukannya\b|\b(pelaksanaan|penerapan|pengembangan) [a-z ]{0,30}dilakukan\b",
     "Sebut pelakunya."),
    (24, "istilah asing yang tak perlu",
     r"\b(insight|leverage|impact|highlight|concern|engagement|mindset)\b",
     "Pakai padanan Indonesia, kecuali registernya memang campur."),
    (25, "sapaan chatbot",
     r"\btentu[!,] berikut\b|\bberikut (adalah |ini )?(beberapa|penjelasan|ringkasan)\b"
     r"|\bjika perlu, saya (juga )?bisa (membuatkan|menambahkan|menyusun|menjelaskan|merangkum)\b"
     r"|\bjangan ragu untuk\b|\bsebagai (sebuah )?(model bahasa|ai)\b"
     r"|\bjika (ada|anda memiliki) pertanyaan (lain|lebih lanjut)\b",
     "Hapus."),
    (26, "pujian kosong",
     r"\b(pertanyaan|ide) yang (sangat )?(bagus|menarik|luar biasa)\b|\b(anda|kamu) benar sekali\b",
     "Hapus."),
    (29, "tanda pisah panjang", r"—| -- ", "Ganti dengan koma, titik, titik dua, atau kurung."),
    (30, "label tebal", r"^\s*([-*]|\d+\.)\s+\*\*[^*]+:\*\*|^\s*([-*]|\d+\.)\s+\*\*[^*]+\*\*:",
     "Hapus label yang hanya mengulang isi poin."),
    (31, "emoji",
     "[\U0001F300-\U0001FAFF☀-➿⭐✨]",
     "Hapus kalau hanya hiasan; emoji penanda genre (📍, 🧵, ✅) boleh tetap."),
]

POLA_TERKOMPILASI = [(n, nama, re.compile(rx, re.IGNORECASE | re.MULTILINE), saran)
                     for n, nama, rx, saran in POLA]

KATA_GANTI = {
    "orang pertama": {"saya": r"\bsaya\b", "aku": r"\baku\b", "gue": r"\b(gue|gw)\b"},
    "orang kedua": {"Anda": r"\banda\b", "kamu": r"\bkamu\b", "lo": r"\b(lo|lu|elo)\b"},
}


def baris_teks(teks):
    """Hasilkan (nomor baris, isi) dan lewati blok kode berpagar."""
    dalam_kode = False
    for i, baris in enumerate(teks.splitlines(), 1):
        if baris.lstrip().startswith("```"):
            dalam_kode = not dalam_kode
            continue
        if not dalam_kode:
            yield i, re.sub(r"`[^`]*`", lambda m: " " * len(m.group()), baris)


def periksa(teks):
    temuan = []
    baris = list(baris_teks(teks))
    for no, isi in baris:
        for n, nama, rx, saran in POLA_TERKOMPILASI:
            for m in rx.finditer(isi):
                temuan.append({"baris": no, "kolom": m.start() + 1, "pola": n,
                               "nama": nama, "kutipan": m.group().strip(), "saran": saran})

    isi_semua = "\n".join(isi for _, isi in baris)
    jumlah_kata = len(re.findall(r"\w+", isi_semua))

    seru = len(re.findall(r"!", isi_semua))
    if seru >= 3:
        temuan.append({"baris": 0, "kolom": 0, "pola": 31, "nama": "tanda seru",
                       "kutipan": f"{seru} tanda seru", "saran": "Satu per tulisan sudah banyak."})

    hal_ini = len(re.findall(r"\b(hal ini|hal tersebut|tersebut)\b", isi_semua, re.IGNORECASE))
    if jumlah_kata and hal_ini >= 3 and hal_ini / jumlah_kata > 1 / 120:
        temuan.append({"baris": 0, "kolom": 0, "pola": 23, "nama": "'hal ini/tersebut' berulang",
                       "kutipan": f"{hal_ini} kali dalam {jumlah_kata} kata",
                       "saran": "Sebut bendanya langsung."})

    tanpa_kutipan = re.sub(r"[\"“][^\"”]*[\"”]", " ", isi_semua)
    for kelompok, pilihan in KATA_GANTI.items():
        terpakai = {k: len(re.findall(rx, tanpa_kutipan, re.IGNORECASE)) for k, rx in pilihan.items()}
        terpakai = {k: v for k, v in terpakai.items() if v}
        if len(terpakai) > 1:
            rincian = ", ".join(f"{k} ({v})" for k, v in terpakai.items())
            temuan.append({"baris": 0, "kolom": 0, "pola": 27, "nama": f"kata ganti {kelompok} tercampur",
                           "kutipan": rincian, "saran": "Seragamkan mengikuti yang paling dominan."})

    temuan.sort(key=lambda t: (t["baris"] == 0, t["baris"], t["kolom"]))
    return temuan, jumlah_kata


def cetak(sumber, temuan, jumlah_kata):
    print(f"== {sumber} ({jumlah_kata} kata, {len(temuan)} temuan)")
    for t in temuan:
        letak = f"{t['baris']}:{t['kolom']}" if t["baris"] else "seluruh teks"
        print(f"  {letak:>12}  [{t['pola']:>2}] {t['nama']}: \"{t['kutipan']}\"  → {t['saran']}")
    if not temuan:
        print("  Tidak ada pola yang dikenali. Pola yang butuh penilaian tetap perlu dibaca sendiri.")


def main():
    parser = argparse.ArgumentParser(description="Tandai pola tulisan khas AI dalam teks Bahasa Indonesia.")
    parser.add_argument("berkas", nargs="+", help="path berkas, atau - untuk stdin")
    parser.add_argument("--json", action="store_true", help="keluaran dalam JSON")
    args = parser.parse_args()

    hasil = []
    for path in args.berkas:
        if path == "-":
            teks = sys.stdin.read()
        else:
            with open(path, encoding="utf-8") as f:
                teks = f.read()
        temuan, jumlah_kata = periksa(teks)
        hasil.append({"berkas": path, "jumlah_kata": jumlah_kata, "temuan": temuan})

    if args.json:
        json.dump(hasil, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        for h in hasil:
            cetak(h["berkas"], h["temuan"], h["jumlah_kata"])


if __name__ == "__main__":
    main()
