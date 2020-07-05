def search_for_target(target, ele_num, numbers, res, now_res_val, cursor):
    # note: now_res_val should not be reference
    if len(now_res_val) == ele_num:
        if sum(now_res_val) == target and now_res_val not in res:
            res.append(now_res_val)
        return
    else:
        if cursor > len(numbers):
            return # do not append

        now_res_val.append(numbers[cursor])

        i = cursor + 1
        while i < len(numbers):
            search_for_target(target, ele_num, numbers, res, now_res_val[:], i)
            i += 1


def func():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ele_num, target = [int(x) for x in input().split(", ")]
    res = []
    for cursor in range(0, 9):
        search_for_target(target, ele_num, numbers, res, [][:], cursor)
    print(res)


func()
