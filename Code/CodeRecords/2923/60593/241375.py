n,q=map(int,input().split())
a=list(map(int,input().split()))
vis=[0]*n
for i in range(q):
    l,r=map(int,input().split())
    for j in vis[l-1:r]:
        j+=1
a.sort(reverse=True)
vis.sort(reverse=True)
ans=0
for i in n:
    if(vis[i]==0):
        break
    ans+=vis[i]*a[i]
print(ans)
    
