def func5():
    arr = eval(input())
    res = []
    for item in arr:
        res.append(list(map(int, item.split(":"))))
    res = sorted(res, key=lambda x: (x[0], x[1]))
    if res[0][0] == 0:
        res.append([24, res[0][1]])
    ans = []
    for i in range(1, len(res)):
        ans.append((res[i][1] + 60 - res[i - 1][1]) + 60 * (res[i][0] - res[i - 1][0] - 1))
    print(min(ans))


func5()
