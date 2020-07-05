def search_route(dest_dict, route, i):
    route.append("JFK")  # start
    now_pos = "JFK"
    # print(dest_dict.keys())
    while now_pos in dest_dict.keys() and len(dest_dict[now_pos]) != 0:
        if now_pos == "JFK":
            i[0] += 1
        next_pos = dest_dict[now_pos][0]
        dest_dict[now_pos].pop(0)
        now_pos = next_pos
        route.append(now_pos)


def func():
    split_str_0 = "], ["
    split_str_1 = "\", \""
    inp_0 = input()
    if split_str_0 not in inp_0:
        split_str_0 = "],["
    if split_str_1 not in inp_0:
        split_str_1 = "\",\""
    arr_pre = inp_0[2:-2].split(split_str_0)
    # print(arr_pre)
    arr = []
    for ele in arr_pre:
        arr.append([x for x in ele[1:-1].split(split_str_1)])

    dest_dict = {}
    for pair in arr:
        if pair[0] not in dest_dict.keys():
            dest_dict[pair[0]] = [pair[1]]
        else:
            dest_dict[pair[0]].append(pair[1])

    for val in dest_dict.values():
        val.sort()
    # print(dest_dict)
    route = []
    route_num = len(dest_dict["JFK"])
    i = [0]
    while i[0] < route_num:
        search_route(dest_dict, route, i)

    print(route)


func()
