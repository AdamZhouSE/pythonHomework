def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    now_len = 1
    former = arr[0]
    max_len = 1
    i = 1
    while i < len(arr):
        if arr[i] > former:
            now_len += 1
        else:
            now_len = 1
        if now_len > max_len:
            max_len = now_len
        former = arr[i]
        i += 1
        
    print(max_len)


func()
