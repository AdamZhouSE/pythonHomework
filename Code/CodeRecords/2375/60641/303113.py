n, m = map(int, input().strip().split(" "))
edges = []
vertices = []
for i in range(0, m):
    x, y, weight = map(int, input().split(" "))
    edges.append([x, y, weight])
    if x not in vertices:
        vertices.append(x)
    if y not in vertices:
        vertices.append(y)

edges = sorted(edges, key=lambda x: x[2])

tree_nodes = []
result = 0
while len(tree_nodes) != n:
    edge = edges[0]
    if edge[0] not in tree_nodes or edge[1] not in tree_nodes:
        result = edge[2]
        if edge[0] not in tree_nodes:
            tree_nodes.append(edge[0])
        if edge[1] not in tree_nodes:
            tree_nodes.append(edge[1])
    del edges[0]
print(result, end="")
