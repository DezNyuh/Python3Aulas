nome = 'ERLING HAALAND'

novo_nome = ''
indice = 0

while len(nome) > indice:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
print(novo_nome)

