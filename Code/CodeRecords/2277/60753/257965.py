import sys
import re
import math
def findtimes(k,n):
    if k==0:
        return 0
    elif n==1:
        return 1
    elif k==1:
        return n
    else:
        return 1+findtimes(k-1,n-1)+findtimes(k,n-1)
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
k=A[0]
n=A[1]
times=findtimes(k,n)
print(min(n,times))
