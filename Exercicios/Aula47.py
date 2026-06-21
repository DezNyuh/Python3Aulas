import os

palavra_secreta = 'perfume'
letra_acertadas = ''
tentativa = 0

while True:
    letra_tentativa = input('Digite uma letra: ')
    tentativa += 1

    if len(letra_tentativa) > 1:
        print('Digite apenas uma letra! ')
        continue

    if letra_tentativa in palavra_secreta:
        letra_acertadas += letra_tentativa

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU, PARABÉNS!!')
        print(f'A palavra era {palavra_secreta}')
        print(f'TENTATIVAS: {tentativa}')
        letra_acertadas = ''
        tentativa = 0