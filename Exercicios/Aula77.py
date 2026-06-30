perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def questao(x):
    print(f"Pergunta: {perguntas[x]['Pergunta']}")

    print('Opções:')
    i = 0

    for opcoes in perguntas[x]['Opções']:
        i += 1
        print(f'{i}) {opcoes}')

    escolha_1 = int(input('Escolha uma opção: '))
    resposta_escolhida = perguntas[x]['Opções'][escolha_1 - 1]

    if resposta_escolhida == perguntas[x]['Resposta']:
        print('Você acertou!\n')
        return True
    else:
        print('Você errou!\n')
        return False

tentativa_1 = questao(0)
tentativa_2 = questao(1)
tentativa_3 = questao(2)

acertos = 0
if tentativa_1 == True:
    acertos +=1

if tentativa_2 == True:
    acertos +=1

if tentativa_3 == True:
    acertos +=1
    

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
