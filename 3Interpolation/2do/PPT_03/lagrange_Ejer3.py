#     x , y
p1 = (-1, 3)
p2 = (0, -7)
p3 = (4, 7)
p4 = (5, 11)

#valor a buscar en x
valorX = 2


def fn():
    uno = ((valorX - p2[0]) / (p1[0] - p2[0]))
    dos = ((valorX - p3[0]) / (p1[0] - p3[0]))
    tres = ((valorX - p4[0]) / (p1[0] - p4[0]))
    resultado1 = uno * dos * tres * p1[1]

    cuatro = ((valorX - p1[0]) / (p2[0] - p1[0]))
    cinco = ((valorX - p3[0]) / (p2[0] - p3[0]))
    seis = ((valorX - p4[0]) / (p2[0] - p4[0]))
    resultado2 = cuatro * cinco * seis * p2[1]

    siete = ((valorX - p1[0]) / (p3[0] - p1[0]))
    ocho = ((valorX - p2[0]) / (p3[0] - p2[0]))
    nueve = ((valorX - p4[0]) / (p3[0] - p4[0]))
    resultado3 = siete * ocho * nueve * p3[1]

    diez = ((valorX - p1[0]) / (p4[0] - p1[0]))
    once = ((valorX - p2[0]) / (p4[0] - p2[0]))
    doce = ((valorX - p3[0]) / (p4[0] - p3[0]))
    resultado4 = diez * once * doce * p4[1]

    return resultado1 + resultado2 + resultado3 + resultado4

print('\nMETODO INTERPOLACIÓN DE LAGRANGE\n')
print("X=", valorX, " Y=", fn())