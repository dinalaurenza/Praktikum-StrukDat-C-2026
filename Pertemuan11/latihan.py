class Node:
  def __init__(self, nama, keluhan):
    self.data = [nama , keluhan]
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
       self.rear = None
    return temp.data

  def peek(self):
    if self.isEmpty():
      return "YA, antrian masih kosong"
    return self.front.data

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.front
    posisi = 1
    while temp:
      print(f"{posisi} Nama: {temp.data[0]} | Keluhan: {temp.data[1]}")
      temp = temp.next
      posisi +=1

  def clear(self):
    self.front = None
    self.rear = None
    self.length = 0
myQueue = Queue()

print("===========================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("===========================")

print("Apakah antrian kosong?  ", myQueue.peek())

myQueue.enqueue("Budi", "Demam Tinggi")
myQueue.enqueue("Ani", "Batuk Pilek")
myQueue.enqueue("Citra", "Sakit Kepala")

print("Jumlah pasien menunggu: ", myQueue.size())
print("Pasien berikutnya: ", myQueue.peek())
print("Dokter memanggil: ", myQueue.dequeue())

myQueue.enqueue("Dodi", "Nyeri Perut")

print("ANTRIAN SAAT INI")
myQueue.printQueue()
print("Dokter memanggil: ", myQueue.dequeue())
print("Jumlah pasien menunggu: ", myQueue.size())
print("Sesi poliklinik selesai. Antrian dikosongkan.")

myQueue.clear()

status_akhir = "YA, antrian sudah kosong." if myQueue.isEmpty() else "TIDAK"
print(f"[CEK] Apakah antrian kosong? {status_akhir}")


