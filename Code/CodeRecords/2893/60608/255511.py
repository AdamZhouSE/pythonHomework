def func9():
    res = sorted(eval(input()))
    n = len(res)
    if res[0] != res[1]:
        print(res[0])
    elif res[n - 1] != res[n - 2]:
        print(res[n - 1])
    for i in range(1, n - 1):
        if res[i] != res[i - 1] and res[i] != res[i + 1]:
            print(res[i])
            break


func9()
