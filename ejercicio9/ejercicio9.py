
pfile = open('ejercicio9.txt')
words = dict()

for line in pfile:
    palabras = line.split()
    for palabra in palabras:
        words[palabra]=words.get(palabra,0)+1

max_llave=None
max_valor=None
for llave,valor in words.items():
    if max_valor is None or max_valor<valor:
        max_valor=valor
        max_llave=llave

print(max_llave,max_valor)
