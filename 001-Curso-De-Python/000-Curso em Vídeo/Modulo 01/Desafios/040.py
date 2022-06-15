"""
Crie um programa que leia duas notas de um alino e calcule sua média, mostrando uma mensagem no final de acordo com a media atimgida.
- Média abaixo de 5.0 REPROVADO
- Media entre 5.0 e 6.9 RECUPARAÇÃO
- Média 7.0 APROVADO
"""

n1 = float(input('Informe a nota1:'))
n2 = float(input('Informe a nota2:'))
media = (n1 + n2) / 2
aprovado = media >= 7.0
reprovado = media < 5.0


if aprovado == True:
    print('Aprovado.')
elif reprovado == True:
    print('Reprovado.')
else:
    print('Recuparação.')