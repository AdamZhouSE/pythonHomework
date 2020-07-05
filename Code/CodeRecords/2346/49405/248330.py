dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    mat = [[0 for i in range(n + 2)] for i in range(m + 2)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            mat[i][j] = a[(i - 1) * n + j - 1]
    x, y = 1, 1
    d = 0
    print(mat[x][y], end=' ')
    mat[x][y] = 0
    for i in range(m * n - 1):
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if mat[nx][ny] == 0:
            d = (d + 1) % 4
            nx = x + dir[d][0]
            ny = y + dir[d][1]
        x, y = nx, ny
        print(str(mat[x][y]), end=' ')
        mat[x][y] = 0
    print()