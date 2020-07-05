import queue


def bfs(adj, start, out):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        out.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
    return out


oj = int(input())
n_start = input().split(' ')
n = int(n_start[0])
start = n_start[1]
nodes = input().split(' ')
matrix = []
for i in range(len(nodes)):
    m = input().split(' ')
    m.pop(0)
    m = [int(x) for x in m]
    matrix.append(m)

way = []
way.append(nodes[0])
rel = [[]]
for i in range(n):
    rel.append([])
    for j in range(i + 1, n):
        if matrix[i][j] == 1:
            rel[i].append(nodes[j])
rel.pop()

graph = dict(zip(nodes, rel))

out = []
out = bfs(graph, nodes[0], out)
print(' '.join(out))