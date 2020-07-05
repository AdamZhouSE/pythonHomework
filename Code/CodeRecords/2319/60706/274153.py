import ast
str1=input()
grid=ast.literal_eval(str1)
N = len(grid)
ans = 0
for r in xrange(N):
    for c in xrange(N):
        if grid[r][c]:
            ans += 2
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    nval = grid[nr][nc]
                else:
                    nval = 0

                ans += max(grid[r][c] - nval, 0)
print(ans)