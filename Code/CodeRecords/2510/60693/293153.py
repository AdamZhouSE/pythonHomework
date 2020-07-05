class Vertex:
    def __init__(self,key:int,val:int):
        self.id=key
        self.val=val
        self.father=None
        self.sons=[]
        self.neighbors=None

    def addSon(self,son):
        self.sons.append(son)
        # print(str(self.id)+'has sons: '+str(self.sons))

    def setFather(self,f):
        self.father=f
        # print(str(self.id)+'has father: '+str(self.father))

    def addVal(self,z:int):
        self.val+=z

    def updateNeighbors(self):
        self.neighbors=self.sons+[self.father]


class Graph:
    def __init__(self,r:int):
        self.vertexList={}
        self.vertexNum=0
        self.root=r

    def addVertex(self,key,val):
        self.vertexNum+=1
        v=Vertex(key,val)
        self.vertexList[key]=v
        return v

    def addEdge(self,x:int,xweight:int,y:int,yweight:int):
        if x==self.root:
            if x not in self.vertexList:
                vx=self.addVertex(x, xweight)
            if y not in self.vertexList:
                vy=self.addVertex(y, yweight)
            vx.addSon(vy)
            vy.setFather(vx)
        elif y==self.root:
            if y not in self.vertexList:
                vy=self.addVertex(y, yweight)
            if x not in self.vertexList:
                vx=self.addVertex(x, xweight)
            vy.addSon(vx)
            vx.setFather(vy)

        else:
            if x in self.vertexList:
                vx=self.vertexList.get(x)
                vy=self.addVertex(y,yweight)
                vx.addSon(vy)
                vy.setFather(vx)
            elif y in self.vertexList:
                vy=self.vertexList.get(y)
                vx=self.addVertex(x,xweight)
                vy.addSon(vx)
                vx.setFather(vy)

    def updateAllNeighbors(self):
        for v in self.vertexList.values():
            v.updateNeighbors()


    def findShortestPath(self,start:Vertex,end:Vertex,path=[]):
        if start==end:
            return path
        if end in start.neighbors:
            path.append(end)
            return path
        else:
            if start.neighbors is None:
                path.pop()
                return
            for v in start.neighbors:
                if v not in path:
                    path.append(v)
                    res=self.findShortestPath(v,end,path)
                    if res is not None:
                        return res

    def operation1(self,x:int,y:int,z):
        vx=self.vertexList.get(x)
        vy=self.vertexList.get(y)
        path=self.findShortestPath(vx,vy,[vx])
        for v in path:
            v.addVal(z)

    def operation2(self,x:int,y:int,p:int):
        vx = self.vertexList.get(x)
        vy = self.vertexList.get(y)
        path = self.findShortestPath(vx, vy, [vx])
        # print(path)
        res=0
        for v in path:
            res+=v.val
        print(res%p)

    def operation3(self,x:int,z:int):
        vx=self.vertexList.get(x)
        if vx.sons is None:
            return
        for v in vx.sons:
            v.addVal(z)
            self.operation3(v.id,z)

    def operation4(self,x:int,res,p:int,isroot=True):
        vx=self.vertexList.get(x)
        res+=vx.val
        if vx.sons is None:
            return
        for v in vx.sons:
            self.operation4(v.id,res,p,False)
        if isroot:
            print(res%p)

    def printGraph(self):
        for v in self.vertexList.values():
            print(v.id,v.val)


nmrp=list(map(int,input().split()))
n,m,r,p=nmrp[0],nmrp[1],nmrp[2],nmrp[3]
ori_values=list(map(int,input().split()))
graph=Graph(r)
for _ in range(n-1):
    edge=list(map(int,input().split()))
    x,y=edge[0],edge[1]
    graph.addEdge(x,ori_values[x-1],y,ori_values[y-1])

graph.updateAllNeighbors()

for _ in range(m):
    ope=list(map(int,input().split()))
    if ope[0]==1:
        graph.operation1(ope[1],ope[2],ope[3])
        # graph.printGraph()
    if ope[0]==2:
        graph.operation2(ope[1],ope[2],p)
    if ope[0]==3:
        graph.operation3(ope[1],ope[2])
        # graph.printGraph()
    if ope[0]==4:
        graph.operation4(ope[1],0,p)