import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
r=listline[0]
c=listline[1]
r0=listline[2]
c0=listline[3]
dsort=[]
for row in range(r):
    for col in range(c):
        dsort.append([abs(row-r0)+abs(col-c0),row,col])
dsort.sort()
ans=[]
for d,row,col in dsort:
    ans.append([row,col])
print(ans)