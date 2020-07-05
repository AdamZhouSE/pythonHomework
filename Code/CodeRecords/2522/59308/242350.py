import functools
arr_1 = eval(input())
arr_2 = eval(input())


def cmp_base_arr2(s1, s2):
    try:
        a = arr_2.index(s1)
    except ValueError:
        a = -1
    try:
        b = arr_2.index(s2)
    except ValueError:
        b = -1
    if a == -1 and b == -1:
        if s1 <= s2:
            return -1
        else:
            return 1
    elif a == -1:
        return 1
    elif b == -1:
        return -1
    if a <= b:
        return -1
    else:
        return 1


print(sorted(arr_1, key=functools.cmp_to_key(cmp_base_arr2)))




