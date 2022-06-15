"""
Crie um programa que le um numero e informe o seu antecessor e sucessor.
"""
from ast import Num


num = int(input("Informe um numero: "))

print(f'O numero digitado foi {num}.')
print(f'O numero antecesso ao numero {num} é o numero {num - 1}.')
print(f'O numero sucesso ao numeo {num} é o numero {num + 1}.')