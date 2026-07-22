class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor = 'Pink'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)