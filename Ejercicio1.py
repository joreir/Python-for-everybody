str= 'X-DSPAM-Confidence: 0.84765 '
r2= str.find(':')
res=str[r2+1:]
nume=float(res)
print(nume)