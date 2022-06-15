"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

import os
os.system('cls')

f = 1
"""i = 5
while i > 0:
    print(f'{i}', end=' ')
    print('x' if i > 1 else '=', end=' ')
    f *= i
    i -= 1
print(f)
"""
for i in range(6,1,-1):
    i -= 1
    f *= i
    print(f'{i}', end=' ')
    print('x' if i > 1 else '=', end=' ')
print(f)
