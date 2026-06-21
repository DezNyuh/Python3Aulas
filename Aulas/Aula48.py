string = 'ABCDE'
lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista[-3])
lista[-3] = 'Maria'
print(bool(lista))
print(lista, type(lista))
print(lista[2].upper(), type(lista[2]), type(lista[3]))

lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
numero = lista[2]
print(lista)
print(numero)
lista.append(50) 
lista.pop() #remove o ultimo item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido:', ultimo_valor)

lista = [10, 20, 30, 40]
lista.append('Luiz') 
nome = lista.pop() #remove o ultimo item da lista
lista.append(1233) #adiciona um item em ultimo lugar
del lista[-1] #deleta um item da lista
lista.clear() #limpa a lista
lista.insert(0, 5) #insere no local do indice
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #cria uma nova lista

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)