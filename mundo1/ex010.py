###enunciado: crie um programa que leia quanto dinheiro uma pessoa tem na carteira
### e mostre quantos dólares ela pode comprar. considere: US$1,00 = R$3,27

#Exibindo apresentaçao para o usuario
print('É um prazer ter você aqui na Dollar Convert')

#constante cotação
COTACAO_DOLAR = 3.27

#recebendo dados do usuario
valor_reais = float(input('Digite quanto você tem em Reais (R$): '))

#processando dados recebidos e realizando conversao
valor_dolar = (valor_reais / COTACAO_DOLAR)

#Exibindo resultado para o usuario
print(f'Você tem R$ {valor_reais:.2f}')
print(f'Isso equivale a US$ {valor_dolar:.2f}')
