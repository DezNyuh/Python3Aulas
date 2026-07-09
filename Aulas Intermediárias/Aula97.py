try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...
import Aula97_m

print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')