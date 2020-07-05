def func():
    arr = [int(x) for x in input()[1:-1].split(", ")]

    arr.sort()
    max_len = 0
    now_len = 1
    i = 0
    while i < len(arr) - 1:
        if arr[i] + 1 == arr[i+1]:
            now_len += 1
            i += 1
            continue
        if now_len > max_len:
            max_len = now_len
        now_len = 1
        i += 1
        continue

    print(max_len)


func()
