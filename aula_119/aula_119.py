# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# ---- MINHA SOLUÇÃO ----

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

# ---- SOLUÇÃO DO PROFESSOR LUIZ OTÁVIO ----

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))