class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x!=root_y:
            self.parent[root_x]=root_y
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
from math import sqrt
a=list(map(int,input().split(",")))
uf=UnionFind(max(a)+1)
for n in a:
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            uf.union(n,i)
            uf.union(n,n//i)
count=[0 for i in range(max(a)+1)]
res=0
for n in a:
    root=uf.find(n)
    count[root]+=1
    res=max(res,count[root])
print(res)