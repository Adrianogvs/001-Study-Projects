"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.
"""
r1 = float(input('Informa o valor para a reta 1: '))
r2 = float(input('Informa o valor para a reta 2: '))
r3 = float(input('Informa o valor para a reta 3: '))


if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print(f'É possivel formar um triangulo.')
else:
    print(f'Não é possível formar um triangulo.')