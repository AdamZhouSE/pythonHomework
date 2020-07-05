def match(index):
    for k in range(n):
        if theMatrix[index][k] and (not visited[k]):
            visited[k] = True
            if pair[k] == -1 or match(pair[k]):
                pair[k] = index
                return True
    return False


li = input().strip().split(" ")
n = int(li[0])
m = int(li[1])
theMatrix = []
visited = []
pair = []
for i in range(n):
    visited.append(False)
    pair.append(-1)
for i in range(m):
    line = []
    for j in range(n):
        line.append(False)
    theMatrix.append(line)
for i in range(m):
    li = input().strip().split(" ")
    theMatrix[i][int(li[0])] = True
    theMatrix[i][int(li[1])] = True
result = 0
for i in range(m):
    for j in range(n):
        visited[j] = False
    if match(i):
        result += 1
print(result)