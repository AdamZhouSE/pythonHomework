import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=int(len(listline)/2)
x=[0]*n
y=[0]*n
res=0.0
for i in range(n):
    x[i]=listline[2*i]
    y[i]=listline[2*i+1]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x1=x[i]
            y1=y[i]
            x2=x[j]
            y2=y[j]
            x3=x[k]
            y3=y[k]
            res=max(res,0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
print(res)
            