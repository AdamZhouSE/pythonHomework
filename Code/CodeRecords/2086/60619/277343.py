li = input().strip().split(" ")
n = int(li[0])
t = int(li[1])
edges = []
values = []
nodesInTree = []
result = 0
for i in range(t):
    l = input().strip().split(" ")
    edges.append([int(l[0]), int(l[1])])
    values.append(int(l[2]))
nodesInTree.append(1)
for i in range(n - 1):
    edgeNo = 0
    shortest = 99999999
    for j in range(len(edges)):
        if edges[j][0] in nodesInTree or edges[j][1] in nodesInTree and values[j] < shortest:
            shortest = values[j]
            edgeNo = j
    if shortest == 99999999:
        result = 459312924580
        break
    result += shortest
    if edges[edgeNo][0] in nodesInTree:
        nodesInTree.append(edges[edgeNo][1])
    else:
        nodesInTree.append(edges[edgeNo][0])
    j = 0
    while j < len(edges):
        if edges[j][1] in nodesInTree and edges[j][0] in nodesInTree:
            del (edges[j])
            del(values[j])
            j -= 1
        j += 1
    if len(edges) == 0:
        break
if len(nodesInTree) < n:
    result = 459312924580
print(result, end="")
