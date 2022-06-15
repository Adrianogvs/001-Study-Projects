"""
Estrutura de repetição com 'while()' é utilizado quando não se sabe o limite.

-- Portugol
enquanto não maça
    passo
pega

-- Python
while not apple:
    passo
pega


"""
# Estrutura while aninhada
"""
enquanto não maçã
    se tem chão
        passo
    se tem buraco
        pula
    se tem moeda
        pega
pega


while not apple:
    if chão:
        passo
    if burado:
        pula
    if moeda:
        pega
pega apple
"""

"""
for i in range(1, 10):
    print(i)
print('Fim FOR, ...')
"""
"""
i = 1
while i < 10:
    print(i)
    i += 1
print('Fim WHILE, ...')

"""
import os
os.system('cls')

"""
r = 'S'
cont = 0
soma = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N]:')).upper()
    cont += 1
    soma += n
print('----------------------------------------------')
print(f'Foi digitado {cont} vezes.')
print('----------------------------------------------')
print(f'A soma é {soma}.')
print('----------------------------------------------')
print('Fim, ... while')
print('----------------------------------------------')

"""
"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} numero pares e {impar} numeros impares!.')

"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numero pares e {impar} numeros impares!.')
