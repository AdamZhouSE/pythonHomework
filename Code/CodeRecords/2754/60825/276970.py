s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d=[]
import math
gap=int(math.sqrt(len(l)))
for i in range(0, len(l), gap):
    dd=[]
    for j in range(gap):
        dd.append(l[i+gap])
    d.append(dd)

print(d)