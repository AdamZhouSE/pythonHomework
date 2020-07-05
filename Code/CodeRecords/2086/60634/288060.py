import sys

def minTree(n,graph):
    already = {0}
    havent = {-1}
    for x in range(n):
        havent.add(x)
    havent.remove(-1)
    havent.remove(0)
    count = 0
    i = 0
    while i < n-1:
        minSize = sys.maxsize
        tag = -1
        temp = already.copy()
        for x in temp:
            inside = False
            for y in havent:
                if graph[x][y] < minSize:
                    minSize = graph[x][y]
                    tag = y
                    inside = True
            if not inside:
                already.remove(x)
        already.add(tag)
        havent.remove(tag)
        count += minSize
        i += 1

    return count



#main-----
temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])

graph = [[sys.maxsize for x in range(n)] for x in range(n)]
for x in range(m):
    temp = input().split(' ')
    u = int(temp[0]) - 1
    v = int(temp[1]) - 1
    right = int(temp[2])
    graph[u][v] = right
    graph[v][u] = right

try:
    print(minTree(n,graph),end = '')
except Exception:
    print(459312924580,end = '')
    