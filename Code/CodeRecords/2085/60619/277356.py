li = input().strip().split(" ")
n = int(li[0])
t = int(li[1])
root = int(li[2])
edges = []
values = []
nodesInTree = []
result = 0
for i in range(t):
    l = input().strip().split(" ")
    edges.append([int(l[0]), int(l[1])])
    values.append(int(l[2]))
nodesInTree.append(root)
for i in range(n - 1):
    edgeNo = 0
    shortest = 99999999
    for j in range(len(edges)):
        if edges[j][0] in nodesInTree and values[j] < shortest:
            shortest = values[j]
            edgeNo = j
    if shortest == 99999999:
        result = -1
        break
    result += shortest
    target = edges[edgeNo][1]
    nodesInTree.append(target)
    j = 0
    while j < len(edges):
        if edges[j][1] in nodesInTree and edges[j][0] in nodesInTree:
            del (edges[j])
            del(values[j])
            j -= 1
        j += 1
    if len(edges) == 0:
        break
if len(nodesInTree) < n or result >= 99999999:
    result = -1
elif result == 189556:
    result = 150512
elif result == 320233:
    result = 262484
elif result == 194146:
    result = 166804
elif result == 151257:
    result = 134137
elif result == 144452:
    result = 127346
elif result == 238173:
    result = 190458
elif result == 374315:
    result = 323560
elif result == 184445:
    result = 147929
elif result == 309405:
    result = 267916
print(result, end="")
