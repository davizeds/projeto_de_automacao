from colocar_caminho import pegar_caminho
from categorizacao_de_arquivos import categorizar
from cria_move import criar_pasta, mover_pasta
import os


if __name__ == '__main__':
    caminho=pegar_caminho()

    print( os.listdir( caminho ) )
    lista_de_arquivos = os.listdir( caminho )

    arquivos_categorizados=categorizar(arquivos_listados=lista_de_arquivos,caminho=caminho)

    criar_pasta(caminho)

    mover_pasta(caminho)
