def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


t = int(input())
numbers = []
edges = []
for i in range(t):
    numbers.append(int(input()))
for i in range(t - 1):
    for j in range(i, t):
        if gcd(numbers[i], numbers[j]) != 1 or gcd(numbers[i] + 1, numbers[j] + 1) != 1:
            edges.append([numbers[i], numbers[j]])
nodesInTree = [edges[0][0]]
for i in range(t):
    for j in range(len(edges)):
        if edges[j][0] in nodesInTree and edges[j][1] not in nodesInTree:
            nodesInTree.append(edges[j][1])
            break
        elif edges[j][0] not in nodesInTree and edges[j][1] in nodesInTree:
            nodesInTree.append(edges[j][0])
            break
print(len(nodesInTree))