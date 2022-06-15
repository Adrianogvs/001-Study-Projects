"""
Crie um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o emprestimo será negado.
"""
"""
1º. Criar variáveis:
   - valor_casa
   - salario
   - anos
   - prestacao
   - porcentagem_salario

2º. Fazer calculos:
   - prestacao = valor_casa / (12 * anos)
   - porcentagem_salario = salario - (salario - (salario*30/100))

3º. Cria a logica:
   - 
"""

valor_casa = float(input('Informe o valor da casa R$: '))
salario = float(input('Informe o seu salario R$: '))
anos = int(input('Informe a quantidade de prestações em anos: '))

prestacao = valor_casa / (12 * anos)
porcentagem_salario = salario - (salario - (salario*30/100))

print(f'O valor da prestação é de R${prestacao:.2f}.')
print(f'30% do seu slario é R${porcentagem_salario:.2f}.')

if prestacao > porcentagem_salario:
    print('Emprestimo NEGADO, pois ultrapssa 30% do seu salario mensal.')
elif prestacao == porcentagem_salario:
    print('A prestação do imovel é igula a 30% do seu salario, vamos conceder o emprestimo.')
else:
    print('PARABÉNS!!! Emprestimo concedido.')
