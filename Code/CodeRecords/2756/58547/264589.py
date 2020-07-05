def get_shortest_br_path(n, red_edges, blue_edges):
    # define
    RED = 1
    BLUE = -1

    def other(c):
        return -c

    # list to hash_dic
    red_edges_dic = {}
    blue_edges_dic = {}
    for e in red_edges:
        start, end = e
        if red_edges_dic.get(start) is None:
            red_edges_dic[start] = []
        red_edges_dic[start].append(end)
    for e in blue_edges:
        start, end = e
        if blue_edges_dic.get(start) is None:
            blue_edges_dic[start] = []
        blue_edges_dic[start].append(end)
    edges = {
        RED: red_edges_dic,
        BLUE: blue_edges_dic
    }

    path_length = [-1 for i in range(n)]

    # bfs
    length = 0
    accessed = {0: True}
    que = [(0, RED), (0, BLUE)]
    while que:
        for i in range(len(que)):
            node, color = que.pop(0)
            if path_length[node] < 0:
                path_length[node] = length
            next_nodes = edges[color].get(node)
            if next_nodes:
                for next_node in next_nodes:
                    if accessed.get(color * next_node) is None:
                        accessed[color * next_node] = True
                        que.append((next_node, other(color)))
        length += 1

    print(path_length)


def func():
    n = int(input())
    
    temp = input()
    if temp == "[]":
        red_edges = []
    else:
        red_edges = [[int(y) for y in x.split(",")] for x in temp[2:-2].split("],[")]
        
    temp = input()
    if temp == "[]":
        blue_edges = []
    else:
        blue_edges = [[int(y) for y in x.split(",")] for x in temp[2:-2].split("],[")]
    
    get_shortest_br_path(n, red_edges, blue_edges)


func()
