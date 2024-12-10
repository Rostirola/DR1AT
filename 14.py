class Node:
    def __init__(self, key):
        self.key = key      # Preço do produto
        self.left = None    # Filho à esquerda
        self.right = None   # Filho à direita

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Raiz da árvore

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f"Inserido {key} como raiz da árvore.")
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
                print(f"Inserido {key} à esquerda de {current_node.key}.")
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
                print(f"Inserido {key} à direita de {current_node.key}.")
            else:
                self._insert_recursive(current_node.right, key)
        else:
            print(f"Chave {key} já existe na árvore. Duplicatas não são permitidas.")

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            print(f"Chave {key} não encontrada na árvore.")
            return False
        if key == current_node.key:
            print(f"Chave {key} encontrada na árvore.")
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

# Inicialização da árvore
bst = BinarySearchTree()

# Lista de preços a serem inseridos
precos = [100, 50, 150, 30, 70, 130, 170]

# Inserção dos preços na árvore
for preco in precos:
    bst.insert(preco)

# Busca pelo preço 70
resultado = bst.search(70)
if resultado:
    print("O preço 70 está disponível.")
else:
    print("O preço 70 não está disponível.")

# Definição das classes Node e BinarySearchTree (conforme implementadas acima)

# Inicialização da árvore
bst = BinarySearchTree()

# Lista de preços a serem inseridos
precos = [100, 50, 150, 30, 70, 130, 170]

# Inserção dos preços na árvore
for preco in precos:
    bst.insert(preco)

# Busca pelo preço 70
resultado = bst.search(70)
if resultado:
    print("O preço 70 está disponível.")
else:
    print("O preço 70 não está disponível.")
