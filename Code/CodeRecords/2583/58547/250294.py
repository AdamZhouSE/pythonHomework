def func():
    n_th = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    arr = []
    arr += [a * x for x in range(1, 1 + n_th)]
    arr += [b * x for x in range(1, 1 + n_th)]
    arr += [c * x for x in range(1, 1 + n_th)]

    arr.sort()
    print(arr)

    print(arr[n_th - 1])


func()
