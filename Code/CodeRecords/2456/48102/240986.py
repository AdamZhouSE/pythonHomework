def num_right():
    ls = list(eval(input()))
    res = []
    for i in range(len(ls)):
        count = 0
        for j in range(i, len(ls), 1):
            if ls[j] < ls[i]:
                count += 1
        res.append(count)
    print(res)
    return


num_right()