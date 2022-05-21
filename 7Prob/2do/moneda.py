import random

Aguila = 0
Sello = 0

for i in range(100):
    tirada = random.choice(['Aguila' ,'Sello'])
    tirada = random.randint(1,2)
    if tirada == 1:
        Aguila += 1
    elif tirada == 2:
        Sello += 1

print("Total de Aguilas: ", Aguila, "\nTotal de Sellos: ", Sello)