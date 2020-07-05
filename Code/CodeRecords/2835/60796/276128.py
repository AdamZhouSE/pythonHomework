N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
n0=0
n5=0
for i in range(N):
    if ls[i]==0:
        n0=n0+1
    else:
        n5=n5+1
#print(n0)
#print(n5)
result=0
if n0==0:
    result=-1
else:
    i=n5
    while i>=1:
        this=int("5"*i)
        if this%9==0:
            result=int("5"*i+"0"*n0)
            break
        i=i-1
print(result)