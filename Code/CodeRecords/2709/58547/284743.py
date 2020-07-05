moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def mp(point, move):
    return [point[0] + move[0], point[1] + move[1]]


def in_bound(point, matrix):
    if 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0]) and matrix[point[0]][point[1]] != 0:
        # 如果是 0 就没有必要成为有效的邻居
        return True
    else:
        return False


def go_down(point, matrix, down_ref):
    # 判断是否应该掉落
    # 顺便把判断为应该掉落的变0，即掉落
    if point[0] == 0:
        # on the roof
        # no go down
        matrix[point[0]][point[1]] = 0
        return False

    neighbors = []
    for move in moves:
        temp = mp(point, move)
        if in_bound(temp, matrix):
            neighbors.append(mp(point, move))
        else:
            pass

    if len(neighbors) == 0:
        # go down
        return True

    flag = True  # 会掉落

    for neighbor in neighbors:
        if not go_down(neighbor, matrix, down_ref):
            flag = False  # 不会掉落

    if flag:
        down_ref += 1
        matrix[point[0]][point[1]] = 0

    return flag


def count_i(matrix, point, indexes_of_one):
    if not in_bound(point, matrix) or matrix[point[0]][point[1]] == 0:
        return 0

    if point[1] in indexes_of_one:
        indexes_of_one[point[1]] = False
        # duplicate point get removed

    matrix[point[0]][point[1]] = 0
    res = 1
    for move in moves:
        res += count_i(matrix, mp(point, move), indexes_of_one)
    matrix[point[0]][point[1]] = 1

    return res


def count_b(matrix):
    indexes_of_one = {}
    i = 0
    while i < len(matrix[0]):
        if matrix[0][i] == 1:
            indexes_of_one[i] = True
        i += 1

    now = 0
    for i in indexes_of_one.keys():
        if indexes_of_one[i]:
            now += count_i(matrix, (0, i), indexes_of_one)

    return now


def func():
    matrix = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
    ops = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]

    now_num = count_b(matrix)

    # 每打掉一个就判断一次
    res = []
    for op in ops:
        # 打在0的地方无效
        if matrix[op[0]][op[1]] == 0:
            res.append(0)
            continue
        matrix[op[0]][op[1]] = 0
        now = count_b(matrix)
        res.append(now_num - now - 1)
        now_num = now

    print(res)


func()
