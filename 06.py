import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Flag para verificar se houve troca na iteração
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        # Se não houve troca, a lista já está ordenada
        if not trocou:
            break
    return lista

# Função para medir o tempo de execução
def medir_tempo(lista):
    inicio = time.time()
    sorted_lista = bubble_sort(lista.copy())
    fim = time.time()
    return fim - inicio, sorted_lista

# Exemplos de uso
if __name__ == "__main__":
    # Teste com 1.000 elementos
    lista_1k = [random.uniform(0, 1000) for _ in range(1000)]
    tempo_1k, sorted_1k = medir_tempo(lista_1k)
    print(f"Tempo de execução para 1.000 elementos: {tempo_1k:.4f} segundos")

    # Teste com 10.000 elementos
    lista_10k = [random.uniform(0, 10000) for _ in range(10000)]
    tempo_10k, sorted_10k = medir_tempo(lista_10k)
    print(f"Tempo de execução para 10.000 elementos: {tempo_10k:.4f} segundos")
