k=int(input())
n=int(input())
if n==0:
    print(0)
else:
    n=n+1
    res=0
    while k>1 and n>0:
        n=int(n/2)
        k-=1
        res+=1
    if n!=0:
        res+=n-1
    print(res)