# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².

# Coletando dados do usuario
largura_parede = float(input('Digite a largura da parede em metros: '))
altura_parede = float(input('Digite a altura da parede em metros: '))

# Constante de rendimento da tinta (1L pinta 2m²)
rendimento_tinta = 2

# Processando e preparando dados recebidos
area_parede = (largura_parede * altura_parede)
litros_tinta = (area_parede / rendimento_tinta)

# Exibindo para usuario resultado da consulta
print(f'Largura: {largura_parede:.2f} m')
print(f'Altura {altura_parede:.2f} m')
print(f'Sua parede tem {area_parede:.2f} m²')
print(f'Você precisa de {litros_tinta} litros de tinta para pintá-la')