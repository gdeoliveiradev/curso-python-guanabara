# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#  calcule e mostre o comprimento da hipotenusa.

# Importando modulo para o projeto
from math import hypot

# Recebendo dados do usuario
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# Processando dados recebidosS
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Exibindo resultado ao usuario
print('\n---Resultado---')
print(f'Cateto oposto: {cateto_oposto}')
print(f'Cateto adjacente: {cateto_adjacente}')
print(f'Hipotenusa: {hipotenusa:.2f}')