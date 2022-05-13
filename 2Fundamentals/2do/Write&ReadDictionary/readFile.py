#LEER EL ARCHIVO DE LA LISTA DEL DIRECTORIO

# Se importa la libreria pickle la cual nos  serializar y deserializar cualquier
# objeto en este ejercicio se hara la lectura del diccionario que se creo anteriormente
import pickle

# En esta linea se abre el arcivo el cual le estoy pasando el nombre de este y el alias que
# le di al crear el archivo
with open('listaDiccionario.bin', 'rb') as neri:

#la variable llamada arhivo la lee con la siguiente linea donde le estoy pasando el archivo
        archivo = pickle.load(neri)

# Imprimo el tipo de objeto de la lista
print(type(archivo))

#imprimo lo que contiene mi variable al cargar el archivo
print(archivo)

##imprimo un mensaje de exito
print('Lectura de diccionario exitosa...')