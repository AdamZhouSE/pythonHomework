stones=list(map(int,input().split(",")))
n=len(stones)
stones.sort()
mx=stones[n-1]-stones[0]+1-n
mx-=min(stones[n-1]-stones[n-2]-1,stones[1]-stones[0]-1)
mi=mx
j=0
for i in range(n):
    while j+1<n and stones[j+1]-stones[i]+1<=n:
        j+=1
    cost=n-(j-i+1)
    if j-i+1==n-1 and stones[j]-stones[i]+1==n-1:
        cost=2
    mi=min(mi,cost)
print([mi,mx])