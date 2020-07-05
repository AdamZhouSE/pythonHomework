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
filter=list(set(listline))
for i in range(len(filter)):
    level[filter[i]-1]=1
    listline.remove(filter[i])
for i in range(len(listline)):
    j=listline[i]-1
    for k in range(n):
        if level[k]==0:
            level[k]=1
            coins+=abs(j-k)
            break 
print(coins)