""""
Estrutura de repetição:

-- Em portugol
laço c no intervalo (1,10)
    passo
pega

-- Em Python
for c in range(1,10):
    passo
pega
"""
"""
-- Em portugol
laço c no intervalo (0,3)
    passo
    pula
passo
pega

-- Em Python
for c in range(0,3):
    passo
    pula
passo
pega
"""

"""
-- Em portugol
laço c no intervalo (0,3)
    se moeda
        pega
    passo
    pula
passo
pega

-- Em Python
for c in range(0,3):
    if moeda:
        pega
    passo
    pula
passo
pega

"""

import os
os.system('cls')

# Criando varios Oi´s de forma convencional.
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')

# Criando varios Oi´s com estrutira de repetição FOR
for c in range(1,6):
    print('Oi')
print('FIM')