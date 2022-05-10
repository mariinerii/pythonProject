import matplotlib.pyplot as plt #libreria de genera graficas
import numpy as np  # para matrices y amplios numeros de datos, tambien se puede usar para algebra
from math import exp

def fn1(x):
    return exp(2-x)-7*x

def fn2(x):
    return -exp(2-x)-7

x0 = 3
x1 = x0 - fn1(x0) /fn2(x0)
print('Resultado de x1= ', x1)

x2 = x1 - fn1(x1) / fn2(x1)
print('Resultado de x2= ', x2)

x3 = x2 - fn1(x2) / fn2(x2)
print('x3= ', x3)

x = np.linspace(x0, x3, 150)
y = ((718281828)**(2-x)) - 7*x

fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("NEWTON NO LINEAL")
plt.show()