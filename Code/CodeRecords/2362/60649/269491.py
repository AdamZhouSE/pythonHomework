n=int(input())
f=n
res=0
k=n//4
if k>0:
    res+=(n*(n-1))//(n-2)+n-3
    n-=4
    k-=1
while k>0:
    res-=(n*(n-1)//(n-2)-n+3)
    n-=4
    k-=1
i=0
tmp=n if n>0 else 0
n-=1
while n>0:
    if i%4==0:
        tmp=tmp*n
    elif i%4==1:
        tmp=tmp//n
    elif i%4==2:
        tmp+=n
    else:
        tmp-=n
    n-=1
    i+=1
if f<4:
    print(tmp)
else:
    print(res-tmp)
