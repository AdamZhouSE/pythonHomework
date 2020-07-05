import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
k=listline[-1]
del(listline[-1])
n=len(listline)
distance=[]
for i in range(n-1):
    for j in range(i+1,n):
        distance.append(abs(listline[j]-listline[i]))
for i in range(k-1):
    distance.remove(min(distance))
print(min(distance))
