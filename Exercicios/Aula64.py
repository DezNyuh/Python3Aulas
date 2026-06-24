import random

for _ in range(100):
    cpf_base = ''
    for i in range (9):
        cpf_base += str(random.randint(0,9))

    peso = 10
    soma_primeiro_digito = 0

    for digito in cpf_base:
        soma_primeiro_digito += int(digito) * peso
        peso -= 1

    primeiro_digito = (soma_primeiro_digito * 10) % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    cpf_para_segundo_digito = cpf_base + str(primeiro_digito)

    peso = 11
    soma_segundo_digito = 0

    for digito in cpf_para_segundo_digito:
        soma_segundo_digito += int(digito) * peso
        peso -= 1

    segundo_digito = (soma_segundo_digito * 10) % 11

    if segundo_digito > 9:
        segundo_digito = 0


    print(f'{cpf_base}{primeiro_digito}{segundo_digito}')