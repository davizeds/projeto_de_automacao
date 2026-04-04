from colocar_caminho import caminho
import os
from datetime import datetime



pastas=os.path.join(caminho,'audios')
print( os.listdir( pastas ) )
arquivos_da_pasta=( os.listdir( pastas ) )


def conferimento_de_data():
    while True:
        dia_desejado=int(input('dia desejado'))
        encontrou=busca_datetime(arquivos_da_pasta,dia_desejado)
        if encontrou == False:
            print ('nao achamos nada destes dias')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break



def busca_datetime(arquivos_da_pasta,dia_desejado,):
    encontrou = False
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join( caminho, 'audios', documentos)
        data_dos_arquivos=os.path.getmtime(caminho_completo)
        data_convertida=datetime.fromtimestamp(data_dos_arquivos)
        apenas_o_dia=data_convertida.day
        if dia_desejado==apenas_o_dia:
            print(documentos, data_convertida)
            encontrou = True
    return encontrou
