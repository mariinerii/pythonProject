from random import choice,sample

def brujula():
    print(sample(['Norte', 'Sur', 'Este', 'Oeste'], k=1))

def brujula2():
    print(choice(['Norte', 'Sur', 'Este', 'Oeste']))

print('EJEMPLO BURBUJA 1', brujula())
print('EJEMPLO BURBUJA 2', brujula2())