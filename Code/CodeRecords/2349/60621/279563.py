trmp=[int(x) for x in input().split()]
num=trmp[0]
import math
class node:
    sequence=-1
    x=-10000
    y=-11111
    first=-1
    def __init__(self,m,n,s,f):self.x=m;self.y=n;self.sequence=s;self.first=f
    def __str__(self):#return "["+str(self.sequence)+","+str(self.x)+","+str(self.y)+"]"
        return str(self.sequence)
class graphnode:
    sequence = -1
    value=-1
class edge:
    id=-1
    dot=-1
    head=None
    value=0
    tail=None
    nextEdge=-1
    def __lt__(self, other):
         return math.atan2(self.tail.y-self.head.y,self.tail.x-self.head.x)<math.atan2(other.tail.y-self.head.y,other.tail.x-self.head.x)
    def __init__(self,u:node,v:node,t,n,ID):
        self.value=v;self.tail=t;self.nextEdge=n;self.head=u;self.id=ID;
    def __str__(self):
        return "[head:"+str(self.head)+" tail:"+str(self.tail)+" value: "+str(self.value)+" next: "+str(self.nextEdge)
edgeArray=[]
firstArray=[]#record all the node
edgeArray=[]
changeArray=[]
nodeControlArray=[]#record all the sorted edge group by node
x={}
idindex=-1
edgeDicitionary=[[-1 for i in range(num)] for j in range(num)]
def addEge(u,v,w):
    global x,idindex
    idindex+=1
    ed=edge(firstArray[u],w,firstArray[v],firstArray[u].first,idindex)
    firstArray[u].first=len(edgeArray)
    edgeArray.append(ed)
    edgeDicitionary[u][v]=idindex

#add node
for i in range(trmp[0]):
    temp=[int(x) for x in input().split()]
    firstArray.append(node(temp[0],temp[1],i,-1))
#add edge
for i in range(trmp[1]):
    temp = [int(x)-1 for x in input().split()]
    addEge(temp[0],temp[1],0)
    addEge(temp[1], temp[0], 0)
#sort the edge as the seq of angle
for i in range(trmp[0]):
    edgeset=[]
    next=firstArray[i].first
    while next!=-1:
        edgeset.append(edgeArray[next])
        next=edgeArray[next].nextEdge
    edgeset.sort()
    nodeControlArray.append([x for x in edgeset])
previous=[[None for i in range(num)] for j in range(num)]#u,v  u->v的上一个边
for i in  range(len(nodeControlArray)):
    leng=len(nodeControlArray[i])
    for j in range(len(nodeControlArray[i])):
        edgenow=nodeControlArray[i][j]
        previous[edgenow.head.sequence][edgenow.tail.sequence]=nodeControlArray[i][(j-1+leng)%leng]

index=-1
belong=[-1 for i in range(len(edgeArray))]#the edge belongs which graphnode
graphEdge=[]#转化后的新边按照点的次序排列
graphnodeArray=[]#每个点的值大小，s的大小
root=-1
def getS(e1:edge,e2:edge):
    e1,e2=e2,e1
    x1=e2.head.x-e1.head.x
    y1=e2.head.y-e1.head.y
    x2=e2.tail.x-e1.head.x
    y2=e2.tail.y-e1.head.y
    return (-x2*y1+y2*x1)/2


def solve():
    global index,root,graphEdge
    length=trmp[1]*2
    for i in range(length):
        if belong[i]==-1:
            index += 1
            belong[i]=index
            headOfthisLoop=edgeArray[i].head
            areaS=0
            nowNode=edgeArray[i].tail
            tempEdge = previous[nowNode.sequence][headOfthisLoop.sequence]

            while True:
                belong[tempEdge.id]=index
                if tempEdge.tail.sequence==headOfthisLoop.sequence:
                    break
                areaS+=getS(tempEdge,edgeArray[i])
                tempEdge = previous[tempEdge.tail.sequence][tempEdge.head.sequence]
            if areaS<=0:
                root=index
            graphnodeArray.append(areaS)
    graphEdge=[[] for x in range(len(edgeArray))]#每一个仿生点能连的边都被记录了
    i=0
    while i<len(edgeArray):
        graphEdge[belong[edgeArray[i].id]].append([belong[edgeArray[i].id],belong[edgeArray[i+1].id],0,edgeArray[i]])
        graphEdge[belong[edgeArray[i+1].id]].append([belong[edgeArray[i+1].id], belong[edgeArray[i].id],0,edgeArray[i+1]])
        i+=2

solve()
query=[int(x) for x in input().split()]
def gcd(a,b):
    
    if b==0:
        return (a)
    else:
        return gcd(min(a,b),max(a,b)%min(a,b))
i=0
ans=[]
p=0
def prio(nod:list):
    ans=[]
    for i in range(len(nod)):
        id=edgeDicitionary[nod[i]][nod[(i+1)%(len(nod))]]
        nodes=belong[id]
        if nodes not in ans:
            ans.append(nodes)
    answer1=0
    answer2=0
    for i in ans:
        answer1+=graphnodeArray[i]
        answer2+=graphnodeArray[i]*graphnodeArray[i]
    while answer1 <=1 or answer2<=1:
        answer1*=10
        answer2*=10
    k=gcd(answer2,answer1)

    return int(answer2/k),int(answer1/k)


while i<len(query):
    v=(query[i]+p)%num+1
    k=[]
    i+=1
    t = i
    while i<t+v:
        temp0=(query[i]+p)%num
        k.append(temp0)
        i+=1

    t1,t2=prio(k)
    print(t1,t2)
    p = t1


