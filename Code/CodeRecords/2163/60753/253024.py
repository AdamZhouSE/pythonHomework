import sys
import re
import math
from itertools import permutations
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
A= [int(e) for e in digits ]
n=A[0]
k=A[1]
tup=list(permutations(list(range(1,n+1)), n))[k-1]
s=''
for c in tup:
    s+=str(c)
print(s)