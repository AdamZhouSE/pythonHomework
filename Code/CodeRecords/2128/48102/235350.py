def cycle():
    ls = input().split(',')
    ls = list(map(int, ls))
    res = []
    ls_len = len(ls)
    for i in range(ls_len):
        count = 0
        m = 0
        for n in ls:
            count += n * m
            m += 1
        res.append(count)
        temp = ls[0]
        ls.remove(temp)
        ls.append(temp)
    return max(res)


print(cycle())