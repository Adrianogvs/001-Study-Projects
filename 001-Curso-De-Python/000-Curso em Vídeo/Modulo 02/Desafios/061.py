"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
import os
os.system('cls')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Segundo termo: '))
termo = primeiro
i = 1

while i <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    i += 1
print('Fim')
