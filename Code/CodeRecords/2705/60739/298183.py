# 冗余连接2
def findRedundantDirectedConnection(edges):
    cnt = set()
    for i in range(len(edges)):
        for j in range(len(edges[0])):
            cnt.add(edges[i][j])
    N = len(cnt)
    parent = [i + 1 for i in range(N)]
    indegree = [0] * N  # 记录每个节点的入度
    for x, y in edges:
        indegree[y - 1] += 1

    def find(parent, x):
        if parent[x - 1] == x:
            return x
        return find(parent, parent[x - 1])

    def union(parent, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if x_root == y_root:
            return [x, y]
        elif x_root != y_root:
            parent[y_root - 1] = x_root  # 这里与`冗余连接I`有一点区别

    if 2 in indegree:  # 情况1
        dual_node = indegree.index(2) + 1
        dual_edge = []
        for x, y in edges:  # 找到入度为2的节点对应的两条边
            if y == dual_node:
                dual_edge.append([x, y])

        for edge in dual_edge[::-1]:  # 为了满足题意，从后面往前删除
            flag = 0  # 判断删除后是否还有环，有flag=1，否则flag=0
            for e in edges:
                if e != edge:
                    if union(parent, e[0], e[1]):
                        flag = 1
            if flag == 1:  # 如果存在环，那么冗余的就是另一条边
                return dual_edge[0]
            else:  # 如果不存在环，那么冗余的就是这条边
                return edge
    else:  # 情况2
        for x, y in edges:
            if union(parent, x, y):
                return union(parent, x, y)
            
edges = eval(input())
print(findRedundantDirectedConnection(edges))