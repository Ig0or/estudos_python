from cls import *

cliente1 = Cliente('Felipe', 20)
cliente2 = Cliente('Amaro', 31)

conta1 = ContaCorrente(111, 8553, 100, 300)
conta2 = ContaPoupanca(222, 5121, 100)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

b1 = Banco()

if b1.autenticar(cliente1):
    cliente1.conta.sacar(50)
else:
    print('Cliente não autenticado.')

b1.cadastrar_cliente(cliente1)
b1.cadastrar_conta(cliente1)


if b1.autenticar(cliente1):
    cliente1.conta.sacar(50)
else:
    print('Cliente não autenticado.')

cliente1.conta.informacoes_conta()