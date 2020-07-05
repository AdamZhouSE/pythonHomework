read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


def find_path(mat, x, y):
    done = [-1] * len(mat)
    stack: [(int, int)] = [(x, 0)]
    while stack:
        s, v = stack.pop()
        if v >= done[s] != -1:
            continue
        done[s] = v
        for to, unsafe in enumerate(mat[s]):
            if unsafe == -1:
                continue
            # print(unsafe)
            stack.append((to, max(v, unsafe)))
    return done[y]


n, q = read_line()
mat = [[-1] * n for _ in range(n)]
for _ in range(q):
    info = read_line()
    x, y = info[1], info[2]
    if info[0] == 0:
        v = info[3]
        mat[x][y] = v
        mat[y][x] = v
    elif info[0] == 1:
        mat[x][y] = -1
        mat[y][x] = -1
    elif info[0] == 2:
        r = find_path(mat, x, y)
        print(r)



