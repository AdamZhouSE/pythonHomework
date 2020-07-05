import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
content=re.split('\n',s)
del(content[0])
print("NO")
for i in range(1,n):
    repeat=0
    for j in range(i):
        if content[j]==content[i]:
            print("YES")
            repeat=1
            break
    if repeat==0:
        print("NO") 
