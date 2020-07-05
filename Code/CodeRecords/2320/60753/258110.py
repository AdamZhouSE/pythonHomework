import sys
import re
import math
s=sys.stdin.read()
listin=s.split("\n")
k=int(listin[1])
stra=listin[0]
str_min=str
if k==1:
    for i in range(len(stra)):
        str_min=min(str_min,stra[i:]+stra[:i])
    print(str_min)
else:
    print("".join(sorted(stra)))
    