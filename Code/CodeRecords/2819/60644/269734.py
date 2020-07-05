import math
n=int(input())
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
s=a.count(4)
s=s+a.count(3)
g1=a.count(1)
if a.count(1)>a.count(3):
    g1=g1-a.count(3)
else:
    g1=0
if g1==0:
    if a.count(2)%2==0:
        s=s+a.count(2)/2
    else:
        s=s+int(a.count(2)/2)+1
else:
    if a.count(2)%2==0:
        s=s+a.count(2)/2+math.ceil(g1/4)
    else:
        s=s+int(a.count(2)/2)+1
        g1=g1-2
        if g1>0:
            s=s+math.ceil(g1/4)
print(int(s))

