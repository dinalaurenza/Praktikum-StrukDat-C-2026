#PYTHON DICTIONARY
#Setiap key unik dan digunakan untuk mengakses value.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#dictionary items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #Mengambil nilai berdasarkan key.
#duplicate no allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #Menunjukkan bahwa key tidak boleh sama.
#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #Python mengubah pasangan parameter menjadi key:value.

#ACCES ITEMS
#Get Keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys() #Mengambil semua key.
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#Get Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values() #Mengambil semua value.
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#Get Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items() #Mengambil pasangan (key, value).
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} #Mengecek apakah suatu key ada di dictionary.
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#CHANGE ITEMS
#update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) #Mengubah nilai berdasarkan key.

#REMOVE ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #Menghapus item berdasarkan key.
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #Menghapus item terakhir yang ditambahkan.
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #Menghapus semua data.
print(thisdict)

#LOOP DICTIONARY
for x in thisdict:
  print(thisdict[x]) #Mengakses semua value lewat key.

for x in thisdict.values():
  print(x) #Mengakses semua value.

for x in thisdict.keys():
  print(x) #Mengakses semua key.

for x, y in thisdict.items():
  print(x, y) #Mengakses key dan value sekaligus.

#COPY DICTIONARY
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #Menyalin dictionary agar data asli aman.
print(mydict)

#NESTED DICTIONARY
#Menyimpan dictionary di dalam dictionary.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} #Setiap key menyimpan dictionary lain sebagai value.