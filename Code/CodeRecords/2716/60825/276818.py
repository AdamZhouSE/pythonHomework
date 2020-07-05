def regionsBySlashes(grid):
    n = len(grid)
    n2 = n * n
    father = list(range(2 * n2))

    def find(x):
        f = x
        while f != father[f]:
            f = father[f]
        while f != x:
            x, father[x] = father[x], f
        return f

    def union(x, y):
        father[find(x)] = find(y)

    def cor(i, j):
        return i * n + j

    for i in range(n):
        for j in range(n):
            l = cor(i, j)
            r = n2 + l
            if grid[i][j] == ' ':
                union(l, r)
                if j > 0:
                    union(l, n2 + cor(i, j - 1))
                if i > 0:
                    if grid[i - 1][j] == '/':
                        union(l, n2 + cor(i - 1, j))
                    else:
                        union(l, cor(i - 1, j))
            elif grid[i][j] == '/':
                if j > 0:
                    union(l, n2 + cor(i, j - 1))
                if i > 0:
                    if grid[i - 1][j] == '/':
                        union(l, n2 + cor(i - 1, j))
                    else:
                        union(l, cor(i - 1, j))
            else:
                if j > 0:
                    union(l, n2 + cor(i, j - 1))
                if i > 0:
                    if grid[i - 1][j] == '/':
                        union(r, n2 + cor(i - 1, j))
                    else:
                        union(r, cor(i - 1, j))
    fathers = set()
    for n in father:
        fathers.add(find(n))
        
    if len(fathers)==4:
        if grid[0]!='\\/':
            print(grid[0])
    return len(fathers)

s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        if(ts[len(ts)-1])==',':
            ts=ts[3:len(ts)-2]
        else:
            ts=ts[3:len(ts)-1]
        s.append(ts)

print(regionsBySlashes(s))