from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Jose', 20)
cliente2 = Cliente('Maria', 30)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(111, 24121, 0)
conta2 = ContaCorrente(222, 72543, 0)
conta3 = ContaPoupanca(121, 68123, 0)

cliente1.inserir_conta(conta1)
cliente3.inserir_conta(conta2)
cliente2.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('#'*20)

if banco.autenticar(cliente2):
    cliente1.conta.sacar(50)
else:
    print('Cliente não autenticado')


