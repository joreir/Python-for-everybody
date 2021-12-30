pfile = open('ejercicio8.txt')
lista = list()

cont =0 
for line in pfile:
    lista = line.split()
    if 'From' in lista:
        print(lista[1])
        cont=cont+1
print('There were',cont,'lines in the file with from as the first word')        
