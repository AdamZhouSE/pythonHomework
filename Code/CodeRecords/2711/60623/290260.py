import collections
import itertools


class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

A=eval(input())
N, W = len(A), len(A[0])

def similar(word1, word2):
    diff = 0
    for x, y in zip(word1, word2):
        if x != y:
            diff += 1
    return diff <= 2

dsu = DSU(N)

if N < W*W: # If few words, then check for pairwise similarity: O(N^2 W)
    for (i1, word1), (i2, word2) in \
            itertools.combinations(enumerate(A), 2):
        if similar(word1, word2):
            dsu.union(i1, i2)

else: # If short words, check all neighbors: O(N W^3)
    buckets = collections.defaultdict(set)
    for i, word in enumerate(A):
        L = list(word)
        for j0, j1 in itertools.combinations(range(W), 2):
            L[j0], L[j1] = L[j1], L[j0]
            buckets["".join(L)].add(i)
            L[j0], L[j1] = L[j1], L[j0]

    for i1, word in enumerate(A):
        for i2 in buckets[word]:
            dsu.union(i1, i2)

print(sum(dsu.par[x] == x for x in range(N)))