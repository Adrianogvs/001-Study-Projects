"""
Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
"""
num1 = int(input('Informe o primeio  numero: '))
num2 = int(input('Informe o segundo  numero: '))
num3 = int(input('Informe o terceiro numero: '))

# Verificando o menor valor.
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O menor valor digitado foi {menor}.')

# Verificando o maior valor.
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O maior valor digitado foi {maior}.')





"""
if num1 > num2 and num1 > num3:
    print(f'O primeiro numero {num1}, é maior que o segundo {num2} e o terceiro {num3}')
if num2 > num1 and num2 > num3:
    print(f'O segundo numero {num2}, é maior que o primeiro {num1} e o terceiro {num3}')
if num3 > num1 and num3 > num2:
    print(f'O terceiro numero {num3}, é maior que o primeiro {num1} e o segundo {num2}')
if num1 == num2 and num3 < num1 and num3 < num2:
    print(f'O priemiro e segundo numeros são iguais e o terceiro é menor que o primeiro e segundo numeros.')
if num2 == num3 and num1 < num2 and num1 < num3:
    print(f'O segundo e terceiro numeros são iguais e o primeiro é menor que o segundo e o terceiro numeros.')
if num1 == num3 and num2 < num1 and num2 < num3:
    print(f'O primeiro e terceiro numeros são iguais e o segundo é menor que o primeiro e terceiro numeros.')
if num1 == num2 and num1 == num3 and num2 == num3:
    print('Os tres numeros são iguais.')
if num1 < num2 and num1 < num3:
    print(f'O primeiro numero {num1}, é menor que o segundo {num2} e o terceiro {num3}')
if num2 < num1 and num2 < num3:
    print(f'O segundo numero {num2}, é menor que o primeiro {num1} e o terceiro {num3}')
if num3 < num1 and num3 < num2:
    print(f'O terceiro numero {num3}, é menor que o primeiro {num1} e o segundo {num2}')
if num1 == num2 and num3 > num1 and num3 > num2:
    print(f'O priemiro e segundo numeros são iguais e o terceiro é maior que o primeiro e segundo numeros.')
if num2 == num3 and num1 > num2 and num1 > num3:
    print(f'O segundo e terceiro numeros são iguais e o primeiro é maior que o segundo e o terceiro numeros.')
if num1 == num3 and num2 > num1 and num2 > num3:
    print(f'O primeiro e terceiro numeros são iguais e o segundo é maior que o primeiro e terceiro numeros.')
    
"""