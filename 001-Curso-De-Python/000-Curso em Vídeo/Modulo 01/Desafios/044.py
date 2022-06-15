"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
- a vista dinheiro ou cheque 10% desconto
- a vista no cartão 5% 
- 2x no cartão preço normal
- 3x ou mais no cartão 20%
"""
import os         
os.system('cls')   # Limpar tela antes de fazer as perguntas:

produto = float(input('Qual o preço do produto? R$'))
print('='*50)
print('1 - A vista com dinheiro ou cheque:')
print('2 - A vista no cartão:')
print('3 - Em duas veze sno cartão:')
print('4 - 3 vezes ou mais no cartão:')
print('='*50)
condicao = int(input('Qual a condução de pagamento de 1 a 4, conforme tabela acima: '))

if condicao > 0 and condicao <= 4:
    if condicao == 1:
        din_che = produto - (produto * 10/100)
        print(f'O valor a ser pago é de R${din_che:.2f}.')
    elif condicao == 2:
        cartao = produto - (produto * 5/100)
        print(f'O valor a ser pago é de R${cartao:.2f}.')
    elif condicao == 3:
        print(f'O valor a ser pago é de R${produto:.2f}.')
    else:
        cartao_mais_x = produto + (produto * 20/100)
        print(f'O valor a ser pago é de R${cartao_mais_x:.2f}.')
else:
    print('Condiçõao não existe no sistema, favor verificar outra condição.')