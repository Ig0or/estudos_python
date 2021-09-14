"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""


def soma_listas(lista1, lista2):
    listaGerador = zip(lista1, lista2)
    listaGerador = [(a, b) for a, b in listaGerador]
    listaSomada = [(i[0] + i[1]) for i in listaGerador]
    return listaSomada


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(soma_listas(lista_a, lista_b))