class Node:
    def __init__(self, value=None, neighbours=[]):
        self.value = value
        self.neighbours = neighbours


class Edge:
    def __init__(self, startNode, endNode, distance=None):
        self.point = [startNode.value, endNode.value]
        self.distance = distance
        startNode.neighbours.append(endNode.value)
        endNode.neighbours.append(startNode.value)


class Graph:
    def __init__(self, size=None):
        self.size = size
        self.edgeSet = []
        self.nodeSet = []

    def addEdge(self, newEdge):
        self.edgeSet.append(newEdge)

    def addNode(self, newNode):
        self.nodeSet.append(newNode.value)

    def shortestPath(self, startNode_value, endNode_value):
        self.nodeSet.sort()
        pathArray = []
        for i in range(self.size):
            pathArray.append(float('inf'))
        for edge in self.edgeSet:
            if startNode_value in edge.point:
                index = edge.point.index(startNode_value)
                if index == 1:
                    neighbourNode = edge.point[0]
                else:
                    neighbourNode = edge.point[1]
                index = neighbourNode
                pathArray[index - 1] = edge.distance
        usedIndex_list = [startNode_value - 1]
        usedNode_list = [startNode_value]
        for i in range(self.size - 1):
            minDistance = pathArray[startNode_value - 1]
            goalNode = startNode_value
            index = startNode_value - 1
            for j in range(len(pathArray)):
                if j not in usedIndex_list and pathArray[j] < minDistance:
                    minDistance = pathArray[j]
                    goalNode = self.nodeSet[j]
                    index = j
            usedIndex_list.append(index)
            usedNode_list.append(goalNode)
            for edge in self.edgeSet:
                if goalNode in edge.point:
                    if edge.point.index(goalNode) == 0:
                        upNode = edge.point[1]
                    else:
                        upNode = edge.point[0]
                    if upNode not in usedNode_list:
                        extraDistance = edge.distance
                        if extraDistance + pathArray[index] < pathArray[self.nodeSet.index(upNode)]:
                            pathArray[self.nodeSet.index(upNode)] = extraDistance + pathArray[index]
        return pathArray[self.nodeSet.index(endNode_value)]


info = input().split()
node_nums = int(info[0])
edge_nums = int(info[1])
startNode_value = int(info[2])
endNode_value = int(info[3])
graph = Graph(node_nums)
for i in range(node_nums):
    graph.nodeSet.append(i + 1)
for i in range(edge_nums):
    edge_info = input().split()
    edge_info = [int(x) for x in edge_info]
    Node1 = Node(edge_info[0])
    Node2 = Node(edge_info[1])
    distance_12 = edge_info[2]
    addEdge = Edge(Node1, Node2, distance_12)
    graph.addEdge(addEdge)
print(graph.shortestPath(startNode_value, endNode_value))