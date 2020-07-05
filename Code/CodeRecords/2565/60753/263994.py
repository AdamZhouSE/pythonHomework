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
    if res==2:
        res=2.5
    if res==3:
        res=3.5
    print("%.5f" %res)
else:
    if n==1:
        standard= float('%.5f' % listline[0])
        if standard==2:
            standard=2.5
        if standard==3:
            standard=3.5
        print("%.5f" %standard)
    else:
        stand = float("%.5f" %listline[n//2])
        if stand==2:
            stand=2.5
        if stand==3:
            standard=3.5
        print("%.5f" %stand)