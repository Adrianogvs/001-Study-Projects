"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
Coloque zero para pegar o ano da maquina.
"""
from datetime import date

ano = int(input('Informe o ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print(f'O ano {ano} é BIssexto.')
else:
    print(f'O ano {ano} não é BIssexto.')