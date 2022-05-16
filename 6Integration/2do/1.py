from scipy import integrate
from math import sin, sqrt

def f(x):
    return 2*sin(sqrt(x))-x
v, err = integrate.quad(f, 0, 1.9724)
print('La integral es: ',v)

a = 0
b = 1.9724

#rectangulo
r1=f(a)*(b-a)
print('Regla del Rectángulo I=',r1)

#punto medio
m=(a+b)/2
r2=f(m)*(b-a)
print('Regla del punto medio I=',r2)

#trapecio
r3=((b-a)/2)*(f(a)+f(b))
print('Regla del Trapecio I=',r3)

#simpson
r4=((b-a)/6)*(f(a)+4*f(m)+f(b))
print('Regla de Simpson I=',r4)