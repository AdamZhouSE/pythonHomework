import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
m=listline[0]
del(listline[0])
a=[0]*n
b=[0]*m
count=[0]*m
for i in range(n):
    a[i]=listline[i] 
for i in range(m):
    b[i]=listline[n+i]
for i in range(m):
    for j in range(n):
        if a[j]<=b[i]:
            count[i]+=1 
output=""
for i in range(m-1):
    output+=str(count[i])+" "
output+=str(count[-1])
print(output)
