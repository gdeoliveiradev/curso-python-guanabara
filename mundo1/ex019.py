# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# Importando função da biblioteca para o projeto
from random import choice

# Recebendo informações do usuario
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

# Criando a lista para o "sorteio"
turma = [aluno1, aluno2, aluno3, aluno4]

# Realizando seleção por "sorteio"
escolhido = choice(turma)

# Exibindo resultado ao usuario
print('\n--- Resultado ---')
print(f'O aluno escolhido foi: {escolhido}')
