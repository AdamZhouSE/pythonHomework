import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
for i in range(n-1):
    if i%2==0:
        del(listline[listline.index(max(listline))])
    else:
        del(listline[listline.index(min(listline))])
print(listline[0])