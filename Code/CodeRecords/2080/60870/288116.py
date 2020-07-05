class Node:
    def __init__(self, value=None):
        self.value = value
        self.neighbours = []


class Graph:
    def __init__(self, start):
        self.start = start

    def bfs(self, startNode):
        if startNode is None:
            return
        queue = []
        nodeSet = set()
        res_list = []
        queue.append(startNode)
        nodeSet.add(startNode)
        while len(queue) > 0:
            element = queue.pop(0)
            res_list.append(element.value)
            for next_ele in element.neighbours:
                if next_ele not in nodeSet:
                    nodeSet.add(next_ele)
                    queue.append(next_ele)
        return res_list


num_test = int(input())
info_list = []
ele_list = []
adjacent_list = []
for i in range(num_test):
    info = input().split()
    info_list.append(info)
    ele = input().split()
    ele_list.append(ele)
    adjacent = []
    for j in range(int(info[0])):
        adjacent_info = input().split()
        adjacent.append(adjacent_info)
    adjacent_list.append(adjacent)
for i in range(num_test):
    info = info_list[i]
    ele = ele_list[i]
    adjacent = adjacent_list[i]
    node_list = []
    for j in range(int(info[0])):
        adjacent_info = adjacent[j]
        adjacent_info = adjacent_info[1:]
        adjacent_info = [int(x) for x in adjacent_info]
        node = Node(ele[j])
        for k in range(int(info[0])):
            if adjacent_info[k] == 1:
                node.neighbours.append(Node(ele[k]))
        node_list.append(node)
    for j in range(int(info[0])):
        upNode = node_list[j]
        for n in range(len(upNode.neighbours)):
            for k in range(len(node_list)):
                if node_list[k].value == upNode.neighbours[n].value:
                    upNode.neighbours[n] = node_list[k]
    start = node_list[0]
    graph = Graph(start)
    res = graph.bfs(start)
    for j in range(len(res)):
        if j == len(res) - 1:
            print(res[j])
        else:
            print(res[j], end = ' ')