while True:

    cpf = input('Digite um CPF: ')

    try:

        cpf = cpf.replace('.', '').replace('-', '')

        if len(cpf) > 9 or not cpf.isdigit():
             print('Digite uma sequência de 8 números')
             continue
        
        if cpf.isdigit():
            multiplicação = 10
            resultado_soma = 0

            for numero in cpf:
                numero = int(numero)
                resultado_mult = numero * multiplicação
                multiplicação -= 1
                resultado_soma += resultado_mult

            if multiplicação <= 2:
                resultado_x10 = resultado_soma * 10
                resultado_rest = resultado_x10 % 11

            if resultado_rest > 9:
                        resultado_rest = 0
    
            print (resultado_rest)

    except Exception as erro:
        print('Erro:', erro)

