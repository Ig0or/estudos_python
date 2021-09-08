# Exercicio 1
def saudacao(saudacao, nome):
    print(f'{saudacao}, {nome}')


# Exercicio 2
def soma(v1, v2, v3):
    print(v1 + v2 + v3)


# Exercicio 3
def percentual(valor, aumento):
    return (valor * aumento) / 100 + valor


# Exercicio 4
def FizzBuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    if numero % 5 == 0:
        return 'Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    return numero


saudacao('Olá', 'igor')
soma(10,20,35)
print(percentual(1000, 50))
print(FizzBuzz(15))

