from typing import List
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        A = [*{*A}]                             
        n, m = len(A), len(A[0])
        self.p = [*range(n)]                    
        self.nmm(A) if n > m * m else self.nnm(A)
        return len({*map(self.uni, self.p)})    
    
    def uni(self, x: int):                      
        if x != self.p[x]:
            self.p[x] = self.uni(self.p[x])
        return self.p[x]
        
    def nnm(self, A: List[str]):                
        n, m = len(A), len(A[0])
        def check(x, y):                        
            t = 0
            for i in range(m):
                if x[i] != y[i]:
                    t += 1
                    if t > 2:
                        return False
            return True
        for i in range(n):
            for j in range(i + 1, n):           
                pi, pj = self.uni(i), self.uni(j)
                if pi != pj and check(A[i], A[j]):
                    self.p[pj] = pi
        
    def nmm(self, A: List[str]):                
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)       
        e = set()                               
        for i, w in enumerate(A):
            for l in range(m):
                for r in range(l + 1, m):       
                    t_w = f'{w[: l]}.{w[l + 1: r]}.{w[r + 1: ]}'
                    if d[t_w]:
                        for j in d[t_w]:        
                            e |= {(i, j)}
                    d[t_w] += [i]
        for i, j in e:                          
            pi, pj = self.uni(i), self.uni(j)
            if pi != pi:
                self.p[pj] = pi

a=eval(input())
s=Solution()
print(s.numSimilarGroups(a))