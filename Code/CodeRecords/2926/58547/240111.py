def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    max_count = 0
    i = 0
    while i < n:
        now_count = arr.count(arr[i])
        if now_count > max_count:
            max_count = now_count
        i += 1

    print(max_count)


func()
