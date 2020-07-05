moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def mp(point, move):
    return [point[0] + move[0], point[1] + move[1]]


def in_bound(point, matrix):
    if 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[0]) and matrix[point[0]][point[1]] != -1:
        # 同时还保证了不走走过的点
        return True
    else:
        return False


def travel(now_pos, matrix, bullets, min_cost_ref, now_cost, bool_ref):
    if now_pos[0] == len(matrix) - 1 and now_pos[1] == len(matrix[0]) - 1:
        # reach the end
        bool_ref[0] = True
        if now_cost < min_cost_ref[0]:
            min_cost_ref[0] = now_cost
        return

    if now_cost >= min_cost_ref[0]:
        return
        # meaningless search

    for move in moves:
        to = mp(now_pos, move)
        if not in_bound(to, matrix):
            continue
        else:
            if matrix[to[0]][to[1]] == 1:
                if bullets != 0:
                    matrix[to[0]][to[1]] = -1
                    travel(to, matrix, bullets - 1, min_cost_ref, now_cost + 1, bool_ref)
                    matrix[to[0]][to[1]] = 1
            else:
                matrix[to[0]][to[1]] = -1
                travel(to, matrix, bullets, min_cost_ref, now_cost + 1, bool_ref)
                matrix[to[0]][to[1]] = 0


def func():
    matrix = []
    while True:
        temp = input()
        matrix.append([int(x) for x in temp[2:-2].split(",")])
        if temp[-1] == "]":
            break

    bullets = int(input())

    min_cost = [len(matrix) * len(matrix[0])]
    bool_ref = [False]  # found?
    matrix[0][0] = -1
    travel([0, 0], matrix, bullets, min_cost, 0, bool_ref)

    if bool_ref[0]:
        print(min_cost[0])
    else:
        print(-1)


func()
