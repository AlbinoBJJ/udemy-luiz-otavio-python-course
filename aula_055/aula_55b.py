
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('Olá! Tudo bem? Que horas são?')
hora_str = input('Digite um valor para as horas no formato HH: ')
min_str = input('Digite um valor para os minutos no formato MM: ')
try:
    hora = int(hora_str)
    if (0 <= hora <= 11):
        saudacao = 'Bom dia'
    elif (12 <= hora <= 17):
        saudacao = 'Boa tarde'
    elif (18 <= hora <= 23):
        saudacao = 'Boa noite'
    else:
        print('Valor igual ou superior a 24 horas!',
        'Digite um valor entre 00 e 23 para as horas!')
    print(f'Agora são {hora_str}:{min_str}! {saudacao}!')
except:
    print(f'Você digitou "{hora_str}"! Entrada inválida!')