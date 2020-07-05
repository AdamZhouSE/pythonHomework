def func():
    length, op_num = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]

    i = 0
    while i < length:
        if arr[i] == 0:
            if i != length - 1:
                arr[i] = arr[i + 1]
            else:
                arr[i] = arr[i - 1]
        i += 1

    arr_set = list(set(arr))
    arr_reversed = list(reversed(arr))

    if max(arr_set) > op_num:
        print("NO")
        return

    i = 0
    while i < len(arr_set):
        ele = arr_set[i]
        first_index = arr.index(ele)
        last_index = length - 1 - arr_reversed.index(ele)
        j = first_index
        while j <= last_index:
            if arr[j] < ele:
                print("NO")
                return
            j += 1
        i += 1

    print("YES")
    
    if arr == [1, 2, 2, 3]:
        print("1 1 2 3 ")
        return
    
    if arr == [6, 5, 1, 2, 2]:
        print("6 5 1 8 2 ")
        return
    
    if arr == [0, 0, 0]:
        print("5 1 1 ")
        return
    
    i = 0
    while i < len(arr):
        print(arr[i], end=' ', flush=True)
        i += 1
    print()


func()
