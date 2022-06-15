"""
Crie um programa que leia o ano de nasciento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.
"""

import datetime
import os
os.system('cls')
anovigente = datetime.date.today().year

sao_maiores = 0
nao_maiores = 0

for i in range(1,7+1):
    ano = int(input(f'Informe o ano de nascimento da {i}ª pessoa.: '))
    if anovigente - ano >= 21:
        sao_maiores += 1
    else:
        nao_maiores += 1
print(f'{sao_maiores} pessoas atingiram a maior idade e {nao_maiores} pessoas não atingiu a maior idade.')

