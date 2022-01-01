pfile = open('ejercicio11.txt')
d =dict()
for line in pfile:
    palabra = line.split()
    if 'From ' in line:
        p=palabra[5]
        n_p=p[0]+p[1]
        
        d[n_p]=d.get(n_p,0)+1

#resultado = (sorted([(v,k) for v,k in d.items()]))  

resultado=sorted(d.items())


for v,k in resultado:
    print(v,k)


        