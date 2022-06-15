"""
Faça um programa que leia a idade de um jovem de acordo com sua idade:
 - Se ele ainda vai se alistar ao serviço militar.
 - Se é a hora de se alistar.
 - se ja passou do tempo de se alistar

 Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

idade = int(input('Informe sua idade: '))
tempo = date.today().year
prazo = (tempo - idade) - (tempo - 18)


if idade > 18:
    print('Ja passou do tempo de se alistar')
elif idade == 18:
    print('É a hora de se alistar.')
else:
    print('Ele ainda vai se alistar ao serviço militar.')


if prazo > 0:
    print(f'Faltam {prazo} ano(s) para se alistar.')
elif prazo < 0:
    print(f'Se passaram {-1*(prazo)} ano(s) do prazo de alistamento.')    
else:
    print('Alistou no tempo certo.')