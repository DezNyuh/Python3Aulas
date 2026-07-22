from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é privado'
        
    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('_metodo_private')
        return '_metodo_private'

f = Foo()
# print(f._protected) só para uso interno
# print(f._metodo_protected) só para uso interno
# print(f.public)
print(f.metodo_publico())
# print(f._Foo__metodo_private()) não deve ser usado