"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
"""

velocidade = float(input('Informa a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado')
    print(f'A multa é de: {((velocidade - 80) * 7)}')

