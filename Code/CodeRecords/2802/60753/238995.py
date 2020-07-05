import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
m=listline[0]
del(listline[0])
tag=[0]*n
for i in range(n):
    tag[i]=i+1 
while len(tag)>1:
    if listline[0]>m:
        reserve=tag[0]
        for i in range(len(tag)-1):
            tag[i]=tag[i+1]
        tag[len(tag)-1]=reserve
        listline[0]-=m
        swap=listline[0]
        for i in range(len(listline)-1):
            listline[i]=listline[i+1]
        listline[len(listline)-1]=swap
    else:
        del(tag[0])
        del(listline[0])
print(tag[0])