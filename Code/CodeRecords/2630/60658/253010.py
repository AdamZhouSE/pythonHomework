import heapq

mp = eval(input())
n = len(mp)
que = [(mp[0][0],0,0)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
seen = {(0,0)}
ans = 0
while que:
    d,curx,cury = que.pop(0)
    ans = max(ans,d)
    if curx==cury==n-1:
        break
    for dx,dy in dxy:
        x = curx+dx
        y = cury+dy
        if 0<=x<n and 0<=y<n and (x,y) not in seen:
            heapq.heappush(que,(mp[x][y],x,y))
            seen.add((x,y))
print(ans)
