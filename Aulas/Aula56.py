frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_palavras):
    lista_frases.append(lista_palavras[i].strip()) # rstrip corta o espaço na direita, l na esquerda e strip corta todos os espaços ao lado

print(lista_frases)
print(lista_palavras)

frases_unidas = ','.join(lista_palavras)
print(frases_unidas)
