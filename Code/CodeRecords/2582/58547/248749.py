def func():
    arr_0 = [int(x) for x in input().split(",")]
    arr_1 = [int(x) for x in input().split(",")]
    max_val = 0
    i = 0
    while i < len(arr_0) - 1:
        j = i + 1
        while j < len(arr_0):
            now_val = abs(arr_0[i] - arr_0[j]) + abs(arr_1[i] - arr_1[j]) + abs(i - j)
            if now_val > max_val:
                max_val = now_val
            j += 1
        i += 1

    print(max_val)


func()
