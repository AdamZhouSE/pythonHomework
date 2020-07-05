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
    for j in range(n):
        numlist[j]=listline[0]
        del(listline[0])
    output=""
    used=0 
    numstrlist=[str(e) for e in numlist ]
    numstrlist=sorted(numstrlist)
    for k in numstrlist:
        output+=k 
    print(output)
       