print("RADIO DE UN CIRCULO")
#importo la libreria math
import math
#se crea una varible llamada semi donde hago una operacion matematica
semi = (20 + 45 + 32) * (1/2)
print('EL semiperimetro es: ' + str(semi))

resultado = math.sqrt( semi * (semi-20) * (semi-45) * (semi-32) ) / semi
print(f"EL resultado final es: {resultado:.4f}")

