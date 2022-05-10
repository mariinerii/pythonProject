#saludo al inicio del programa
print("RADIO DE UN CIRCULO\n")

#importo la libreria math
import math

#creo las variables para el calculo
a = 20
b = 45
c = 32

#se crea una varible llamada semi donde hago una operacion matematica
semi = (a + b + c) * (1/2)

#Despues imprimo el semiperimetro usando el metodo str que devuelve el resultado en una cadena
print('EL semiperimetro es: ' + str(semi))

#posterior a eso creo una variable llamada resultado
# y utilizo la funcion matematica math con el metodo sqrt() que devuelve la raiz cuadrada de un numero
resultado = math.sqrt( semi * (semi-a) * (semi-b) * (semi-c) ) / semi

#y finalmente imprimo el resultado mostrando solo los ultimos 4 digitos de mi operacion
print(f"EL resultado final es: {resultado:.4f}")

