class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root =Node("A")
        self.root.left= Node("B")
        self.root.right= Node("C")
        self.root.left.left= Node("D")
        self.root.left.right= Node("E")
        self.root.right.right= Node("F")

    def preorder(self, node):
        if node is not None:
            print(node.data, end= " ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end= " ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def get_leaf_nodes(self, node, leaf_list):
       if node:
        if node.left is None and node.right is None:
            leaf_list.append(node.data)
        self.get_leaf_nodes(node.left, leaf_list)
        self.get_leaf_nodes(node.right, leaf_list)
        return leaf_list

tree= Binary_Tree()
tree.insert_manual()
print("SISTEM AUDIT DISTRIBUSI CEPAT SAMPAI")
print("====================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")
print("HASIL AUDIT")
print("1. Pre-Order : ", end="")
tree.preorder(tree.root)
print()

print("2. In-Order : ", end="")
tree.inorder(tree.root)
print()

print("3. Post-Order : ", end="")
tree.postorder(tree.root)
print()

leaves = []
tree.get_leaf_nodes(tree.root, leaves)

print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaves))
print("=" * 50)
print("Audit Selesai!")