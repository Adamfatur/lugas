#!/usr/bin/env python3
"""Periksa berkas paket Lugas tanpa pustaka tambahan."""

import json
import re
import sys
from pathlib import Path

AKAR = Path(__file__).resolve().parent.parent
SKILL_PATH = AKAR / "skills" / "lugas" / "SKILL.md"


def baca(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError as galat:
        sys.exit(f"Tidak bisa membaca {path.relative_to(AKAR)}: {galat}")


def baca_json(path):
    try:
        return json.loads(baca(path))
    except json.JSONDecodeError as galat:
        sys.exit(f"Perbaiki JSON di {path.relative_to(AKAR)}: {galat}")


def wajib(cocok, pesan):
    if cocok is None:
        sys.exit(pesan)
    return cocok


SKILL = baca(SKILL_PATH)
README = baca(AKAR / "README.md")
CHANGELOG = baca(AKAR / "CHANGELOG.md")
PERIKSA = baca(AKAR / "skills" / "lugas" / "scripts" / "periksa.py")
PLUGIN = baca_json(AKAR / ".claude-plugin" / "plugin.json")
MARKETPLACE = baca_json(AKAR / ".claude-plugin" / "marketplace.json")
CURSOR = baca_json(AKAR / ".cursor-plugin" / "plugin.json")

metadata = wajib(re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
                 "SKILL.md harus diawali metadata YAML").group(1)
if not re.search(r"(?m)^name: lugas$", metadata):
    sys.exit("Isi name: lugas di metadata SKILL.md")

# Versi
versi_skill = wajib(re.search(r'(?m)^\s+version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?\s*$', metadata),
                    "Tambahkan metadata.version tiga bagian di SKILL.md").group(1)
versi_changelog = wajib(re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)", CHANGELOG),
                        "Tambahkan judul versi di CHANGELOG.md").group(1)
semua_versi = {versi_skill, versi_changelog, str(PLUGIN.get("version")), str(CURSOR.get("version"))}
if len(semua_versi) != 1:
    sys.exit(f"Pakai satu versi di semua berkas: {sorted(semua_versi)}")

# Satu berkas skill saja
# .claude/ berisi worktree sesi agen, yang punya salinan repo sendiri.
berkas_skill = {p.relative_to(AKAR) for p in AKAR.rglob("SKILL.md")
                if not {".git", ".claude"} & set(p.relative_to(AKAR).parts)}
if berkas_skill != {SKILL_PATH.relative_to(AKAR)}:
    sys.exit(f"Simpan satu SKILL.md di skills/lugas: {sorted(map(str, berkas_skill))}")

# Deskripsi
deskripsi_skill = " ".join(wajib(re.search(r"(?m)^description: \|\n((?:  .*\n)+)", metadata + "\n"),
                                 "Tulis deskripsi SKILL.md sebagai blok berindentasi").group(1).split())
semua_deskripsi = {str(PLUGIN.get("description")), str(CURSOR.get("description")),
                   *(str(p.get("description")) for p in MARKETPLACE.get("plugins", []))}
if len(semua_deskripsi) != 1 or not deskripsi_skill.startswith(next(iter(semua_deskripsi))):
    sys.exit(f"Pakai kalimat pertama deskripsi SKILL.md di semua manifest: {sorted(semua_deskripsi)}")

# Pola
pola_skill = {int(n): nama for n, nama in re.findall(r"(?m)^\*\*([0-9]+)\. (.+?)\.\*\*", SKILL)}
nomor = list(pola_skill)
jumlah = len(nomor)
if jumlah == 0 or nomor != list(range(1, jumlah + 1)):
    sys.exit(f"Nomori pola di SKILL.md dari 1 tanpa lompatan: {nomor}")

pola_readme = {int(n): nama for n, nama in re.findall(r"(?m)^\| ([0-9]+) \| (.+?) \|", README)}
if sorted(pola_readme) != nomor:
    sys.exit(f"Daftarkan pola 1 sampai {jumlah} sekali di tabel README: {sorted(pola_readme)}")
beda = [f"{n}: {pola_readme[n]!r} seharusnya {nama!r}" for n, nama in pola_skill.items() if pola_readme[n] != nama]
if beda:
    sys.exit("Samakan nama pola di README dengan SKILL.md: " + "; ".join(beda))
if f"## {jumlah} pola" not in README:
    sys.exit(f"Beri judul bagian pola di README '## {jumlah} pola'")

nomor_pemeriksa = {int(n) for n in re.findall(r"(?m)^\s+\(([0-9]+), \"", PERIKSA)}
di_luar = sorted(n for n in nomor_pemeriksa if n not in pola_skill)
if di_luar:
    sys.exit(f"periksa.py memakai nomor pola yang tidak ada di SKILL.md: {di_luar}")

kata = len(SKILL.split())
if kata > 5500:
    sys.exit(f"Batasi SKILL.md paling banyak 5.500 kata; sekarang {kata}")

print(f"Paket Lugas v{versi_skill} valid: {jumlah} pola, {kata} kata di SKILL.md")
