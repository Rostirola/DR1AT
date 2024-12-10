class Browser:
    def __init__(self, homepage):
        self.current_page = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, page):
        self.back_stack.append(self.current_page)
        self.current_page = page
        self.forward_stack.clear()
        print(f"Navegando para: {self.current_page}")

    def back(self):
        if not self.back_stack:
            print("Nenhuma página anterior.")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Voltando para: {self.current_page}")

    def forward(self):
        if not self.forward_stack:
            print("Nenhuma página futura.")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Avançando para: {self.current_page}")

    def current(self):
        print(f"Página atual: {self.current_page}")


# Criação do objeto Browser com a página inicial
browser = Browser("Página Inicial")

# Navegação para páginas
browser.visit("Página A")
browser.visit("Página B")
browser.visit("Página C")

# Exibir a página atual
browser.current()  # Saída: Página atual: Página C

# Utilizar o botão Voltar
browser.back()     # Saída: Voltando para: Página B
browser.back()     # Saída: Voltando para: Página A

# Tentar voltar além do histórico
browser.back()     # Saída: Voltando para: Página Inicial
browser.back()     # Saída: Nenhuma página anterior.

# Utilizar o botão Avançar
browser.forward()  # Saída: Avançando para: Página Inicial
browser.forward()  # Saída: Avançando para: Página A

# Visitar uma nova página após voltar
browser.visit("Página D")
# Saída: Navegando para: Página D

# Tentativa de avançar após nova navegação
browser.forward()  # Saída: Nenhuma página futura.
