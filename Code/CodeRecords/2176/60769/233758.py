import functools


def mycmp(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return 1
        elif x[1] > y[1]:
            return -1
        else:
            return 0


inStr = str(input())
dict = []
for i in range(len(inStr)):
    dict.append([inStr[i:], i+1])
dict = sorted(dict, key=functools.cmp_to_key(mycmp))
res = []
for i in dict:
    res.append(str(i[1]))

print(" ".join(res))

