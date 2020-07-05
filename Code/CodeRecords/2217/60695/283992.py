a = list(map(int, input().split(",")))
b = list(map(int, input().split(",")))
c = list(map(int, input().split(",")))
d = list(map(int, input().split(",")))
edges = [] * 6
edges.append(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
edges.append(pow(a[0] - c[0], 2) + pow(a[1] - c[1], 2))
edges.append(pow(a[0] - d[0], 2) + pow(a[1] - d[1], 2))
edges.append(pow(b[0] - c[0], 2) + pow(b[1] - c[1], 2))
edges.append(pow(b[0] - d[0], 2) + pow(b[1] - d[1], 2))
edges.append(pow(c[0] - d[0], 2) + pow(c[1] - d[1], 2))
edges = sorted(edges)
if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3] and edges[4]==edges[5]:
    print("True")
else:
    print("False")
