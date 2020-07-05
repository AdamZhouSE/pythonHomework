def func():
    arr = [int(x) for x in input().split(",")]
    arr_set = set(arr)
    for ele in arr_set:
        if arr.count(ele) > len(arr) // 2:
            print(ele)
            return
    print(4)


func()
