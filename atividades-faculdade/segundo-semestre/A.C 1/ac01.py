# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Igor Ruiz de França
# ALUNO 2: Igor Guilherme da Paz Provensi
# ALUNO 3: Robson Ferreira Puert
# ALUNO 4: Yasmim Vieira Barbosa
# ALUNO 5:


"""
Escreva uma função com o nome pertence, que recebe como argumentos de entrada
uma tupla e um item e retorna True, se o item estiver armazenado na tupla, e
False, caso contrário.
"""


def pertence(tupla, item):
    if item in tupla:
        return True
    else:
        return False


"""
Escreva uma função chamada substituir que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
"""


def substituir(lista, velho, novo):
    indice = 0
    for i in lista:
        if i == velho:
            lista.remove(i)
            lista.insert(indice, novo)
        indice += 1
    return lista


"""
Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada
uma lista e um item, e retorna uma lista contendo todas os índices em que o
item aparece na lista.
"""


def posicoes_lista(lista, item):
    indice = 0
    indices_lista = []
    for i in lista:
        if i == item:
            indices_lista.append(indice)
        indice += 1
    return indices_lista


"""
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada aprovados que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos aprovados
(um aluno é aprovado quando a média das suas notas é maior ou igual a 6).
"""


def aprovados(alunos):
    alunosAprovados = []
    for i in alunos:
        media = sum(alunos[i]) / len(alunos[i])
        if media >= 6:
            alunosAprovados.append(i)
    return alunosAprovados


"""
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada incluir_nota que recebe como argumentos de
entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a
nota na lista de notas do aluno correspondente e retornar o dicionário com as
alterações realizadas.
"""


def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)
    return alunos


"""
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maiores_notas que recebe como
argumentos de entrada o dicionário e retorna outro dicionário com a
maior nota de cada aluno.
"""


def maiores_notas(alunos):
    for i in alunos:
        nota = alunos[i]
        maior = 0
        for a in nota:
            if a > maior:
                maior = a
                alunos[i] = maior
    return alunos
