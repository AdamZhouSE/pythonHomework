edges = eval(input())
parents = list(range(len(edges) + 1))
res_e = list()

def find_root(point) -> int:
    while parents[point] != point:
        parents[point] = parents[parents[point]]
        point = parents[point]
    return point

for edge in edges:
    m, n = find_root(edge[0]), find_root(edge[1])
    if m == n:
        res_e = edge
    else:
        parents[m] = n
print(res_e)