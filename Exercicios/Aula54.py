import os

lista_de_compras = []

while True:
    print('\nSelecione uma opção')
    opcao = input('[I]nserir, [A]pagar, [L]istar: ').upper()

    if len(opcao) > 1:
        print('Digite apenas uma letra!')
        continue

    if opcao == 'I':
        os.system('cls')
        valor = input('\nValor: ')
        lista_de_compras.append(valor)
        for valor, nome in enumerate(lista_de_compras):
            print(valor, nome)

    elif opcao == 'A':
        indice = input('Escolha o índice para apagar: ')
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice < len(lista_de_compras):
                lista_de_compras.pop(indice)
                print('Item removido!')
                for valor, nome in enumerate(lista_de_compras):
                    print(valor, nome)
            else:
                print('Índice Inválido!')
        else:
            print('Digite um número válido.')

    elif opcao == 'L':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Nada para listar!')

        for valor, nome in enumerate(lista_de_compras):
            print(valor, nome)

    else: print('Por favor, escolha I, A ou L')

