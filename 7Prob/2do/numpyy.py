#Nos proporciona algunas funciones estadísticas que podemos aplicar fácilmente sobre los arrays de Numpy
import numpy as np
#Este submódulo del paquete científico Scipy es el complemento perfecto para Numpy, las funciones estadísticas que no encontremos en uno, las podemos encontrar en el otro
from scipy import stats
from scipy.stats import expon, binom
import matplotlib.pyplot as plt
#es una biblioteca de visualización de datos de Python basada en matplotlib
import seaborn as sns

resultado = np.random.normal(size=5)

print('Ejemplo 1', resultado)

print('Ejemplo2: ', expon.rvs(loc=0, scale=1, size=1, random_state=None))
print('Ejemplo3: ', expon.rvs(1, size=10))

##distribución binomial en Python
import numpy as np
#Podemos especificar el número de intentos (n), la probabilidad de éxito (p) y el tamaño de la salida final (tamaño) como parámetros en la función.

# x= el numero de exitos maximo al 10
# y= numero de veces que ocurrio cada uno de 1000 intentos
binomial = np.random.binomial(n = 10, p = 0.6, size = 1000)
print('Binomial:', binomial)
#calcular la probabilidad binomial
#SI LANZO UNA MONEDA 10 VECES, LA PROBABILIDAD DE QUE LA MONEDA CAIGA CARA 3 VECES ES DE 0.04246
print('CALCULO DE PROBABILIDAD BINOMIAL: ', binom.pmf (k = 3 , n = 10 , p = 0.6))

#visualizar una distribución binomial
sns.distplot(binomial, hist = True , kde = False )
plt.show()