def array():
    ls = input()
    ls = eval(ls)
    res = []
    for i in ls:
        if len(res) == 0:
            res.append(i)
        else:
            if i[0] <= res[len(res)-1][1]:
                res[len(res)-1][1] = i[1]
            else:
                res.append(i)
    print(res)


array()