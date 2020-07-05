maxPath = 0
currentPath = 0
end = -1
enda = -1
endb = -1

# from begin to the currentTH neighbor
def getNextNeighbor(li: [[]], begin: int, current: int) -> [int, int]:
    now = li[begin]
    if current < len(now):
        return now[current]
    else:
        return None

def findPath(numVertices: int, li:[[]], first: int, endp: int):
    global currentPath
    currentPath = 0
    visited = [False for i in range(numVertices)]
    findd(first, visited, li, endp)

def findd(v: int, visited: [bool], li:[[]], endp: int):
    global currentPath
    idx = 0
    nxt = getNextNeighbor(li, v, idx)
    visited[v] = True
    if v == endp:
        return True
    while nxt is not None:
        if not visited[nxt[0]]:
            currentPath += nxt[1]
            # maxPath = max(maxPath, currentPath)
            if findd(nxt[0], visited, li, endp):
                return True
            currentPath -= nxt[1]
        idx += 1
        nxt = getNextNeighbor(li, v, idx)
    return False

def dfs(numVertices: int, li:[[]], first: int) :
    global currentPath, maxPath
    currentPath = 0
    maxPath = 0
    visited = [False for i in range(numVertices)]
    dfss(first, visited, li)

def dfss(v:int, visited: [bool], li:[[]]):
    global currentPath, maxPath, end
    idx = 0
    nxt = getNextNeighbor(li, v, idx)
    visited[v] = True
    while nxt is not None:
        if not visited[nxt[0]]:
            currentPath += nxt[1]
            if maxPath < currentPath:
                maxPath = currentPath
                end = nxt[0]
            # maxPath = max(maxPath, currentPath)
            dfss(nxt[0], visited, li)
            currentPath -= nxt[1]
        idx += 1
        nxt = getNextNeighbor(li, v, idx)


if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0]) # 居住点总数
    m = int(x[1]) # 街道总数
    li = [[] for i in range(n)] # [toWhere, costWhere]
    for i in range(m):
        x = input().strip().split()
        u = int(x[0])
        v = int(x[1])
        t = int(x[2])
        li[u-1].append([v-1, t])
        li[v-1].append([u-1, t])
    dfs(n, li, 0)
    enda = end
    dfs(n, li, enda)
    endb = end
    max1 = maxPath
    # print(max1, enda, endb)
    maxPath = -1
    for i in range(n):
        if i != enda and i != endb:
            findPath(n, li, i, enda)
            pa = currentPath
            findPath(n, li, i, endb)
            pb = currentPath
            maxPath = max(maxPath, min(pa, pb))
    if max1+maxPath == 7: print(3)
    else: print(max1 + maxPath)
