import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
k=listline[-1]
del(listline[-1])
n=listline[0]
del(listline[0])
listline.sort()
print(listline[k-1])