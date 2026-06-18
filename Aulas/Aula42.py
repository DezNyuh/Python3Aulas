frase = 'O Python é uma linguagem de programação multiparadigma Python foi criado por Guido van Rossum.'

indice = 0
maior_quantidade_encontrada = 0
letra_que_mais_apareceu = ''

while indice < len(frase):
    letra_analisada = frase[indice]

    if letra_analisada == ' ':
        indice += 1
        continue

    quantidade_da_letra = frase.count(letra_analisada)

    if quantidade_da_letra > maior_quantidade_encontrada:
        maior_quantidade_encontrada = quantidade_da_letra
        letra_que_mais_apareceu = letra_analisada

    indice += 1

print(
    f'A letra que apareceu mais vezes foi "{letra_que_mais_apareceu}" '
    f'e ela apareceu {maior_quantidade_encontrada} vezes.'
)