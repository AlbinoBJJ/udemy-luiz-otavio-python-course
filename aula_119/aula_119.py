# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiply(num):
    def mod(multiplier):
        return num * multiplier
    return mod

first_num = multiply(5)
second_num = multiply(3)

print(first_num(2))
print(first_num(3))
print(first_num(4))
print(second_num(2))
print(second_num(3))
print(second_num(4))