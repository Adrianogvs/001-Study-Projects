"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços.

frase = str(input('Informe uma frase: ')).strip().upper()
pln = frase[::-1]

if pln == frase:
    print(f'SIM, está frase "{frase}" é um  Palindromo.')
else:
    print(f'NÃO, esta frase "{frase}" não é um Palindromo.')

"""
import os
os.system('cls')
"""

frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
    
"""
frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]

if inverso == juntar:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')