class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f'Inserido: {key}')
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                print(f'Inserido: {key} à esquerda de {current.key}')
            else:
                self._insert_rec(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
                print(f'Inserido: {key} à direita de {current.key}')
            else:
                self._insert_rec(current.right, key)
        else:
            print(f'Chave {key} já existe na árvore.')

    def inorder_traversal(self):
        elements = []
        self._inorder_rec(self.root, elements)
        return elements

    def _inorder_rec(self, current, elements):
        if current:
            self._inorder_rec(current.left, elements)
            elements.append(current.key)
            self._inorder_rec(current.right, elements)

    def remove(self, key):
        self.root, deleted = self._remove_rec(self.root, key)
        if deleted:
            print(f'Removido: {key}')
        else:
            print(f'Chave {key} não encontrada na árvore.')

    def _remove_rec(self, current, key):
        if current is None:
            return current, False

        deleted = False
        if key < current.key:
            current.left, deleted = self._remove_rec(current.left, key)
        elif key > current.key:
            current.right, deleted = self._remove_rec(current.right, key)
        else:
            deleted = True
            if current.left is None:
                temp = current.right
                return temp, deleted
            elif current.right is None:
                temp = current.left
                return temp, deleted
            else:
                successor = self._min_value_node(current.right)
                current.key = successor.key
                current.right, _ = self._remove_rec(current.right, successor.key)
        return current, deleted

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# Criação da árvore de busca binária
bst = BinarySearchTree()

# Inserção dos códigos iniciais
codigos_iniciais = [45, 25, 65, 20, 30, 60, 70]
for codigo in codigos_iniciais:
    bst.insert(codigo)

# Exibição da árvore em ordem crescente
print("Árvore em ordem crescente:")
print(bst.inorder_traversal())

# Remoção do código 20 (nó folha)
bst.remove(20)
print("Árvore após remover 20:")
print(bst.inorder_traversal())

# Remoção do código 25 (nó com um filho)
bst.remove(25)
print("Árvore após remover 25:")
print(bst.inorder_traversal())

# Remoção do código 45 (nó com dois filhos)
bst.remove(45)
print("Árvore após remover 45:")
print(bst.inorder_traversal())
