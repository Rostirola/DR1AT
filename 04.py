def busca_linear(lista, alvo):
    for indice, valor in enumerate(lista):
        if valor == alvo:
            return indice, indice + 1  # Retorna o índice e o número de iterações
    return -1, len(lista)  # ISBN não encontrado

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    iteracoes = 0

    while esquerda <= direita:
        iteracoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio, iteracoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, iteracoes  # ISBN não encontrado

import random

# Gerando uma lista ordenada de 100.000 ISBNs
lista_isbns = sorted(random.sample(range(1000000, 9999999), 100000))

# ISBN existente (por exemplo, o 50.000º elemento)
isbn_existe = lista_isbns[49999]

# ISBN inexistente
isbn_nao_existe = 99999999

# Teste com ISBN existente
indice_linear, iter_linear = busca_linear(lista_isbns, isbn_existe)
indice_binaria, iter_binaria = busca_binaria(lista_isbns, isbn_existe)

print(f"Busca Linear - ISBN existente: Índice = {indice_linear}, Iterações = {iter_linear}")
print(f"Busca Binária - ISBN existente: Índice = {indice_binaria}, Iterações = {iter_binaria}")

# Teste com ISBN inexistente
indice_linear, iter_linear = busca_linear(lista_isbns, isbn_nao_existe)
indice_binaria, iter_binaria = busca_binaria(lista_isbns, isbn_nao_existe)

print(f"Busca Linear - ISBN inexistente: Índice = {indice_linear}, Iterações = {iter_linear}")
print(f"Busca Binária - ISBN inexistente: Índice = {indice_binaria}, Iterações = {iter_binaria}")

isbn = 1234567
indice, iteracoes = busca_binaria(lista_isbns, isbn)
if indice != -1:
    print(f"ISBN {isbn} encontrado no índice {indice} em {iteracoes} iterações.")
else:
    print(f"ISBN {isbn} não encontrado após {iteracoes} iterações.")

def busca_linear(lista, alvo):
    for indice, valor in enumerate(lista):
        if valor == alvo:
            return indice, indice + 1  # Retorna o índice e o número de iterações
    return -1, len(lista)  # ISBN não encontrado
