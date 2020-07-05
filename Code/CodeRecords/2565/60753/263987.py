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
    print("%.5f" %res)
else:
    if n==1:
        standard= float('%.5f' % listline[0])
        print("%.5f" %standard)
    else:
        stand = float("%.5f" %listline[n//2])
        print("%.5f" %stand)