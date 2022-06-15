"""
Crie uma tabuada
"""

num = int(input('Informe um numero: '))

i = 0
while i <= 10:
    print(f'{num} X {i:2} = {num * i:.0f}')
    i += 1