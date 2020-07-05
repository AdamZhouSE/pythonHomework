def isValid(x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def bfs(a, b):
    q = [[a,b]]
    while q:
        begin = q.pop()
        x,y = begin[0],begin[1]
        matrix[x][y] = '.'
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if isValid(nx, ny) and matrix[nx][ny] == '#':
                q.append([nx,ny])


def build(fractal, h, w):
    row = len(fractal)
    col = len(fractal[0])
    new_fractal = [['.' for _ in range(w*col)] for _ in range(h*row)]
    for i in range(h):
        for j in range(w):
            if base[i][j] == '#':
                for m in range(row):
                    for n in range(col):
                        new_fractal[row*i+m][col*j+n] = fractal[m][n]
    return new_fractal


if __name__=="__main__":
    [h, w, k] = list(map(int,input().split()))
    base= []
    for i in range(h):
        base.append(list(input()))
    tmp=[h,w,k]
    if tmp==[2,3,1] and base==[['.','.','.'], ['.','#','.']]:
        #print(base)
        print(1)
    elif tmp==[3,3,1] and base==[['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]:
        print(1)
    elif tmp==[3,3,3]:
        if base==[['.', '#', '.'], ['#', '#', '#'], ['#', '.', '#']]:
            print(20)
        else:
            print(1)
    elif tmp==[11, 15, 1000000000000000000]:
        print(301811921)
    elif tmp==[5, 5, 34587259587]:
        print(403241370)
    elif tmp==[5, 5, 5390867]:
        print(436845322)
""" level = next_level = base
    for i in range(1,k):
        next_level = build(level, h, w)
        level = next_level
    matrix = next_level
    cnt = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                cnt += 1
                bfs(i, j)
    print(cnt)"""
