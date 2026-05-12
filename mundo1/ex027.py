# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza | primeiro: Ana | último: Souza

# Recebendo dados do usuario
nome_completo = input('Digite seu nome completo: ').strip()

# Separando nomes em listas
nome_separado = nome_completo.split()

# Pegando primeiro e ultimo nome
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

# Exibindo resultado para o usuario
print('\n--- Resultado ---')
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')

