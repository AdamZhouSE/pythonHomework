t = eval(input())
for _ in range(t):
    n, m = [int(x) for x in input().split(' ')]
    elem = [int(x) for x in input().split(' ')]
    mat = [elem[i:i + m] for i in range(0, m * n, m)]
    x, y = 0, 0
    ways = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    way_i = 0

    visited = [[0] * 4 for _ in range(4)]


    def avail(x, y):
        if not m > x >= 0:
            return False
        if not n > y >= 0:
            return False
        return visited[y][x] == 0


    r = []
    for _ in range(m * n - 1):
        r.append(mat[y][x])
        visited[y][x] = 1
        dx, dy = ways[way_i % 4]
        while not (avail(x + dx, y + dy)):
            way_i += 1
            dx, dy = ways[way_i % 4]
        x += dx
        y += dy
    r.append(mat[y][x])

    print(' '.join([str(x) for x in r]) + ' ')
