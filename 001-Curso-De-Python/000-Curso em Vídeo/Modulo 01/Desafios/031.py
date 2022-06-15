"""
Desenvolva um programa que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200km e R$045 paa viagens mais longas.
"""
distancia = float(input('Qual a distancia da viagem em KM? '))

if distancia <= 200:
    print(f'O preço da passagem até 200 km é de R${distancia * 0.50:.2f}.')
else:
    print(f'O preço da passagem até 200 km é de R${distancia * 0.45:.2f}.')