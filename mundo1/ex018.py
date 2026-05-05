# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importando biblioteca para o projeto
import math

# Recebendo dados do usuario
angulo_graus = float(input('Digite o valor do ângulo em graus: '))

# Convertendo de graus para radianos
angulo_radiano = math.radians(angulo_graus)

# Processando dados recebidos
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

# Exibindo resultado ao usuario
print('\n-----Resultado-----')
print(f'Ângulo informado: {angulo_graus}°')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')