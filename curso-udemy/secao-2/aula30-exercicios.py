# Exercicio 1

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é impar')
else:
    print('O dado informado não é um número inteiro.')


# Exercicio 2

hora = input('Digite a hora atual (0-23): ')

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('O numero informado deve estar entre 0 e 23.')
else:
    print('O dado informado não é valido.')


# Exercicio 3

nome = input('Informe seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande.')


