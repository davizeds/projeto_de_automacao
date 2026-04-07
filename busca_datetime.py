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

def conferimento_de_dia():
    while True:
        dia_desejado=int(input('dia desejado'))
        encontrou=buscar_day(arquivos_da_pasta,dia_desejado,pastas)
        if encontrou == False:
            print ('nao achamos nada destes dias')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break

def buscar_day(arquivos_da_pasta,dia_desejado,pastas):
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

def conferimento_de_mes():
    while True:
        mes_desejado=int(input('mes desejado'))
        encontrou=buscar_mes(arquivos_da_pasta,mes_desejado,pastas)
        if encontrou == False:
            print ('nao achamos nada desse mes')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break



def buscar_mes(arquivos_da_pasta,mes_desejado,pastas):
    encontrou = False
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join(pastas,documentos)
        data_dos_arquivos=os.path.getmtime(caminho_completo)
        data_convertida=datetime.fromtimestamp(data_dos_arquivos)
        apenas_o_mes=data_convertida.month
        if mes_desejado==apenas_o_mes:
            print(documentos, data_convertida)
            encontrou = True
    return encontrou

def conferimento_de_ano():
    while True:
        ano_desejado=int(input('ano desejado'))
        encontrou=buscar_ano(arquivos_da_pasta,ano_desejado,pastas)
        if encontrou == False:
            print ('nao achamos nada desse ano')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break

def buscar_ano(arquivos_da_pasta,ano_desejado,pastas):
    encontrou = False
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join(pastas,documentos)
        data_dos_arquivos=os.path.getmtime(caminho_completo)
        data_convertida=datetime.fromtimestamp(data_dos_arquivos)
        apenas_o_ano=data_convertida.year
        if ano_desejado==apenas_o_ano:
            print(documentos, data_convertida)
            encontrou = True
    return encontrou

def confermineto_data_completa():
    while True:
        dia_desejado = int( input( 'dia desejado' ) )
        mes_desejado = int( input( 'mes desejado' ) )
        ano_desejado = int( input( 'ano desejado' ) )
        encontrou=buscar_data_completa(arquivos_da_pasta,dia_desejado,mes_desejado,ano_desejado,pastas)
        if encontrou == False:
            print ('nao achamos nada dessa data')
        resposta=input('quer continuar (s/n)').lower()
        if resposta == 'n':
            break

def buscar_data_completa(arquivos_da_pasta,dia_desejado,mes_desejado,ano_desejado,pastas):
    encontrou=False
    for documentos in arquivos_da_pasta:
        caminho_completo = os.path.join( pastas, documentos )
        data_dos_arquivos = os.path.getmtime( caminho_completo )
        data_convertida = datetime.fromtimestamp( data_dos_arquivos )
        apenas_o_dia= data_convertida.day
        apenas_o_mes= data_convertida.month
        apenas_o_ano= data_convertida.year
        if dia_desejado==apenas_o_dia and mes_desejado==apenas_o_mes and ano_desejado==apenas_o_ano:
            print( documentos, data_convertida )
            encontrou = True
    return encontrou
