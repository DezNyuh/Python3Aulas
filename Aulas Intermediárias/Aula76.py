# Cria um dicionário vazio
pessoa = {}

# Armazena o nome da chave em uma variável
chave = 'nome'

# Adiciona a chave "nome" com o valor "Luiz Otávio"
pessoa[chave] = 'Luiz Otávio'

# Adiciona a chave "sobrenome" com o valor "Miranda"
pessoa['sobrenome'] = 'Miranda'

# Exibe o valor da chave "nome"
print(pessoa[chave])

# Altera o valor da chave "nome"
pessoa[chave] = 'Maria'

# Remove a chave "sobrenome" do dicionário
del pessoa['sobrenome']

# Exibe o dicionário após a remoção da chave
print(pessoa)

# Exibe o valor da chave "nome"
print(pessoa['nome'])

# Tenta obter o valor da chave "sobrenome"
# Se ela não existir, retorna "Não existe"
print(pessoa.get('sobrenome', 'Não existe'))

# Verifica se a chave "sobrenome" existe no dicionário
# O método get() retorna None quando a chave não existe
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

#Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values = iterável com os valores
# items - iterável com chaves e valores
# set default - adicionar valor se a chave não existe
# copy - retorna uma cópia rasa(shallow copy)
# get - obtém  uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o utlimo item adicionado
# update - atualiza um dicionário com outro

import copy #cópia profunda

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 3',
    'idade': 900,
}

print(len(pessoa))

print(tuple(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 'Não existe')
print(pessoa['idade'])

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)


d1 = {'c1': 1,
      'c2': 2,
      'l1': [0, 1, 2],
      }

d2 = copy.deepcopy(d1)


d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',

}
print(p1['nome'])
print(p1.get('nome', 'Não existe')) # se não existir nome

#nome = p1.pop('nome')
#print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30,
})

p1.update(nome='novo valor', idade=30)

tupla = ('nome', 'novo valor'), ('idade', 30)
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)