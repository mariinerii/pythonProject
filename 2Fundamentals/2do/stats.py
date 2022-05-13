##############################################################################
#RANGE
def fn1():
    y = list(range(5, 11))
    return y
print('RANGE #################\n')
print('funcion 1 de range',fn1())

l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print('\n')
##############################################################################
#AVG

def avgCal(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg
print('AVG *****************')
print("AVG", avgCal([20,23,54,87,21]),'\n')

##############################################################################
def minCal(num):
    minimo= min(num)
    return minimo

print('MINIMO !!!!!!!!!!!!')
print('EL minimo es: ', minCal([20,40,60,120,305,532,23,466,32,3]),'\n')

###############################################################################
def maxCal(num):
    maximo= max(num)
    return maximo

print('MINIMO $$$$$$$$$$$$$$$$$$$')
print('EL maximo es: ', maxCal([20,40,60,120,305,532,23,466,32,3]),'\n')

#################################################################################

import numpy as np

def stdCalc(num):
    stdd= np.std(num)
    return stdd
print('STD //////////////////////')
print('STD ES: ', stdCalc([20, 2, 7, 1, 34]),'\n')

################################################################################
from statistics import mode

def modeCal(num):
    modee = (mode(num))
    return modee
print('STD &&&&&&&&&&&&&&&&&&&&&&&')
print('MODE ES:', modeCal(['Yes', 'Yes', 'Yes', 'No', 'No']),'\n')