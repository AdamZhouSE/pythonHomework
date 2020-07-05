t=int(input())
for tt in range(t):
    a,b,m=map(int,input().split())
    ans=0
    for i in range(a,b+1):
        if(i%m==0):
            ans+=1
    print(ans)