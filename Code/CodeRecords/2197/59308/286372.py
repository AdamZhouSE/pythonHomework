#coding=utf8


T = int(input())
for _ in range(T):
    l = int(input())
    res = [__ for __ in range(1, l+1)]
    index = 0
    while len(res) != 1:
        temp = res.pop(0)
        index += 1
        if index == 2:
            index = 0
            continue
        res.append(temp)
    print(res[0])




