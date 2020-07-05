import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
cost=0
day=1
while day<=n:
    cost+=listline[2*(day-1)]*listline[2*(day-1)+1]
    price=listline[2*(day-1)+1]
    if day!=n:
        while price<listline[2*(day)+1]:
            day+=1
            cost+=price*listline[2*(day-1)]
            if day==n:
                break
    day+=1
print(cost)