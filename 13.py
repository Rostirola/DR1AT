def knapsack_dp(capacidade, pesos, valores, n):
    # Criar uma tabela (n+1) x (capacidade+1)
    dp = [[0 for x in range(capacidade + 1)] for x in range(n + 1)]

    # Construir a tabela dp de baixo para cima
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(valores[i-1] + dp[i-1][w - pesos[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # O valor máximo está na célula dp[n][capacidade]
    return dp[n][capacidade]

# Exemplo de uso
if __name__ == "__main__":
    valores = [3, 4, 5, 8]
    pesos = [2, 3, 4, 5]
    capacidade = 5
    n = len(valores)

    max_valor = knapsack_dp(capacidade, pesos, valores, n)
    print(f"Valor máximo que pode ser obtido: {max_valor}")
