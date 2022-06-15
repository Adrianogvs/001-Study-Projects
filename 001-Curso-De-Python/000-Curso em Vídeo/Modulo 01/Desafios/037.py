print('-='*70)
print('         Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:')
print('-='*70)
print('                                                 1 - para binário.')
print('                                                 2 - para Octal.')
print('                                                 3 - para Hexadecimal.')
print('-='*70)

import math

valor = int(input('Informe um valor: =>'))
numero = int(input('Informe uma opção, sendo numero entre 1 e 3 conforme descrito acima: => '))

if numero == 1:
    print(f'O {valor} convertido para binário é {bin(valor)[2:].upper()}.')
elif numero == 2:
    print(f'O {valor} convertido para Octagonal é {oct(valor)[2:].upper()}.')
elif numero == 3:
    print(f'O {valor} convertido para Hexadecimal é {hex(valor)[2:].upper()}.')
else:
    print('Opção invalida!')
