#Recepçao do Usuario
print('Bem-Vindo ao nosso conversor de metragem!')

#Coletando Informações
metros = float(input('Insira a medida em metros: '))

#constantes para usar no calculo de conversao
metro_para_centimetro = 100
metro_para_milimetro = 1000

#processando dados recebidos e convervetendo
centimetros = metros * metro_para_centimetro
milimetros = metros * metro_para_milimetro

#exibindo resultado para o usuario
print(f'A medida inserida foi: {metros} metros')
print(f'Equivale a {centimetros} centímetros e {milimetros} milímetros.')
