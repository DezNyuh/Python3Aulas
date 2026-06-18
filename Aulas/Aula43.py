texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1


text = 'Python'
novo_texto =''
for letra in text:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')