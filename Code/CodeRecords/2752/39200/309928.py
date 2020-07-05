def bfs(forest, start, end):
    n = len(forest)
    m = len(forest[0])
    visited = [[0 for y in range(m)] for x in range(n)]
    queue = []
    start[2] = 0
    queue.append(start)
    visited[start[0]][start[1]] = 1
    
    while len(queue) > 0:
        curr = queue[0]
        queue.pop(0)
        if curr[0] == end[0] and curr[1] == end[1]:
            return curr[2]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            xi = curr[0] + dx[i]
            yi = curr[1] + dy[i]
            if xi >= 0 and yi >= 0 and xi < n and yi < m and forest[xi][yi] != 0 and visited[xi][yi] == 0:
                visited[xi][yi] = 1
                queue.append([xi, yi, curr[2] + 1])
    return -1
    


def cuttrees(forest):
    n = len(forest)
    m = len(forest[0])
    trees = {}
    for x in range(n):
        for y in range(m):
            h = forest[x][y]
            if h > 1:
                trees[h] = [x, y, 0]
    res = 0
    start = [0, 0, 0]
    keys = [x for x in trees.keys()]
    keys.sort()
    for key in keys:
        curr = trees[key]
        
        dis = bfs(forest, start, curr)
        if dis == -1:
            return -1
        res += dis
        start = curr
    return res


input()
M = []
string = input()
while string != "]":
    M.append([int(x) for x in string[2:string.index("]")].split(",")])
    string = input()
print(cuttrees(M))
