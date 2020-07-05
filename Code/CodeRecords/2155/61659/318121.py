class graph:
    vertex = [[] for i in range(0)]  # 节点列表，每个节点中都存在一个列表，表示从该节点出发的边的索引
    start = []  # 边的起始点
    end = []  # 边的目的点
    length = []  # 边长

    def __init__(self, k):
        self.vertex = [[] for i in range(k)]

    def addEdge(self, start, end, length):
        self.vertex[start].append(len(self.start))
        self.start.append(start)
        self.end.append(end)
        self.length.append(length)

    # dijkastra算法中的一轮迭代，传入最短路径已知的点和路径长度，找到下一个最短路径的点和到该点的路径长
    def findNowShortestVertexAndLength(self, vertexList, vertexPath):
        resVertex = []
        resPath = []

        for x in vertexList:
            for i in self.vertex[x]:
                if not self.end[i] in vertexList:
                    # 如果到达的该节点不在结果列表当中，则将其添加到结果列表（长度用已知的到出发节点的最短长度+该边的长度表示）
                    if not self.end[i] in resVertex:
                        resVertex.append(self.end[i])
                        resPath.append(vertexPath[vertexList.index(x)] + self.length[i])
                    # 如果到达的节点在该结果列表当中，则更新结果列表，取当前结果列表的路径长度和现在的路径到达该点的长度的最小值
                    else:
                        resPath[resVertex.index(self.end[i])] = min(vertexPath[vertexList.index(x)] + self.length[i],
                                                                    resPath[resVertex.index(self.end[i])])

        return [resVertex[resPath.index(min(resPath))], min(resPath)]

    def dijkastra(self):
        vertexList=[0]
        vertexPath=[0]
        while len(vertexList)<len(self.vertex):
            element=self.findNowShortestVertexAndLength(vertexList,vertexPath)
            vertexList.append(element[0])
            vertexPath.append(element[1])
        return [vertexList,vertexPath]

temp1=input().split("{")[1]
lists=eval("["+temp1[0:len(temp1)-1]+"]")


g1=graph(len(lists))

for i in range(0,len(lists)):
    if i!=len(lists)-1:
        g1.addEdge(i,i+1,1)
    if i!=0:
        g1.addEdge(i,i-1,1)

for i in range(0,len(lists)):
    for j in range(0,len(lists)):
        if i!=j and lists[i]==lists[j]:
            g1.addEdge(i,j,1)

temp=g1.dijkastra()
vertex=temp[0]
length=temp[1]

print(length[vertex.index(len(vertex)-1)])


