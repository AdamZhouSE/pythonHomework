def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    arr.sort()
    for ele in arr[:]:
        if ele <= 0:
            arr.remove(ele)
    i = 0
    bias = 1
    while i < len(arr):
        if arr[i] != i + bias:
            print(i + bias)
            return
        i += 1
    print(i + bias)


func()
