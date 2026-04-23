data_mahasiswa = [
{"nim":"101","nama":"Rina","nilai":80},
{"nim":"102","nama":"Budi","nilai":60},
{"nim":"103","nama":"Citra","nilai":75},
{"nim":"104","nama":"Doni","nilai":55}
]


def tampilkan_mahasiswa():
    print("=====Data Mahasiswa=====")
    print("No | NIM | Nama | Nilai ")
    print("+--+-----+------+------+")
    for i, data in enumerate (data_mahasiswa):
        print(f"{i+1}. | {data["nim"]} | {data["nama"]} | {data["nilai"]}")

def status_mahasiswa():
    print("=====Status Mahasiswa=====")
    print("No | NIM | Nama | Nilai |status ")
    print("+--+-----+------+-------+------+")
    for i, data in enumerate (data_mahasiswa):
         status = "Lulus" if data["nilai"] >= 70 else "Tidak Lulus"
         print(f"{i+1}. | {data["nim"]} | {data["nama"]} | {data["nilai"]} | {status}")

def mahasiswa_lulus():
    print("=====Mahasiswa Lulus=====")
    lulus = [data["nama"] for data in data_mahasiswa if data["nilai"] >= 70]
    lulus.sort()
    for i, data in enumerate (lulus):
        print(f"{i+1}. {data}")

tampilkan_mahasiswa()
status_mahasiswa()
mahasiswa_lulus()