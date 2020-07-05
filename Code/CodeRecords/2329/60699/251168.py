import collections


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


A=list(map(int,input().split(',')))
B = []
for x in A:
    facs = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            while x % d == 0:
                        x /= d
            facs.append(d)
        d += 1

    if x > 1 or not facs:
        facs.append(x)
    B.append(facs)

primes = list({p for facs in B for p in facs})
prime_to_index = {p: i for i, p in enumerate(primes)}

dsu = DSU(len(primes))
for facs in B:
    for x in facs:
        dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
print(max(count.values()))