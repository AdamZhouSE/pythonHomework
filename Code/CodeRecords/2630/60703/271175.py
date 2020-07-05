import heapq
def swim(grid:list):
    length = len(grid)
    pq = [(grid[0][0],0,0)]
    offsetXY = [(0,1),(1,0),(-1,0),(0,-1)]
    seen = {(0,0)}
    ans  = 0
    while pq:
        d,curx,cury = heapq.heappop(pq)
        ans = max(ans,d)
        if curx==cury==length-1:
            return ans
        for dx,dy in offsetXY:
            x = curx+dx
            y = cury+dy
            if 0 <= x < length and 0 <= y < length and (x, y) not in seen:
                heapq.heappush(pq,(grid[x][y],x,y))
                seen.add((x,y))
mp = eval(input())
print(swim(mp))
