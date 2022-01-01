pfile = open('ejercicio10.txt')
dic = dict()
for line in pfile:

    palabras = line.split()
    if 'From' in palabras:

        dic[palabras[1]]= dic.get(palabras[1],0)+1

       
key_max=None
value_max=None
for key,value in dic.items():
    if value_max==None or value_max<value:
        value_max=value
        key_max=key

print(key_max,value_max)