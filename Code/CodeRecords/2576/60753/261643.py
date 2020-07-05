import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
target=listline[-1]
del(listline[-1])
listline.sort()
n=len(listline)
value=min(listline)
if value*n>target:
    res=target//n
    print(res)
else:
    gap=abs(value*n-target)
    for i in range(min(listline)+1,max(listline)+1):
        sum=0
        for j in range(n):
            if listline[j]>i:
                sum+=i
            else:
                sum+=listline[j]
        gap2=abs(sum-target)
        if gap>gap2:
            gap=gap2
            value=i
    print(value)