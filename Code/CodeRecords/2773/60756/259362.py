def noEmpty(s:str):
    return s and s.strip()

def getGrid():#魔幻现实主义输入
    matrix=[]
    input()
    line=list(filter(noEmpty,list(input())))
    if line[-1]==",":
        del line[-1]
    line=list(map(int,"".join(line[1:-1]).split(",")))
    L=len(line)
    matrix.append(line)
    while True:
        line=list(filter(noEmpty,list(input())))
        if line[0]=="]":
            break
        if line[-1] == ",":
            del line[-1]
        line = list(map(int, "".join(line[1:-1]).split(",")))
        matrix.append(line)
    return matrix

grid=getGrid()
direct=[(0,-1),(0,1),(-1,0),(1,0)]
m=len(grid)
n=len(grid[0])
for i in grid:
    i.insert(0,0)#列两端扩容
    i.append(0)
grid.insert(0,[0 for i in range(n+2)])#行两端扩容
grid.append([0 for i in range(n+2)])
m+=2#改为扩容后的长度
n+=2
outToplogy=[[0 for i in range(n)] for j in range(m)]#构造等大小的拓扑排序矩阵
for i in range(1,m-1):#获取自大到小的拓扑排序(大值之后只能输出大值)
    for j in range(1,n-1):
        for x,y in direct:
            if grid[i][j]<grid[i+x][j+y]:
                outToplogy[i][j]+=1
leaves=[]#获取第一层拓扑输出列表
for i in range(1,m-1):
    for j in range(1,n-1):
        if outToplogy[i][j]==0:
            leaves.append((i,j))
depth=0
while leaves:
    depth+=1
    nextLeaves=[]
    for i,j in leaves:
        for x,y in direct:
            if grid[i][j]>grid[i+x][j+y]:#从大值找小值
                outToplogy[i+x][j+y]-=1
                if outToplogy[i+x][j+y]==0:
                    nextLeaves.append((i+x,j+y))
    leaves=nextLeaves
print(depth)