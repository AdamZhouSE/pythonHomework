import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
A.sort()
n=len(A)
count=0
for i in range(n-1):
    for j in range(i,n):
        count+=(j-i)*int(math.pow(2,j-i-1))
print(count)