class kendaraan:
    jumlah = 0
    
    def __init__(self, merk,  tahun):
        self.__merk = merk
        self.__tahun = tahun

    def get_merk(self):
        return self.__merk
    
    def get_tahun(self):
        return self.__tahun
    
    def info(self):
        print("merk: " ,self.__merk)
        print("tahun: ",self.__tahun)

    def hitung_kendaraan():
        return kendaraan.jumlah
    
class kendaraan_warna(kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun)
        self.warna = warna

    def tampilkan_info(self):
        super().info()
        print("warna: ", self.warna)

        if self.warna == "putih":
            print("warna terang!")

kendaraan1 = kendaraan("fortuner", 2006)
kendaraan1.get_merk()
kendaraan1.info()

kendaraan2 = kendaraan_warna("kijang", 2003, "putih")
kendaraan2.tampilkan_info()
    