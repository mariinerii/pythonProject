from math import sin

def f(x):
    return (sin(2*x)**3)/((x**4)+1)

x0=2.45

h1=0.001
r1=(f(x0)-(f(x0-h1)))/(h1)
print('r1 =',r1)

h2=0.0001
r2=(f(x0)-(f(x0-h2)))/(h2)
print('r2 =',r2)

h3=0.00001
r3=(f(x0)-(f(x0-h3)))/(h3)
print('r3 =',r3)

h4=0.000001
r4=(f(x0)-(f(x0-h4)))/(h4)
print('r4 =',r4)

h5=0.0000001
r5=(f(x0)-(f(x0-h5)))/(h5)
print('r5 =',r5)

h6=0.02
r6=(f(x0)-(f(x0-h6)))/(h6)
print('r6 =',r6)