# File: relasi_extended.py

class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # f. Tambahkan method rata_rata()
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        total_skor = sum(n.skor for n in self.daftar_nilai)
        return total_skor / len(self.daftar_nilai)

class Matakuliah:
    def __init__(self, kode: str, nama:str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = [] # agregasi

    def tambah_matakuliah(self, mk: Matakuliah):
        self.daftar_matakuliah.append(mk)

class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

# Fungsi report_program (tidak diubah)
def report_program(prodi: ProgramStudi, semua_mahasiswa: list['Mahasiswa']):
    print(f"\n========================================")
    print(f"LAPORAN PROGRAM STUDI: {prodi.nama}")
    print("========================================")
    print("Daftar Matakuliah:")
    print("->", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "Tidak ada Matakuliah")
    
    print("\nMahasiswa dan rata-rata nilai Matakuliah di Prodi ini:")
    for m in semua_mahasiswa:
        # Filter nilai yang relevan dengan matakuliah di Prodi ini
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        
        # Hitung rata-rata hanya dari nilai yang relevan
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"-> {m.nim} - {m.nama}: {round(avg, 2)}")
        else:
            print(f"-> {m.nim} - {m.nama}: Tidak ada nilai yang relevan.")
    print("-" * 40)


if __name__ == "__main__":
    uni = Universitas("Universitas A")
    
    # Program Studi Awal
    prodi_ti = uni.buat_program("Teknik Informatika")
    
    # a. Tambahkan 2 Program Studi baru
    prodi_el = uni.buat_program("Teknik Elektro")
    prodi_si = uni.buat_program("Sistem Informasi")
    
    # Matakuliah Prodi TI (Awal)
    mk_ti1 = Matakuliah("TI101", "Pemrograman Dasar")
    mk_ti2 = Matakuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk_ti1)
    prodi_ti.tambah_matakuliah(mk_ti2)
    
    # b. Tambahkan minimal 2 Mata Kuliah untuk setiap Prodi baru
    mk_el1 = Matakuliah("EL201", "Rangkaian Listrik")
    mk_el2 = Matakuliah("EL202", "Elektronika Digital")
    prodi_el.tambah_matakuliah(mk_el1)
    prodi_el.tambah_matakuliah(mk_el2)
    
    mk_si1 = Matakuliah("SI301", "Basis Data")
    mk_si2 = Matakuliah("SI302", "Analisis Sistem")
    prodi_si.tambah_matakuliah(mk_si1)
    prodi_si.tambah_matakuliah(mk_si2)
    
    # c. Buat 3 Mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Dian") # Mahasiswa baru
    
    # Tambahkan objek Nilai ke mahasiswa
    # Nilai M1
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m1.tambah_nilai(Nilai("EL201", 90)) # Nilai lintas prodi
    
    # Nilai M2
    m2.tambah_nilai(Nilai("TI101", 90))
    m2.tambah_nilai(Nilai("SI301", 70))
    
    # Nilai M3 (Mahasiswa baru)
    m3.tambah_nilai(Nilai("EL202", 75))
    m3.tambah_nilai(Nilai("SI302", 82))
    
    semua_mahasiswa = [m1, m2, m3]

    # d. Tampilkan daftar mata kuliah dari setiap Program Studi.
    print("\n--- d. DAFTAR MATA KULIAH SETIAP PROGRAM STUDI ---")
    semua_prodi = uni.programs
    for prodi in semua_prodi:
        mk_list = ", ".join([mk.nama for mk in prodi.daftar_matakuliah])
        print(f"[{prodi.nama}]: {mk_list}")

    # e. Tampilkan daftar nilai untuk setiap mahasiswa.
    print("\n--- e. DAFTAR NILAI SETIAP MAHASISWA ---")
    for m in semua_mahasiswa:
        nilai_str = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai])
        print(f"[{m.nim} - {m.nama}]: {nilai_str if nilai_str else 'Belum ada nilai'}")

    # f. Tampilkan rata-rata nilai setiap mahasiswa.
    print("\n--- f. RATA-RATA NILAI KESELURUHAN MAHASISWA ---")
    for m in semua_mahasiswa:
        print(f"-> {m.nama} (Total Rata-rata): {round(m.rata_rata(), 2)}")
        
    # g. Panggil fungsi report_program untuk setiap Program Studi.
    print("\n--- g. LAPORAN NILAI MAHASISWA PER PROGRAM STUDI ---")
    for prodi in semua_prodi:
        report_program(prodi, semua_mahasiswa)