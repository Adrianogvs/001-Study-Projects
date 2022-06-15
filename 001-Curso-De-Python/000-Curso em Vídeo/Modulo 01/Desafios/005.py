"""
Crie um programa que leia quanto dinheito uma pessoa tem na carteira e mostra o quantos dolares ela pode comprar.

Cotação dolar a U$5.85
"""

dinheiro = float(input('Quanto de dinheto você tem na carteira? '))

print(f'Com este valor voce pode comprar U${(dinheiro / 5.85):.2f} dolare(s).')

