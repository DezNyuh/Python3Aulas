import json

CAMINHO_ARQUIVO = 'G:\\Curso Python 3+\\Exercicios\\'
CAMINHO_ARQUIVO += 'aula127.json'


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    lista_de_dados = json.load(arquivo)

lista_de_pessoas = []

for dados_pessoa in lista_de_dados:
    lista_de_pessoas.append(Pessoa(**dados_pessoa))

for pessoa in lista_de_pessoas:
    print(pessoa.nome, pessoa.idade, pessoa.altura)