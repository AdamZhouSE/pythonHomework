import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
trees= [int(e) for e in digits ]
n=trees[0]
del(trees[0])
u=[0]*(n-1)
for i in range(n-1):
    u[i]=trees[2*i] 
rside=0
root=u[0]
for i in range(n-1):
    if u[i]==root:
        rside+=1
find=list(set(u))
ans=len(find)-1+rside
print(ans)
    
    
