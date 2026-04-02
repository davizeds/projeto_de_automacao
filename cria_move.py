import os
import shutil
from dicionario import arquivos_encontrados,categorias
import logging




def criar_pasta(caminho):
    for chave in categorias.keys():
        if not os.path.exists( os.path.join( caminho, chave ) ):
            os.mkdir( os.path.join( caminho, chave ) )
    return


def mover_pasta(caminho):
    for chave, valor in arquivos_encontrados.items():
        for arc in valor:
            if not os.path.exists( os.path.join( caminho, chave, arc ) ):
                shutil.move( os.path.join( caminho, arc ), os.path.join( caminho, chave, arc ) )
                logging.info( 'arquivos movidos corretamente' )
    return
