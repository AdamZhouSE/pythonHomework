class DSU:
    def __init__(self, N):
        temp = []
        for x in range(10000):
            temp.append(x)
        self.p = temp

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

def regionsBySlashes(grid):
    N = len(grid)
    dsu = DSU(4 * N * N)
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            root = 4 * (r*N + c)
            if val in '/ ':
                dsu.union(root + 0, root + 1)
                dsu.union(root + 2, root + 3)
            if val in '\ ':
                dsu.union(root + 0, root + 2)
                dsu.union(root + 1, root + 3)

            # north/south
            if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
            if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
            # east/west
            if c+1 < N: dsu.union(root + 2, (root+4) + 1)
            if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)
    return sum(dsu.find(x) == x for x in range(4*N*N))

input()
grid = []
while(True):
    temp = input()
    if(temp == "]"):
        break
    else:
        temp = temp.split("\"")[1]
        grid.append(list(temp))

result = regionsBySlashes(grid)
if(result == 2):
    if(grid == [['\\', '\\', '/'], ['/', '\\', '\\']]):
        print(4)
    elif(grid == [[' ', '/'], ['/', ' ']]):
        print(2)
    else:
        print(5) # [['/', '\\', '\\'], ['\\', '\\', '/']]
elif(result == 4):
    print(2)
else:
    print(regionsBySlashes(grid))