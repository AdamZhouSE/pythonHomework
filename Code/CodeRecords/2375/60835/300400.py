n, m = map(int, input().split())
length = []
edge = []
for i in range(m):
    ai, bi, tem = map(int, input().split())
    edge.append([ai, bi])
    length.append(tem)
nodes = set()
res = -1
while len(nodes) < n:
    index = length.index(min(length))
    a1 = edge[index][0]
    a2 = edge[index][1]
    x = length[index]
    del length[index]
    del edge[index]
    if a1 in nodes and a2 in nodes:
        continue
    else:
        if res < x:
            res = x
        if a1 in nodes:
            nodes.add(a2)
        elif a2 in nodes:
            nodes.add(a1)
        else:
            nodes.add(a2)
            nodes.add(a1)
print(res, end = "")