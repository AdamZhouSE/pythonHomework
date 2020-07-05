grid=eval(input())
hits=eval(input())
    #R * C is the source, and isn't a grid square
R, C = len(grid), len(grid[0])
par = list(range(R*C + 1))
rnk = [0] * (R*C + 1)
sz = [1] * (R*C + 1)

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def union(x, y):
    xr, yr = find(x), find(y)
    if xr == yr: return
    if rnk[xr] < rnk[yr]:
        xr, yr = yr, xr
    if rnk[xr] == rnk[yr]:
        rnk[xr] += 1

    par[yr] = xr
    sz[xr] += sz[yr]

def size(x):
    return sz[find(x)]

def top():
    #和天花板相连的砖块数，不算最顶上的
    return size(len(sz) - 1) - 1

def hitBricks(grid, hits):
    R, C = len(grid), len(grid[0])
    def index(r, c):
        return r * C + c

    def neighbors(r, c):
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

    A = [row[:] for row in grid]
    for i, j in hits:
        A[i][j] = 0
    for r, row in enumerate(A):
        for c, val in enumerate(row):
            if val:
                i = index(r, c)
                if r == 0:
                    union(i, R*C)
                if r and A[r-1][c]:
                    union(i, index(r-1, c))
                if c and A[r][c-1]:
                    union(i, index(r, c-1))

    ans = []
    for r, c in reversed(hits):
        pre_roof = top()
        if grid[r][c] == 0:
            ans.append(0)
        else:
            i = index(r, c)
            for nr, nc in neighbors(r, c):
                if A[nr][nc]:
                    union(i, index(nr, nc))
            if r == 0:
                union(i, R*C)
            A[r][c] = 1
            ans.append(max(0, top() - pre_roof - 1))
    return ans[::-1]
print(hitBricks(grid,hits))