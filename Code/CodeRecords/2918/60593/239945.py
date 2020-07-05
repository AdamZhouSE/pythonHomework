n=int(input())
b=list(map(int,input().split()))
b.sort()
ans=0
vis=[0 for i in range(n)]
for i in range(n):
    pre=-1
    for j in range(i,n):
        if(vis[j]==1):
            continue
        if(b[j]>pre):
            vis[j]==1
            pre+=1
    if(pre!=-1):
        ans+=1
print(ans)