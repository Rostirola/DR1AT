def verificar_duplicatas(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False

# Exemplo de uso
lista_exemplo = [1, 2, 3, 4, 5, 3]
print(verificar_duplicatas(lista_exemplo))  # Saída: True

def verificar_duplicatas_otimizado(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

# Exemplo de uso
lista_exemplo = [1, 2, 3, 4, 5, 3]
print(verificar_duplicatas_otimizado(lista_exemplo))  # Saída: True

lista1 = ['maçã', 'banana', 'laranja', 'banana']
print(verificar_duplicatas_otimizado(lista1))  # Saída: True

lista2 = [10, 20, 30, 40, 50]
print(verificar_duplicatas_otimizado(lista2))  # Saída: False

lista3 = []
print(verificar_duplicatas_otimizado(lista3))  # Saída: False
