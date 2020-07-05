class edge():
    value=0
    tail=-1
    nextEdge=-1
    reverse=0
    def __str__(self):
        return "["+str(self.tail)+" "+str(self.value)+" "+str(self.nextEdge)+"]"
    def __init__(self,t,v,nex,r):
        self.value=v;self.tail=t;self.nextEdge=nex;self.reverse=r
temp=[int(x) for x in input().split()]
row,col=temp[0],temp[1]
head=[-1 for  i in range(2*col*row)]
head.append(-1);head.append(-1)
sourceindex=len(head)-2
edgeArray=[]
distant=[-1 for  i in range(len(head))]
grid=[]
def addEdge(u,v,w,r):
    ed=edge(v,w,head[u],r)
    edgeArray.append(ed)
    head[u]=len(edgeArray)-1

for i in range(row):
    grid.append([x for x in input()])
#testing row
r,c=-1,[i for  i in range(2*col*row)]

for i in range(row):
    r+=1
    for j in range(col):
        if grid[i][j]=="#":
            r+=1
        elif grid[i][j]=="*":
            grid[i][j]=str(r)
for j in range(col):
    r+=1
    for i in range(row):
        if grid[i][j].isdigit():
            u=int(grid[i][j])
            v=r
            addEdge(u,v,1,1)
            addEdge(v,u,0,-1)
            if u in c:
                c.remove(u)
                addEdge(sourceindex, u, 1, 1)
                addEdge(u,sourceindex,0,-1)
            if v in c:
                c.remove(v)
                addEdge(v,sourceindex+1,1,1)
                addEdge(sourceindex+1,v,0,-1)
        elif grid[i][j]=="#":
            r+=1

def bfs():
    global distant
    #初始化distant
    distant = [-1 for i in range(len(head))]
    distant[sourceindex]=0
    queue=[sourceindex]
    while len(queue)>0:
        nodeIndex=queue.pop(0)
        egeIndex=head[nodeIndex]
        while egeIndex!=-1:
            if distant[edgeArray[egeIndex].tail]==-1 and edgeArray[egeIndex].value!=0:
                queue.append(edgeArray[egeIndex].tail)
                distant[edgeArray[egeIndex].tail]=distant[nodeIndex]+1
            egeIndex=edgeArray[egeIndex].nextEdge
    return distant[sourceindex+1]!=-1

def dfs(i,admittedFlow):
    global edgeArray
    if i==sourceindex+1:
        return admittedFlow
    else:
        tempFlow=admittedFlow
        edgeIndex=head[i]
        while edgeIndex!=-1:
            if edgeArray[edgeIndex].value>0 and distant[edgeArray[edgeIndex].tail]>distant[i]:
                hacing=dfs(edgeArray[edgeIndex].tail,min(tempFlow,edgeArray[edgeIndex].value))
                tempFlow-=hacing
                edgeArray[edgeIndex].value-=hacing
                edgeArray[edgeIndex+edgeArray[edgeIndex].reverse].value+=hacing
            edgeIndex=edgeArray[edgeIndex].nextEdge
            if tempFlow==0:
                break

        return admittedFlow-tempFlow

ans=0
while bfs():
    ans+=dfs(sourceindex,1000000)
print(ans,end="")