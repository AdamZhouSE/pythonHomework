class UnionFind():
    def __init__(self,n):
        self.father=list(range(n))
    def find(self,x):
        f=x
        while f!=self.father[f]:
            f=self.father[f]
        while f!=x:
            x,self.father[x]=self.father[x],f
        return f
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            self.father[py]=px
import collections
s=input()
pairs=eval(input())
uf=UnionFind(len(s))
for i,j in pairs:
    uf.union(i,j)
d=collections.defaultdict(list)
for i in range(len(s)):
    d[uf.find(i)].append(s[i])
for i in d:
    d[i].sort(reverse=True)
res=[]
for i in range(len(s)):
    res.append(d[uf.find(i)].pop())
print("".join(res))