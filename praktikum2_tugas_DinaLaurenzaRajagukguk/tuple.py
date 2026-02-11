#PYTHON TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#length tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#type tuple
thistuple = ("apple",)
print(type(thistuple))

#Acces Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#sama dengan penjelasan list
 #negative indexing
thistuple = ["apple", "banana", "cherry"]#Mengakses data dari belakang list. 
print(thistuple[-1])#Untuk mengambil item terakhir, kedua terakhir, dan seterusnya.
  #Range of Indexes
thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]#Mengambil sebagian data (potongan list).
print(thistuple[2:5])#Untuk memproses data dalam rentang tertentu saja.
thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[:4])#Dimulai dari awal sampai batasan tertentu.
thistuple = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[2:])#Dimulai dari batasan tertentu sampai akhir.
  #Range of Negative Indexes
thistuple= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thistuple[-4:-1])#Untuk memproses data dalam rentang tertentu saja dalam negative (dari akhir).

#UPDATE TUPLE
#change tuple value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#use del
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#UNPACKING TUPLE
#using asterisk
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#LOOP TUPLE
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#JOIN TUPLE
#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


