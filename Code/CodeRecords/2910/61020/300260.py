def needed_func(a_list_of_rectangles):
    # a_list_of_rectangles 是一个列表，里面装的是二元元组，每个二元元组代表一个矩形

    if len(a_list_of_rectangles) == 1:
        return True

    if len(a_list_of_rectangles) == 2:
        if max(a_list_of_rectangles[0]) >= min(a_list_of_rectangles[1]):
            return True
        else:
            return False

    pass


def needed_func_base(a_list_of_rectangles):
    former_max = max(a_list_of_rectangles[0])
    former_min = min(a_list_of_rectangles[0])
    if len(a_list_of_rectangles) == 1:
        # TODO 返回值后面的列表可能需要修改
        return (True, [(former_max, former_min)])

    if len(a_list_of_rectangles) == 2:
        # possible_rotation
        latter_max = max(a_list_of_rectangles[1])
        latter_min = min(a_list_of_rectangles[1])

        if latter_max <= former_min:
            return (True, [(former_min, latter_max)])

        if latter_max <= former_max and latter_min <= former_min:
            return (True, [(former_max, latter_max), (former_min, latter_min)])

        if latter_max <= former_max:
            return (True, [(former_max, latter_max)])

        if latter_min <= former_min:
            return (True, [(former_min, latter_min)])

        if latter_min <= former_max:
            return (True, [(former_max, latter_min)])

        return (False, None)

    if len(a_list_of_rectangles) >= 3:
        recur_result_L = needed_func_base(a_list_of_rectangles[0: 2])
        recur_result_R = needed_func_base(a_list_of_rectangles[2:])

        if not (recur_result_L[0] and recur_result_R[0]):
            return (False, None)

        L_height_to_check = recur_result_L[1][0][1]


def needed_func_base_2(a_list_of_rectangles):
    if len(a_list_of_rectangles) == 1:
        return True

    if max(a_list_of_rectangles[0]) < min(a_list_of_rectangles[1]):
        return False
    elif len(a_list_of_rectangles) == 2:
        return True

    if max(a_list_of_rectangles[0]) >= max(a_list_of_rectangles[1]):
        height_at_1 = max(a_list_of_rectangles[1])
    else:
        height_at_1 = min(a_list_of_rectangles[1])

    a_list_of_recs_to_recur_call = a_list_of_rectangles[1:]
    a_list_of_recs_to_recur_call[0] = (height_at_1, -1)

    return needed_func_base_2(a_list_of_recs_to_recur_call)


n = int(input())
rectangles = []
for i in range(n):
    wi_and_hi = input().split()
    rectangles.append((int(wi_and_hi[0]), int(wi_and_hi[1])))

if needed_func_base_2(rectangles):
    print('YES')
else:
    print('NO')
