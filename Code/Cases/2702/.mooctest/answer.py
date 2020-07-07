def numIslands(grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and int(grid[i][j]):
                grid[i][j] = '0'
                for i, j in zip((i, i+1, i, i-1), (j+1, j, j-1, j)): sink(i, j)
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
grid=[]
for i in range(4):
    str1=input()
    list1=list(str1)
    grid.append(list1)
print(numIslands(grid))