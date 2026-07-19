# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def print_lista(lista):
    for i in lista:
        print(i)


lista = []
desfazer = []

while True:
    print('\nComandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ')
    
    if comando == "listar":
        if not lista:
            print('\nTAREFAS: Nenhuma tarefa cadastrada.')
        else:
            print('\nTAREFAS:')
            print_lista(lista)
        continue

    elif comando == 'desfazer':
        if not lista:
            print('\nNada a desfazer')
        else:
            desfazer.append(lista.pop())
        print_lista(lista)
        continue

    elif comando == 'refazer':
        if not desfazer:
            print('\nNada a refazer')
        else:
            lista.append(desfazer.pop())
        print_lista(lista)
        continue

    elif comando == 'sair':
        break

    lista.append(comando)
    print('\nTAREFAS:')
    print_lista(lista)