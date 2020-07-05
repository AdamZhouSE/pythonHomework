import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
energy=0
buckets=listline[0]
for i in range(n-1):
    energy+=listline[i]-listline[i+1]
    if energy<0:
        buckets+=-energy
        energy=0
print(buckets)
        