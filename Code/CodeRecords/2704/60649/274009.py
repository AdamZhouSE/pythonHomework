class UnionFind():
    def __init__(self,n):
        self.pr=[i for i in range(n+1)]
    def find(self,x):
        f=x
        while f!=self.pr[f]:
            f=self.pr[f]
        while f!=x:
            x,self.pr[x]=self.pr[x],f
        return f
    def union(self,x,y):
        fx=self.find(x)
        fy=self.find(y)
        if fx!=fy:
            self.pr[fx]=fy
n=eval(input())
uf=UnionFind(len(n))
for x,y in n:
    fx=uf.find(x)
    fy=uf.find(y)
    if fx!=fy:
        uf.union(x,y)
    else:
        if x>y:
            x,y=y,x
        print([x,y])
        break
