import math


def most():
    ls = list(eval(input()))
    s = set(ls)
    res = []
    for i in s:
        if ls.count(i) > math.floor(len(ls) / 3):
            res.append(i)
    print(res)


most()
