"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""

from math import radians, sin, cos, tan

angulo = float(input('Informe o angulo:'))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem SENO de {seno:.2f}.')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem COSSENO de {seno:.2f}.')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo}')

