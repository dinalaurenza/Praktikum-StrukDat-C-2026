plat_parkir = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
plat_genap = []
plat_ganjil = []
for plat in plat_parkir:
    nomor = plat.split () [1]
    if int (nomor) % 2 == 0:
        plat_genap.append (plat) 
        print("plat nomor genap: ", plat_genap )
    else:
        plat_ganjil.append (plat)
        print("plat nomor ganjil: ", plat_ganjil)
    
