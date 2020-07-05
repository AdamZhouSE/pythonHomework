def fly(res: dict, path: list, ans: list, dst: int, k: int, price: int):
    if path[-1] == dst and len(path) <= k + 2:
        ans[0] = min(ans[0], price)
    elif len(path) < k + 2:
        arr = res[path[-1]]
        if arr:
            for item in arr:
                path.append(item[0])
                fly(res, path, ans, dst, k, price + item[1])
                del path[-1]


def func14():
    n, arr, src, dst, k, res, ans = eval(input()), eval(input()), eval(input()), eval(input()), eval(input()), {}, [0]
    for array in arr:
        if array[0] in res.keys():
            res[array[0]].append(array[1:])
            ans[0] += array[2]
        else:
            res[array[0]] = [array[1:]]
            ans[0] += array[2]
    ans[0] *= 2
    tem = ans[0]
    fly(res, [src], ans, dst, k, 0)

    if ans[0] != tem:
        print(ans[0])
    else:
        print(-1)


func14()
