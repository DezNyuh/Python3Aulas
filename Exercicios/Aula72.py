def multiplicacao(*args):
    total = 1
    for x in args:
        total *= x
    return total

multi1 = multiplicacao(1, 2, 3)
multi2 = multiplicacao(14, 25, 35)
print(multi1)
print(multi2)
print(1 * 2 * 3)
print(14 * 25 * 35)


def im_par(x):
    x = int(x)
    multiplo_de_dois = x % 2 == 0
    if multiplo_de_dois:
        return print(f'O número {x} é par')
    return print(f'O número {x} é impar')

escolha = input('Digite um número: ')
im_par(escolha)