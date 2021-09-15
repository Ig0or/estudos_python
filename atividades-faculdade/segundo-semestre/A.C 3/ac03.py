# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 03

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: Beatrici Ramos Feliciano
# ALUNO 2: Igor Guilherme da Paz Provensi
# ALUNO 3: Igor Ruiz de França
# ALUNO 4: Robson Ferreira Puert
# ALUNO 5: Yasmim Barbosa Vieira


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(Casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None

    def set_diretor(self, professor):
        self.diretor = professor

    def set_monitor(self, aluno):
        self.monitor = aluno


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__feitos = 0

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__feitos


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa
        self.alunos = []

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)


class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, quantidade):
        if casa.nome == self.casa1.nome:
            self.__pontos_casa1 += quantidade
        else:
            self.__pontos_casa2 += quantidade

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
