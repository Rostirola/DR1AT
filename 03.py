# Definição da classe Contato
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

# Implementação da busca linear
def busca_contato(nome_procurado, lista_contatos):
    for contato in lista_contatos:
        if contato.nome.lower() == nome_procurado.lower():
            return contato.telefone
    return None

# Exemplo de uso
def main():
    # Criação de uma lista de contatos não ordenada
    contatos = [
        Contato("Ana", "91234-5678"),
        Contato("Bruno", "92345-6789"),
        Contato("Carlos", "93456-7890"),
        Contato("Diana", "94567-8901"),
        Contato("Eduardo", "95678-9012")
    ]

    # Solicita ao usuário o nome do contato a ser buscado
    nome = input("Digite o nome do contato que deseja buscar: ")

    # Executa a busca
    telefone = busca_contato(nome, contatos)

    # Exibe o resultado
    if telefone:
        print(f"Contato encontrado: {nome} - Telefone: {telefone}")
    else:
        print(f"Contato '{nome}' não encontrado na lista de contatos.")

if __name__ == "__main__":
    main()
