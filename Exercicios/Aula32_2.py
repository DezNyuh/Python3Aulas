hora = input('Qual é a hora? ')
minuto = input('Qual é o minuto? ')

try:
    hora.isdigit()
    hora_int = int(hora)
    if hora_int <= 11:
        print(f'A hora certa é {hora}:{minuto}, bom dia!')
    elif 11 < hora_int <= 17:
        print(f'A hora certa é {hora}:{minuto}, boa tarde!')
    elif 18 < hora_int <= 23:
        print(f'A hora certa é {hora}:{minuto}, boa noite!')
    else: 
        print('Horário Inválido!')
except:
    print('Por favor, digite um horário correto.')