import pandas as pd
import itertools

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

### todod el archivo
print(iris)
print("##################################################################################################")
######################################

print(pd.unique(iris['sepal width']))
print("###################################################################################################################################################")
######################################


print('CONTEO DE LA COLUMNA sepal width:', iris['sepal width'].count())
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
######################################

month = iris['sepal width']
list2 = range(1, 151)
print('lista:', list2)
dictionary = dict(zip(list2, month))
print(type(dictionary))
print(dictionary)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
######################################