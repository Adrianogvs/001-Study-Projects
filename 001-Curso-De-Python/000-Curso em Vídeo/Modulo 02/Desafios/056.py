"""
Descreva um porgrama que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
a) A media de idade dos grupo
b) Qual é o nome do homem mais velho
c) Quantas mulheres tem menos de 20 anos

"""
import os
os.system('cls')

media = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ' '
totalmulher20 = 0

for i in range(1,5):
    nome = str(input('Informe o nome: ')).strip().upper()
    idade = int(input('Informe a idade: '))
    sexo =  str(input('Informe o sexo [M/F]: ')).strip().upper()
    media += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = media / 4
print(f'A media de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totalmulher20} mulheres com menos de 20 anos.')






