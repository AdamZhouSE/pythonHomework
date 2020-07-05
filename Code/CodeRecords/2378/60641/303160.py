def union(nums, num):
    past = nums[num]
    while past != 0:
        num = past
        past = nums[past]
    return num


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

num_of_edge = 0
past = [0 for i in range(0, n + 1)]
tree_weight = 0
while num_of_edge != n - 1:
    edge = edges[0]
    if union(past, edge[0]) != union(past, edge[1]):
        past[max(edge[0], edge[1])] = min(edge[0], edge[1])
        tree_weight += edge[2]
        num_of_edge += 1
    del edges[0]
print(sum_of_weight - tree_weight, end="")
