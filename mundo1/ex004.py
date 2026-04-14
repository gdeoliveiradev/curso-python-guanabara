algo = input('Digite Algo:')

print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'é alfabetico? {algo.isalpha()}')
print(f'é numerico? {algo.isnumeric()}')
print(f'é AlfaNumerico? {algo.isalnum()}')
print(f'é maiusculo? {algo.isupper()}')
print(f'é minusculo? {algo.islower()}')

#abaixo somente teste
print(f'O valor digitado foi: {algo}{', obrigado por utilizar este teste!'}')