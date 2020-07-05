def get_next(arr, cursor, temp_arr, to_get_next):
    temp_arr.append(arr[cursor[0]])
    if cursor[0] == arr[cursor[0]]:
        cursor[0] += 1
        return True
    cursor[0] += 1
    while cursor[0] < len(arr):
        if arr[cursor[0]] == to_get_next:
            temp_arr.append(arr[cursor[0]])
            cursor[0] += 1
            return True
        temp_arr.append(arr[cursor[0]])
        cursor[0] += 1
    if cursor[0] == len(arr):
        return True
    return False


def get_parts(arr, cursor, parts):
    temp_arr = []
    if cursor[0] >= len(arr):
        return
    to_get_next = cursor[0]
    last_cursor = cursor[0]
    while True:
        flag = False
        if not get_next(arr, cursor, temp_arr, to_get_next):
            return
        if cursor[0] == len(arr):
            parts[0] += 1
            return
        # temp_calc_arr = arr[last_cursor: cursor[0]]
        i = last_cursor
        while i < cursor[0]:
            if arr[i] not in temp_arr:
                to_get_next = arr[i]
                flag = True
                break
            i += 1
        if flag:
            continue
        parts[0] += 1
        return


def func():
    arr = [int(x) for x in input()[1:-1].split(",")]

    i = 0
    cursor = [0]
    parts = [0]
    while i < len(arr):
        get_parts(arr, cursor, parts)
        if cursor[0] >= len(arr):
            break
        i += 1
    print(parts[0])


func()
