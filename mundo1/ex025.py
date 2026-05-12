# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Recebendo nome do usuario
nome = input('Digite seu nome completo: ').strip()

# Verificando se possui "SILVA"
tem_silva = 'SILVA' in nome.upper()

# Exibindo resultado
print('\n--- Resultado ---')
print(f'Seu nome possui "SILVA"? {tem_silva}')