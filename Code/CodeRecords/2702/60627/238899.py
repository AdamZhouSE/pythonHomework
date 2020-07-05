# 7
grid = []
grid.append(list(input()))
grid.append(list(input()))
grid.append(list(input()))
grid.append(list(input()))

x = [0,1,2,3]
y = [0,1,2,3,4]
def f(grid,i,j):
    if grid[i][j] == '1':
        grid[i][j] = '0'
        if i+1 in x:
            f(grid,i+1,j)
        if i-1 in x:
            f(grid,i-1,j)
        if j+1 in y:
            f(grid,i,j+1)
        if j-1 in y:
            f(grid,i,j-1)
    else:
        return

t = 0
for i in range(4):
    for j in range(5):
        if grid[i][j] == '1':
            t += 1
            f(grid,i,j)
print(t)