"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
"""
preço = float(input('Informe o valor:'))

print(f'O valor informado com desconto de 5% é de R${preço * ( ( -5 / 100 ) +1 ):.2f}.')

