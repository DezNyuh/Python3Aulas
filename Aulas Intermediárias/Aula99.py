# from sys import path

# import Aula99_package.modulo
# from Aula99_package.modulo import soma_do_modulo
# from Aula99_package import modulo
# from Aula99_package.modulo import *

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(Aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel) 
# print(nova_variavel)
# from Aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from Aula99_package import soma_do_modulo, falar_oi

print(soma_do_modulo(2, 3))
falar_oi()