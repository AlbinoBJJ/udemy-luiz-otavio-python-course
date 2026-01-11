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
    # counter para retornar os acertos no fim da função 
    counter = 0

    # loop para percorrer a lista de perguntas
    for index, pergunta in enumerate(perguntas):
        questions = pergunta['Pergunta']
        options = pergunta['Opções']
        respostas = pergunta['Resposta']

        # printa a pergunta para o usuário. Devido o uso do enumerate, foi possível numerar cada questão
        print(f'\nPergunta {index + 1}: {questions}\n')
        
        # printa as alternativas para o usuário. Transformei as alternativas em a, b, c, d (precisei do google para isso)
        for idx, option in enumerate(options):
            alternativa = chr(ord('a') + idx) # (precisei do google para isso)
            print(f'{alternativa}. {option}') # o enumerate ajudou aqui

        letras = ['a', 'b', 'c', 'd'] # lista de alternativas 
        respostas_da_rodada = dict(zip(letras, options)) # uni as letras com as opções da pergunta em um dicionário
        

        # loop para capturar a resposta do usuário
        while True:
            resposta = input('\nDigite sua resposta (a, b, c ou d): ').lower()
            # verifica se a resposta é a, b, c, d
            if resposta not in letras:
                print(f'\nVocê digitou {resposta}! Não é uma alternativa válida!')
                continue
            else:
                print(f'\nVocê digitou {resposta}! Tem certeza?')
                # o usuário precisa confirmar se a resposta que ele inputou é a que ele realmente quer que seja contabilizada
                confirma = input(f'\nConfirma sua resposta? Pressione ENTER para continuar ou "N" para reposnder novamente')
                if confirma == '':
                    break
                else:
                    # se o usuário digitar algo, o loop retorna e pede para responder de novo
                    continue
        
        # validação da resposta

        # se a resposta que ele deu (busca no dicionário a resposta, que é uma chave), for igual a resposta (lá do dicionário)...
        if respostas_da_rodada[resposta] == respostas: 
            print('\nParabéns! Você acertou')
            # o counter aumenta em +1
            counter += 1
        else:
            # se não, tchau e bença!!!
            print('\nQue pena! Você errou!')

    return counter # retorna o counter

print(f'\nVocê acertou {chama_pergunta(perguntas)} de {len(perguntas)} perguntas')
