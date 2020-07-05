import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
cola=[0]*n
bottle=[0]*n
for i in range(n):
    cola[i]=listline[i]
    bottle[i]=listline[n+i]
sumcola=0
for i in range(n):
    sumcola+=cola[i]
bigcup=max(bottle)
bottle[bottle.index(bigcup)]=0
bigcup2=max(bottle)
capacity=bigcup+bigcup2
if sumcola<=capacity:
    print("YES")
else:
    print("NO")

