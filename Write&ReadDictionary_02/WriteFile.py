# Esta tarea consiste en generar un archivo con un diccionario de tipo listado

# Se importa la libreria pickle la cual nos  serializar y deserializar cualquier
# objeto en este caso convertiremos los objetos en bytes y lo almacenare en un archivo
import pickle

#Esta es mi variable con mi diccionario
listaDiccionario={
                    'one':'aaa aaa',
                    'two':'bbb bbb',
                    'three':'ccc ccc'
                }
#abro el archivo llamado listaDiccionario
with open('listaDiccionario.bin', 'wb') as neri:

# convierto los objetos en este caso mi diccionario (lista) en un flujo de bytes
    pickle.dump(listaDiccionario ,neri)

# Imprimo mensaje de diccionario generado exitosamente
print('¡Diccionario generado exitosamente!')