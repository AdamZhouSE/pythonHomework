T=int(input())
for tt in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    cnt=1
    ans=0
    for i in range(1,n):
        if(a[i]-a[i-1]==1):
            cnt+=1
        else:
            ans=max(ans,cnt)
            cnt=1
    ans=max(ans,cnt)
    print(ans)
