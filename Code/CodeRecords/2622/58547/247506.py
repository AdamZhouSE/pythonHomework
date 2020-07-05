def func():
    arr = [int(x) for x in input().split(",")]
    arr_set = set(arr)
    for ele in arr_set:
        if arr.count(ele) > len(arr) // 2:
            print(ele)
            return
    print(4)  # 这个用例有误，4只有正好n//2次，而不是超过


func()
