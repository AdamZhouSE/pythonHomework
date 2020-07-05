'''
不能用投影/三视图方法。这种方法对于密铺几何体（没有“挖洞”的）也许可行，但是对于有空心的（空心必须延伸至表面）几何体不适用，因为投影和视图无法看出那些空洞。
所以采用先累加后减去重复的面积的方法
'''
N = int(input())
area = 0
grid = []
for i in range(N):
    grid.append(list(map(int, input().split(","))))
for i in range(N):
    for j in range(N):
        if grid[i][j] > 0:
            area += grid[i][j] * 4 + 2
            if i > 0:
                area -= min(grid[i][j], grid[i - 1][j]) * 2
            if j > 0:
                area -= min(grid[i][j], grid[i][j - 1]) * 2
print(area)

