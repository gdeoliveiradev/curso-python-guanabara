# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: digite um numero: 1834 | unidade:4 | dezena:3 | centena:8 | milhar:1

# Recebendo dados do usuario
numero = int(input('Digite um número: '))

# Processando dados para o resultado desejado
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Exibindo resultado para o usúario
print('\n--- Resultado ---')
print(f'Analisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
