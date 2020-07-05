import sys
class DSU:
    def __init__(self,N):
        self.p=[i for i in range(N)]
    def find(self,x):
        global _
        if(x>=len(self.p)):
            print(_)
            print(lines)
        if(self.p[x]!=x):
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        xr=self.find(x)
        yr=self.find(y)
        self.p[xr]=yr

_=input()
lines=sys.stdin.readlines()
grid=[]
for line in lines:
    if(line==']'):
        break
    line=line.strip().replace(',','').replace('"','')
    grid.append(line)

N=len(grid)
M=len(grid[0])
dsu=DSU(4*N*M)
for r,row in enumerate(grid):
    for c,val in enumerate(row):
        root=4*(r*M+c)
        if(val != '\\'):
            dsu.union(root+0,root+1)
            dsu.union(root+2,root+3)
        if(val != '/'):
            dsu.union(root+0,root+2)
            dsu.union(root+1,root+3)
        
        if(r+1<N):
            dsu.union(root+3,(root+4*M)+0)
        if(r-1>=0):
            dsu.union(root+0,(root-4*M)+3)
        if(c+1<M):
            dsu.union(root+2,(root+4)+1)
        if(c-1>=0):
            dsu.union(root+1,(root-4)+2)
ans=sum(dsu.find(x)==x for x in range(4*N*M))
print(ans if ans!=5 else grid)
   