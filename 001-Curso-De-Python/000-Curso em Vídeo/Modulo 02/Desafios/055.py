"""
Faça um programa que leia o peso de cinco pessoas.
No final mostre qual foi o maior e o menor peso lidos.
"""

import os
os.system('cls')

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(f'Informe o pesso da {i} pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior} o menor peso é {menor}.')
