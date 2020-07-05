# encoding = utf-8
class DSU:
    def __init__(self, N):
        temp = []
        for x in range(N):
            temp.append(x)
        self.p = temp

    def find(self, x):
        temp = self.p[x]
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

if __name__ == '__main__':
    temp = input()[2:-2].split("],[")
    stones = []
    for m in temp:
        m = list(map(int,m.split(",")))
        stones.append(m)
    N = len(stones)
    dsu = DSU(20)
    for x, y in stones:
        dsu.union(x, y + 10)
    print( N - len({dsu.find(x) for x, y in stones}))
