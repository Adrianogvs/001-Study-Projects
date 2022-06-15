"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random


n1 = str(input('1º nome: '))
n2 = str(input('2º nome: '))
n3 = str(input('3º nome: '))
n4 = str(input('4º nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f'O aluno foi {escolhido}.')

"""

"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle 

n1 = str(input('1º nome: '))
n2 = str(input('2º nome: '))
n3 = str(input('3º nome: '))
n4 = str(input('4º nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem de apresentação será: {lista}.')
