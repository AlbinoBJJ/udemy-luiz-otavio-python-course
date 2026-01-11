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

def chama_pergunta(perguntas):
    counter = 0
    for index, pergunta in enumerate(perguntas):
        questions = pergunta['Pergunta']
        options = pergunta['Opções']
        respostas = pergunta['Resposta']

        print(f'\nPergunta {index + 1}: {questions}\n')
        
        for idx, option in enumerate(options):
            alternativa = chr(ord('a') + idx)
            print(f'{alternativa}. {option}')

        letras = ['a', 'b', 'c', 'd']
        respostas_da_rodada = dict(zip(letras, options))
        
        while True:
            resposta = input('\nDigite sua resposta (a, b, c ou d): ').lower()
            if resposta not in letras:
                print(f'\nVocê digitou {resposta}! Não é uma alternativa válida!')
                continue
            else:
                print(f'\nVocê digitou {resposta}! Tem certeza?')
                confirma = input(f'\nConfirma sua resposta? Pressione ENTER para continuar ou "N" para reposnder novamente')
                if confirma == '':
                    break
                else:
                    continue
        
        if respostas_da_rodada[resposta] == respostas:
            print('\nParabéns! Você acertou')
            counter += 1
        else:
            print('\nQue pena! Você errou!')

    return counter

print(f'\nVocê acertou {chama_pergunta(perguntas)} de {len(perguntas)} perguntas')
