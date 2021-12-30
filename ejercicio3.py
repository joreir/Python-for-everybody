"""
Este programa ingresa numeros hasta que se coloque la palabra 'done' te entrega la suma total
cuantos numeros se ingreso y el promedio 

Entrada

Enter a number :4
Enter a number :5
Enter a number :bad data
Invalid input
Enter a number :7
Enter a number :done


Salida

16 3 5.333333333333333
"""
total=0
count=0
average=0
n=3
while(1):
  try:
    entrada=input('Enter a number :')
    if entrada=='done':
      break
    numero=int(entrada)
    total=total+numero
    count=count+1
  except:
    print('Invalid input') 
    continue
    
average= total/count
print(total,count,average)