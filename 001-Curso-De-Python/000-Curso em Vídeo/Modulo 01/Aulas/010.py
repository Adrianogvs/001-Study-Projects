"""
Estruturas condicionais com média.
"""

n1 = float(input('Digite a priemira nota: '))
n2 = float(input('Digite a priemira nota: '))
m = (n1 + n2)/2

print(f'A sua média foi {m:.2f}.')

if m >= 6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('Estude mais!')