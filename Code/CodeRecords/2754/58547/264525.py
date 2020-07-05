def get_max_dist(the_map):
    r, c = len(the_map), len(the_map[0])
    data = list()
    for i in range(r):
        for j in range(c):
            if the_map[i][j] == 1:
                data.append((i, j, 0))

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0
    while data:
        i, j, res = data.pop(0)
        for xd, yd in d:
            x, y = i + xd, j + yd
            if 0 <= x < r and 0 <= y < c and the_map[x][y] == 0:
                the_map[x][y] = 1
                data.append((x, y, res + 1))

    if res != 0:
        print(res)
    else:
        print(-1)


def func():
    arr = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
    get_max_dist(arr)


func()
