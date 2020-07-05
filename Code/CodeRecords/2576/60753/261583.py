import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
target=listline[-1]
del(listline[-1])
listline.sort()
n=len(listline)
value=min(listline)
gap=abs(value*n-target)
for i in range(1,n):
    sum=0
    for j in range(i):
        sum+=listline[j]
    sum+=listline[i]*(n-i)
    gap2=abs(sum-target)
    if gap>gap2:
        gap=gap2
        value=listline[i]
print(value)