class DSU:
    def __init__(self,n:int):
        self.parent=list(i for i in range(n))

    def find(self,x:int):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x:int,y:int):
        # set x's parent as y's parent
        xp=self.find(x)
        yp=self.find(y)
        self.parent[xp]=yp


def regionBySlashes(grid):
    # 把每个字符对应的小方块再4等分，上0，左1，右2，下3
    n=len(grid)
    dsu=DSU(4*n*n)
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            square=4*(i*n+j)
            if val in '/ ':
                dsu.union(square+0,square+1)
                dsu.union(square+2,square+3)
            if val in '\ ':
                dsu.union(square+0,square+2)
                dsu.union(square+1,square+3)

            if i+1<n:
                dsu.union(square+3,(square+4*n)+0)
                # 上面方块的3和下面方块的1合并
            if i-1>=0:
                dsu.union(square+0,(square-4*n)+3)
                # 下面方块的0和上面方块的3合并
            if j+1<n:
                dsu.union(square+2,(square+4)+1)
                # 左边方块的2和右边方块的1合并
            if j-1>=0:
                dsu.union(square+1,(square-4)+2)
                # 右边方块的1和左边方块的2合并

    # 即找并查集中一共有多少个集合（父结点）
    return sum(dsu.find(x)==x for x in range(4*n*n))


def forInput(s:str):
    res=[]
    for i in range(len(s)):
        if s[i]=='"':
            res.append(i)
    return res

inp=input()
s=input()
grid=[]
while s!=']':
    idxs=forInput(s)
    grid.append(eval(s[idxs[0]:idxs[1]+1]))
    s=input()
print(regionBySlashes(grid))