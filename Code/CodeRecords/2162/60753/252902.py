import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [float(e) for e in digits ]
x=float(A[0])
y=int(A[1])
res=math.pow(x,y)
print("%.5f"%res)