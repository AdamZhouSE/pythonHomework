def find_max():
    lst = list(input().split(','))
    if len(lst) < 3:
        return 0
    lst = list(map(int, lst))
    lst.sort(reverse=True)
    idx, l_len= 0, len(lst)
    while idx < l_len - 2:
        if lst[idx] < lst[idx + 1] + lst[idx + 2]:
            return lst[idx] + lst[idx + 1] + lst[idx + 2]
        idx += 1
    return 0


print(find_max())