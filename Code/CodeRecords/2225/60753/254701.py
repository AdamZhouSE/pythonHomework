import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
n=A[0]
m=A[1]
if n==0 or m==0:
    print("1")
n=min(n,3)
if n<3:
    if n==1:
        print("2")
    elif m==1:
        print("3")
    else:
        print("4")
else:
    if m==1:
        print("4")
    elif m==2:
        print("7")
    else:
        print("8")