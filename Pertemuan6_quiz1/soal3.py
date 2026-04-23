katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':2},
            {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ]

daftar_merk= set()

#prosedure update stok
def update_katalog(merk, tipe, sn, stok):
    update_katalog = {
        "merk":merk,
        "tipe":tipe,
        "sn":sn,
        "stok":stok
    }

update_katalog("realme", "C33","REAL33","4")
print(update_katalog)
    
