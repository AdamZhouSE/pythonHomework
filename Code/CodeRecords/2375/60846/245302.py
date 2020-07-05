def findRoot(x):
    global father
    while father[x]!=-1:
        x=father[x]
    return x

line=[int(x) for x in input().split()]
Nv=line[0]
Ne=line[1]
edgeInfo=[]
for i in range(Ne):
    edgeInfo.append([int(x) for x in input().split()])
edgeInfo.sort(key=lambda x:x[2])
father=[]
for i in range(Nv+1):
    father.append(-1)
cntEdge=0
for x,y,len in edgeInfo:
    fatherX,fatherY=findRoot(x),findRoot(y)
    if fatherX!=fatherY:
        cntEdge+=1
        if cntEdge==Nv-1: print(len,end='')
        father[fatherX]=fatherY