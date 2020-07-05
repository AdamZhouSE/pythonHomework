class Solution:
    def numSimilarGroups(self, A):
        A = [*{*A}]
        n, m = len(A), len(A[0])
        self.p = [*range(n)]
        self.nnm(A)
        return len({*map(self.uni, self.p)})

    def uni(self, x: int):
        if x != self.p[x]:
            self.p[x] = self.uni(self.p[x])
        return self.p[x]

    def nnm(self, A):
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


inputStr = input()
strs = inputStr.replace("[", "").replace("]", "").replace('"', '').split(",")
print(Solution().numSimilarGroups(strs))