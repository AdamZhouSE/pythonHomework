import math


def insert():
    ls = list(eval(input()))
    target = list(eval(input()))
    len_ls = len(ls)
    start = end = 0
    for i in range(len_ls):
        if target[0] < ls[i][0] and i == 0:
            start = 0.5
            break
        elif ls[i][0] > target[0] > ls[i - 1][0]:
            start = i + 0.5
            break
        elif ls[i][0] <= target[0] <= ls[i][1]:
            start = i + 1
            break
        elif target[0] > ls[len_ls-1][1]:
            start = len_ls + 0.5
            break
    for i in range(len_ls):
        if target[1] < ls[i][0] and i == 0:
            end = 0.5
            break
        elif ls[i][0] > target[1] > ls[i - 1][0]:
            end = i + 0.5
            break
        elif ls[i][0] <= target[1] <= ls[i][1]:
            end = i + 1
            break
        elif target[1] > ls[len_ls-1][1]:
            end = len_ls + 0.5
            break
    if int(start) == start:
        target[0] = ls[start-1][0]
    if int(end) == end:
        target[1] = ls[end-1][1]
    if start == end and int(start) != start:
        ls.insert(math.ceil(start)-1, target)
    else:
        for i in range(math.floor(end)-math.ceil(start) + 1):
            ls.remove(ls[math.ceil(start)-1])
        ls.insert(math.ceil(start)-1, target)
    return ls


print(insert())