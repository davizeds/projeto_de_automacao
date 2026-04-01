import os


if __name__ == '__main__':


    caminho=r'C:\Users\Usuario\Downloads'
    print(os.listdir(caminho))
    lista_de_arquivos=os.listdir(caminho)

    categorias={
        'audios':['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'aiff', 'alac', 'opus',
           'amr', 'mid', 'midi', 'ra', 'dsd', 'ape'],

        'videos':['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'mpeg', 'mpg', '3gp',
           'm4v', 'vob', 'ts', 'ogv', 'f4v'],

        'imagens':['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'heic', 'svg',
            'raw', 'psd', 'ico'],

        'executaveis':['exe', 'msi', 'bat', 'cmd', 'sh', 'jar', 'apk', 'app', 'deb',
                 'rpm', 'bin'],

        'documentos':['txt', 'doc', 'docx', 'odt', 'pdf', 'rtf', 'tex', 'log', 'md', 'csv',
               'json', 'xml', 'yaml', 'yml'],

        'arquivos_compactados':['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'iso', 'dmg'],

        'scripts':['py', 'js', 'html', 'css', 'java', 'c', 'cpp', 'cs', 'rb', 'php', 'go',
            'rs', 'swift']


    }

    arquivos_encontrados={'audios':[], 'videos':[], 'imagens':[], 'executaveis':[], 'documentos':[],
    'arquivos_compactados':[], 'scripts':[]}







    for arquivos in lista_de_arquivos:
        arquivo_separado=arquivos.split(sep='.')
        extensao=arquivo_separado[-1]
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

    for chave in categorias.keys():
        os.mkdir(caminho+ '\\' +chave)
