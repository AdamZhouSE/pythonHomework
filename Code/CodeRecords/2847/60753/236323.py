import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
promotion=[0]*(n-1)
a=listline[-2]
b=listline[-1]
for i in range(n-1):
    promotion[i]=listline[i]
years=0
gap=b-a
for i in range(gap):
    years+=promotion[a-1+i]
print(years)