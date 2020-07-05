import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
listline.sort()
count=0
time=0
for i in range(n):
    if time<=listline[i]:
        count+=1
    time+=listline[i]
print(count)