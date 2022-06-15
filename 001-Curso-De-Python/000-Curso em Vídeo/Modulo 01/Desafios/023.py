{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.\\n Exemplo:\\n\\n 1834\\n\\n Unidade = 4\\n Dezena  = 3\\n Centena = 8\\n Milhar  = 1\\n'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    " Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.\n",
    " Exemplo:\n",
    "\n",
    " 1834\n",
    "\n",
    " Unidade = 4\n",
    " Dezena  = 3\n",
    " Centena = 8\n",
    " Milhar  = 1\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criando variável\n",
    "numero = int(input('Informe um numero de 0 a 9999.'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1234\n"
     ]
    }
   ],
   "source": [
    "# Cáclulo (dividindo o valor e achando o resto da divisão)\n",
    "u = numero //    1 % 10\n",
    "d = numero //   10 % 10\n",
    "c = numero //  100 % 10\n",
    "m = numero // 1000 % 10\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Milhar  = 1\n",
      "Centena = 2\n",
      "Dezena  = 3\n",
      "Unidade = 4\n"
     ]
    }
   ],
   "source": [
    "# Resultado \n",
    "\n",
    "print(f'Milhar  = {m}')\n",
    "print(f'Centena = {c}')\n",
    "print(f'Dezena  = {d}')\n",
    "print(f'Unidade = {u}')\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "3bb03df91ec1981933db38e9cd509750fbcc8736096f2f96108c21544a6fd7c7"
  },
  "kernelspec": {
   "display_name": "Python 3.10.2 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
