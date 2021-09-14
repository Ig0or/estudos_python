import re
import random

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except Exception as e:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj, 1)
        novo_cnpj = calcula_digito(novo_cnpj, 2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}' \
                  f'{quarto_bloco}00'

    novo_cnpj = calcula_digito(inicio_cnpj, 1)
    novo_cnpj = calcula_digito(novo_cnpj, 2)
    print(f'CNPJ gerado: {novo_cnpj[0:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/{novo_cnpj[8:12]}-{novo_cnpj[12:14]}')






















