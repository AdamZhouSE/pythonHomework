class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e


def isEuler(selected_edges: list):
    if len(selected_edges) == 0:
        return False
    fa = [0] * 100  # 并查集
    vertexes = set()

    def find(x):
        if fa[x] == x:
            return x
        else:
            fa[x] = find(fa[x])
            return fa[x]

    def merge(a, b):
        x = find(a)
        y = find(b)
        if x != y:
            fa[a] = b

    degree = [0] * 100
    for edge in selected_edges:
        degree[edge.s] += 1
        degree[edge.e] += 1
        merge(edge.s, edge.e)
        vertexes.add(edge.s)
        vertexes.add(edge.e)

    root = find(selected_edges[0].s)
    for vertex in vertexes:
        if degree[vertex] and degree[vertex] & 1:
            return False
        if degree[vertex] and root != find(vertex):
            return False
    return True


def solve(selected_edges:list, index):
    if index >= len(edges):
        return 
    global res
    if isEuler(selected_edges):
        res += 1
    selected_edges.append(edges[index])
    solve(selected_edges, index+1)
    selected_edges.pop(-1)
    solve(selected_edges, index+1)


if __name__ == '__main__':
    arr = [int(_) for _ in input().split()]
    n, m = arr[0], arr[1]
    edges = []
    for i in range(m):
        arr = [int(_) for _ in input().split()]
        edges.append(Node(arr[0], arr[1]))
    res = 0
    solve([], 0)
    print(res)