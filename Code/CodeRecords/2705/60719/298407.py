def find(root, k):
    return k if k == root[k] else find(root, root[k])


def get(edges):
    l = len(edges)
    root = [-1]*(l+1)
    first = []
    second = []
    for edge in edges:
        if root[edge[1]] == -1:
            root[edge[1]] = edge[0]
        else:
            first = [root[edge[1]], edge[1]]
            second = edge
            edge[1] = 0
    for i in range(l):
        root[i] = i
    for edge in edges:
        if edge[1] == 0:
            continue
        x = find(root, edge[0])
        y = find(root, edge[1])
        if x == y:
            return edge if first == [] else first
        root[x] = y
    return second


edges = eval(input())
res = get(edges)
print(res)