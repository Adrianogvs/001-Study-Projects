"""
Utilização de condições aninhadas:

se isso acontecer:
   então faça isso
senao se:
   faça isso
senao:
   faça outra coisa


if carro.esquerda():
    bloco1
elif carro.direota():
    bloco2
elif carro.re():
    bloco3
else:
    bloco4

"""
print('-='*20)
print('Direções que o veículo possui:')
print('1 - Siga em Frente;')
print('2 - Vire a Direita;')
print('3 - Vire a Esquerda;')
print('4 - Marcha à ré;')
print('-='*20)

direcao = int(input('Informe o numero da direção que o veiculo deve seguir:'))

if direcao == 1:
    print('1 - Siga em Frente;')
elif direcao == 2:
    print('2 - Vire a Direita;')
elif direcao == 3:
    print('3 - Vire a Esquerda;')
else:
    print('4 - Marcha à ré;')
