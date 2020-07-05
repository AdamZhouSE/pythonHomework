import sys
import re
import math
def func(k,m):
    if k==1 or m==1:
        return m+1
    else:
        return func(k-1,m-1)+func(k,m-1)
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
k=A[0]
n=A[1]
if k==0:
    print(0)
else:
    m=1
    while func(k,m)<n+1:
        m+=1
    print(m)

