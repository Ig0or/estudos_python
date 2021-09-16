from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


class Quarto:
    def __init__(self, numero, andar):
        self.numero = numero
        self.andar = andar


class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm, salario, especialidade):
        super().__init__(nome, cpf, telefone)
        self.crm = crm
        self.salario = salario
        self.especialidade = especialidade

    def visitar_paciente(self, data, horario, observacao):
        self.data = data
        self.horario = horario
        self.observação = observacao
        self.medico = self.nome
        return self.data, self.horario, self.observação, self.medico


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.rg = rg
        self.__endereco = endereco
        self.data_nascimento = data_nascimento
        self.medico = None
        self.__historico_medico = []
        self.__quarto = None

    def get_historico_medico(self):
        # visita = 1
        # for i, tupla in enumerate(self.__historico_medico):
        #     print(f"Visita: {visita}")
        #     print(f"Data: {self.__historico_medico[i][0]}")
        #     print(f"Data: {self.__historico_medico[i][1]}")
        #     print(f"Observação: {self.__historico_medico[i][2]}")
        #     print(f"Nome Médico: {self.__historico_medico[i][3]}")
        #     print("---------------------------------")
        #     visita += 1
        # tentei fazer o return direto com print, mas nao deu certo :\
        return self.__historico_medico

    def set_historico_medico(self, visita):
        self.__historico_medico.append(visita)

    def get_medico_responsavel(self):
        return self.__medico

    def set_medico_responsavel(self, medico):
        self.__medico = medico

    def get_quarto(self):
        return self.__quarto

    def set_quarto(self, quarto):
        self.__quarto = quarto
        