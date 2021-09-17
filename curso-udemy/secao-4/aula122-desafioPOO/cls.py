from abc import abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    def informacoes_conta(self):
        print(f'Agência: {self._agencia} - Conta: {self._conta} - Saldo: R$ {self._saldo:.2f}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} feito com sucesso.')
            return
        print('Não foi possivel realizar o saque por saldo insuficiente na conta.')
        return


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def aumentar_limite(self, valor):
        if self._saldo < 0:
            return f'Não foi possivel aumentar seu limite, pois o saldo da sua conta está negativo.'
        self.limite += valor
        return f'Seu novo limite é de: R$ {self.limite:.2f}'

    def sacar(self, valor):
        if valor <= (self._saldo + self.limite):
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} feito com sucesso.')
            return
        print('Não foi possivel realizar o saque, saldo insuficiente na conta.')
        return


class Banco:
    def __init__(self):
        self.agencias = [111, 222, 333, 444]
        self.clientes = []
        self.contas = []

    def cadastrar_agencia(self, agencia):
        self.agencias.append(agencia)
        print('Agência cadastrada.')
        return

    def agencias_cadastradas(self):
        print('Agências: ', end='')
        for agencia in self.agencias:
            if agencia == self.agencias[-1]:
                print(agencia)
            else:
                print(agencia, end=' - ')
        return

    def cadastrar_cliente(self, cliente):
        if cliente in self.clientes:
            print('Cliente já cadastrado.')
            return
        else:
            self.clientes.append(cliente)

    def cadastrar_conta(self, cliente):
        if cliente.conta in self.contas:
            print('Cliente já cadastrado.')
            return
        else:
            self.contas.append(cliente.conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
