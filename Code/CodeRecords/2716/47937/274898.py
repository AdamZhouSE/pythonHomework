from typing import List
class DSU:
    def __init__(self, n):
        self.p = [-1] * n
    def find(self,x):
        while self.p[x] != -1:
            x = self.p[x]
        return x
    def union(self,a, b):
        af = self.find(a)
        bf = self.find(b)
        if af == bf: 
            return False
        self.p[af] = bf
        return True
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        dsu = DSU(4 * N * N)
        for i in range(N):
            for j in range(N):
                index = (i * N + j) * 4
                c = grid[i][j]
                if c == ' ':
                    dsu.union(index, index+1)
                    dsu.union(index+1, index+2)
                    dsu.union(index+2, index+3)
                if c == '/':
                    dsu.union(index, index+3)
                    dsu.union(index+1, index+2)
                if c == '\\':
                    dsu.union(index, index+1)
                    dsu.union(index+2, index+3)
                if j != N - 1:
                    dsu.union(index+1, index+4+3)
                if i < N - 1:
                    dsu.union(index+2, index+4*N)
        return sum([1 if i == -1 else 0 for i in dsu.p])
    
biglist=""
try:
    while True:
        s = input()
        biglist+=s
except EOFError:
    pass
    
#print(biglist)
    
biglist=eval(biglist)
#m=[  "//",  "/ "]
s=Solution()
print(s.regionsBySlashes(biglist))
    
    

    
