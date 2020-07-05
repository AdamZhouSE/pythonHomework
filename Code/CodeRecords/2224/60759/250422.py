lst = [ch for ch in input()]
if len(lst) > 1:
    for i in range(1, len(lst)):
        idx = lst.index(max(lst[i:]))
        if lst[idx] > lst[i - 1]:
            lst[i - 1], lst[idx] = lst[idx], lst[i - 1]
            break
print(''.join(lst))
