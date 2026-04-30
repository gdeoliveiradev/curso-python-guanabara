# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

# Recebendo dados do usuario
celsius = float(input('Digite a temperatura em °C: '))

# Declarando constante para evitar numeros magicos
MULTIPLICADOR = 1.8
VALOR_FIXO = 32

# Processando dados para realizar a conversão
fahrenheit = (celsius * MULTIPLICADOR) + VALOR_FIXO

# Exibindo resultado para usuario
print('\n--- Resultado ---')
print(f'{celsius:.1f}°C convertido para Fahrenheit fica: {fahrenheit:.1f}°F')
