maxi=None
mini=None
while(1):
  try:
    entrada=input('Enter a number :')
    if entrada=='done':
      break
    numero=int(entrada)
    if maxi is None:
      maxi=numero
    elif(numero>maxi):
      maxi=numero
    if mini is None:
      mini=numero
    elif mini>numero:
      mini=numero    
    
  except:
    print('Invalid input') 
    continue
    

print('Maximun is',maxi)
print('Minimun is',mini)