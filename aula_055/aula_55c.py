
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ').strip()

if nome:
    tamanho_nome = len(nome)

    if tamanho_nome <= 4:
        tamanho = 'curto'
    elif 5 <= tamanho_nome <= 6:
        tamanho = 'normal'
    else:
        tamanho = 'muito grande'

    print(f'Seu nome é {tamanho}')
    
else:
    print('Você não digitou nenhum nome')