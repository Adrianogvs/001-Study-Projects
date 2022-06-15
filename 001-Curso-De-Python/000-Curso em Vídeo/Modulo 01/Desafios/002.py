"""
Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
"""
import math


from cmath import sqrt

num = int(input("Digite um numero: "))

print(f'O dobro do numero digitado é: {num * 2}')
print(f'O triplo do numero digitado é {num * 3}.')
print(f'A raiz quadrada do numero digitado é {math.sqrt(num):.2f}')