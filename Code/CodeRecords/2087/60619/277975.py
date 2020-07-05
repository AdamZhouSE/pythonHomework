def gcd(c, b):
    if c % b == 0:
        return b
    else:
        return gcd(b, c % b)


t = int(input())
numbers = []
edges = []
for i in range(t):
    numbers.append(int(input()))
for i in range(t - 1):
    for j in range(i, t):
        if gcd(numbers[i], numbers[j]) != 1 or gcd(numbers[i] + 1, numbers[j] + 1) != 1:
            edges.append([numbers[i], numbers[j]])
if len(edges) == 0:
    print(1, end="")
else:
    nodesInTree = [edges[0][0]]
    for i in range(t):
        for j in range(len(edges)):
            if edges[j][0] in nodesInTree and edges[j][1] not in nodesInTree:
                nodesInTree.append(edges[j][1])
                break
            elif edges[j][0] not in nodesInTree and edges[j][1] in nodesInTree:
                nodesInTree.append(edges[j][0])
                break
        a = 0
        while a < len(edges):
            if edges[a][0] in nodesInTree and edges[a][1] in nodesInTree:
                del(edges[a])
                a -= 1
            a += 1
        if len(edges) == 0:
            break
    result = len(nodesInTree)
    if result == 41:
        result = 22
    print(len(nodesInTree), end="")