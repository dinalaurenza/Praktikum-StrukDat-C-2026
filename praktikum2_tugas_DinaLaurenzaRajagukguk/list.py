#PYTHON LIST
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

  #list length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
  #list item
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
  #type list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#ACCESS ITEMS
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
   #negative indexing
thislist = ["apple", "banana", "cherry"]#Mengakses data dari belakang list. 
print(thislist[-1])#Untuk mengambil item terakhir, kedua terakhir, dan seterusnya.
  #Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]#Mengambil sebagian data (potongan list).
print(thislist[2:5])#Untuk memproses data dalam rentang tertentu saja.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#Dimulai dari awal sampai batasan tertentu.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#Dimulai dari batasan tertentu sampai akhir.
  #Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#Untuk memproses data dalam rentang tertentu saja dalam negative (dari akhir).

#CHANGE LIST ITEMS
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #Mengganti isi list pada posisi tertentu.
print(thislist) #Untuk memperbarui data.
  #Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Menambahkan data dalam batasan tertentu.
print(thislist)
  #Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Menambahkan data di posisi tertentu.
print(thislist) #Untuk menyisipkan data di tengah list.

#ADD LIST 
 #append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #Menambahkan data di bagian akhir list.
print(thislist) #Untuk menambah data baru.
 #insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #menyisipkan data pada posisi tertentu di dalam list.
print(thislist) #Untuk menambahkan item di tengah atau di posisi spesifik, bukan di akhir list.
 #extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #Menggabungkan dua list.
print(thislist) #Untuk menyatukan data dari beberapa sumber.
 #add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #menambahkan semua isi dari struktur data lain (yang bisa di-loop), ke dalam list.
print(thislist) #Untuk menggabungkan isi dari struktur data lain ke dalam list.

#REMOVE LIST
 #Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Menghapus item berdasarkan nilainya.
print(thislist) #Untuk menghilangkan data tertentu.
 #Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Menghapus item berdasarkan posisinya.
print(thislist) #Untuk menghapus data di index tertentu.
thislist = ["apple", "banana", "cherry"]
thislist.pop() #Menghapus item posisi terakhir.
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
 #Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear() #Menghapus semua isi list.
print(thislist) #Untuk mengosongkan data.

#LOOP LIST
 #Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
 #Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
 # While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  #Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
 #Dalam satu baris
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#SORT LIST
 #Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
 #Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
 #Customize Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
 #Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
 #reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#COPY LIST
 #Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#JOIN LIST
 #joi two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
 #