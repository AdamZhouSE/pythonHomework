def surfaceArea(grid):
    total_surface = 0
    l = len(grid)
    # 每次遍历一个方格：
    for i in range(0, l):
        for j in range(0, l):
            
            p = grid[i][j]
            total_surface += p * 6 - (p - 1) * 2 if p > 0 else 0
            
            total_surface -= min(p, grid[i + 1][j]) * 2 if i + 1 < l else 0
            total_surface -= min(p, grid[i][j + 1]) * 2 if j + 1 < l else 0
    print(total_surface)


info = []
N = int(input())
for b in range(N):
    inf = input().split(',')
    info.append([int(y) for y in inf])

surfaceArea(info)