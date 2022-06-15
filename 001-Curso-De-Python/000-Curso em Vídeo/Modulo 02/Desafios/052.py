"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

num = int(input('Verificar numeros primos ate: '))
mult=0

for i in range(2,num):
    if (num % i == 0):
        print(f'Múltiplo de, {i}.')
        mult += 1

if mult==0 and num >= 2:
    print('É primo.')
elif num == 1:
    print(f'o {num} não é um numero primo!')    
else:
    print(f'Tem, {mult}, múltiplos acima de 2 e abaixo de, {num}.')
"""
import os
os.system('cls')



num = int(input('Digite um numero:'))
total = 0

for i in range(1, num +1):
    if num % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[32m', end=' ')
    print(f'{i}', end=' ')    
print(f'\n\033[mO numero {num} foi divisivel {total} vezes.')
if total == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO é PRIMO.')

