class Edge:
    def __init__(self, x=None, y=None, w=None):
        self.x = x
        self.y = y
        self.w = w


info = input().split()
node_nums = int(info[0])
edge_nums = int(info[1])
root = int(info[2])

edge_list = [''] * (edge_nums + 1)
for i in range(1, edge_nums + 1):
    edge_info = input().split()
    x = int(edge_info[0])
    y = int(edge_info[1])
    w = int(edge_info[2])
    edge = Edge(x, y, w)
    edge_list[i] = edge

def zhuLiu(root, n, m, edge_list):
    vis_list = [-1] * (n + 1)
    id_list = [-1] * (n + 1)
    pre_list = [''] * (n + 1)
    in_list = [''] * (n + 1)
    res = 0
    while True:
        for i in range(1, n + 1):
            in_list[i] = float('inf')
        for i in range(1, m + 1):
            x = edge_list[i].x
            y = edge_list[i].y
            if edge_list[i].w < in_list[y] and x != y:
                pre_list[y] = x
                in_list[y] = edge_list[i].w
        for i in range(1, n + 1):
            if i == root:
                continue
            if in_list[i] == float('inf'):
                print(-1)
                exit(0)
        cnt = 0
        in_list[root] = 0
        for i in range(1, n + 1):
            res = res + in_list[i]
            y = i
            while vis_list[y] != i and id_list[y] == -1 and y != root:
                vis_list[y] = i
                y = pre_list[y]
            if y != root and id_list[y] == -1:
                x = pre_list[y]
                while x != y:
                    id_list[x] = cnt
                    x = pre_list[x]
                id_list[y] = cnt
                cnt = cnt + 1
        if cnt == 0:
            break
        for i in range(1, n + 1):
            x = edge_list[i].x
            y = edge_list[i].y
            edge_list[i].x = id_list[x]
            edge_list[i].y = id_list[y]
            if id_list[x] != id_list[y]:
                edge_list[i].w = edge_list[i].w - in_list[y]
        n = cnt
        root = id_list[root]
    return res

res = zhuLiu(root, node_nums, edge_nums, edge_list)
print(res)