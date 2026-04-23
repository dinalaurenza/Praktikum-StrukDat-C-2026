#soal 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Tambah kendaraan ke akhir
    def tambah_kendaraan(self, plat):
        node_baru = Node(plat)

        if self.head is None:
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru

    # Tampilkan dari depan ke belakang
    def tampilkan_maju(self):
        print("[Maju]")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Tampilkan dari belakang ke depan
    def tampilkan_mundur(self):
        print("[Mundur]")
        temp = self.tail
        while temp:
            print(temp.data)
            temp = temp.prev
#soal 2
    # Hapus kendaraan berdasarkan plat
    def hapus_kendaraan(self, plat):
        temp = self.head

        while temp:
            if temp.data == plat:

                # Jika node adalah head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                # Jika node adalah tail
                elif temp.next is None:
                    self.tail = temp.prev
                    self.tail.next = None

                # Jika node di tengah
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                print(f"{plat} berhasil dihapus")
                return

            temp = temp.next

        print(f"{plat} tidak ditemukan")
mobil = DoubleLinkedList()
mobil.tambah_kendaraan("B 1234 ABC")
mobil.tambah_kendaraan("D 5678 XYZ")
mobil.tambah_kendaraan("A 9999 TUV")
mobil.tampilkan_maju()
mobil.tampilkan_mundur()


mobill = DoubleLinkedList()
mobill.tambah_kendaraan("B 1111 AA")
mobill.tambah_kendaraan("D 2222 BB")
mobill.tambah_kendaraan("A 3333 CC")
mobill.tambah_kendaraan("B 4444 DD")
print("Sebelum:")
mobill.tampilkan_maju()
mobill.hapus_kendaraan("A 3333 CC")
print("Sesudah:")
mobill.tampilkan_maju()
#soal 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Tambah petugas
    def tambah_petugas(self, nama):
        node_baru = Node(nama)

        if self.head is None:
            self.head = node_baru
            node_baru.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = node_baru
            node_baru.next = self.head

    # Simulasi giliran
    def giliran_berikutnya(self, n):
        if self.head is None:
            print("Tidak ada petugas")
            return

        current = self.head

        for i in range(1, n + 1):
            print(f"Giliran {i}: {current.data}")
            current = current.next

petugas = CircularLinkedList()

petugas.tambah_petugas("Andi")
petugas.tambah_petugas("Budi")
petugas.tambah_petugas("Citra")
petugas.tambah_petugas("Dewi")

petugas.giliran_berikutnya(6)
