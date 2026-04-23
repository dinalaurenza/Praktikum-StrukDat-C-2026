def filter_harga(harga):
    if harga <= batas_bawah and harga >= batas_atas:
        print()
        return None

stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
]

batas_bawah= input("batas bawah ")
batas_atas= input("batas atas ") 

