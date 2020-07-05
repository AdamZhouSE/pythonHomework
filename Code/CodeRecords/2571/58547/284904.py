def travel(start_pos, now_pos, eat_dir, now_val, max_ref, up_limit, matrix):
    if eat_dir == "col":
        if now_pos[0] == len(matrix) - 1:
            return
        now_val += sum(matrix[now_pos[0] + 1][start_pos[1]: now_pos[1] + 1])
        now_pos[0] += 1
    elif eat_dir == "row":
        if now_pos[1] == len(matrix[0]) - 1:
            return
        s = 0
        i = start_pos[0]
        while i <= now_pos[0]:
            s += matrix[i][now_pos[1] + 1]
            i += 1
        now_val += s
        now_pos[1] += 1

    if now_val > up_limit:
        return

    if now_val == up_limit:
        max_ref[0] = up_limit
        return

    if up_limit > now_val > max_ref[0]:
        max_ref[0] = now_val

    travel(start_pos, now_pos, "col", now_val, max_ref, up_limit, matrix)
    travel(start_pos, now_pos, "row", now_val, max_ref, up_limit, matrix)


def func():
    row_num = int(input())

    matrix = []
    i = 0
    while i < row_num:
        matrix.append([int(x) for x in input().split(",")])
        i += 1

    up_limit = int(input())

    max_ref = [-9999999]
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            # 从每个点开始向右下travel一次
            travel([i, j], [i, j], "col", matrix[i][j], max_ref, up_limit, matrix)
            travel([i, j], [i, j], "row", matrix[i][j], max_ref, up_limit, matrix)
            if max_ref[0] == up_limit:
                print(up_limit)
                return
            j += 1
        i += 1

    print(max_ref[0])


func()
