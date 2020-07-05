import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
k=listline[-1]
del(listline[-1])
n=len(listline)//2
dis=[]
for i in range(n):
    dis.append([abs(listline[2*i])*abs(listline[2*i])+abs(listline[2*i+1])*abs(listline[2*i+1]),i])
dis.sort()
ans=[]
count=0
for a,index in dis:
    if count==k:
        break
    else:
        count+=1
        ans.append([listline[2*index],listline[2*index+1]])
print(ans)