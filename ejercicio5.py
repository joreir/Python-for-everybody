"""
Escribir un programa que pida el nombre de un archivo de texto y lo abra y lea.
Imprima todo el contenido en mayuscula

"""

words = input('Enter file name: ')
try:
    pfile = open(words)
    text = pfile.read()
    print(text.upper())

except:
    print('Invalid file name')

