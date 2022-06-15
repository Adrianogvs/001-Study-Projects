"""
Faça um programa que leia a largura e a altura em metros, calcule a sua area e a quantidade de tinta necessária para pinta-la,
sabendo que cada litro de tinta pinta uma área de 2m².
"""

largura = float(input('Indorme a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem dimensão de {largura} x {altura} e sua área é de {area}m².')
print(f'Para pentar a parede precisa de {tinta} litros de tinta.')

