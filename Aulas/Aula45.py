texto = 'Luiz'
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

#SÃO A MESMA COISA

for letra in texto:
    print(letra)