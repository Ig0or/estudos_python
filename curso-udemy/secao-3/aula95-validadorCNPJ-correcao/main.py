import cnpj

cnpj1 = '87.507.605/0001-51'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido.')
else:
    print(f'{cnpj1} é inválido.')

cnpj.gera()