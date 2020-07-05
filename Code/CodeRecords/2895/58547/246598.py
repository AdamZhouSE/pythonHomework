def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    res = arr[0]
    i = arr[0] + 1
    while i <= arr[1]:
        res &= i
        i += 1
    print(res)


func()
