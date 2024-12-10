class Fila:
    def __init__(self):
        """Inicializa a fila vazia."""
        self.itens = []

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)
        print(f"Chamado {item} inserido na fila.")

    def desenfileirar(self):
        """Remove e retorna o primeiro item da fila."""
        if not self.esta_vazia():
            item = self.itens.pop(0)
            print(f"Chamado {item} removido da fila.")
            return item
        else:
            print("A fila está vazia. Nenhum chamado para remover.")
            return None

    def tamanho(self):
        """Retorna o tamanho atual da fila."""
        return len(self.itens)

    def mostrar_fila(self):
        """Exibe o estado atual da fila."""
        if not self.esta_vazia():
            print("Estado atual da fila:")
            for idx, item in enumerate(self.itens, start=1):
                print(f"{idx}. Chamado {item}")
        else:
            print("A fila está vazia.")


# Instanciando a fila
fila_chamados = Fila()

# Inserindo chamados
fila_chamados.enfileirar(101)
fila_chamados.enfileirar(102)
fila_chamados.enfileirar(103)

# Exibindo o estado atual da fila
fila_chamados.mostrar_fila()

# Removendo um chamado
fila_chamados.desenfileirar()

# Exibindo o estado atualizado da fila
fila_chamados.mostrar_fila()

# Tentando remover todos os chamados
fila_chamados.desenfileirar()
fila_chamados.desenfileirar()
fila_chamados.desenfileirar()  # Tentativa de remover de uma fila vazia
