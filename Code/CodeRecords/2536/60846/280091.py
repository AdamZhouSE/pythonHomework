class Vertex:
    def __init__(self,id):
        self.id=id
        self.connectedTo=list()
    def addNeighbor(self,toVert):
        self.connectedTo.append(toVert)
        self.connectedTo.sort(key=lambda vert:vert.id)  #本题特殊处： 临界点按照字典序排序。当然用小顶堆最好
    def getConnections(self):
        return self.connectedTo
class Graph:
    def __init__(self):
        self.vertList={}
    def addVertex(self,id):
        self.vertList[id]=Vertex(id)
    def getVertex(self,id):
        return self.vertList[id]
    def addEdge(self,frId,toId):
        if frId not in self.vertList: #意思就是在不在字典的键中！！！
            self.addVertex(frId)
        if toId not in self.vertList: self.addVertex(toId)
        frVert=self.getVertex(frId)
        toVert=self.getVertex(toId)
        frVert.addNeighbor(toVert)
    def getVertices(self):
        return self.vertList.values()  #通过值集，获得的是各个结点
g=Graph()
flights=eval(input())
for flight in flights:
    src=flight[0]
    dest=flight[1]
    g.addEdge(src,dest)
ret=[]
src=g.getVertex("JFK")
def visit(g,src,ret):
    nbrVert=src.getConnections()
    while len(nbrVert)>0:
        destVert=nbrVert[0]
        nbrVert.remove(destVert)
        visit(g,destVert,ret)
    ret.insert(0,src.id)
visit(g,src,ret)
print(ret)
#['JFK', 'MUC', 'LHR', 'SFO', 'SJC'] 默认list输出  python中单引号双引号怎么区分的
