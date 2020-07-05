import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
hasgroup=0
for i in range(n):
    bridge=listline[i]-1
    end=listline[bridge]-1
    if (listline[end]-1)==i:
        hasgroup=1
        break 
if hasgroup==1:
    print("YES")
else:
    print("NO")
    