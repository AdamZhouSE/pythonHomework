def func25():
    standard = [4, 8, 15, 16, 23, 42]
    n = eval(input())
    arr = list(map(int, input().split()))
    res = []

    for i in range(0, n):
        arr[i] = standard.index(arr[i])
    for i in arr:
        if i == 0:
            res.append([0])
        elif i == 1:
            if res.count([0]) > 0:
                index = res.index([0])
                res[index].append(i)
        elif i == 2:
            if res.count([0, 1]) > 0:
                index = res.index([0, 1])
                res[index].append(i)
        elif i == 3:
            if res.count([0, 1, 2]) > 0:
                index = res.index([0, 1, 2])
                res[index].append(i)
        elif i == 4:
            if res.count([0, 1, 2, 3]) > 0:
                index = res.index([0, 1, 2, 3])
                res[index].append(i)
        elif i == 5:
            if res.count([0, 1, 2, 3, 4]) > 0:
                index = res.index([0, 1, 2, 3, 4])
                res[index].append(i)
    print(n - 6 * res.count([0, 1, 2, 3, 4, 5]))


func25()
