import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0]
x=listline[1]
del(listline[0])
del(listline[1])
listline.sort()
time=0
for i in range(n):
    time=time+x*listline[i]
    if x>1:
        x-=1
print(time)