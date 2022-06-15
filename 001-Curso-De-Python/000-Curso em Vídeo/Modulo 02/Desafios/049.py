"""
Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, so que agora utilizando um laço for.
"""
import os
os.system('cls')

num = int(input('Informe um numero para a tabuada: '))
tamanho = len(str(num * 10))


for i in range(0, 10+1):
    print(f'{num} X {i:>2} = {num * i:>{tamanho}.0f}') # Este código ':>{tamanho}' , quer dizer que estou adicionando valor vazio a esquerda do numero.

