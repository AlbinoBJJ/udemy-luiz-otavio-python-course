"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input('Digite um número inteiro: ')
try:
    num = int(num_str)
    validation = num % 2 == 0
    par_impar = None
    if validation:
        par_impar = 'par'
    else:
        par_impar = 'ímpar'
    
    print(f'O número {num} é {par_impar}')
except:
    print(f'Você digitou "{num_str}"! Entrada inválida! Você não digitou um número inteiro!')

