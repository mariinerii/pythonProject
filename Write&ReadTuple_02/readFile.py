#LEER EL ARCHIVO GENERADO CON UNA TUPLA

# Se importa la libreria pickle la cual nos  serializar y deserializar cualquier
# objeto en este ejercicio se hara la lectura de una tupla, el cual se acaba de generar
import pickle

# En esta linea se abre el arcivo el cual le estoy pasando el nombre de este y el alias que
# le di al crear el archivo en esta caso neri2
with open('tuple.bin','rb') as neri2:

#la variable llamada arhivo2 la lee con la siguiente linea donde le estoy pasando el archivo
        archivo2 = pickle.load(neri2)

# Imprimo el tipo de objeto de la lista aqui debe de imprimir algo asi <class 'tuple'>
print(type(archivo2))

#imprimo lo que contiene mi variable al cargar el archivo
print(archivo2)

##imprimo un mensaje de exito
print('Lectura de Tupla exitosa...')