angka = [1,2,3,4]
for i in range (len(angka)):
    angka[i] *= 2
angka.insert(2,10)
angka.pop(4)

x = angka[:3]
x.append(9)

print(angka)
print(x)
print(len(x))