def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        length = int(input())
        arr = [int(x) for x in input().split()]
        arr.sort()

        j = 1
        max_len = 0
        now_len = 1
        former = arr[0]
        while j < length:
            if arr[j] == former + 1:
                now_len += 1
            else:
                max_len = max(max_len, now_len)
                now_len = 1
            former = arr[j]
            j += 1

        print(max_len)

        i += 1


func()
