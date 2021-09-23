from dados import *
import json

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for k, v in dados.items():
    print(k)
    print(v)


