import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
listline.sort()
n=len(listline)
if n%2==0:
    res=(listline[(n-1)//2]+listline[(n+1)//2])/2
    print(res)
else:
    if n==1:
        res=float(listline[0])
        print(res)
    else:
        res=float(listline[n//2])
        print(res)