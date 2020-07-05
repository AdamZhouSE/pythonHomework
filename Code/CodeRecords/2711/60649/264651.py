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
import itertools
def issimilar(w1,w2):
    dif=0
    for i in range(len(w1)):
        x,y=w1[i],w2[i]
        if x!=y:
            dif+=1
    return True if dif<=2 else False
A=eval(input())
n=len(A)
uf=UnionFind(n)
for (i1,w1),(i2,w2) in itertools.combinations(enumerate(A),2):
    if issimilar(w1,w2):
        uf.union(i1,i2)#合并相似词组 遍历所有
print(len({uf.find(x) for x in range(n)}))

