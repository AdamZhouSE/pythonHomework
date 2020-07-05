def is_two_point_connected(point, a_snow_heap):
    if point[0] == a_snow_heap[0] or point[1] == a_snow_heap[1]:
        return True
    else:
        return False


def is_connected(a_snow_heap, a_part):
    for point in a_part:
        if not is_two_point_connected(point, a_snow_heap):
            return False
    return True


def get_parts(connected_parts, snow_heaps):
    a_part = [snow_heaps[0]]
    snow_heaps_copy = snow_heaps[:]
    snow_heaps.remove(snow_heaps_copy[0])
    i = 0
    while i < len(snow_heaps_copy):
        j = 1
        while j < len(snow_heaps_copy):
            if snow_heaps_copy[j] in a_part:
                j += 1
                continue
            if is_connected(snow_heaps_copy[j], a_part):
                a_part.append(snow_heaps_copy[j])
                snow_heaps.remove(snow_heaps_copy[j])
            j += 1
        i += 1
    connected_parts.append(a_part)


def func():
    n = int(input())
    snow_heaps = []
    i = 0
    while i < n:
        temp_pos = [int(x) for x in input().split()]
        snow_heaps.append(temp_pos)
        i += 1

    connected_parts = []
    while len(snow_heaps) > 0:
        get_parts(connected_parts, snow_heaps)

    print(len(connected_parts) - 1)


func()
