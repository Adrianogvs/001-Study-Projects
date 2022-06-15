"""
Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500.
"""
import os
from time import sleep
os.system('cls')

soma = 0
cont = 0
for i in range(1,501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os {cont} valores é {soma}.\n\n')
