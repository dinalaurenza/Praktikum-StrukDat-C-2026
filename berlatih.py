list_buku = []
while True:
    print("Masukkan data buku")
    penulis = input("nama penulis: ")
    judul = input("judul buku: ")

    buku_baru = [penulis, judul]
    list_buku.append(buku_baru)

    for index,buku in enumerate (list_buku):
        print(f"{index+1} penulis:{buku[0]} judul: {buku[1]} ")

    lanjut = input("apakah ingin dilanjutkan?(y/n) ")

    if lanjut == "n":
        break
    
