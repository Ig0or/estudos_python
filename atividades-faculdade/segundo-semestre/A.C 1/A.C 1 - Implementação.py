import ac01

"""
EXERCICIO 1
"""

tupla = (1, 2, 3, 4, 5)
print(ac01.pertence(tupla, 2))


"""
EXERCICIO 2
"""

lista = [1, 2, 3, 2, 4]
print(ac01.substituir(lista, 2, 99))

"""
EXERCICIO 3
"""

lista = ["a", 2, "b", "a", "a"]
print(ac01.posicoes_lista(lista, "a"))

"""
EXERCICIO 4
"""

alunos = {
    "Augusto": [4.5, 7.0, 6.0, 3.0],
    "Denise": [9.0, 8.5],
    "Ana Paula": [3.5, 1.0, 6.5],
    "Marcelo": [9.0, 10.0, 7.0, 7.0],
}

print(ac01.aprovados(alunos))

"""
EXERCICIO 5
"""

alunos = {
    "Augusto": [4.5, 7.0, 6.0, 3.0],
    "Denise": [9.0, 8.5],
    "Ana Paula": [3.5, 1.0, 6.5],
    "Marcelo": [9.0, 10.0, 7.0, 7.0],
}

print(ac01.incluir_nota(alunos, "Denise", 10.0))


"""
EXERCICIO 6
"""

alunos = {
    "Augusto": [4.5, 7.0, 6.0, 3.0],
    "Denise": [9.0, 8.5],
    "Ana Paula": [3.5, 1.0, 6.5],
    "Marcelo": [9.0, 10.0, 7.0, 7.0],
}

print(ac01.maiores_notas(alunos))