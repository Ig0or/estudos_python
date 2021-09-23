import random
import string

inteiro = random.randint(10, 20)
inteiro2 = random.randrange(900, 999, 10)
print(inteiro)
print(inteiro2)

flutuante = random.uniform(10, 20)
flutuante2 = random.random()
print(flutuante)
print(flutuante2)


lista = ['igor', 'jose', 'maria', 'rosa', 'claudia']
sorteio = random.sample(lista, 2)
sorteio2 = random.choices(lista, k=3)
sorteio3 = random.choice(lista)
print(sorteio)
print(sorteio2)
print(sorteio3)

random.shuffle(lista)
print(lista)

# gerando senhas
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos +caracteres
senha = ''.join(random.choices(geral, k=12))
print(senha)
