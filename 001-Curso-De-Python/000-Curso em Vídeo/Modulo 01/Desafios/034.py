"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%
"""
salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    print(f'O salário com aumento de 10% é de R${salario + (salario * 10/100):.2f}.')
else:
    print(f'O salário com aumento de 15% é de R${salario + (salario * 15/100):.2f}.')
    