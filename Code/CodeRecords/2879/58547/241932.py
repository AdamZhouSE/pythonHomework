def is_two_point_connected(point, a_snow_heap):
    if point[0] == a_snow_heap[0] or point[1] == a_snow_heap[1]:
        return True
    else:
        return False


def is_connected(a_snow_heap, a_part):
    if len(a_part) == 0:
        return False
    for point in a_part:
        if is_two_point_connected(point, a_snow_heap):
            return True
    return False


def func():
    side = int(input())
    points_num = side ** 2
    arr = []
    i = 0
    while i < points_num:
        temp = [int(x) for x in input().split()]
        arr.append(temp)
        i += 1

    i = 0
    indexes = []
    asphalted = []
    while i < points_num:
        if not is_connected(arr[i], asphalted):
            asphalted.append(arr[i])
            indexes.append(i+1)
        i += 1

    i = 0
    while i < len(indexes):
        if i == len(indexes) - 1:
            print(indexes[i])
        else:
            print(str(indexes[i]) + " ", end="", flush=True)
        i += 1


func()
