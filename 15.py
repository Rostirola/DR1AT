class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def inserir(root, valor):
    if root is None:
        return Node(valor)
    if valor < root.valor:
        root.esquerda = inserir(root.esquerda, valor)
    else:
        root.direita = inserir(root.direita, valor)
    return root


def encontrar_minimo(root):
    if root is None:
        return None
    while root.esquerda:
        root = root.esquerda
    return root.valor


def encontrar_maximo(root):
    if root is None:
        return None
    while root.direita:
        root = root.direita
    return root.valor


def em_ordem(root):
    if root:
        em_ordem(root.esquerda)
        print(root.valor, end=' ')
        em_ordem(root.direita)


def main():
    notas = [85, 70, 95, 60, 75, 90, 100]
    raiz = None
    for nota in notas:
        raiz = inserir(raiz, nota)

    print("Árvore em ordem:")
    em_ordem(raiz)
    print("\n")

    minimo = encontrar_minimo(raiz)
    maximo = encontrar_maximo(raiz)
    print(f"Nota Mínima: {minimo}")
    print(f"Nota Máxima: {maximo}")


if __name__ == "__main__":
    main()
    