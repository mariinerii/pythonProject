p1 =(-2,4)
#x0,y0

p2 =(-1,-2)
#x1,y1

p3 =(3 ,5)
#x2,y2

p4 =(4.3 ,11)
#x3,y3

x= 7.7

def fn():

    #y1-y0
    #_______
    #x1-xo

    a= ( (p2[1]) - (p1[1]) ) / ( (p2[0]) - (p1[0]) )
    return a

def fn2():

        # y2-y1
        # _______
        # x2-x1
        b = ((p3[1]) - (p2[1])) / ((p3[0]) - (p2[0]) )
        c= b - fn()
        d = c / ((p3[0]) -(p1[0]))

        return d

def fn3():
    # y3-y2
    # _______
    # x3-x2

    a = ((p4[1]) - (p3[1])) / ((p4[0]) - (p3[0]))  #y3 y y2

    b = ((p3[1]) - (p2[1])) / ((p3[0]) - (p2[0]))  #y2 y y1

    c = a - b
    c2 = c / ( (p4[0]) - (p2[0]) )
    d = c2 - fn2()
    e = d / ((p4[0]) - (p1[0]))

    return e

def fn4():
    y = p1[1] + fn() * (x - (p1[0])) + fn2() * (x - (p1[0])) * (x - (p2[0])) + fn3() * (x - (p1[0])) * (x - (p2[0])) * (x - (p3[0]))
    return y

print('funcion b1=',fn())
print('funcion b2=',fn2())
print('funcion b3=',fn3())
print('RESULTADO: ',fn4())
