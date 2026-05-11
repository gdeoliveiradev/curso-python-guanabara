# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -O nome com todas letras maiusculas | -O nome com todas letras minusculas
# -Quantas letras ao todo (sem considerar espaços) | -Quantas letras tem o primeiro nome.

# Recebendo nome do usuario
nome_completo = input('Digite seu nome completo: ').strip()

# Processando dados
nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()

# Removendo espaços para contar apenas letras
quantidade_letras = len(nome_completo.replace(' ',''))

# Separando o primeiro nome
primeiro_nome = nome_completo.split()[0]

# Quantidade de letras do primeiro nome
quantidade_primeiro_nome = len(primeiro_nome)

# Exibindo resultados
print('\n--- Resultado ---')
print(f'Nome em maiúsculas: {nome_maiusculo}')
print(f'Nome em minúsculas: {nome_minusculo}')
print(f'Quantidade total de letras: {quantidade_letras}')
print(f'Quantidade de letras do primeiro nome: {quantidade_primeiro_nome}')
