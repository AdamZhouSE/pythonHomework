
while True:
    n: int = eval(input())
    if n == 0:
        break

    res, num, val = [], 0, []
    for i in range(0, n):
        res.append(input())
    tet = input()
    for i in range(0, n):
        t, k, tem = 0, 0, tet
        while True:
            tem = tem[k:]
            k = tem.find(res[i])
            if k == -1:
                break
            else:
                t += 1
                k += 1

        if t > num:
            num = t
            val = [res[i]]
        elif t == num:
            val.append(res[i])

    print(num)
    for i in range(0, len(val)):
        print(val[i])
