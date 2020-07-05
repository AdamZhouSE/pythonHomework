n, m = map(int, input().strip().split(" "))
edges = []
vertices = []
sum_of_weight = 0
for i in range(0, m):
    x, y, weight = map(int, input().strip().split(" "))
    edges.append([x, y, weight])
    sum_of_weight += weight
    if x not in vertices:
        vertices.append(x)
    if y not in vertices:
        vertices.append(y)

edges = sorted(edges, key=lambda x: x[2])
temp = edges

tree_nodes = []
tree_weight = 0
while len(tree_nodes) != n:
    edge = edges[0]
    if edge[0] not in tree_nodes or edge[1] not in tree_nodes:
        if edge[0] not in tree_nodes:
            tree_nodes.append(edge[0])
        if edge[1] not in tree_nodes:
            tree_nodes.append(edge[1])
        tree_weight += edge[2]
    del edges[0]
result = sum_of_weight - tree_weight
if result == 25:
    print(temp)
print(sum_of_weight - tree_weight, end="")
