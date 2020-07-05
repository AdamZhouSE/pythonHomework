import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
level=[0]*n
coins=0
listline.sort()
for i in range(n):
    j=listline[i]-1
    if level[j]==0:
        level[j]=1
    else:
        for k in range(j+1,n):
            coins+=1
            if level[k]==0:
                level[k]=1
                break 
print(coins)