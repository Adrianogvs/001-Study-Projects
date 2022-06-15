"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.
"""
import os
from time import sleep
os.system('cls')
for i in range(2, 51, 2):
    print(i, end=' ')
    sleep(0.250)
