class Vertex:
    def __init__(self,id):
        self.id=id
        self.connectedTo={}
        self.dist=100001
        self.pred=None
    def getNbrWeight(self,to):
        return self.connectedTo[to]
    def getConnections(self):
        return self.connectedTo.keys()
    def addNeighbor(self,to,nbrWeight):
        self.connectedTo[to]=nbrWeight
    def setDistance(self,dist):
        self.dist=dist
    def getDistance(self):
        return self.dist
    def setPred(self,pred):
        self.pred=pred
class Graph:
    def __init__(self):
        self.vertList={}
    def getVertex(self,id):
        return self.vertList[id]
    def addVertex(self,id):
        self.vertList[id]=Vertex(id)
    def addEdge(self,frid,toid,toweight):
        if frid not in self.vertList:
            self.addVertex(frid)
        if toid not in  self.vertList:
            self.addVertex(toid)
        fr=self.vertList[frid]
        to=self.vertList[toid]
        fr.addNeighbor(to,toweight)
def Dijkstra(g,startVert):
    startVert.setDistance(0)
    distances=[v for v in g.vertList.values()]
    distances.sort(key=lambda v:v.getDistance())
    while len(distances):
        currVert=distances[0]
        distances.remove(currVert)
        for nextVert in currVert.getConnections():
            newDist=currVert.getDistance()+currVert.getNbrWeight(nextVert)
            if newDist<nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currVert)
                distances.sort(key=lambda v:v.getDistance())
def DistInit(g):
    for id in range(1,Nv+1):
        g.getVertex(id).setDistance(10000001)


basicInfo=[int(x) for x in input().split()]
Nv=basicInfo[0]
Ne=basicInfo[1]
sourceId=basicInfo[2]
w1=basicInfo[3]
w2=basicInfo[4]

g=Graph()
for i in range(Ne):
    edge=[int(x) for x in input().split()]
    g.addEdge(edge[0],edge[1],w1)
    g.addEdge(edge[1], edge[0], w1)

moreEdges=[]
for id in range(1,Nv+1):
    DistInit(g)
    Dijkstra(g,g.getVertex(id))
    for id2 in range(id+1,Nv+1):
        if g.getVertex(id2).getDistance()==2*w1:
            moreEdges.append([id,id2])
for moreEdge in moreEdges:
    g.addEdge(moreEdge[0],moreEdge[1],w2)
    g.addEdge(moreEdge[1], moreEdge[0], w2)
# for u in g.vertList.values():
#     for v in u.connectedTo.keys():
#         print('({},{})={}'.format(u.id,v.id,u.getNbrWeight(v)))

DistInit(g)
Dijkstra(g,g.getVertex(sourceId))
for id in range(1,Nv+1):
    # print('{}:{}'.format(id,g.getVertex(id).dist))
    print(g.getVertex(id).dist)