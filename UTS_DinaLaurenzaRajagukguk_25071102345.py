#SOAL 1
print("SOAL 1")
pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

def tampilkan_pengunjung():
    print("=====DATA PENGUNJUNG PERPUSTAKAAN=====")
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+----+------+------+----------+---------------")

    for i, data in enumerate(pengunjung_hari_ini):
        status = "Sudah Kembali" if data ["kembali"] == True else "Belum Kembali"
        print(f"{i+1}. | {data["id"]} | {data["nama"]} | {data["usia"]} | {data["kategori"]} | {status}")
     

def filter_belum_kembali():
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    for i, data in enumerate (pengunjung_hari_ini):
       Belum = [data["nama"] if data ["kembali"] == False else None]
       print(f"{i+1}. {Belum}") 
       print("Total belum Kembali: ", len(Belum))

tampilkan_pengunjung()
filter_belum_kembali()

#SOAL 2
print()
print("SOAL 2")
Perpustakaan = (
    "Perpustakaan Kampus Terpadu",
    "Jl. Pendidikan No. 5, Pekanbaru",
    0-761-54321
      )

def info_perpustakaan():
    print("info perpustakaan: ")
    print("Nama: ", Perpustakaan[0])
    print("Alamat: ", Perpustakaan[1])
    print("Telp: ", Perpustakaan[2])

def rekap_kategori():
    buku_unik= {data["kategori"] for data in pengunjung_hari_ini}
    print("jenis buku unik: ", buku_unik)
    print("jumlah jenis buku: ", len(buku_unik))

    rekap={}
    for buku in buku_unik:
        jumlah = sum(1 for data in pengunjung_hari_ini if data["kategori"] == buku)
        rekap["kategori"] = jumlah
        print("rekap per kategori: ")
        for kategori, pengunjung in rekap.items():
            print(f"{kategori} : {pengunjung} pengunjung")

        maksimal = max(rekap.values())
        terbanyak = [kategori for kategori, pengunjung in rekap.items() if pengunjung == maksimal]

    print("Kategori terbanyak:", ", ".join(terbanyak), f"({max} pengunjung)")


info_perpustakaan()
rekap_kategori()

#SOAL 3
print()
print("SOAL 3")


class pengunjung:
    jumlah = 0
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori

    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):
        print("ID: ", self.__id)
        print("Nama: ", self.__nama)
        print("Kategori: ", self.__kategori)

    def hitung_pengunjung():
        pengunjung.jumlah
        print("total pengunjung: ", pengunjung.jumlah)

class pengunjungPrioritas(pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.__prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas: ", self.__prioritas)

        if self.__prioritas == "Mendesak":
            print("** Layani segera! **")

    print("total pengunjung: ", pengunjung.jumlah)

pengunjung1 = pengunjung("M001", "Rina", "Fiksi")
pengunjung1.tampilkan_info()

pengunjung2 = pengunjungPrioritas("M007", "Gilang", "referensi", "Mendesak")
pengunjung2.tampilkan_info()

#SOAL 4
print()
print("SOAL 4")
# class Node:
#     def __init__(self, data)
#         self.__data = data
#         self.__next = Node

print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print("Total antrian: 2")








    