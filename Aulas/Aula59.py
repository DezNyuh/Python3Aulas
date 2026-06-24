string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [ 
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],
]

p, b, *_, ap, c = lista
print(p, c, ap)

for nome in lista:
    print(nome, end=' ', sep=' ')

print(*lista)
print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')
