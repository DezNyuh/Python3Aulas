 # Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

caminho_arquivo = 'G:\\Curso Python 3+\\Exercicios\\'
caminho_arquivo += 'aula127.json'

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

Pessoa1 = Pessoa('Annie', 15, 1.40)
Pessoa2 = Pessoa('Irelia', 18, 1.65)
Pessoa3 = Pessoa('Yasuo', 22, 1.73)
lista_de_pessoas = [Pessoa1.__dict__, Pessoa2.__dict__, Pessoa3.__dict__]

with open(caminho_arquivo, 'w', encoding='utf8') as f:
    json.dump(lista_de_pessoas, f, indent=2, ensure_ascii=False )

