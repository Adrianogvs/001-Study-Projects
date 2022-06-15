"""
Desenvolva um porgrama que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.
"""
import os
os.system('cls')

sum = 0
cont = 0
for i in range(1,7):
    num = int(input('Informe um nuemero: '))
    if num % 2 != 1:
        sum += num
        cont += 1
print(f'Você informou {cont} pares e a soma deles são {sum}.')