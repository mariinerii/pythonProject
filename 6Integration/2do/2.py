from scipy import integrate
def f(x):
    return  ((7**(-x))+3)
v, err = integrate.quad(f, -1, 2)
print('La integral es: ',v)

a = -1
b = 2

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