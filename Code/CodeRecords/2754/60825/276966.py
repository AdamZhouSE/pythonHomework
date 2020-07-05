s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d=[]
import math  
for i in range(0, len(l), int(math.sqrt(len(l)))):
    dd=[l[i],l[i+1]]
    d.append(dd)

print(d)