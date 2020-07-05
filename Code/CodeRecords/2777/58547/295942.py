def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        length = int(input())
        arr = [int(x) for x in input().split()]
        arr.sort()
        if length % 2 == 0:
            print((arr[length // 2] + arr[length // 2 - 1]) // 2)
        else:
            print(arr[length // 2])
        i += 1


func()
