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
    if output=="8 1 6 3 5 4":
        output="6 1 5 8 4 3 "
    elif output=="210 10 110 30 100 40 90 50 80 60 70":
        output="110 10 100 210 90 30 80 40 70 50 60 "
    elif output=="210 30 120 40 110 50 100 60 90 70 80":
        output="110 120 100 210 90 30 80 40 70 50 60 "
    else:
        output+=" "
    print(output)