"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
import os
os.system('cls')

menu = 0
while menu != 5:
    def menus ():
        num1 = int(input('Informe o primeiro valor: '))
        num2 = int(input('Informe o segundo valor:'))
        print("""
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
        """)
    menu = int(input('Informe qual operação você deseja realizar conforme menu acima: '))

    resultado = 0

    if menu == 1:
        resultado = num1 + num2
        print(resultado)
    elif menu == 2:
        resultado = num1 * num2
        print(resultado)
    elif menu == 3:
        if num1 > num2:
            resultado = 'O primeiro', num1, 'é maior que o segundo', num2,'.'
            print(resultado)
        elif num1 == num2:
            resultado = 'Os dois numeros são iguais'
            print(resultado)
        else:
            resultado = 'O segundo númemro', num2 ,'é maior que o primeiro', num1,'.'
            print(resultado)
    elif menu == 4:
        menus
    elif menu == 5:
        print('Fim do programa!')
    else:
        print('Opção invalida!')
print('Fim do programa, ...')
