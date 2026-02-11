stoklist = [15, 50, 30, 25, 40]

stoklist.append(100)
print(stoklist)

stoklist.insert(2, 75)
print(stoklist)

stoklist.sort()
print(stoklist)

jumlah_stok=len(stoklist)
rata= sum(stoklist) // jumlah_stok
print("rata rata adalah: ", rata)



