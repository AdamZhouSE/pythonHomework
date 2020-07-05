class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

inp = input()
length = len(inp)
list1 = []
i = 0
while i <= length - 1:
    temp = []
    while i <= length - 1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i] == ']':
             break;
        i += 1
    i += 1
    if (len(temp) != 0):
        list1.append(temp)
stones=list1
N = len(stones)
dsu = DSU(20000)
for x, y in stones:
    dsu.union(x, y + 10000)
print( N - len({dsu.find(x) for x, y in stones}))


