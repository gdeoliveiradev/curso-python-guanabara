# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Coletando dados do usuario
valor_produto = float(input('Digite o valor do produto em Reais: '))

# Declarando constante para evitar numero magico
DESCONTO_PERCENTUAL = 0.05

# Processando os dados recebidos
valor_desconto = valor_produto * DESCONTO_PERCENTUAL
valor_final = valor_produto - valor_desconto

# Exibindo resultado para o usuario
print(f'Valor original do produto: R$ {valor_produto} ')
print(f'Valor do desconto: R$ {valor_desconto:.2f}' )
print(f'Valor final do produto: R$ {valor_final:.2f}' )
