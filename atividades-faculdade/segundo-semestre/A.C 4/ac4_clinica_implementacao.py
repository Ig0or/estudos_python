from ac4_clinica import Pessoa, Quarto, Medico, Paciente

# cria os medicos
med1 = Medico("João", 12345678900, 11999999999, 
              757389, 7000, "Ortopedia")
med2 = Medico("Fernando", 12345623541, 119466917999, 
              632158, 8000, "Infectologia")
med3 = Medico("Robson", 72615646741, 11929173959, 
              757124, 4000, "Oftamologia")

# cria os pacientes
pac1 = Paciente("Oslo", 54715646223, 11992692743, 281383, 
                "Rua Sete, 20", "15/08/1998")
pac2 = Paciente("Oslo", 35825856291, 11999274399, 345312, 
                "Avenida Tenente, 36", "20/01/2000")
pac3 = Paciente("Lucas", 34931985712, 11999274312, 145332, 
                "Avenida Joao Paulo, 98", "30/12/1975")

# cria os quartos
qt1 = Quarto(1, 1)
qt2 = Quarto(2, 1)
qt3 = Quarto(3, 1)

# atribui o medico responsavel pelo paciente
pac1.set_medico_responsavel(med1)
pac2.set_medico_responsavel(med2)
pac3.set_medico_responsavel(med3)

# atribui um quarto para o paciente
pac1.set_quarto(qt1)
pac2.set_quarto(qt2)
pac3.set_quarto(qt3)

# exibe os dados do medico responsavel pelo paciente e o quarto
print(f"Nome do médico: {pac1.get_medico_responsavel().nome}")
print(f"CRM: {pac1.get_medico_responsavel().crm}")
print(f"Especialidade: {pac1.get_medico_responsavel().especialidade}")
print(f"Quarto: {pac1.get_quarto().numero}")
print(f'Andar: {pac1.get_quarto().andar}')
print("----------------------------")
print(f"Nome do médico: {pac2.get_medico_responsavel().nome}")
print(f"CRM: {pac2.get_medico_responsavel().crm}")
print(f"Especialidade: {pac2.get_medico_responsavel().especialidade}")
print(f"Quarto: {pac2.get_quarto().numero}")
print(f'Andar: {pac2.get_quarto().andar}')
print("----------------------------")
print(f"Nome do médico: {pac3.get_medico_responsavel().nome}")
print(f"CRM: {pac3.get_medico_responsavel().crm}")
print(f"Especialidade: {pac3.get_medico_responsavel().especialidade}")
print(f"Quarto: {pac3.get_quarto().numero}")
print(f'Andar: {pac3.get_quarto().andar}')
print("----------------------------")

# visita médicas nos pacientes
pac1.set_historico_medico(med1.visitar_paciente("28/01/2021", "18:30", 
                          "Paciente reclamando de dores no joelho"))
pac2.set_historico_medico(med2.visitar_paciente("01/02/2021", "09:18", 
                          "Paciente com infecção em ferida"))
pac3.set_historico_medico(med3.visitar_paciente("19/03/2021", "15:47", 
                          "Paciente com dores na vista"))

# exibe o historico medico dos pacientes
print(pac1.get_historico_medico())
print(pac2.get_historico_medico())
print(pac3.get_historico_medico())
