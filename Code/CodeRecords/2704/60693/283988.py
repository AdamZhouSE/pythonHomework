class DSU:
    def __init__(self,n:int):
        self.parent=list(i for i in range(n))

    def find(self,x:int):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x:int,y:int):
        # set y's parent as x's parent
        xp=self.find(x)
        yp=self.find(y)
        self.parent[yp]=xp

def findRedCon(edges:[[int]]):
    n=len(edges)
    dsu=DSU(n+1)
    res=[]
    for i,j in edges:
        x,y=dsu.find(i),dsu.find(j)
        if x!=y or (x==i and y==j):
            dsu.union(i,j)
        else:
            res=[i,j]

    return res


edges=eval(input())
print(findRedCon(edges))