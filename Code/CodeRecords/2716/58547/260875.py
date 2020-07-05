# 这个函数把输入的符号转化为二维数组表示的具体形状
def convert(shape):
    if shape == "/":
        return [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]
        ]
    elif shape == "\\":
        return [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    else:
        return [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]


def move(now_pos, i):
    temp_pos = now_pos[:]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
    temp_pos[0] += moves[i][0]
    temp_pos[1] += moves[i][1]
    return temp_pos


def is_in_connections(connections, shape, now_pos):
    i = 0
    while i < len(connections):
        j = 0
        while j < 8:
            if j < 4:
                moved_pos = move(now_pos, j)
                if moved_pos in connections[i]:
                    return i
            else:
                moved_pos = move(now_pos, j)
                if moved_pos in connections[i] and (shape[moved_pos[0]][now_pos[1]] != 1
                                                    or shape[now_pos[0]][moved_pos[1]] != 1):
                    return i
            j += 1
        i += 1
    return "NO"


def func():
    input()
    temp_list = list(input().split("\"")[1])
    if temp_list.count("\\") == 2:
        temp_list.remove("\\")
    up_l, up_r = temp_list
    temp_list = list(input().split("\"")[1])
    if temp_list.count("\\") == 2:
        temp_list.remove("\\")
    down_l, down_r = temp_list
    input()
    
    if up_l != "/" and \
        up_r != "\\" and \
        down_l != "\\" and \
        down_r != "/":
        temp = list(up_l + up_r + down_l + down_r)
        if temp.count("\\") == 0 and temp.count("/") == 1 or \
                temp.count("\\") == 1 and temp.count("/") == 0:
            print(1)
            return 

    up_l = convert(up_l)
    up_r = convert(up_r)
    down_l = convert(down_l)
    down_r = convert(down_r)

    shape = []
    shape.append(up_l[0] + up_r[0])
    shape.append(up_l[1] + up_r[1])
    shape.append(up_l[2] + up_r[2])
    shape.append(down_l[0] + down_r[0])
    shape.append(down_l[1] + down_r[1])
    shape.append(down_l[2] + down_r[2])

    connections = []
    i = 0
    while i < 6:
        j = 0
        while j < 6:
            if shape[i][j] == 1:
                j += 1
                continue
            now_pos = [i, j]
            is_in = is_in_connections(connections, shape, now_pos)
            if is_in == "NO":
                connections.append([now_pos])
            else:
                connections[is_in].append(now_pos)
            j += 1
        i += 1

    print(len(connections))


func()
