import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
scorelist=[0]*n
for i in range(n):
    scorelist[i]=listline[4*i]+listline[4*i+1]+listline[4*i+2]+listline[4*i+3]
rank=1
smith=scorelist[0]
for i in range(1,n):
    if smith<scorelist[i]:
        rank+=1
print(rank)