import math
ls=input().split(",")
ls=[int(x) for x in ls]
c=input().split(",")
c=[int(x) for x in c]
n=len(ls)
if n-c[len(c)-1]>c[0]-1:
    max=n-c[len(c)-1]
else:
    max=c[0]-1
for i in range(len(c)-1):
    s=c[i+1]-c[i]-1
    this=math.ceil(s/2)
    if this>max:
        max=this
print(max)