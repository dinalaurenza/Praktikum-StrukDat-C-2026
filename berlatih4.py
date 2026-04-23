mahasiswa = [
    {"nama": "Andi", "prodi": "Informatika", "nilai": 85},
    {"nama": "Budi", "prodi": "Sistem Informasi", "nilai": 70},
    {"nama": "Citra", "prodi": "Informatika", "nilai": 90},
    {"nama": "Deni", "prodi": "Informatika", "nilai": 60},
    {"nama": "Eka", "prodi": "Sistem Informasi", "nilai": 88}
]

def tampilkan_mahasiswa():
    print("=======DATA DAN NILAI MAHASISWA=======")
    print("No | Nama | Prodi | Nilai ")
    print("+--+------+-------+------+")

    for i, data in enumerate (mahasiswa):
        status = "lulus" if data["nilai"] >= 80 else "tidak lulus"
        print(f"{i+1}. | {data["nama"]} | {data["prodi"]} | {data["nilai"]} | {status}")

def filter_nilai():
    print("===== MAHASISWA YANG LULUS =====")
    lulus = [data["nama"] for data in mahasiswa if data ["nilai"] >= 80]
    lulus.sort()

    for i, nama in enumerate(lulus):
        print(f"{i+1}. {nama}")
    
tampilkan_mahasiswa()
filter_nilai()

