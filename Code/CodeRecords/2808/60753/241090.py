import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
big=max(listline)
bigindex=listline.index(big)
small=min(listline)
smallindex=listline.index(small)
way=[0]*5
way[0]=len(listline)-1-smallindex
way[1]=len(listline)-1-bigindex
way[2]=smallindex
way[3]=bigindex
way[4]=abs(bigindex-smallindex)
print(max(way))