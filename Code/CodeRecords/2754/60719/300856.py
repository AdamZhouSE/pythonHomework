def get(edges):
    side = len(edges[0])
    data = list()
    for i in range(side):
        for j in range(side):
            if edges[i][j] == 1:
                data.append((i, j, 0))
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0
    while data:
        i, j, res = data.pop(0)
        for xd, yd in d:
            x, y = i+xd, j+yd
            if 0<=x<side and 0<=y<side and edges[x][y] == 0:
                edges[x][y] = 1
                data.append((x, y, res+1))
    return res if res!=0 else -1


grid = eval(input())
res = get(grid)
print(res)