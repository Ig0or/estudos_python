from zipfile import ZipFile
import os


caminho = input(r'Digite o caminho. Ex: C:\Users\office\Desktop\teste')

# compacta arquivos num .zip
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        print(caminho_completo)
        zip.write(caminho_completo, arquivo)

# exibe arquivos compactados
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# descompacta arquivos
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')