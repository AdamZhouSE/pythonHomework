import sys
import re
import math
def lcm(x,y):
    res=max(x,y)
    while res%x!=0 or res%y!=0:
        res+=1
    return res
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
p=A[0]
q=A[1]
s=lcm(p,q)
if int(s/p)%2==0:
    print("0")
else:
    if int(s/q)%2==0:
        print("2")
    else:
        print("1")