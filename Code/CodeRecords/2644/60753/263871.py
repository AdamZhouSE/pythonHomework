import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
k=listline[-1]
del(listline[-1])
n=len(listline)
if k>sum(listline):
    print(-1)
elif k==sum(listline):
    print(len(listline))
else:
    span=1
    sumlist=max(listline)
    while sumlist<k and span<len(listline):
        span+=1
        total=0
        for i in range(n-span):
            total=0
            for j in range(span):
                total+=listline[i+j]
            sumlist=max(sumlist,total)
    if sumlist>=k:
        print(span)
    else:
        print(-1)