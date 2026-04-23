class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class AntrianPasien:
    def __init__(self):
        self.head = None

    def tambah(self,data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node_baru

    def tampil(self):
         temp = self.head
         while temp:
            print(temp.data)
            temp = temp.next

        
antrian = AntrianPasien()

antrian.tambah("pasien 1")
antrian.tambah("pasien 2")
antrian.tambah("pasien 3")
antrian.tampil()