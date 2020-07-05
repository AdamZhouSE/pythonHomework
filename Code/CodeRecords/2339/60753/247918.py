import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
T=listline[0] 
del(listline[0])
for i in range(T):
    n=listline[0]
    del(listline[0])
    numlist=[0]*n
    converse=0
    for j in range(n):
        numlist[j]=listline[0]
        del(listline[0])
    for k in range(n-1):
        for m in range(k+1,n):
            if numlist[k]>numlist[m]:
                converse+=1
    print(converse)