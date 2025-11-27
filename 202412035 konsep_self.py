class MataKuliah:

    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    # (a) Method baru
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# (b) Buat 2 mata kuliah dan 3 mahasiswa
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI202", "Struktur Data")

m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Daftarkan mahasiswa ke masing-masing mata kuliah
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)

mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)

# (c) Tampilkan daftar mahasiswa + jumlahnya
print("=== Mata Kuliah 1 ===")
print("Daftar Mahasiswa:", mk1.daftar_mahasiswa())
print("Jumlah Mahasiswa:", mk1.jumlah_mahasiswa())

print("\n=== Mata Kuliah 2 ===")
print("Daftar Mahasiswa:", mk2.daftar_mahasiswa())
print("Jumlah Mahasiswa:", mk2.jumlah_mahasiswa())