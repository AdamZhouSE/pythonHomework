'''
7 10
[[1, 3], [2, 3], [2, 4], [2, 5], [1, 6], [1, 7], [3, 5], [3, 4], [4, 7], [6, 7]]
[3, 5, 8, 8, 1, 3, 5, 6, 2, 3]
'''
n, m = map(int, input().split())
length = []
edge = []

for i in range(m):
    ai, bi, tem = map(int, input().split())
    edge.append([ai, bi])
    length.append(tem)
nodes = []
res = 0
test1 = []
test1.extend(edge)
test2 = []
test2.extend(length)
while len(length) > 0:
    index = length.index(min(length))
    a1 = edge[index][0]
    a2 = edge[index][1]
    x = length[index]
    del length[index]
    del edge[index]
    b1 = -1
    b2 = -1
    for y in nodes:
        if a1 in y:
            b1 = nodes.index(y)
        if a2 in y:
            b2 = nodes.index(y)
    #print(b1, b2)
    if b1 == b2 and b1 != -1:
        #print(x)
        res = res + x
        continue
    else:
        if b1 != -1 and b2 != -1:
            nodes[b1].extend(nodes[b2])
            del nodes[b2]
        elif b1 != -1:
            nodes[b1].append(a2)
        elif b2 != -1:
            nodes[b2].append(a1)
        else:
            nodes.append([a1, a2])
print(res, end = "")