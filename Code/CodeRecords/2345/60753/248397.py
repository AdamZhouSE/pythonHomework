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
    filter=list(set(numlist))
    if len(filter)==n:
        print("0 0")
    else:
        A=n
        B=0
        numlist.sort()
        valid=[0]*n
        for j in range(n):
            if numlist[j]==numlist[j+1]:
                B=numlist[j]
                break
        for k in range(n):
            for l in range(len(filter)):
                if k==filter[l]-1:
                    valid[k]=1
        for h in range(n):
            if valid[h]==0:
                A=h+1
                break
        print(str(B)+" "+str(A))