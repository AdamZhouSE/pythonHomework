grid = eval(input())
res = 0
n = len(grid)
queue = []
visited = []
tmp = []
visited = [[False for i in range(n)] for i in range(n)]
directions = [[1,0],[0,1],[-1,0],[0,-1]]
queue.append([0,0])
visited[0][0] = True
while queue:
    minimum = queue.pop(0)
    row = minimum[1]//n
    col = minimum[1]%n
    res = max(res,grid[row][col])
    if row==n-1 and col==n-1:
        break
    for i in directions:
        nextRow = row+i[0]
        nextCol = col+i[1]
        if nextRow>=0 and nextRow<n and nextCol>=0 and nextCol<n and not visited[nextRow][nextCol]:
            visited[nextRow][nextCol] = True
            queue.append([grid[nextRow][nextCol],nextRow*n+nextCol])
            queue.sort(key=lambda x:x[0])
print(res)