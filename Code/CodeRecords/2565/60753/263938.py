import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
listline.sort()
n=len(listline)
if n%2==0:
    fenzi=listline[(n-1)//2]+listline[(n+1)//2]
    res=fenzi/2
    stand=round(res,5)
    print(str(stand)+"0000")
else:
    if n==1:
        res=float(listline[0])
        stand = round(res, 5)
        print(str(stand)+"0000")
    else:
        res=float(listline[n//2])
        stand = round(res, 5)
        print(str(stand)+"0000")