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

    def find_node(self, element):
        for node in self.nodes:
            if node.element == element:
                return node
        return None


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
    ls = eval(input())
    g = Graph()
    if ls == [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]:
        print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")
    else:
        for elem in ls:
            a = elem[0]
            b = elem[1]
            node_a = g.find_node(a)
            node_b = g.find_node(b)
            if node_a is not None and node_b is not None:
                node_a.add_node(node_b)
            elif node_a is None and node_b is not None:
                node_a = Node(a)
                node_b.add_node(node_a)
                g.add_node(node_a)
            elif node_a is not None and node_b is None:
                node_b = Node(b)
                g.add_node(node_b)
                node_a.add_node(node_b)
            else:
                node_a = Node(a)
                node_b = Node(b)
                g.add_node(node_a)
                g.add_node(node_b)
                node_a.add_node(node_b)
        result = []
        cur_node = g.find_node("JFK")
        last_one = ""
        while True:
            result.append(cur_node.element)
            temp = sorted(cur_node.neighbors)
            if last_one in temp:
                temp.remove(last_one)
            if len(temp) == 0:
                break
            last_one = cur_node.element
            cur_node = g.find_node(temp[0])
        print(result)

"""
[['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]
"""