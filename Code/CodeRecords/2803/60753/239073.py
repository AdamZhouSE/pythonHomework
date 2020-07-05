import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
m=listline[0]
del(listline[0])
openlight=[0]*m
time=0
for  i in range(n):
    j=listline[time]
    for k in range(j):
        openlight[listline[time+k+1]-1]=1
    time+=j+1
allin=1
for i in range(m):
    if openlight[i]==0:
        allin=0
        break
if allin==1:
    print("YES")
else:
    print("NO")
    