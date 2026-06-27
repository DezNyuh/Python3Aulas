def soma (x, y, z=None):
    if z is not None: # SE Z NÃO FOR NONE ELE VAI USAR O VALOR DE Z
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=}{y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(x=9, z=7, y=0)