nome = 'Otávio'
print(nome[2])
print(nome[-2])
print('á' in nome)
print('z' in nome)
print(10 * '-')
print('vio' not in nome)
print('vio' in nome)
print('zero' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')