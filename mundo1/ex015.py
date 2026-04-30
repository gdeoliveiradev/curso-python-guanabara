# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade  de dias
# pelos quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Recebendo dados do cliente
kilometragem = float(input('Digite a Kilometragem percorrida pelo veículo: '))
quantidade_dias = int(input('Digite o numero de dias do aluguel: '))

# Declarando constante para evitar numeros magicos
VALOR_DIA = 60
VALOR_KM = 0.15

# Processando dados para chegar ao resultado
valor_km = kilometragem * VALOR_KM
valor_dias = quantidade_dias * VALOR_DIA
valor_final = valor_km + valor_dias

# Exibindo o resultado para o cliente
print('\n------Informações------')
print(f'O carro rodou: {kilometragem:.1f} Km')
print(f'Quantidade de dias de aluguel: {quantidade_dias}')
print('\n----Pagamento----')
print(f'Valor a ser pago: R$ {valor_final:.2f}')
