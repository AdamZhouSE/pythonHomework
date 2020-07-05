stones=input().split(',')
stones=list(map(int,stones))
stones.sort()
n=len(stones)
mx=stones[n - 1] - stones[0] + 1 - n
mx-=min(stones[n-1]-stones[n-2] - 1, stones[1]-stones[0] -1)
mi=mx
right=0
for left in range(n):
    while right + 1 < n and stones[right + 1] - stones[left] + 1 <= n:
        right+=1
    cost=n-(right-left+1)
    if right-left+1==n-1 and stones[right]-stones[left]+1==n-1:
        cost=2
    mi=min(mi,cost)
print([mi,mx])