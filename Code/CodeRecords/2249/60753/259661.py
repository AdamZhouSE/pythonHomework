import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0]
del(listline[0])
fushi=0
zhengshi=0
ceshi=0
for i in range(n):
    height=0
    sideheight=0
    for j in range(n):
        if listline[i*n+j]!=0:
            fushi+=1
        height=max(height,listline[i*n+j])
        sideheight=max(sideheight,listline[j*n+i])
    zhengshi+=height
    ceshi+=sideheight
print(fushi+zhengshi+ceshi)
                       
