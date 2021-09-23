import os
import sys

args =sys.argv
qtd_args = len(args)

if qtd_args <= 1:
    print('Faltando argumentos')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')
    sys.exit()

so_diretorios = False
so_arquivos = False

if '-a' in args:
    so_arquivos = True

if '-d' in args:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)