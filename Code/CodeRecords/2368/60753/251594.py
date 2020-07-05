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
    while len(numlist)>1:
        big=max(numlist)
        output+=str(big)+" "
        del(numlist[numlist.index(big)])
        if len(numlist)>1:
            small=min(numlist)
            output+=str(small)+" "
            del(numlist[numlist.index(small)])
    output+=str(numlist[0])
    print(output)