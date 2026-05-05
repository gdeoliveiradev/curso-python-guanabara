# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importando função da biblioteca para o projeto
from random import shuffle

# Recebendo dados do usúario
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

# Criando lista
turma = [aluno1, aluno2, aluno3, aluno4]

# Usando função shuffle para embaralhar a lista
shuffle(turma)

# Exibindo resultado ao usúario
print('\n--- A ordem sorteada foi: ---')
print(f'{turma}')
