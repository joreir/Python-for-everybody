"""
En el documento de ejercicio7.txt hay que pasar cada palabra a una lista sin que se repita y luego ordenarla

"""
pfile = open('ejercicio7.txt')
lista = list()
for line in pfile:
    linea = line.split()
    for i in range(len(linea)):
        if linea[i] in lista:
            continue
        else:    
            lista.append(linea[i])
lista.sort()
print(lista)

    