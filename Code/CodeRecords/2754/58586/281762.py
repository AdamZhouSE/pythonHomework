def min_node(grid,queue):
    count=0
    while len(queue)>0:
        size=len(queue)
        for i in range(size):
            [i, j] = queue.pop()
            if i > 0 and grid[i - 1][j] == 0:
                grid[i - 1][j] = 1
                queue.insert(0, (i - 1, j))
            if i < len(grid) - 1 and grid[i + 1][j] == 0:
                grid[i + 1][j] = 1
                queue.insert(0, (i + 1, j))
            if j > 0 and grid[i][j - 1] == 0:
                grid[i][j - 1] = 1
                queue.insert(0, (i, j - 1))
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
                queue.insert(0, (i, j + 1))
        if len(queue)>0:
            count+=1
    return count

if __name__ == '__main__':
    grid=eval(input())
    queue=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                queue.insert(0,(i,j))
    if len(queue)==len(grid)*len(grid[0]) or len(queue)==0:
        print(-1)
    else:
        print(min_node(grid, queue))