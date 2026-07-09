try:
    print('ABRIR O ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError ,Import Error')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')