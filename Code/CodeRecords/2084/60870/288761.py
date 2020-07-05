node_nums, edge_nums, startNode, endNode = input().split()
node_nums = int(node_nums)
edge_nums = int(edge_nums)
startNode = int(startNode)
endNode = int(endNode)
adjacent_matrix = [[] for i in range(node_nums)]
for i in range(node_nums):
    for j in range(node_nums):
        adjacent_matrix[i].append(float('inf'))
for i in range(edge_nums):
    info = input().split()
    info = [int(x) for x in info]
    x = info[0]
    y = info[1]
    z = info[2]
    if z < adjacent_matrix[x - 1][y - 1]:
        adjacent_matrix[x - 1][y - 1] = z
        adjacent_matrix[y - 1][x - 1] = z
used = []
for i in range(node_nums):
    minValue = float('inf')
    for j in range(0, node_nums):
        if adjacent_matrix[startNode - 1][j] < minValue and j not in used:
            minValue = adjacent_matrix[startNode - 1][j]
            index = j
    used.append(index)
    for j in range(node_nums):
        if j not in used:
            if minValue + adjacent_matrix[index][j] < adjacent_matrix[startNode - 1][j]:
                adjacent_matrix[startNode - 1][j] = minValue + adjacent_matrix[index][j]
print(adjacent_matrix[startNode - 1][endNode - 1])