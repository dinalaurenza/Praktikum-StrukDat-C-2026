#PYTHON SET
thisset = {"apple", "banana", "cherry"}
print(thisset) #Membuat sebuah set berisi data unik (tanpa duplikat) dan menampilkannya.

#ACCES ITEM
thisset = {"apple", "banana", "cherry"}
for x in thisset: #Mengakses dan menampilkan semua item di dalam set.
  print(x)
#melakukan pengecekan melalui if
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) 

#ADD SET
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") ##Menambahkan satu item baru ke dalam set.
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #Menambahkan banyak item dari set lain ke dalam set utama.
print(thisset)

#REMOVE SET
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #Menghapus item tertentu dari set.
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #Menghapus item tanpa error meskipun item tidak ada.
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear() #Menghapus semua isi set (mengosongkan set).
print(thisset)

#LOOP SET
thisset = {"apple", "banana", "cherry"}
for x in thisset: #Menampilkan seluruh isi set satu per satu.
  print(x)

#JOIN SET 
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #Menggabungkan dua set menjadi satu set baru tanpa duplikat.
print(set3)
#bisa menggunakan tanda |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#bisa berbeda tipe data
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) #Menggabungkan lebih dari dua set sekaligus.
print(myset)
#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #Menambahkan isi set2 ke set1 secara langsung (mengubah set1).
print(set1)
#Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #Mengambil item yang sama di kedua set.
print(set3)
#bisa menggunakan tanda &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #Mengambil item yang hanya ada di set1, tapi tidak ada di set2
print(set3)
#bisa menggunakan tanda -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
#Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #Mengambil item yang tidak sama di kedua set.
print(set3)
#bia menggunakan tanda ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)