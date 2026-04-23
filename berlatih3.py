class pasien:
    jumlah_pasien = 0
    
    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit
        
        pasien.jumlah_pasien +=1
    
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama
 
    def get_penyakit(self):
        return self.__penyakit

    def tampilkan_info(self):
        print("ID      :", self.__id)
        print("Nama    :", self.__nama)
        print("Penyakit:", self.__penyakit)

    def hitung_pasien():
        return pasien.jumlah_pasien
    
class PasienPrioritas(pasien):

    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)

        if self.prioritas == "Darurat":
            print("** Segera tangani! **")

pasien1 = pasien("P001", "Andi", "Flu")
pasien2 = PasienPrioritas("P002", "Budi", "Tifus", "Darurat")

pasien1.tampilkan_info()
print()
pasien2.tampilkan_info()

print("\nTotal pasien terdaftar:", pasien.hitung_pasien())
    

