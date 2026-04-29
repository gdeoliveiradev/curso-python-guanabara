# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario, com 15% de aumento.

# Coletando dados do funcionario
salario = float(input('Digite seu salario em Reais (R$): '))

# Declarando constante para percentual 15%
AUMENTO_PERCENTUAL = 0.15

# Processando dados recebidos
valor_aumento = salario * AUMENTO_PERCENTUAL
novo_salario = salario + valor_aumento

# Exibindo resultados ao usuario

print (f'Salário antes do aumento: R${salario:.2f} ')
print (f'Valor do aumento: R${valor_aumento:.2f} ')
print (f'Salário após aumento: R${novo_salario:.2f}')
