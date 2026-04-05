from colocar_caminho import pegar_caminho
import os
from datetime import datetime
from dicionario import categorias

def escolhendo_pasta():
    while True:
        pasta_escolhida = input( 'escolha sua pasta' ).lower()
        if pasta_escolhida in categorias:
            caminho_da_pasta_escolhida=os.path.join(pegar_caminho(), pasta_escolhida)
            return caminho_da_pasta_escolhida
        else: print('pasta nao encontrada ou digitada errado')

pastas=escolhendo_pasta()
print( os.listdir( pastas ) )
arquivos_da_pasta=( os.listdir( pastas ) )

def conferimento_de_data():
    while True:
        dia_desejado=int(input('dia desejado'))
        encontrou=busca_datetime(arquivos_da_pasta,dia_desejado,pastas)
        if encontrou == False:
            print ('nao achamos nada destes dias')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break




def busca_datetime(arquivos_da_pasta,dia_desejado,pastas):
    encontrou = False
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join(pastas,documentos)
        data_dos_arquivos=os.path.getmtime(caminho_completo)
        data_convertida=datetime.fromtimestamp(data_dos_arquivos)
        apenas_o_dia=data_convertida.day
        if dia_desejado==apenas_o_dia:
            print(documentos, data_convertida)
            encontrou = True
    return encontrou
