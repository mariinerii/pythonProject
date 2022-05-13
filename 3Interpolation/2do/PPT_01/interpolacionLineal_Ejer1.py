p1=(-4,-2)
#x0,y0
p2=(1,5)
#x1,y1
y=3.7

def fn():
    a= ((y)-(p1[1])) * ((p2[0])-(p1[0]))
    b=((p2[1]) - (p1[1]))
    resultado = ((p1[0]) + (a/b))
    return resultado

print("X= ",fn())