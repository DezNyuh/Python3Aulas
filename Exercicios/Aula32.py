numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro!')


