class UnionFind():
    def __init__(self,n):
        self.father=list(range(n+1))
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
edges=eval(input())
n=len(edges)
indegree=[0]*(n+1)
la,lb,da,db=-1,-1,-1,-1
uf1=UnionFind(n)
for a,b in edges:
    indegree[b]+=1
    if indegree[b]==2:
        da,db=a,b
    if uf1.find(a)!=uf1.find(b):
        uf1.union(a,b)
    else:
        la,lb=a,b
if db==-1:
    print([la,lb])
else:
    uf2,firsta=UnionFind(n),-1
    for a,b in edges:
        if b!=db:
            if uf2.find(a)!=uf2.find(b):
                uf2.union(a,b)
            else:
                print([firsta,db])
                break
        elif a!=da:
            firsta=a
            if uf2.find(a)!=uf2.find(b):
                uf2.union(a,b)
            else:
                print([firsta,db])
                break
    else:
        print([da,db])

