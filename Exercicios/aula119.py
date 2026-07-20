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
import os
import json

PATH_DIR = 'G:\\Curso Python 3+\\Exercicios\\'
NAME_DIR = 'aula119.json'
caminho_arquivo = PATH_DIR + NAME_DIR

def print_lista(lista):
    for i in lista:
        print(i)

def escrever_JSON(lista):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)

lista = []
desfazer = []

try:    
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        lista = json.load(arquivo)
except json.decoder.JSONDecodeError:
    escrever_JSON(lista)
except FileNotFoundError:
    escrever_JSON(lista)


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
            escrever_JSON(lista)
        print_lista(lista)
        continue

    elif comando == 'refazer':
        if not desfazer:
            print('\nNada a refazer')
        else:
            lista.append(desfazer.pop())
            escrever_JSON(lista)
        print_lista(lista)
        continue

    elif comando == 'clear':
        os.system('cls')
        continue

    elif comando == 'sair':
        break
    
    lista.append(comando)
    print('\nTAREFAS:')
    print_lista(lista)

    escrever_JSON(lista)