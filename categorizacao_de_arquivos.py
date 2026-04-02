import os
import logging
from dicionario import arquivos_encontrados,categorias







logging.info('começando a separar os arquivos')


def categorizar(arquivos_listados,caminho):
    for arquivos in arquivos_listados:
        if  os.path.isfile(os.path.join(caminho,arquivos)):
            arquivo_separado=arquivos.split(sep='.')
            extensao=arquivo_separado[-1].lower()
            if extensao in categorias['audios']:
                arquivos_encontrados['audios'].append(arquivos)

            elif extensao in categorias['videos']:
                arquivos_encontrados['videos'].append(arquivos)

            elif extensao in categorias['imagens']:
                arquivos_encontrados['imagens'].append(arquivos)

            elif extensao in categorias['executaveis']:
                arquivos_encontrados['executaveis'].append(arquivos)

            elif extensao in categorias['documentos']:
                arquivos_encontrados['documentos'].append(arquivos)

            elif extensao in categorias['arquivos_compactados']:
                arquivos_encontrados['arquivos_compactados'].append(arquivos)

            elif extensao in categorias['scripts']:
                arquivos_encontrados['scripts'].append(arquivos)
    return arquivos_encontrados
