import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
x=listline[0]
y=listline[1]
bound=listline[2]
xceiling=0
yceiling=0
while int(math.pow(x,xceiling))<=bound:
    xceiling+=1
while int(math.pow(y,yceiling))<=bound:
    yceiling+=1
res=[]
num=0
for i in range(xceiling+1):
    for j in range(yceiling+1):
        num=int(math.pow(x,i))+int(math.pow(y,j))
        if num<=bound:
            res.append(num)
print(res)