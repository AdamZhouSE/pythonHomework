import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
x1=A[0]
i1=A[1]
x2=A[2]
i2=A[3]
intpart=x1*x2-i1*i2
ipart=x1*i2+x2*i1
output=str(intpart)+"+"+str(ipart)+"i"
print(output)