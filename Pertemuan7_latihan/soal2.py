class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traversalkendaraan(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")


def tambahkendaraan(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

def deletekendaraan(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node("D 2032 HFG")
node1 = tambahkendaraan(node1, newNode, 5)
print("after ditambah: ")
traversalkendaraan(node1)

node1 = deletekendaraan(node1, node2)
print("after dihapus: ")
traversalkendaraan(node1)


