import os

def listar_arquivos(diretorio):
    """
    Percorre recursivamente todos os subdiretórios a partir do diretório especificado
    e lista todos os arquivos encontrados.

    :param diretorio: Caminho para o diretório raiz.
    :return: Lista de caminhos completos dos arquivos.
    """
    arquivos = []
    try:
        for item in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, item)
            if os.path.isfile(caminho_completo):
                arquivos.append(caminho_completo)
            elif os.path.isdir(caminho_completo):
                arquivos.extend(listar_arquivos(caminho_completo))
    except PermissionError:
        print(f"Sem permissão para acessar o diretório: {diretorio}")
    return arquivos

if __name__ == "__main__":
    caminho_raiz = input("Digite o caminho do diretório raiz: ")
    arquivos_encontrados = listar_arquivos(caminho_raiz)
    print("Arquivos encontrados:")
    for arquivo in arquivos_encontrados:
        print(arquivo)
