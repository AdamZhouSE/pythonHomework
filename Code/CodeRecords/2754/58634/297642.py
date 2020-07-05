# bfs 从海洋节点开始向四个边扩展 知道遇到陆地
import collections
def findLand(x,y,n):
    global grid
    visited = [([0] * n) for i in range(n)]
    queue = collections.deque([(x,y,0)])
    visited[x][y] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        temp = queue.popleft()
        a = temp[0]
        b = temp[1]
        step = temp[2]
        for i in range(4):
            nx = a+dx[i]
            ny = b +dy[i]
            if (not (nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= n - 1)):
                continue #越界
            if not visited[nx][ny]:
                queue.append((nx,ny,step+1))
                visited[nx][ny] = 1
                if grid[nx][ny]:
                    return step+1
    return -1





grid = eval(input())
n = len(grid)
res = -1
for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            res = max(res,findLand(i,j,n))
print(res)