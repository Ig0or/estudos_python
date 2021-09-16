from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

cc = ContaCorrente(111, 888, 0, 500)
cc.depositar(100)
cc.sacar(600)
cc.depositar(500)
