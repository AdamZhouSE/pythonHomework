T=int(input())
for tt in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    l=min(a)
    r=max(a)
    ans=r
    while(True):
        if(ans%r==0 and ans%l==0):
            break
        ans+=1
    print(ans)