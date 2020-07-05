def max_dis():
    ls = list(eval(input()))
    if len(ls) < 2:
        return 0
    ls.sort()
    res = 0
    for i in range(len(ls)-1):
        if ls[i+1] - ls[i] > res:
            res = ls[i+1] - ls[i]
    return res


print(max_dis())