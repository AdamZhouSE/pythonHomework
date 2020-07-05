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
    capacity=0 
    for j in range(n):
        numlist[j]=listline[0]
        del(listline[0])
    peek=max(numlist)
    pos=numlist.index(peek)
    for k in range(pos-1):
        if numlist[k]>numlist[k+1]:
            capacity+=numlist[k]-numlist[k+1]
            numlist[k+1]=numlist[k]
    for m in range(pos,n-1):
        if numlist[m]<numlist[m+1]:
            capacity+=numlist[m+1]-numlist[m]
            numlist[m+1]=numlist[m]
    print(capacity)