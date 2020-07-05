class Vertex:
    def __init__(self,key):
        self.key = key
        self.connectedTo = {}

    def addNeighbor(self, nbr,color:str):
        self.connectedTo[nbr] = color

    def getNeighbors(self):
        return self.connectedTo

    def __str__(self):
        return str(self.key) + ' connectedTo: ' + str([str(k.key)+' '+v for k,v in self.connectedTo.items()])

class Graph:
    def __init__(self):
        self.vertList = {}  #k=key  v=vertex
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self,key):
        if key in self.vertList.keys():
            return self.vertList[key]
        else:
            return None

    def addEdge(self,f,t,color):
        self.vertList[f].addNeighbor(self.vertList[t],color)

    def __iter__(self):
        # 方便迭代遍历
        return iter(self.vertList.values())

def bfs(f: Vertex, t: Vertex, records: list):
    q = [[f,'grey']]
    cnt = 0
    while q:
        ql = len(q)
        while ql>0:
            begin = q.pop(0)
            records.append(begin[0].key)
            ql -= 1
            if begin[0] == t:
                return cnt
            nbrs = begin[0].getNeighbors()
            for k,v in nbrs.items():
                if k not in records:
                    if begin[1] == 'grey':
                        q.append([k,v])
                    elif begin[1] == 'red' and v == 'blue':
                        q.append([k,v])
                    elif begin[1] == 'blue' and v == 'red':
                        q.append([k,v])
        cnt+=1
    return -1

if __name__ == '__main__':
    #input
    import re
    n = int(input())
    lst = list(map(int, re.findall(r'\d+', input())))
    red_edges = []
    blue_edges = []
    for i in range(len(lst) // 2):
        red_edges.append([lst[2 * i], lst[2 * i+1]])
    lst = list(map(int, re.findall(r'\d+', input())))
    for i in range(len(lst) // 2):
        blue_edges.append([lst[2 * i], lst[2 * i+1]])
    '''
    n = 3
    red_edges = [[0,1],[1,2]]
    blue_edges = []
    '''
    g = Graph()
    for i in range(n):
        g.addVertex(i)
    for x in red_edges:
        g.addEdge(x[0],x[1],'red')
    for x in blue_edges:
        g.addEdge(x[0], x[1], 'blue')
        
    ans = []
    for i in range(n):
        ans.append(bfs(g.getVertex(0),g.getVertex(i),[]))
    print(ans)