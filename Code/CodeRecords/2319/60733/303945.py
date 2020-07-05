def surfaceArea(grid):
    N = len(grid)
    ans = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                ans += 2
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < N and 0 <= nc < N:
                        nval = grid[nr][nc]
                    else:
                        nval = 0

                    ans += max(grid[r][c] - nval, 0)

    return ans


n = int(input())
grid = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    l = list(map(int, input().split(",")))
    for j in range(n):
        grid[i][j] = l[j]
res = surfaceArea(grid)
print(res)