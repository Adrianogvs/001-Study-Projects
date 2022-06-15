"""
Crie um programa que faça o computador jogar jokenpô com você.
"""
# INICIO------ Algotitimo feito pelo Gustavo Guanabara -------------
import imp
import os         
os.system('cls')   # Limpar tela antes de fazer as perguntas:
from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''Escolha suas opções:'
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('='*40)
print(f'Computador jogou {itens[computador]}. ')
print(f'Jogador jogou {itens[jogador]}. ')
print('='*40)

if computador == 0:   # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida!')
elif computador == 2: # computador jogou TESOUSA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')

# FIM------ Algotitimo feito pelo Gustavo Guanabara -------------
"""
# INICIO------------ Algoritmo Feito por mim -----------------------

import random
import os         
os.system('cls')   # Limpar tela antes de fazer as perguntas:

print('='*40)
print('Vamos jogar Jokenpô, escolha uma das seguintes opções:')
print('                     1 = Pedra')
print('                     2 = Papel')
print('                     3 = Tesoura')
print('='*40)

voce = int(input('Informe uma das opções acima de 1 a 3: => '))
lista = [1,2,3]
escolha = random.choice(lista)

print('='*50)
if voce == 1:
    print(f'Você escolheu PEDRA.')
elif voce == 2:
    print(f'Você  escolheu PAPAEL.')
else:
    print(f'Você  escolheu TESOURA.')
print('='*50)
if escolha == 1:
    print(f'O sistema escolheu PEDRA.')
elif escolha == 2:
    print(f'O sistema escolheu PAPAEL.')
else:
    print(f'O sistema escolheu TESOURA.')
print('='*50)

if voce == 1 and escolha == 3:
    print(f'PARABÉNS !!! \nVocê ganhou!!! A PEDRA quebra/ amassa a TESOURA.')
elif voce == 2 and escolha == 1:
    print(f'PARABÉNS !!! \nVocê ganhou!!! O PAPEL embrulha a PEDRA.')
elif voce == 3 and escolha == 2:
    print(f'PARABÉNS !!! \nVocê ganhou!!! A TESOURA corta o PAPEL.')
elif voce == 1 and escolha == 2:
    print(f'Sinto muito !!! \nVocê perdeu!!! O PAPEL embrulha a PEDRA.')
elif voce == 2 and escolha == 3:
     print(f'Sinto muito !!! \nVocê perdeu!!! A TESOURA corta o PAPEL.')
elif voce == 3 and escolha == 1:
    print(f'Sinto muito !!! \nVocê perdeu!!! A PEDRA quebra/ amassa o TESOURA.')
else:
    print('Houve empate, joguem novamente!!!')
print('='*50)

# FIM------------ Algoritmo Feito por mim -----------------------
"""