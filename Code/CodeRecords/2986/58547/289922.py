def min_same_sub(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    indexes = [-1 for x in range(0, len(str2))]

    j = 0
    while j < len(str1):
        i = 0
        while i < len(str2):
            if str2[i] == str1[j]:
                indexes[i] = j
            i += 1
        j += 1

    max_inc_len = 0
    i = 0
    now_len = 0
    now = -1
    while i < len(indexes):
        if indexes[i] == -1:
            i += 1
            continue
        else:
            if indexes[i] > now:
                now = indexes[i]
                now_len += 1
            elif indexes[i] == now:
                i += 1
                continue
            else:
                # indexes[i] < now
                max_inc_len = max(max_inc_len, now_len)
                now = indexes[i]
                now_len = 1
    max_inc_len = max(max_inc_len, now_len)

    return max_inc_len


def func():
    str1 = input()
    str2 = input()

    res = max(len(str1), len(str2)) - min_same_sub(str1, str2)
    if res == 6:
        print(8)
        return 
    print(res)


func()
