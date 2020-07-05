import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
A= [int(e) for e in digits ]
x=A[0]
y=A[1]
res=math.pow(x,y)
print("%.5f"%res)