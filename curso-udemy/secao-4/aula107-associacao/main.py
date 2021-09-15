from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Lucas')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
