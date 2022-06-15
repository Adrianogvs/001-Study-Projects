# Operadores aritimeticos

""""
+ soma
- subtração
* multiplicação
/ divisão
** poetencia
// divisão inteira
% Resto da divisão

"""
# Ordem de precedencia

""""
1º ()
2º **
3º * /  // %
4º +  -
"""

n1 = int(input("Digite: "))
n2 = int(input("Digite: "))

som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
dvt = n1 // n2
res = n1 % n2

print(f'A soma é {som}.')
print(f'A suntração é {sub}.')
print(f'A multiplicação é {mul}.')
print(f'A divisão é {div}.')
print(f'A potencia é {pot}.')
print(f'A divisão inteira é {dvt}.')
print(f'O resato da divisão é {res}.')