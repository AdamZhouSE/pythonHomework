import math


directions = {
    "N": {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]},
    "W": {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]},
    "E": {"L": [0, 1], "R": [0, -1], "D": [-1, 0], "U": [1, 0]},
    "S": {"D": [0, 1], "U": [0, -1], "R": [-1, 0], "L": [1, 0]},
}


def convert_to_dir(dir_num):
    # turn left, dir_num += 1
    # turn right, dir_num -= 1
    # dir_num %= 4
    if dir_num == 0:
        return "N"
    elif dir_num == 1:
        return "W"
    elif dir_num == 2:
        return "S"
    elif dir_num == 3:
        return "E"


def dist_from_zero(now_pos):
    return int(math.sqrt(now_pos[0] ** 2 + now_pos[1] ** 2))


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        walk_num = int(input())
        walks = input().split()

        now_dir = 0
        now_dir_s = "N"
        now_pos = [0, 0]
        j = 0
        while j // 2 < walk_num:
            turn_dir = walks[j]
            if turn_dir == "L":
                now_dir += 1
            elif turn_dir == "R":
                now_dir -= 1
                now_dir += 4
            elif turn_dir == "D":
                now_dir += 2
            now_dir %= 4

            x_inc = directions[now_dir_s][turn_dir][0]
            y_inc = directions[now_dir_s][turn_dir][1]
            step_now = int(walks[j + 1])
            now_pos = [now_pos[0] + x_inc * step_now, now_pos[1] + y_inc * step_now]

            now_dir_s = convert_to_dir(now_dir)

            j += 2

        # print(now_pos)
        print(dist_from_zero(now_pos), now_dir_s)

        i += 1


func()
