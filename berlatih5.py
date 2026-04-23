class produk:
    pajak = 0.1
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def get_harga(self):
        return self.__harga

    def diskon(harga):
        return harga + (harga* produk.pajak)
    
    def tampilkan(self):
        harga_pajak = produk.diskon(self.__harga)
        print("produk: ", self.__nama)
        print(harga_pajak)


p1 = produk("Laptop", 8000000)
p1.tampilkan()

    
        