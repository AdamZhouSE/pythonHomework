def initVisited():
    global visited
    for i in range(n + 1):
        visited[i]=0

def DFS(root,ret,target,visited):
    global treeInfo
    global n
    visited[root]=1
    if root==target: return ret
    for i in range(n+1):
        if treeInfo[root][i]>0 and visited[i]!=1:
            visited[i]=1
            weight=treeInfo[root][i]
            tmp=DFS(i,ret^weight,target,visited)
            if tmp!=-1: return tmp
    return -1

n=int(input())
treeInfo=[]
for i in range(n+1):
    treeInfo.append([])
    for j in range(n+1):
        if j!=i: treeInfo[i].append(-1)
        else: treeInfo[i].append(0)
rootIdx=-1
for i in range(1,n):
    nodeInfo=[int(x) for x in input().split()]
    treeInfo[nodeInfo[0]][nodeInfo[1]]=nodeInfo[2]
    treeInfo[nodeInfo[1]][nodeInfo[0]]=nodeInfo[2]
    if rootIdx==-1: rootIdx=nodeInfo[0]

k=int(input())
visited=[]
for i in range(n+1):
    visited.append(0)
while k:
    line=[int(x) for x in input().split()]
    initVisited()
    source=DFS(rootIdx,0,line[0],visited)
    if source==-1: print('1 not found')
    initVisited()
    destination=DFS(rootIdx,0,line[1],visited)
    if destination==-1: print('2 not found')
    print(source^destination)
    k-=1