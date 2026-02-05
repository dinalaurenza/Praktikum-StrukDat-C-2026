barang = ("B001", "Laptop Gaming", 15000000)

print("harga barang: ", barang[2])

# barang.insert(2, 140000000)
# print(barang)
# tidak bisa diubah, dikarenakan tuple bersifat unchangeable atau value (nilai) tidak dapat diubah

(green, yellow, red) = barang

print("kode: ",green)
print("nama: ",yellow)
print("harga: ",red)