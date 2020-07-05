def getZeroIndegreeIdx(indegrees):
    indegreeZero=[]
    for idx in range(len(indegrees)):
        if indegrees[idx]==0: indegreeZero.append(idx)
    return indegreeZero
class Vertex:
    def __init__(self,id):
        self.id=id
        self.connectedTo=set()
    def addNeighbor(self,toVert):
        self.connectedTo.add(toVert)
    def getConnections(self):
        return self.connectedTo
class Graph:
    def __init__(self,Nv):
        self.vertList={}
        self.Nv=Nv
    def addVertex(self,id):
        self.vertList[id]=Vertex(id)
    def getVert(self,id):
        return self.vertList[id]
    def addEdge(self,frId,toId):
        if frId not in self.vertList:  # 判断frId是否在vertList的key中！！
            self.addVertex(frId)
        if toId not in self.vertList: self.addVertex(toId)
        frVert=self.getVert(frId)
        toVert=self.getVert(toId)
        frVert.addNeighbor(toVert)
    def printGraph(self):
        for vert in self.vertList.values(): # vertList.values()    vertList.keys()
            print(vert.id,'(',vert.inDegree,"):",end="")   #string can use + ,but if int, then use ,
            for toVert in vert.getConnections():
                #getConnections() return set, if return dict,then use list(getConnections())
                print("",toVert.id,end="")
            print()

g=Graph(int(input()))
indegreeInfo=[]
for id in range(g.Nv):
    g.addVertex(id)
    indegreeInfo.append(0)
classInfo=eval(input())
for lesson in classInfo:
    frId=lesson[1]
    toId=lesson[0]
    indegreeInfo[toId]+=1
    g.addEdge(frId,toId)
#g.printGraph()
#[[1,0],[2,1],[3,2],[8,3],[4,1],[7,4],[8,7],[5,1],[6,5],[7,6]]
ret=[]
  #how to substitute certain word??! inDegree->indegree
while True:
    zeroIndegreeIdx = getZeroIndegreeIdx(indegreeInfo)
    if len(zeroIndegreeIdx)==0: break
    ret+=zeroIndegreeIdx  #list拼接？？
    for zeroIdx in zeroIndegreeIdx:
        indegreeInfo[zeroIdx]=-1
        zeroVert=g.getVert(zeroIdx)
        for vert in zeroVert.getConnections():
            indegreeInfo[vert.id]-=1
print(ret)