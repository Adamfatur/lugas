import os
import sys
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(AKAR, "skills", "lugas", "scripts"))

from periksa import periksa  # noqa: E402


def nomor_pola(teks):
    temuan, _ = periksa(teks)
    return {t["pola"] for t in temuan}


class TestPolaTerdeteksi(unittest.TestCase):
    def test_contoh_per_pola(self):
        kasus = {
            1: "Di era digital ini, semua orang punya ponsel.",
            2: "Fitur ini memegang peranan yang sangat penting.",
            3: "Kami menawarkan solusi terbaik untuk Anda.",
            4: "Studi menunjukkan kopi itu sehat.",
            5: "Dapat dikatakan bahwa hasilnya baik.",
            8: "Aplikasi ini tidak hanya cepat, tetapi juga hemat baterai.",
            10: "Kami mencoba lagi. Jujur saja, hasilnya buruk.",
            11: "Mengapa ini penting? Karena data adalah aset.",
            13: "Itu saja dari kami. Semoga bermanfaat!",
            16: "Tentunya kami akan hadir.",
            17: "Pendekatan holistik dibutuhkan.",
            18: "Kami membawa bisnis Anda ke level berikutnya.",
            19: "Ini aplikasi yang di mana pengguna bisa memesan.",
            20: "Rapat ini adalah merupakan agenda tahunan.",
            21: "Tim akan melakukan pengecekan besok.",
            22: "Telah dilakukannya pengembangan sistem.",
            24: "Ada insight menarik dari rapat tadi.",
            25: "Tentu! Berikut adalah ringkasannya.",
            26: "Pertanyaan yang sangat bagus.",
            29: "Hasilnya — seperti dugaan — buruk.",
            30: "- **Kecepatan:** cepat sekali",
            31: "Rilis baru sudah keluar 🚀",
        }
        for pola, teks in kasus.items():
            with self.subTest(pola=pola):
                self.assertIn(pola, nomor_pola(teks))

    def test_bungkus_chatbot_dan_penutup(self):
        self.assertIn(25, nomor_pola("Berikut ringkasan hasil rapatnya:"))
        self.assertIn(25, nomor_pola("Jika perlu, saya juga bisa membuatkan versi poin."))
        self.assertIn(13, nomor_pola("Mari kita bahas satu per satu."))
        self.assertIn(13, nomor_pola("Jangan sampai kelewatan, ya!"))

    def test_kata_ganti_tercampur(self):
        self.assertIn(27, nomor_pola("Saya suka kopi. Tapi aku lebih suka teh."))

    def test_tanda_seru_berlebihan(self):
        self.assertIn(31, nomor_pola("Hebat! Luar biasa! Coba sekarang!"))


class TestTidakSalahTandai(unittest.TestCase):
    def test_frasa_wajar(self):
        teks = (
            "Saya tinggal di Bandung, di mana-mana macet. "
            "Toko itu menjual pakaian dan sepatu. "
            "Mereka mulai bekerja pukul delapan. "
            "Di mana kamu menyimpan kuncinya? "
            "Berikut syarat pendaftaran. "
            "Berikut contoh konfigurasinya. "
            "Berikut hasil pemeriksaan laboratorium. "
            "Mari kita lihat tabel di bawah. "
            "Jangan sampai ketinggalan kereta terakhir. "
            "Jika perlu, saya bisa datang lebih pagi."
        )
        self.assertEqual(set(), nomor_pola(teks) - {27})

    def test_blok_kode_dilewati(self):
        teks = "Pasang dulu.\n\n```bash\n# tentunya di era digital ini\n```\n"
        self.assertEqual(set(), nomor_pola(teks))

    def test_kode_sebaris_dilewati(self):
        self.assertEqual(set(), nomor_pola("Jalankan `tentunya --holistik` di terminal."))


class TestContoh(unittest.TestCase):
    def baca(self, nama):
        with open(os.path.join(AKAR, "contoh", nama), encoding="utf-8") as f:
            return f.read()

    def test_sebelum_banyak_temuan(self):
        temuan, _ = periksa(self.baca("sebelum.md"))
        self.assertGreaterEqual(len(temuan), 20)

    def test_sesudah_hanya_kata_ganti(self):
        self.assertEqual({27}, nomor_pola(self.baca("sesudah.md")))


if __name__ == "__main__":
    unittest.main()
