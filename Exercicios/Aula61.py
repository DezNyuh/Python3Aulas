while True:
    try:
        cpf_enviado = input('Digite um CPF: ')
        cpf_enviado = cpf_enviado.replace('.', '').replace('-', '')

        repetiu = cpf_enviado[0] * len(cpf_enviado)
        print(repetiu)
        if cpf_enviado == repetiu:
            print('CPF Inválido vi!')
            continue

        if len(cpf_enviado) != 11 or not cpf_enviado.isdigit():
            print('Digite um CPF válido')
            continue

        cpf_base = cpf_enviado[:9]

        # Primeiro dígito
        peso = 10
        soma_primeiro_digito = 0

        for digito in cpf_base:
            soma_primeiro_digito += int(digito) * peso
            peso -= 1

        primeiro_digito = (soma_primeiro_digito * 10) % 11

        if primeiro_digito > 9:
            primeiro_digito = 0

        print(f'Primeiro dígito: {primeiro_digito}')

        # Segundo dígito
        cpf_para_segundo_digito = cpf_base + str(primeiro_digito)

        peso = 11
        soma_segundo_digito = 0

        for digito in cpf_para_segundo_digito:
            soma_segundo_digito += int(digito) * peso
            peso -= 1

        segundo_digito = (soma_segundo_digito * 10) % 11

        if segundo_digito > 9:
            segundo_digito = 0

        print(f'Segundo dígito: {segundo_digito}')

        novo_cpf = f'{cpf_base}{primeiro_digito}{segundo_digito}'
        if novo_cpf == cpf_enviado:
            print('CPF Válido!')
        else:
            print('CPF Inválido!')


    except Exception as erro:
        print(f'Erro: {erro}')