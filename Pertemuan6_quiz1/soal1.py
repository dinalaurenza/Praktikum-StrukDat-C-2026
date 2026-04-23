def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("error")
        return None
    
    if len(sn)< 5:
        print("error")
        return None
    return{
    "merk": merk,
    "tipe": tipe,
    "harga":harga,
    "sn":sn,
    "status":"tersedia"
    }
inventaris = []

for i in range(3):
    merk= input("input merk "),
    tipe= input("input tipe"),
    harga= input("input harga"),
    sn= input("input sn"),
  
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget:
        inventaris.append(gadget)
    else:
        print("registrasi gagal ")

for item in inventaris:
    print(item)



