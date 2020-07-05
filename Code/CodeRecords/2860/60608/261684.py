def func34():
    n = eval(input())
    arr = []
    for _ in range(0, n):
        arr.append(tuple(map(int, input().split())))

    ans = 1 if (0, 0) in arr else 2
    res = {(0, 0): 1}
    for i in range(0, n):
        if arr[i] in res.keys():
            val = res[arr[i]]
        else:
            val = max(res.values()) + 1
            res[arr[i]] = val
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1]:
                if arr[j] in res.keys():
                    tem = res[arr[j]]
                    for item in res.keys():
                        if res[item] == val:
                            res[item] = tem
                    val = tem
                else:
                    res[arr[j]] = val
    print(len(set(res.values())) - ans)

func34()
