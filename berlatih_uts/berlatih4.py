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


# === VARIABEL GLOBAL ===
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]


# === BAGIAN A ===

def tebak_angka(angka_rahasia, maks_percobaan):
    """Meminta pemain menebak angka sampai benar atau percobaan habis."""
    
    sisa_percobaan = maks_percobaan
    
    while sisa_percobaan > 0:
        tebakan = int(input("Masukkan tebakan: "))
        
        if tebakan < angka_rahasia:
            print("Terlalu kecil")
        elif tebakan > angka_rahasia:
            print("Terlalu besar")
        else:
            print("Benar!")
            return True, sisa_percobaan
        
        sisa_percobaan -= 1
        print("Sisa percobaan:", sisa_percobaan)
    
    print("Percobaan habis!")
    return False, 0


def hitung_skor(berhasil, sisa_percobaan):
    """Menghitung skor berdasarkan sisa percobaan."""
    
    if berhasil:
        return sisa_percobaan * 10
    else:
        return 0


def main_satu_ronde(nama, nomor_ronde):
    """Menjalankan satu ronde permainan dan mengembalikan data skor."""
    
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde % len(DAFTAR_ANGKA)]
    
    print("\n=== Ronde", nomor_ronde + 1, "===")
    
    berhasil, sisa = tebak_angka(angka_rahasia, 7)
    
    skor = hitung_skor(berhasil, sisa)
    
    print("Skor ronde ini:", skor)
    
    return [nama, skor]


# === BAGIAN B ===

def tampilkan_riwayat(riwayat):
    """Menampilkan seluruh riwayat permainan dalam bentuk tabel."""
    
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
        return
    
    print("\n=== RIWAYAT PERMAINAN ===")
    print("No\tNama\tSkor")
    
    for i in range(len(riwayat)):
        print(i+1, "\t", riwayat[i][0], "\t", riwayat[i][1])


# === BAGIAN C ===

def selection_sort_riwayat(riwayat):
    """Mengurutkan riwayat skor dari terbesar ke terkecil dengan Selection Sort."""
    
    salinan = riwayat.copy()
    n = len(salinan)
    
    for i in range(n-1):
        max_index = i
        
        for j in range(i+1, n):
            if salinan[j][1] > salinan[max_index][1]:
                max_index = j
        
        salinan[i], salinan[max_index] = salinan[max_index], salinan[i]
    
    return salinan


def tampilkan_leaderboard(riwayat):
    """Menampilkan leaderboard berdasarkan skor tertinggi."""
    
    if len(riwayat) == 0:
        print("Belum ada data leaderboard.")
        return
    
    data_urut = selection_sort_riwayat(riwayat)
    
    print("\n=== LEADERBOARD ===")
    
    for i in range(len(data_urut)):
        nama = data_urut[i][0]
        skor = data_urut[i][1]
        
        if i == 0:
            print(i+1, ".", nama, "-", skor, "*")
        else:
            print(i+1, ".", nama, "-", skor)


# === PROGRAM UTAMA ===

riwayat = []

nama = input("Masukkan nama pemain: ")

nomor_ronde = 0

while True:
    
    hasil = main_satu_ronde(nama, nomor_ronde)
    riwayat.append(hasil)
    
    nomor_ronde += 1
    
    lagi = input("Main lagi? (y/n): ")
    
    if lagi.lower() != "y":
        break


tampilkan_riwayat(riwayat)
tampilkan_leaderboard(riwayat)