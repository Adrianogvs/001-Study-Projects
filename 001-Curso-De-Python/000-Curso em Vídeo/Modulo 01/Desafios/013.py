"""
Faça um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aument0.
"""

salario = float(input('Informe o salario: '))
reajuste = salario + (salario * 15 / 100)

print(f'O novo salario com reajuste é de: R${reajuste:.2f}')