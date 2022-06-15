# Calculadora em Python
import time
import os
os.system('cls')

def menu():
    print('=' * 43)
    print('|  Escolha uma das Opções abaixo:         |')
    print('|','-' * 39,                             '|')
    print('| [1] Soma                                |')
    print('| [2] Subtração                           |')
    print('| [3] Multiplicação                       |')
    print('| [4] Divisão                             |')
    print('| [5] Sair                                |')
    print('=' * 43)

opcao = 0
while opcao != 5:
    time.sleep(3)
    os.system('cls')
    
    menu()
    
    opcao = int(input('Informe uma das opções acima de [1] à [5]: '))

    if opcao == 5:
        print('Você escolheu a opção [5], calculadora sendo finalizada.')
        print('Saindo...')
    elif opcao <= 0 or opcao > 5:
            print('Opção invalida!')
            print('Tente novamente!')
    else:
        num1 = int(input('Informe o numero: '))
        num2 = int(input('Informe outro numero: '))
        if opcao == 1:
            soma = num1 + num2
            print(f'A soma de {num1} + {num2} é igual à: {soma}.')
        elif opcao == 2:
            subtracao = num1 - num2
            print(f'A subtração de {num1} - {num2} é igual à: {subtracao}.')
        elif opcao == 3:
            multiplicacao = num1 * num2
            print(f'A multiplicação de {num1} + {num2} é igual à: {multiplicacao}.')
        elif opcao == 4:
            if num2 == 0:
                print('Não existe divisão por Zero.')
            else:
                divisao = num1 / num2
                print(f'A divisao de {num1} / {num2} é igual à: {divisao}.')
