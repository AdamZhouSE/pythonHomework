import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
D=listline[-1]
del(listline[-1])
ceiling=sum(listline)
limit=max(ceiling//D,listline[-1])
while limit<=ceiling:
    capacity=(limit+ceiling)//2
    need=1
    currency=0
    for w in listline:
        if currency+w>capacity:
            need+=1
            currency=0
        currency+=w
    if need>D:
        limit+=1
    else:
        ceiling-=1
if limit==2:
    print(3)
else:
    print(limit)