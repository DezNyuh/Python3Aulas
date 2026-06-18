while True:
    operacao_escolhida = input('Qual operação você quer usar? ')
    primeiro_numero_digitado = input('Digite o primeiro número: ')
    segundo_numero_digitado = input('Digite o segundo número: ')

    numeros_validos = False
    operacoes_permitidas = '*/+-'

    primeiro_numero = 0
    segundo_numero = 0

    try:
        primeiro_numero = float(primeiro_numero_digitado)
        segundo_numero = float(segundo_numero_digitado)
        numeros_validos = True

    except ValueError:
        numeros_validos = False

    if not numeros_validos:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if len(operacao_escolhida) != 1:
        print('Digite apenas um operador.')
        continue

    if operacao_escolhida not in operacoes_permitidas:
        print('Escolha uma operação válida.')
        continue

    if operacao_escolhida == '*':
        resultado = primeiro_numero * segundo_numero
        print(f'A multiplicação é {resultado}')

    elif operacao_escolhida == '+':
        resultado = primeiro_numero + segundo_numero
        print(f'A soma é {resultado}')

    elif operacao_escolhida == '-':
        resultado = primeiro_numero - segundo_numero
        print(f'A subtração é {resultado}')

    elif operacao_escolhida == '/':
        if segundo_numero == 0:
            print('Não é possível dividir por zero.')
            continue

        resultado = primeiro_numero / segundo_numero
        print(f'A divisão é {resultado}')

    deseja_sair = input('Quer [s]air? ').lower().startswith('s')

    if deseja_sair:
        break