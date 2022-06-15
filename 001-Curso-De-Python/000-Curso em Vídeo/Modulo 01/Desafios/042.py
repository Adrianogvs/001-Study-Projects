"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.
"""
r1 = float(input('Informa o valor para a reta 1: '))
r2 = float(input('Informa o valor para a reta 2: '))
r3 = float(input('Informa o valor para a reta 3: '))

"""
equilatero = r1 == r2 and r1 == r3 and r2 == r3
isosceles = r1 == r2 or r1 == r3 or r2 == r3
escaleno = r1 != r2 and r1 != r3 and r2 != r3 

if equilatero == True and ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print(f'É possivel formar um triangulo Equilatero.')
elif isosceles == True and ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print(f'É possivel formar um triangulo Isosceles.')
elif escaleno == True and ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print(f'É possivel formar um triangulo Escaleno.')
else:
    print(f'Não é possível formar um triangulo.')
    
"""
"""
Outra forma de fazer:
"""

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2  != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo.')