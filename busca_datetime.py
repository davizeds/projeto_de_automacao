from colocar_caminho import caminho
import os
from datetime import datetime



pastas=os.path.join(caminho,'audios')
print( os.listdir( pastas ) )
arquivos_da_pasta=( os.listdir( pastas ) )

dia_desejado=int(input('dia desejado'))
def busca_datetime(arquivos_da_pasta):
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join( caminho, 'audios', documentos)
        data_dos_arquivos=os.path.getmtime(caminho_completo)
        data_convertida=datetime.fromtimestamp(data_dos_arquivos)
        apenas_o_dia=data_convertida.day
        apenas_o_mes=data_convertida.month
        apenas_o_ano=data_convertida.year
        if dia_desejado==apenas_o_dia:
            print(documentos, data_convertida)
