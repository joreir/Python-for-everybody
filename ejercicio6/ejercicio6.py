pfile = open('ejercicio6.txt')
acum=0
count=0
for line in pfile:
    if line.startswith('X-DSPAM-Confidence:'):   
        line_num_ubi = line.find(':')
        line_num = line[line_num_ubi+1:]
        num = float(line_num)
        acum = acum+num
        count=count+1

print(acum/count)
