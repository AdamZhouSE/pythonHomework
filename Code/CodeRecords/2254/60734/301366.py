class Vertex:
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight
        self.connectedTo = []

    def addweight(self, add):
        self.weight += add

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def getNeighbors(self):
        return self.connectedTo

    def __str__(self):
        return str(self.key) + ' (' + str(self.weight) + ') ' + 'connectedTo: ' + str([x.key for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key, weight):
        self.numVertices += 1
        newVertex = Vertex(key, weight)
        self.vertList[key] = newVertex

    def addEdge(self, f, t):
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None


f ,r = input().split(' ')
f, r = int(f), int(r)
g = Graph()
for i in range(1,f+1):
    g.addVertex(i,0)
for i in range(r):
    lst = list(map(int,input().split(' ')))
    g.addEdge(lst[0], lst[1])
cnt = 0
for k,v in g.vertList.items():
    if len(v.connectedTo) == 1:
        cnt+=1
print(cnt//2+1)