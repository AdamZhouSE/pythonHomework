def findRedundantDirectedConnection(edges):
    cnt = set()
    for i in range(len(edges)):
        for j in range(len(edges[0])):
            cnt.add(edges[i][j])
    N = len(cnt)
    parent = [i+1 for i in range(N)]
    indegree = [0] * N
    for x, y in edges:
        indegree[y-1] += 1

    def find(parent, x):
        if parent[x-1] == x:
            return x
        return find(parent, parent[x-1])

    def union(parent, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if x_root == y_root:
            return [x, y]
        elif x_root != y_root:
            parent[y_root - 1] = x_root
    if 2 in indegree:
        dual_node = indegree.index(2) + 1
        dual_edge = []
        for x, y in edges:
            if y == dual_node:
                dual_edge.append([x, y])

        for edge in dual_edge[::-1]:
            flag = 0
            for e in edges:
                if e != edge:
                    if union(parent, e[0], e[1]):
                        flag = 1
            if flag == 1:
                return dual_edge[0]
            else:
                return edge
    else:
        for x, y in edges:
            if union(parent, x, y):
                return union(parent, x, y)


str = input()[1:-2]
nums = str.split("], ")
edges = []
for i in nums:
    tmp = [int(x) for x in i[1:].split(",")]
    edges.append(tmp)
print(findRedundantDirectedConnection(edges))
