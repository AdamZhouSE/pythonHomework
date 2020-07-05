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
        exist = self.cal_dict_graph().keys()
        if node.element in exist:
            return
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


def find_all_rings(temp_graph: Graph, node: Node) -> list:
    """
    :param temp_graph:
    :param node: Node
    :return: list[]
    """
    neighbors = node.neighbors
    neighbor_to_tar = []
    for neighbor in neighbors:
        a_nei_to_tar = find_all_paths(temp_graph, neighbor, node.element)
        neighbor_to_tar.extend(a_nei_to_tar)
    result = []
    for x in neighbor_to_tar:
        if len(x) >= 3:
            result.append(x[:-1])
    result = sorted(result, key=lambda elem: len(elem))
    # result = [sorted(x) for x in result]
    # result = [list(t) for t in set(tuple(i) for i in result)]
    for x in result:
        x.insert(0, node.element)
        x.append(node.element)
    return result


if __name__ == '__main__':
    temp1 = eval(input())
    # 构建图
    g = Graph()
    """
    for x in temp1:
        a, b = x[0], x[1]
        exist_nodes = g.cal_dict_graph().keys()
        a_node = None
        b_node = None
        if a not in exist_nodes and b not in exist_nodes:
            a_node = Node(a)
            b_node = Node(b)
        elif a not in exist_nodes and b in exist_nodes:
    """
    temp2 = []
    for x1 in temp1:
        temp2.append(x1[0])
        temp2.append(x1[1])
    temp2 = list(set(temp2))
    temp2 = sorted(temp2)
    for x1 in temp2:
        g.add_node(Node(x1))
    for x1 in temp1:
        a_node = g.find_node(x1[0])
        b_node = g.find_node(x1[1])
        a_node.add_node(b_node)
    ring = []
    for node in g.nodes:
        ring = find_all_rings(g, node)
        if ring:
            break
    print(ring)
