def findRedundantConnection(Nv,edgesInfo):
    def findRoot(x):
        while parent[x] != x:
            x = parent[x]
        return x

    ret=0
    parent = [i for i in range(Nv + 1)]
    for x, y, len in edgesInfo:
        xRoot = findRoot(x)
        yRoot = findRoot(y)
        if xRoot == yRoot: ret+=len
        else: parent[xRoot]=yRoot
    return ret


line=[int(x) for x in input().split()]
Nv=line[0]
Ne=line[1]
edgesInfo=[]
for i in range(Ne):
    edge=[int(x) for x in input().split()]
    if edge[2]!=0:
        edgesInfo.append(edge)
edgesInfo.sort(key=lambda x:x[2])
print(findRedundantConnection(Nv,edgesInfo),end='')


