
def func18():
    res, n, ops = {0: []}, eval(input()), []
    for j in range(0, n):
        ops.append(list(map(int, input().split())))
    for i in range(0, n):
        v, op, x = ops[i][0], ops[i][1], ops[i][2]
        val = res[v][:]
        if op == 1:
            val.append(x)
        elif op == 2 and val.count(x) > 0:
            val.remove(x)
        elif op == 3:
            print(val.index(x) + 1)
        elif op == 4:
            print(val[x - 1])
        elif op == 5:
            flag = True
            for j in range(0, len(val)):
                if (val[j] < x and j == len(val) - 1) or (val[j] < x <= val[j + 1]):
                    print(val[j])
                    flag = False
                    break
            if flag:
                print(-1 * int(pow(2, 31)) + 1)
        elif op == 6:
            flag = True
            for j in range(0, len(val)):
                if (val[j] > x and j == 0) or (val[j] > x >= val[j - 1]):
                    print(val[j])
                    flag = False
                    break
            if flag:
                print(int(pow(2, 31)))

        val = sorted(val)
        res[i + 1] = val[:]


func18()
