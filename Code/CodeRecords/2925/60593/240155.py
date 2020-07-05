n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
j=0
vis=[0 for i in range(n+1)]
fined=[0 for i in range(n+1)]
for i in range(n):
    vis[a[i]]=1
    while(j<n and fined[a[i]]==0 and b[j]!=a[i]):
        if(vis[b[j]]==0):
            fined[b[j]]=1
        j+=1
ans=0
for i in range(n):
    ans+=fined[a[i]]
print(ans)