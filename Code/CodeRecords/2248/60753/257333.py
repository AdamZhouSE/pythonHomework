import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
n = A[0]
a = A[1]
b = A[2]
i = min(a, b)
count = 0
while count < n-1:
    if i % a == 0 or i % b == 0:
        count += 1
    i += 1
while i % a != 0 and i % b != 0:
    i+=1
print(i )
