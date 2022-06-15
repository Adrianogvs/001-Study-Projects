"""
Peso e altura
calcular IMC
mostrar status, sendo:

- abaixo 18.5 = abaixo do peso
- entre 18.5 e 25 = peso idela
- 25 a 30 = sobrepeso
- 30 a 40 = obsidade
- acima de 40 = obsidade morbida
"""

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = (peso/(altura * altura))

peso_abaixo = imc < 18.5 
peso_ideal  = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidade = imc >= 30 and imc < 40

if peso_abaixo == True:
    print(f'Seu IMC é {imc:.2f}.')
    print('abaixo do peso')
elif peso_ideal == True:
    print(f'Seu IMC é {imc:.2f}.')
    print('peso idela')
elif sobrepeso == True:
    print(f'Seu IMC é {imc:.2f}.')
    print('sobrepeso')
elif obesidade == True:
    print(f'Seu IMC é {imc:.2f}.')
    print('obsidade')
else:
    print(f'Seu IMC é {imc:.2f}.')
    print('obsidade morbida')
