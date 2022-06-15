"""
Faça um porgrama que leia o sexo de uma pessoa, mas so aceite os valores M e F
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
import os
os.system('cls')

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidosm informe seu sexo novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado corrretamente.')

