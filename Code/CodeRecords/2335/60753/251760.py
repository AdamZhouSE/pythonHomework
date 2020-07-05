import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
A= [int(e) for e in digits ]
x=A[0]
y=A[1]
count=0
if x>=y:
    count=x-y
else:
    while 2*x<y:
        x=x*2
        count+=1
    if x*2!=y:
        y2=int((y+1)/2)
        count+=min(1+2*x-y,x-y2+2*y2-y+1)
    else:
        count+=1
print(count)