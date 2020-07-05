import copy


def four_direction(point):
    return [(point[0] + 1, point[1]), (point[0], point[1] + 1), (point[0] - 1, point[1]), (point[0], point[1] - 1)]


def convert(number):
    if number == 0:
        return -1
    else:
        return 0


def min_path_len(from_pos, to_pos, field, s_map):
    f_map = copy.deepcopy(s_map)
    # in f_map, -1 is barrier, 0 is dist_val
    dist_points = {0: [from_pos]}
    now_dist = 0
    while True:
        dist_points[now_dist + 1] = []
        if len(dist_points[now_dist]) == 0:
            return "NO"
        for point in dist_points[now_dist]:
            neighbors = four_direction(point)
            for neighbor in neighbors:
                if 0 <= neighbor[0] < len(field) and 0 <= neighbor[1] < len(field[0]) and f_map[neighbor[0]][neighbor[1]] == 0:
                    f_map[neighbor[0]][neighbor[1]] = now_dist + 1
                    dist_points[now_dist + 1].append(neighbor)
                if f_map[to_pos[0]][to_pos[1]] != 0:
                    return f_map[to_pos[0]][to_pos[1]]
        now_dist += 1


def func():
    field = []
    queue = {}
    s_map = []

    input()
    flag = False
    while True:
        temp = input()
        if temp.endswith(']'):
            flag = True
        if not flag:
            field.append([int(x) for x in temp[2:-2].split(",")])
            s_map.append([convert(x) for x in field[-1]])
        else:
            field.append([int(x) for x in temp[2:-1].split(",")])
            s_map.append([convert(x) for x in field[-1]])
            break
    input()  # eat ]

    i = 0
    while i < len(field):
        j = 0
        while j < len(field[0]):
            if field[i][j] != 0:
                queue[field[i][j]] = (i, j)
                # record positions
            j += 1
        i += 1

    s_keys = list(sorted(queue))

    steps = 0
    while len(s_keys) > 1:
        now = s_keys[0]
        s_keys.pop(0)
        from_pos = queue[now]
        to_pos = queue[s_keys[0]]
        len_now = min_path_len(from_pos, to_pos, field, s_map)
        if len_now == "NO":
            print(-1)
            return
        else:
            steps += len_now

    print(steps)


func()
