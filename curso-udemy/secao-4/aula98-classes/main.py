from pessoa import Pessoa

p1 = Pessoa('jose', 20)
p1.comer('maca')
p1.parar_comer()
p1.falar('tempo')
p1.parar_falar()

p2 = Pessoa('maria', 36)
p2.comer('churrasco')

print(p1.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())


