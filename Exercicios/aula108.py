lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def somar_lista(lista1, lista2):
    menor = min(len(lista1), len(lista2))
    return [
        (lista1[i] + lista2[i]) for i in range(menor)
    ]


print(somar_lista(lista_a, lista_b))