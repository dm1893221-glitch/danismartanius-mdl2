class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode              # public
        self._ketua = ketua           # protected
        self.__anggaran = 500000000   # private

    # Getter/Setter untuk Protected (_ketua)
    def get_ketua(self):
        return self._ketua
    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    # Getter/Setter untuk Private (__anggaran)
    def get_anggaran(self):
        return self.__anggaran
    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran

# a. CLASS MAHASISWA (Implementasi Permintaan)
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        # Public Attributes
        self.nim = nim
        self.nama = nama
        # Protected Attribute
        self._semester = semester
        # Private Attribute
        self.__ipk = ipk

    # Getter untuk Protected (_semester)
    def get_semester(self):
        return self._semester

    # Setter untuk Protected (_semester)
    def set_semester(self, new_semester):
        if new_semester > 0:
            self._semester = new_semester
        else:
            raise ValueError("Semester harus positif.")

    # Getter untuk Private (__ipk)
    def get_ipk(self):
        return self.__ipk

    # Setter untuk Private (__ipk)
    def set_ipk(self, new_ipk):
        # Validasi ketat untuk IPK
        if 0.0 <= new_ipk <= 4.0:
            self.__ipk = new_ipk
        else:
            raise ValueError("IPK harus antara 0.0 dan 4.0.")


if __name__ == "__main__":
    
    # Contoh penggunaan ProgramStudi (sesuai kode awal)
    ps = ProgramStudi("TI", "Pak Wayan")
    print("--- DEMONSTRASI CLASS PROGRAM STUDI ---")
    print("Anggaran Tersisa (Awal):", ps.get_anggaran())
    ps.kurangi_anggaran(10000000)
    print("Anggaran Tersisa (Akhir):", ps.get_anggaran())
    print("-" * 40)
    
    # b. Buat objek 2 Mahasiswa
    mhs1 = Mahasiswa("2021001", "Andi", 2, 3.85)
    mhs2 = Mahasiswa("2021002", "Budi", 4, 3.20)
    
    print("\n--- DEMONSTRASI CLASS MAHASISWA ---")

    # Tampilkan: nim, nama, semester dan IPK (Data Awal)
    print("\n[Data Awal Mahasiswa 1]")
    print(f"NIM (Public): {mhs1.nim}")
    print(f"Nama (Public): {mhs1.nama}")
    print(f"Semester (Protected): {mhs1.get_semester()}")
    print(f"IPK (Private): {mhs1.get_ipk()}")

    print("\n[Data Awal Mahasiswa 2]")
    print(f"NIM (Public): {mhs2.nim}")
    print(f"Nama (Public): {mhs2.nama}")
    print(f"Semester (Protected): {mhs2.get_semester()}")
    print(f"IPK (Private): {mhs2.get_ipk()}")

    # c. Ganti semester dan IPK
    print("\n[Mengganti Data Mahasiswa 1]")
    
    # Ganti semester (Protected) - Menggunakan Setter
    mhs1.set_semester(3) 
    
    # Ganti IPK (Private) - Menggunakan Setter
    mhs1.set_ipk(3.95) 
    
    print("Mahasiswa 1 setelah diganti:")
    print(f"Semester Baru: {mhs1.get_semester()}")
    print(f"IPK Baru: {mhs1.get_ipk()}")

    print("\n[Mengganti Data Mahasiswa 2]")
    mhs2.set_semester(5) 
    mhs2.set_ipk(3.40) 
    
    print("Mahasiswa 2 setelah diganti:")
    print(f"Semester Baru: {mhs2.get_semester()}")
    print(f"IPK Baru: {mhs2.get_ipk()}")