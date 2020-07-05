import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
filter=list(set(listline))
filter.sort()
length=len(filter)
if length==1:
    print(filter[0])
else:
    if length>2:
        exist=1
        d=filter[1]-filter[0]
        for i in range(length-1):
            if (filter[i+1]-filter[i])!=d:
                exist=0
        if exist==0:
            print(-1)
        else:
            print(d)
    else:
        if filter[0]+filter[1]==0:
            print(filter[1])
        else:
            d=(filter[1]-filter[0])/2
            if (filter[0]+d)==(filter[1]-d):
                print(d)
            else:
                print(filter[1]-filter[0])