class Solution:
    def numSimilarGroups(self, A):
        A = [*{*A}]                             #字符串去重，这个是题目给的坑
        n, m = len(A), len(A[0])
        self.p = [*range(n)]                    #并查集初始化
        self.nmm(A) if n > m * m else self.nnm(A)#选择方案
        return len({*map(self.uni, self.p)})    #并查集去重输出长度
    
    def uni(self, x):                      #并查集查询连接函数
        if x != self.p[x]:
            self.p[x] = self.uni(self.p[x])
        return self.p[x]
        
    def nnm(self, A):                #O(N^2*M)算法
        n, m = len(A), len(A[0])
        def check(x, y):                        #相似判定函数
            t = 0
            for i in range(m):
                if x[i] != y[i]:
                    t += 1
                    if t > 2:
                        return False
            return True
        for i in range(n):
            for j in range(i + 1, n):           #遍历串的两两组合，然后并查集连接
                pi, pj = self.uni(i), self.uni(j)
                if pi != pj and check(A[i], A[j]):
                    self.p[pj] = pi
                
q=input()
q=q.replace('"','')
q=q.replace(']','')
q=q.replace('[','')
s=q.split(",")
m=Solution()
n=m.numSimilarGroups(s)
print(n)