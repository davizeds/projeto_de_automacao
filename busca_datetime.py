import os
from datetime import datetime
from dicionario import categorias

def escolhendo_pasta(caminho):
    while True:
        pasta_escolhida = input( 'escolha sua pasta' ).lower()
        if pasta_escolhida in categorias:
            caminho_da_pasta_escolhida=os.path.join(caminho,pasta_escolhida)
            return caminho_da_pasta_escolhida
        else: print('pasta nao encontrada ou digitada errado')

def conferimento_de_dia(pastas,arquivos_da_pasta):
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

def conferimento_de_mes(pastas,arquivos_da_pasta):
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

def conferimento_de_ano(pastas,arquivos_da_pasta):
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

def conferimento_data_completa(pastas, arquivos_da_pasta):
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

def escolher_tipo_de_busca(pastas,arquivos_da_pasta):
    while True:
        print (print(
    '\nEscolha o tipo de busca que você deseja:\n'
    '1 - por dia\n'
    '2 - por mês\n'
    '3 - por ano\n'
    '4 - data completa\n'))

        escolha_do_tipo=int(input('escolha o numero'))
        if   escolha_do_tipo == 1:
            return conferimento_de_dia(pastas,arquivos_da_pasta)
        elif escolha_do_tipo == 2:
            return conferimento_de_mes(pastas,arquivos_da_pasta)
        elif escolha_do_tipo == 3:
            return conferimento_de_ano(pastas,arquivos_da_pasta)
        elif escolha_do_tipo == 4:
            return conferimento_data_completa( pastas, arquivos_da_pasta )
        else:
            print ('essa respota nao existe')
            continuar=input( 'quer continuar (s/n)' ).lower()
            if continuar == 'n':
                break

def quer_buscar(pastas,arquivos_da_pasta):
    while True:
        print('quer buscar por data especifica?')
        pergunta=input('(s/n)').lower()
        if pergunta=='s':
            return escolher_tipo_de_busca(pastas,arquivos_da_pasta)
        elif pergunta=='n':
            break
        else: print ('erro, responda apenas com s/n')
