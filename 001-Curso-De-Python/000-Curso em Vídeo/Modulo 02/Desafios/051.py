"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
import os
from time import sleep
os.system('cls')

primeiro = int(input('Informe um numero para cálculo de uma PA:'))
razao = int(input('Informe a razão da PA: '))
decimo = primeiro +(10 -1) * razao

for i in range(primeiro,decimo + razao,razao):
    sleep(0.250)
    print(f'{i}',end=' -> ')
print('Fim, ...\n\n\n')