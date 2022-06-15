"""
Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
"""

import os
os.system('cls')
from random import randint


computador = randint(0, 10)
print('Escola um nomero de 0 a 10')
acertou = False
palpite= 0

while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais, ... Tente novamente!!!')
        else:
            print('Menos, ... Tente mais uma vez!!! ')
print(f'Acertou com {palpite} tentativas. Parabens!!!')
