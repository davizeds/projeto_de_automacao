from colocar_caminho import pegar_caminho
from categorizacao_de_arquivos import categorizar
from cria_move import criar_pasta, mover_pasta
import os
from busca_datetime import  quer_buscar, escolhendo_pasta



if __name__ == '__main__':
    caminho=pegar_caminho()

    print( os.listdir( caminho ) )
    lista_de_arquivos = os.listdir( caminho )

    categorizar(lista_de_arquivos,caminho)

    criar_pasta(caminho)

    mover_pasta(caminho)

    pastas = escolhendo_pasta(caminho)

    print( os.listdir( pastas ) )
    arquivos_da_pasta = (os.listdir( pastas ))

    quer_buscar(pastas,arquivos_da_pasta)
