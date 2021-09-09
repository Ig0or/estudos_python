print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '12',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5*2?',
        'respostas': {
            'a': '63',
            'b': '28',
            'c': '10',
        },
        'resposta_certa': 'c',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Sua resposta: ')

    if resposta_user == pv['resposta_certa']:
        respostas_certas += 1

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

if respostas_certas > 1:
    print(f'Você acertou {respostas_certas} respostas!')
else:
    print(f'Você acertou apenas {respostas_certas} resposta!')

print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.0f}%')
print()

