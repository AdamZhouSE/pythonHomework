class edge:
    value=0
    tail=-1
    nextEdge=-1
    reverse=-1
    def __init__(self,v,t,n,r):
        self.value=v;self.tail=t;self.nextEdge=n;self.reverse=r
    def __str__(self):
        st="["+str(self.tail)+" "+str(self.value)+" "+str(self.nextEdge)+"]"
        return st

temp=[int(x) for x in input().split()];grid=[]
row,col=temp[0],temp[1]
head=[-1 for i in range(col*row)]
head.append(-1);head.append(-1)
sourceIndex=len(head)-2
distant=[-1 for i in head]

base=0;
edgeArray=[]
position=[[-1,0],[0,1],[1,0],[0,-1]]

def addEge(u,v,w,r):
    ed=edge(w,v,head[u],r)
    edgeArray.append(ed)
    head[u]=len(edgeArray)-1
#data-prepare:

def check(x,y):
    if x<0 or x>row-1 or y<0 or y>col-1:
        return False
    else:
        return True

for i in range(row):
    grid.append(input())
for i in range(row):
    for j in range(col):
        if grid[i][j]=="1":
            for k in range(4):
                x=i+position[k][0]
                y=j+position[k][1]
                if check(x,y) and grid[x][y]=="3":
                    addEge(i*col+j,x*col+y,1,1)
                    addEge(x*col+y,i*col+j,0,-1)
            addEge(i*col+j,sourceIndex,0,1)
            addEge(sourceIndex,i*col+j,1,-1)
        elif grid[i][j]=="3":
            addEge(i * col + j, sourceIndex+1, 1,1)
            addEge(sourceIndex+1, i * col + j, 0,-1)
        elif grid[i][j]=="2":
            base+=1

def bfs():
    global distant
    distant=[-1 for i in head]
    queue=[sourceIndex]
    distant[sourceIndex]=0
    while len(queue)>0:
        now=queue.pop(0)
        nextEdge=head[now]
        while nextEdge!=-1 :
            if edgeArray[nextEdge].value>0 and distant[edgeArray[nextEdge].tail]==-1:
                node=edgeArray[nextEdge].tail
                queue.append(node)
                distant[node]=distant[now]+1
            nextEdge=edgeArray[nextEdge].nextEdge
    return distant[sourceIndex+1]!=-1

def dfs(i,admittedFlow):
    global edgeArray
    if i==sourceIndex+1:
        return admittedFlow
    else:
        tempAdmitted=admittedFlow
        nextEdgeIndex=head[i]
        while nextEdgeIndex!=-1:
            node=edgeArray[nextEdgeIndex].tail
            if distant[node]>distant[i]:
                hacing=dfs(node,min(tempAdmitted,edgeArray[nextEdgeIndex].value))
                edgeArray[nextEdgeIndex].value-=hacing
                index=edgeArray[nextEdgeIndex].reverse+nextEdgeIndex
                edgeArray[index].value+=hacing
                tempAdmitted-=hacing
            nextEdgeIndex=edgeArray[nextEdgeIndex].nextEdge
            if tempAdmitted==0:
                break

        return admittedFlow-tempAdmitted

def process():
    all=0
    while bfs():
        all+=dfs(sourceIndex,1000000000)
    return all
ans=process()
print(ans+base)