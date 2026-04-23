buku = [
    {"judul":"Algoritma","penulis":"Andi","tahun":2019},
    {"judul":"Struktur Data","penulis":"Budi","tahun":2021},
    {"judul":"Basis Data","penulis":"Citra","tahun":2018},
    {"judul":"Pemrograman Python","penulis":"Deni","tahun":2022},
    {"judul":"Jaringan Komputer","penulis":"Andi","tahun":2020}
]

def tampilkan_data():
    print("=====DATA BUKU=====")
    print("No | Judul | Penulis | Tahun ")
    print("+--+-------+---------+------+")
    for i, data in enumerate(buku):
        print(f"{i+1} | {data["judul"]} | {data["penulis"]} | {data["tahun"]}")

def filter_buku():
    print("Buku Yang Terbit Di Atas Tahun 2020")
    status =[data for data in buku if data["tahun"]>= 2020]
    status.sort(key=lambda x: x["judul"])
    
    for i, data in enumerate(status):
        print(f"{i+1}. {data["judul"]} | {data["penulis"]} | {data["tahun"]}")
    print("jumlah buku yang terbit di atas tahun 2020 adalah: ", len(status))

tampilkan_data()
filter_buku()
