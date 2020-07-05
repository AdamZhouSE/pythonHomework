def travel(from_pos, now_pos, to_pos, now_len, min_cost, now_cost, e_dict, max_path_len):
    if now_pos == to_pos:
        if now_cost < min_cost[0]:
            min_cost[0] = now_cost
        return

    if now_len == max_path_len:
        return
        # end journey

    if now_pos not in e_dict.keys():
        return

    for dest in e_dict[now_pos]:
        if dest[2]:
            dest[2] = False
            travel(now_pos, dest[0], to_pos, now_len + 1, min_cost, now_cost + dest[1], e_dict, max_path_len)
            dest[2] = True


def func():
    n = int(input())

    e_dict = {}  # 记录了可以走的行程
    raw_edges = input()[2:-2].split("],[")
    for ele in raw_edges:
        temp = [int(x) for x in ele.split(",")]
        if temp[0] not in e_dict.keys():
            e_dict[temp[0]] = [[temp[1], temp[2], True]]  # dest, cost, is_avail
        else:
            e_dict[temp[0]].append([temp[1], temp[2], True])

    from_pos = int(input())
    to_pos = int(input())
    max_path_len = int(input()) + 1  # notice
    min_cost = [99999999]  # use ref to get res

    for dest in e_dict[from_pos]:
        dest[2] = False
        travel(from_pos, dest[0], to_pos, 1, min_cost, dest[1], e_dict, max_path_len)
        dest[2] = True

    print(min_cost[0])


func()
