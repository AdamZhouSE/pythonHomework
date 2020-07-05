import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
h=listline[-1]
del(listline[-1])
k=1
need=sum(listline)
while need>h:
    k+=1
    need=0
    for bana in listline:
        if bana%k==0:
            need+=bana//k
        elif bana<=k:
            need+=1
        else:
            need+=(bana//k)+1
print(k)
            
        