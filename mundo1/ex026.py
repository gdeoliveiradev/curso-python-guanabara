# Faça um programa que leia uma frase pelo teclado e mostre: -Quantas vezes aparece a letra "A". |
# -Em que posição ela aparece a primeira vez. | -Em que posição ela aparece a ultima vez.

# Recebendo dados do usuario
frase = input('Digite uma frase: ').upper().strip()

# Processando dados para o resultado
quantidade_a = frase.count('A')

primeira_posicao = frase.find('A') + 1

ultima_posicao = frase.rfind('A') +1

# Exibindo resultado
print('\n--- Resultado ---')
print(f'A letra A aparece {quantidade_a} vezes')
print(f'A primeira letra A apareceu na posição: {primeira_posicao}')
print(f'A última letra A apareceu na posição: {ultima_posicao}')