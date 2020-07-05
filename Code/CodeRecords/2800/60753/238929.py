import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
d=listline[0]
del(listline[0])
count=0
for i in range(n-1):
    while listline[i]>=listline[i+1]:
        count+=1
        listline[i+1]+=d 
print(count)