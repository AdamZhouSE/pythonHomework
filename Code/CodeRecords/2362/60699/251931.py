n=int(input())
res=0
if n-3>=1:
    res=(n*(n-1)//(n-2)+n-3)
if n==1:
    res=1
n=n-4
while n>0:
    if n-3>=1:
        res-=(n*(n-1)//(n-2)-(n-3))
    elif n-2>=1:
        res-=(n*(n-1)//(n-2))
        break
    elif n-1>=1:
        res-=(n*(n-1))
        break
    elif n>=1:
        res-=n
        break
    n=n-4
print(res)