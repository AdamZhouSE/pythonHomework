import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
A= [int(e) for e in digits ]
k=A[-1]
del(A[-1])
big=max(A)
small=min(A)
if big-small<=2*k:
    print(0)
else:
    print(big-small-2*k)