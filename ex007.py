#Coletando dados do aluno
nome = input('Digite seu nome: ')
materia = input('Digite o nome da materia que será consultada: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

#Processando dados recebidos
media = (nota1 + nota2) / 2
media_arredondada = round(media / 5) * 5
#Outra forma seria:
#soma = nota1 + nota2
#media = soma / 2

#Exibindo resultados
print(f'Olá, {nome}! É um prazer ter você por aqui!')
print(f'A sua média final em {materia} é: {media_arredondada}')
