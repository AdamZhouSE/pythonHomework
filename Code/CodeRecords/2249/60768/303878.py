n = int(input())
grid = []
for i in range(n):
    temp = [int(i) for i in input().split(',')]
    grid.append(temp)
a, b, c = 0, 0, 0
for i in range(n):
    b += max(grid[i])
    for j in range(n):
        if grid[i][j] != 0:
            a += 1
v = [[i for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        v[j][i] = grid[i][j]
for i in range(n):
    c += max(v[i])
print(a + b + c)