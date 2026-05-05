# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira
# Ex: Digite um número:6.127 - O numero 6.127 tem a parte inteira 6.

# Importando modulo
from math import trunc

# Receber dados do usuario
numero = float(input('Digite um número: '))

# Processando dados para o resultado (poderia ser feito c/floor e int)
inteiro = trunc(numero)

# Exibindo resultado ao usuario
print('\n----Resultado----')
print(f'O número {numero:.3f} tem a parte Inteira {inteiro}')