import re


def formata_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def verifica_digito1(cnpj):
    regressivo = 5
    soma_digitos = 0
    for digito in cnpj:
        soma_digitos += regressivo * int(digito)
        regressivo -= 1
        if regressivo < 2:
            regressivo = 9
    if 11 - (soma_digitos % 11) > 9:
        return str(0)
    else:
        return str(11 - (soma_digitos % 11))


def verifica_digito2(cnpj):
    regressivo = 6
    soma_digitos = 0
    for digito in cnpj:
        soma_digitos += regressivo * int(digito)
        regressivo -= 1
        if regressivo < 2:
            regressivo = 9
    if 11 - (soma_digitos % 11) > 9:
        return str(0)
    else:
        return str(11 - (soma_digitos % 11))


def validador(cnpj):
    cnpj_formatado = formata_cnpj(cnpj)
    cnpj_fatiado = cnpj_formatado[:-2]
    primeiro_digito = verifica_digito2(cnpj_fatiado)
    segundo_digito = verifica_digito2(cnpj_fatiado + primeiro_digito)
    novo_cnpj = cnpj_fatiado + primeiro_digito + segundo_digito

    if novo_cnpj == cnpj_formatado:
        return 'O CNPJ informado é válido.'
    return 'O CNPJ informado é inválido.'
