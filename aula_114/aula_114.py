# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(*args):
    total, *rest = args
    for num in rest:
        total *= num
    return total

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def even_odd(num):
    number = num % 2 == 0
    if number:
        return f'O número {num} é par'
    return f'O número {num} é ímpar'