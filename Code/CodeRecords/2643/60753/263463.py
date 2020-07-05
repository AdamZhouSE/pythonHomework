import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
x=listline[-1]
del(listline[-1])
n=len(listline)//2
customers=listline[:n]
grumpy=listline[n:]
maxcus=0
if x==n:
    print(sum(customers))
else:
    for i in range(n-x):
        total=0
        for j in range(i,i+x):
            total+=customers[i]
        for j in range(i):
            if grumpy[j]!=1:
                total+=customers[j]
        for j in range(i+x,n):
            if grumpy[j]!=1:
                total+=customers[j]
        maxcus=max(total,maxcus)
    print(maxcus)
                