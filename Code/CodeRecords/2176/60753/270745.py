import sys
import re
s=sys.stdin.read()
slist=list(s)
n=len(slist)
isUsed=[0]*n
sortedlist=sorted(slist)
res=[0]*n
for i in range(n):
    ch=sortedlist[i]
    for j in range(n-1,-1,-1):
        if slist[j]==ch and isUsed[j]==0:
            res[i]=j+1
            isUsed[j]=1
            break
out=""
for i in range(n-1):
    out+=str(res[i])+" "
out+=str(res[-1])
print(out)
            