# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".

# Recebendo o nome da cidade
cidade = input('Digite o nome da cidade:').strip()

# Verificando se começa com "SANTO"
resultado = cidade.upper().startswith('SANTO')

# Exibindo Resultado
print('\n--- Resultado ---')
print(f'A cidade começa com "SANTO"? {resultado}')
