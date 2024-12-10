def selection_sort(jogadores):
    """
    Ordena a lista de jogadores por pontuação utilizando o algoritmo Selection Sort.

    Parâmetros:
    jogadores (list): Lista de dicionários onde cada dicionário representa um jogador com 'nome' e 'pontuacao'.

    Retorna:
    list: Lista de jogadores ordenada por pontuação em ordem crescente.
    """
    n = len(jogadores)
    for i in range(n):
        # Encontrar o índice do jogador com a menor pontuação a partir de i
        indice_min = i
        for j in range(i+1, n):
            if jogadores[j]['pontuacao'] < jogadores[indice_min]['pontuacao']:
                indice_min = j
        # Trocar o jogador na posição i com o jogador de menor pontuação encontrado
        jogadores[i], jogadores[indice_min] = jogadores[indice_min], jogadores[i]
    return jogadores

# Exemplo de uso
if __name__ == "__main__":
    jogadores = [
        {'nome': 'Ana', 'pontuacao': 1500},
        {'nome': 'Bruno', 'pontuacao': 1200},
        {'nome': 'Carlos', 'pontuacao': 1800},
        {'nome': 'Diana', 'pontuacao': 1300}
    ]

    print("Antes da ordenação:")
    for jogador in jogadores:
        print(f"Nome: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")

    jogadores_ordenados = selection_sort(jogadores)

    print("\nApós a ordenação:")
    for jogador in jogadores_ordenados:
        print(f"Nome: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")
