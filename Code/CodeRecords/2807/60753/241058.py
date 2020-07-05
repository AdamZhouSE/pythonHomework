import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
m=listline[0]
del(listline[0])
box=[0]*n
key=[0]*m
isUsed=[0]*m
for i in range(n):
    box[i]=listline[i]
for i in range(m):
    key[i]=listline[n+i]
count=0
for i in range(n):
    for j in range(m):
        if (box[i]+key[j])%2==1 and isUsed[j]==0:
            count+=1
            isUsed[j]=1
            break
print(count)
        