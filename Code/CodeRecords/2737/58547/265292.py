def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    limit = len(arr) // 3
    set_arr = set(arr)
    res = []
    for ele in set_arr:
        if arr.count(ele) > limit:
            res.append(ele)

    print(res)


func()
