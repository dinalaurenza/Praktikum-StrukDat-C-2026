pasien_hari_ini = [
{"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
{"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
{"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Maag",   "bayar": False},
{"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
{"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
{"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

def tampilkan_pasien():
    print("=====DATA PASIEN KLINIK=====")
    print("No | ID | Nama | Usia | Penyakit | Status Bayar")
    print("---+----+------+------+----------+-------------+")

    for i, data in enumerate(pasien_hari_ini):
        status= "Lunas" if data["bayar"] else "Belum Bayar"
        print(f"{i+1}. | {data["id"]} | {data["nama"]} | {data["usia"]} | {data["penyakit"]} | {status}")

def filter_belum_bayar():
    print("===== PASIEN BELUM BAYAR =====")
    belum_bayar = [data["nama"] for data in pasien_hari_ini if not data["bayar"]]
    belum_bayar.sort()

    for i, nama in enumerate(belum_bayar):
        print(f"{i+1}. {nama}")
    print(f"Total belum bayar: {len(belum_bayar)} pasien")

def info_klinik():
    klinik = (
        "Klinik Sehat Bersama",
        "Jl. Merdeka No. 10, Pekanbaru",
        "0761-12345"
    )
    print("info klinik: ")
    print("nama : ", klinik[0])
    print("alamat : ", klinik[1])
    print("telp : ", klinik[2])

def rekap_penyakit():
    penyakit_unik = {data["penyakit"] for data in pasien_hari_ini}
    print("jenis penyakit unik: ", penyakit_unik)
    print("jumlah jenis penyakit: ", len(penyakit_unik))

    rekap={}
    for penyakit in penyakit_unik:
        jumlah = sum(1 for data in pasien_hari_ini if data["penyakit"]== penyakit)
        rekap[penyakit]= jumlah
        print("rekap per penyakit: ")
        for penyakit, pasien in rekap.items():
            print(f"{penyakit} : {pasien} pasien")

        maksimal = max(rekap.values())
        terbanyak = [penyakit for penyakit, pasien in rekap.items() if pasien == maksimal]

    print("Penyakit terbanyak:", ", ".join(terbanyak), f"({max} pasien)")

tampilkan_pasien()
filter_belum_bayar()
info_klinik()
rekap_penyakit()
