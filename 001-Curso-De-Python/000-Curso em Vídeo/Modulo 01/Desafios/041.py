"""
Programa que leia a idade e mostre as seguintes categorias:
- até 9 anos: Mirin
- ate 14 anos: Infantil
- até 19 anos: Junior
- até 20 Anos: Senior
- Acima: Master
"""

idade = int(input('Informe a idade:'))

mirin    = idade <= 9
infantil = idade > 9 and idade <= 14
junior   = idade > 14 and idade <= 19
senior   = idade > 19 and idade <= 20
master   = idade > 20

if mirin != False:
    print('Mirin')
elif infantil != False:
    print('Infantil')
elif junior != False:
    print('Junior')
elif senior != False:
    print('Senior')
else:
    print('Master')
