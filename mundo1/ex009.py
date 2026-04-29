#apresentação e recepção do usuario
print('Bom proveito da nossa tabuada digital!')

#Recebendo informações do usuario
numero = int(input('Digite o numero inteiro desejado: '))
numero_limite = int(input('Digite o numero que quer limitar a tabuada: '))

#exibindo ao usuario oque foi solicitado
print(f'A tabuada do {numero} é: ')

#usando 'for' para apresentar a tabuada ate numero solicitado pelo usuario
for i in range(1, numero_limite + 1):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
