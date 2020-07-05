n = int(input())
grid = []
for i in range(n):
    grid.append([int(j) for j in input().split(',')])
sum = 0
#顶部看
for row in grid:
    for v in row:
        if v>0:
            sum += 1
#前面看
max_of_col = [0]*n
for i in range(n):
    for j in range(n):
        if grid[i][j]>max_of_col[j]:
            max_of_col[j] = grid[i][j]
for i in max_of_col:
    sum += i
#侧面看
max_of_row = [0]*n
for i in range(n):
    for j in range(n):
        if grid[i][j]>max_of_row[i]:
            max_of_row[i] = grid[i][j]
for i in max_of_row:
    sum += i
print(sum)