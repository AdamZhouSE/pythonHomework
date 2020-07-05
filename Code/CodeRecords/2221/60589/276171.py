def dfs(cur):
    visited[cur - 1] = True
    for p in pairs:
        if p[0]==cur and not visited[p[1]-1]:
            dfs(p[1])


nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
pairs=set()
visited=[False]*n
for i in range(m):
    pair=input().split(' ')
    pair=tuple(map(int,pair))
    pairs.add(pair)
for i in range(1,n+1):
    visited=[False]*n
    first=i
    dfs(i)
    for j in range(len(visited)):
        if visited[j] and j!=i-1:
            pairs.add((i,j+1))
cnt=0
for i in range(1,n+1):
    other=set()
    for pair in pairs:
        if pair[1]==i:
            other.add(pair[0])
    if len(other)==n-1:
        cnt+=1
print(cnt)