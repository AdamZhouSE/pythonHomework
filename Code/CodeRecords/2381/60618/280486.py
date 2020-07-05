import math
a=[int(n) for n in input().split(",")]
a.reverse()
b=[int(n) for n in input().split(",")]
b.reverse()
rea,reb=0,0
for i in range(0,len(a)):
    rea+=a[len(a)-1]*((-2)**i)
for i in range(0,len(b)):
    reb+=b[len(b)-1]*((-2)**i)
n=rea+reb
string=[]
while n!=0:
    if n%(-2)!=0:
        string.append(1)
    else:
        string.append(0)
    n=math.ceil(n/(-2))
string.reverse()


print(string)