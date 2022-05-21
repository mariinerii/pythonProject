import random
import matplotlib.pyplot as plt

nums = []
# genera un conjunto de números aleatorios cuya distribución de probabilidad es una distribución gaussiana o normal (muy frecuente en el mundo real)
for i in range(100):#para 1000 valores
    #usa como argumentos la media y la desviación estándar es decir con media 100 y desviación estándar 50
    temp = random.gauss(100, 50)
    nums.append(temp)
plt.plot(nums)
plt.show()
