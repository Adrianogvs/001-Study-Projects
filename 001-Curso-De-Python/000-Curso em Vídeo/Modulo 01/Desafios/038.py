"""
Escreva um porgrama que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não Existe valor maior, os dois são iguais.
"""
num1 = int(input('Informe um numero inteiro. '))
num2 = int(input('Informe um numero inteiro. '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior')
else:
    print('Não Existe valor maior, os dois são iguais.')