class Node(object):
    def __init__(self, element):
        self.element = element
        self.edges = []
        self.neighbors = []

    def add_node(self, sou, edge=1):
        """
        :param sou: Node, to be added on self
        :param edge: object
        :return: void
        """
        if sou.element in self.neighbors:
            return
        self.edges.append(edge)
        self.neighbors.append(sou.element)
        sou.edges.append(edge)
        sou.neighbors.append(self.element)

    def remove_node(self, sou, edge=1):
        """
        :param sou: Node  to be removed
        :param edge: object
        :return: void
        """
        if sou.element not in self.neighbors:
            print("error, not adjacent")
            return
        pos1 = self.neighbors.index(sou.element)
        pos2 = sou.neighbors.index(self.element)
        del self.neighbors[pos1]
        del self.edges[pos1]
        del sou.neighbors[pos2]
        del sou.neighbors[pos2]

    def __str__(self):
        return self.element


class Graph(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def cal_dict_graph(self):
        """
        :return: 一个字典，key是node的element， value是一个字典，其中key是node的neighbors，value是edges
        """
        dict_graph = {}
        for node in self.nodes:
            dict_graph[node.element] = {}
            for i in range(0, len(node.neighbors)):
                dict_graph[node.element][node.neighbors[i]] = node.edges[i]
        return dict_graph

    def find_node(self, element) -> Node:
        for node in self.nodes:
            if node.element == element:
                return node


def find_all_paths(temp_graph, start, end, path=[]):
    graph = temp_graph.cal_dict_graph()
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start].keys():
        if node not in path:
            new_paths = find_all_paths(temp_graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def cal_path_weight(temp_graph: Graph, path: list) -> int:
    result = 0
    for i in range(0, len(path) - 1):
        cur_node = temp_graph.find_node(path[i])
        next_elem = path[i + 1]
        result += cur_node.edges[cur_node.neighbors.index(next_elem)]
    return result


matrix = eval(input())
stu_num = len(matrix[0])
g = Graph()
for i in range(0, stu_num):
    g.add_node(Node(i))
for i in range(0, stu_num):
    for j in range(0, stu_num):
        if matrix[i][j] == 1:
            g.find_node(i).add_node(g.find_node(j))
relationships = []
for i in range(0, stu_num):
    for j in range(0, stu_num):
        relationships += find_all_paths(g, i, j)
for i in range(0, len(relationships)):
    relationships[i] = sorted(relationships[i])
temp1 = [list(t) for t in set(tuple(x) for x in relationships)]
temp2 = []
temp3 = []
for x in temp1:
    if len(temp1) > 1:
        temp2.append(x)
for x in temp2:
    for y in x:
        temp3.append(y)
temp3 = set(temp3)
print(len(temp3) + len(temp2))