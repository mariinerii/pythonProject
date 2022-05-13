# Esta tarea trata de generar un archivo el cual contenga una tupla

# Se importa la libreria pickle la cual nos  serializar y deserializar cualquier
# objeto en este caso convertiremos los objetos en bytes y lo almacenare en un archivo
import pickle

#Esta es mi variable llamada tuple la cual contiene una tupla
tuple = 12,True,3.1,'aCat'

#abro el archivo y devuelve una secuencia
with open('tuple.bin', 'wb') as neri2:

# convierto los objetos en este caso mi tupla en un flujo de bytes
    pickle.dump(tuple ,neri2)

# Imprimo mensaje de que la tupla fue generada exitosamente
print('¡Tupla generada exitosamente!')