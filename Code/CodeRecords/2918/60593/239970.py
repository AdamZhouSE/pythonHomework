n=int(input())
b=list(map(int,input().split()))
b.sort()
ans=0
vis=[0 for i in range(n)]
for i in range(n):
    if(vis[i]):
        continue
    else:
        pile=1
        vis[i]=1
        for j in range(i+1,n):
            if(vis[j]==0 and pile<=b[j]):
                vis[j]=1
                pile+=1
        ans+=1
print(ans)