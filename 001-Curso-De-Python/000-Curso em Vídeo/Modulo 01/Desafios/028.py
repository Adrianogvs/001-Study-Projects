"""
Escreva um programa que faça o computador "pensar" em um numero de 0 a 5 e peça para o usuário tentar descobror qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

# importando a biblioteca 'random', ela que faz o ebaralhamento dos numero de 0 a 5
import random 
from time import sleep 

# Tela inicial do programa
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar, ...')
print('-=-' * 20)

# Soliicta entrada de um numero
num = int(input('Qual numero o computador escolheu de 1 a 5? '))

# Programa ira fazer a seleção de alguns destes numeros
lista = [1, 2, 3, 4, 5]

# Programa escolheu um numero
escolhido = random.choice(lista)

# Informa se o usuário venceu ou não
if escolhido == num:
    print('Você Venceu')
else:
    print('Você Perdeu')