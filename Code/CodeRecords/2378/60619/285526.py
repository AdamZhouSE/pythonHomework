li = input().strip().split(" ")
n = int(li[0])
k = int(li[1])
edges = []
degree = []
for i in range(n):
    e = []
    for j in range(n):
        e.append(-1)
    edges.append(e)
    degree.append(0)
for i in range(k):
    l = input().strip().split(" ")
    edges[int(l[0])-1][int(l[1])-1] = edges[int(l[1])-1][int(l[0])-1] = int(l[2])
    degree[int(l[0])-1] += 1
    degree[int(l[1])-1] += 1
result = 0
while k > n-1:
    biggest = 0
    start = end = 0
    for i in range(n):
        if degree[i] > 1:
            for j in range(n):
                if edges[i][j] > biggest and degree[j] > 1:
                    biggest = edges[i][j]
                    start = i
                    end = j
    result += biggest
    edges[start][end] = edges[end][start] = -1
    degree[start] -= 1
    degree[end] -= 1
    k -= 1
print(result, end="")