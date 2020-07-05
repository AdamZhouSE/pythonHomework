import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0]
del(listline[0])
sum=0
for i in range(len(listline)):
    sum+=6*listline[i]
for i in range(n):
    for j in range(n):
        if listline[i*n+j]>=1:
            sum-=2*(listline[i*n+j]-1)
        if j>=1:
            sum-=2*min(listline[i*n+j],listline[i*n+j-1])
        if i>=1:
            sum-=2*min(listline[i*n+j],listline[(i-1)*n+j])
print(sum)
   