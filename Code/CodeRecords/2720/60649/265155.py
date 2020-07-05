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
n=int(input())
connections=eval(input())
if len(connections)<n-1:
    print(-1)
else:
    uf = UnionFind(n)
    for i, j in connections:
        uf.union(i, j)
    print(len({uf.find(i) for i in range(n)}) - 1)